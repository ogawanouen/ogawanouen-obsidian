#!/usr/bin/env python3
"""Create an Ogawa Nouen vegetable database Markdown template."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path


def normalize_name(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).strip()
    value = re.sub(r"\s+", "", value)
    return value.casefold()


def safe_filename(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).strip()
    value = re.sub(r"[\\/:\*\?\"<>\|]", "_", value)
    value = re.sub(r"\s+", " ", value)
    return value or "野菜"


def extract_declared_name(markdown: str) -> str | None:
    return extract_scalar_field(markdown, "category_small")


def clean_yaml_value(value: str) -> str:
    value = value.strip()
    if value in {"[]", "{}", "null", "Null", "NULL", "~"}:
        return ""
    return value.strip("\"'")


def extract_scalar_field(markdown: str, field: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(field)}:\s*(.*?)\s*$", markdown)
    if not match:
        return None
    value = clean_yaml_value(match.group(1))
    return value or None


def find_existing(target_dir: Path, vegetable: str) -> Path | None:
    if not target_dir.exists():
        return None

    target_normalized = normalize_name(vegetable)

    for path in sorted(target_dir.glob("*.md")):
        try:
            declared = extract_declared_name(path.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            continue

        if declared and normalize_name(declared) == target_normalized:
            return path

    return None


def load_profile(path: Path | None) -> dict[str, object]:
    if path is None:
        return {}

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON profile: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc

    if not isinstance(data, dict):
        print("ERROR: JSON profile must be an object", file=sys.stderr)
        raise SystemExit(2)
    return data


def text(profile: dict[str, object], key: str) -> str:
    value = profile.get(key, "")
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, list):
        return "、".join(str(item).strip() for item in value if str(item).strip())
    return str(value).strip() if value else ""


def profile_value(profile: dict[str, object], *keys: str) -> object:
    for key in keys:
        value = profile.get(key)
        if value not in (None, ""):
            return value
    return ""


def yaml_scalar(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return "、".join(str(item).strip() for item in value if str(item).strip())
    return str(value).strip()


def yaml_field(name: str, value: object = "") -> str:
    if isinstance(value, list):
        items = [str(item).strip() for item in value if str(item).strip()]
        if not items:
            return f"{name}:"
        return f"{name}:\n" + "\n".join(f"  - {item}" for item in items)

    scalar = yaml_scalar(value)
    return f"{name}: {scalar}" if scalar else f"{name}:"


def render_frontmatter(vegetable: str, mode: str, profile: dict[str, object]) -> str:
    today = date.today().isoformat()
    is_general = mode == "general"
    status = "general-draft" if is_general else "draft"
    category_small = profile_value(profile, "category_small") if is_general else ""
    if not category_small:
        category_small = vegetable

    frontmatter_lines = [
        "type: vegetable-database",
        "aliases: []",
        f"status: {status}",
        f"template_mode: {mode}",
    ]

    if is_general:
        frontmatter_lines.extend([f"created: {today}", f"updated: {today}"])

    frontmatter_lines.extend(
        [
            yaml_field("category_large", profile_value(profile, "category_large")),
            yaml_field("category_medium", profile_value(profile, "category_medium")),
            yaml_field("category_small", category_small),
            yaml_field("crop_family", profile_value(profile, "crop_family", "family")),
            yaml_field("edible_part", profile_value(profile, "edible_part")),
            yaml_field("color", profile_value(profile, "color")),
            yaml_field("shape", profile_value(profile, "shape")),
            yaml_field("size_class", profile_value(profile, "size_class")),
            yaml_field("texture", profile_value(profile, "frontmatter_texture", "texture")),
            yaml_field("flavor", profile_value(profile, "flavor")),
            yaml_field("best_uses", profile_value(profile, "best_uses")),
            yaml_field("sales_angle", profile_value(profile, "sales_angle")),
        ]
    )

    return "\n".join(frontmatter_lines)


def render_sources(profile: dict[str, object]) -> str:
    sources = profile.get("sources", [])
    if not isinstance(sources, list) or not sources:
        return "- 未記入"

    lines = []
    for source in sources:
        if not isinstance(source, dict):
            continue
        title = str(source.get("title", "")).strip() or "参考情報"
        url = str(source.get("url", "")).strip()
        note = str(source.get("note", "")).strip()
        line = f"- {title}"
        if url:
            line += f": {url}"
        if note:
            line += f" ({note})"
        lines.append(line)
    return "\n".join(lines) if lines else "- 未記入"


def render_template(vegetable: str, mode: str, profile: dict[str, object]) -> str:
    today = date.today().isoformat()
    is_general = mode == "general"
    mode_note = (
        "Webで確認した一般情報を入れた下書きです。小川農園固有の情報は確認して追記してください。"
        if is_general
        else ""
    )
    history_line = f"- {today}: {mode} テンプレート作成" if is_general else "-"
    sources = render_sources(profile) if is_general else "-"

    return f"""---
{render_frontmatter(vegetable, mode, profile)}
---

