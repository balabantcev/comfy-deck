#!/usr/bin/env python3
"""Build or verify self-contained Claude/Codex packages from the canonical skill."""

from __future__ import annotations

import argparse
import io
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NAME = "comfy-deck"
PACKAGE_PARTS = ("SKILL.md", "references", "assets")
ARCHIVES = ("comfy-deck.zip", "comfy-deck.skill")
ZIP_DATE = (2026, 1, 1, 0, 0, 0)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical_files() -> dict[str, bytes]:
    files = {}
    for part in PACKAGE_PARTS:
        source = ROOT / part
        require(source.exists(), f"Missing canonical source: {part}")
        paths = [source] if source.is_file() else sorted(source.rglob("*"))
        for path in paths:
            require(not path.is_symlink(), f"Symlinks are not packaged: {path.relative_to(ROOT)}")
            if not path.is_file():
                continue
            require(path.suffix not in {".zip", ".skill", ".pyc"}, f"Unexpected nested package: {path.relative_to(ROOT)}")
            require(path.name != ".DS_Store", "Remove .DS_Store from canonical resources")
            files[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    return dict(sorted(files.items()))


def validate_source(files: dict[str, bytes]) -> str:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    require(bool(re.fullmatch(r"\d+\.\d+\.\d+", version)), "VERSION must be MAJOR.MINOR.PATCH")
    skill = files["SKILL.md"].decode("utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", skill, re.S)
    require(frontmatter is not None, "SKILL.md requires YAML frontmatter")
    header = frontmatter.group(1)
    require(re.search(r"^name: comfy-deck$", header, re.M) is not None, "Skill name must match its package folder")
    desc_match = re.search(r'^description: (".*")$', header, re.M)
    require(desc_match is not None, "description must be a quoted string")
    description = json.loads(desc_match.group(1))
    require(0 < len(description) <= 1024, "description must contain 1–1024 characters")
    require(f'  version: "{version}"' in header.splitlines(), "metadata.version differs from VERSION")
    require("[TODO:" not in skill, "Unfinished skill scaffold")
    require(f"Поточна версія: **{version}**." in (ROOT / "README.md").read_text(encoding="utf-8"), "README version differs from VERSION")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    latest = re.search(r"^## \[(\d+\.\d+\.\d+)\]", changelog, re.M)
    require(latest is not None and latest.group(1) == version, "Latest CHANGELOG entry differs from VERSION")

    for relative, data in files.items():
        if not relative.endswith(".md"):
            continue
        text = data.decode("utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
                continue
            resolved = ((ROOT / relative).parent / target.split("#", 1)[0]).resolve()
            require(resolved.is_relative_to(ROOT), f"Link escapes skill: {relative}: {target}")
            require(resolved.relative_to(ROOT).as_posix() in files, f"Missing packaged reference: {relative}: {target}")

    metadata = ROOT / "codex" / NAME / "agents" / "openai.yaml"
    ui = metadata.read_text(encoding="utf-8")
    fields = {}
    for key, literal in re.findall(r'^  (\w+): (".*")$', ui, re.M):
        fields[key] = json.loads(literal)
    require(25 <= len(fields.get("short_description", "")) <= 64, "Codex short_description must be 25–64 characters")
    require(f"${NAME}" in fields.get("default_prompt", ""), "Codex default_prompt must invoke the skill")
    for key in ("icon_small", "icon_large"):
        require(fields.get(key, "").removeprefix("./") in files, f"Missing Codex icon: {key}")
    return version


def archive_bytes(files: dict[str, bytes]) -> bytes:
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for relative, data in files.items():
            entry = zipfile.ZipInfo(f"{NAME}/{relative}", date_time=ZIP_DATE)
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return output.getvalue()


def verify_package(platform: str, files: dict[str, bytes]) -> None:
    folder = ROOT / platform / NAME
    expected = dict(files)
    if platform == "codex":
        expected["agents/openai.yaml"] = (folder / "agents/openai.yaml").read_bytes()
    require(folder.is_dir(), f"Missing package: {platform}/{NAME}")
    actual = {}
    for path in folder.rglob("*"):
        require(not path.is_symlink(), f"Symlink in {platform} package")
        if path.is_file():
            actual[path.relative_to(folder).as_posix()] = path.read_bytes()
    require(actual == expected, f"{platform} package is stale or contains unexpected files; rebuild it")


def build(files: dict[str, bytes], data: bytes) -> None:
    for platform in ("claude", "codex"):
        folder = ROOT / platform / NAME
        require(not folder.is_symlink(), f"Refusing symlink package: {platform}/{NAME}")
        for part in PACKAGE_PARTS:
            target = folder / part
            require(not target.is_symlink(), f"Refusing symlink target: {target}")
            if target.is_dir():
                shutil.rmtree(target)
            elif target.exists():
                target.unlink()
        for relative, content in files.items():
            target = folder / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
    for name in ARCHIVES:
        (ROOT / name).write_bytes(data)


def verify_archives(files: dict[str, bytes], data: bytes) -> None:
    for name in ARCHIVES:
        target = ROOT / name
        require(target.is_file(), f"Missing archive: {name}")
        require(target.read_bytes() == data, f"{name} is stale or not reproducibly built")
        with zipfile.ZipFile(target) as archive:
            require(archive.testzip() is None, f"Corrupt archive: {name}")
            expected = {f"{NAME}/{path}": content for path, content in files.items()}
            actual = {entry.filename: archive.read(entry) for entry in archive.infolist()}
            require(len(actual) == len(archive.infolist()), f"Duplicate entries in {name}")
            require(actual == expected, f"Incomplete or unexpected archive contents: {name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify versions, references, generated packages and archives without writing")
    args = parser.parse_args()
    try:
        files = canonical_files()
        version = validate_source(files)
        data = archive_bytes(files)
        if not args.check:
            build(files, data)
        for platform in ("claude", "codex"):
            verify_package(platform, files)
        verify_archives(files, data)
    except (ValueError, OSError, zipfile.BadZipFile, json.JSONDecodeError) as error:
        print(f"Package validation failed: {error}", file=sys.stderr)
        return 1
    print(f"{'Verified' if args.check else 'Built and verified'} {NAME} {version}: Claude, Codex, ZIP and .skill ({len(files)} canonical files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