# {vegetable}

## 基本情報

- 野菜名: {vegetable}
- 品種:{' ' + text(profile, 'varieties') if is_general else ''}
- 科・分類:{' ' + text(profile, 'crop_family') if is_general and text(profile, 'crop_family') else (' ' + text(profile, 'family') if is_general else '')}
- 主な栽培場所:
- 主な用途:{' ' + text(profile, 'uses') if is_general else ''}
- 情報メモ: {mode_note}

## 栽培情報

- 播種・定植時期:
- 栽培期間:
- 栽培方法:
- 小川農園での育て方の特徴:
- 栽培中に気をつけていること:

## 収穫・出荷

- 収穫時期:
- 収穫の目安:
- 出荷時期:
- お届け時の状態:

## 味・食感・香り

- 味:{' ' + text(profile, 'taste') if is_general else ''}
- 食感:{' ' + text(profile, 'texture') if is_general else ''}
- 香り:{' ' + text(profile, 'aroma') if is_general else ''}
- 火を入れたときの変化:{' ' + text(profile, 'cooking_change') if is_general else ''}

## おすすめの食べ方

- 生食:{' ' + text(profile, 'raw') if is_general else ''}
- 加熱:{' ' + text(profile, 'cooked') if is_general else ''}
- 相性のよい食材・調味料:{' ' + text(profile, 'pairings') if is_general else ''}
- 簡単な調理例:{' ' + text(profile, 'simple_recipes') if is_general else ''}

## 保存方法

- 常温:{' ' + text(profile, 'storage_room') if is_general else ''}
- 冷蔵:{' ' + text(profile, 'storage_fridge') if is_general else ''}
- 冷凍:{' ' + text(profile, 'storage_freezer') if is_general else ''}
- 早めに食べたい状態:{' ' + text(profile, 'eat_soon_state') if is_general else ''}

## 紹介文に使える素材

- お客様に伝えたい一言:
- 季節感:{' ' + text(profile, 'season') if is_general else ''}
- 畑での様子:
- 食卓での楽しみ方:{' ' + text(profile, 'table_ideas') if is_general else ''}
- POP・SNS向けの短い表現:

## 避けたい表現・注意点

- 避けたい言葉:
- 事実確認が必要な表現:
- アレルギー・注意事項:

## メモ

-

## 参考情報源

{sources}

## 更新履歴

{history_line}
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a vegetable database template under knowledge/vegetables."
    )
    parser.add_argument("vegetable", help="Vegetable name, e.g. トマト")
    parser.add_argument(
        "--workspace",
        default=".",
        help="Workspace root. Defaults to the current directory.",
    )
    parser.add_argument(
        "--mode",
        choices=("blank", "general"),
        default="general",
        help="Template mode: blank leaves fields empty; general pre-fills researched common information.",
    )
    parser.add_argument(
        "--profile-file",
        type=Path,
        help="JSON file with web-researched general information for --mode general.",
    )
    args = parser.parse_args()

    vegetable = unicodedata.normalize("NFKC", args.vegetable).strip()
    if not vegetable:
        print("ERROR: vegetable name is empty", file=sys.stderr)
        return 2

    workspace = Path(args.workspace).expanduser().resolve()
    target_dir = workspace / "knowledge" / "vegetables"
    existing = find_existing(target_dir, vegetable)
    if existing:
        print(f"EXISTS\t{vegetable}\t{existing}")
        return 0

    if args.mode == "general" and args.profile_file is None:
        print("ERROR: --profile-file is required when --mode general", file=sys.stderr)
        return 2

    profile = load_profile(args.profile_file) if args.mode == "general" else {}

    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / f"{safe_filename(vegetable)}.md"
    if target_path.exists():
        print(f"PATH_EXISTS\t{vegetable}\t{target_path}")
        return 3

    target_path.write_text(render_template(vegetable, args.mode, profile), encoding="utf-8")
    print(f"CREATED\t{vegetable}\t{args.mode}\t{target_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
