---
name: vegetable-database-template
description: Create a new Markdown database template for a vegetable in the Ogawa Nouen Obsidian vault, defaulting to knowledge/vegetables under the current workspace. By default, research web sources and create a general-info-filled database unless the user explicitly asks for a blank/no-information template. Use when the user asks in Japanese or English to create, add, make, or prepare a vegetable database or template, especially requests like "トマトのデータベースを作成して下さい", "ナスのDBを作って", "一般的な情報入りでキュウリのDBを作成", "情報を入力しないで作成して", or "create a blank tomato vegetable database". If a matching vegetable database already exists, report that it already exists and do not create a duplicate.
---

# Vegetable Database Template

## Core Workflow

1. Extract the vegetable name from the user's request.
2. Treat `knowledge/vegetables/` in the current workspace as the default destination. If the user writes `knowladge`, interpret it as `knowledge` unless an actual `knowladge/` directory exists.
3. Before creating anything, check for an existing database for the same vegetable under `knowledge/vegetables/`.
4. If one exists, do not create a new file. Tell the user the existing file path.
5. Decide the template mode:
   - Use `blank` only when the user explicitly asks for `空`, `項目だけ`, `野菜名と項目以外なし`, `情報を入力しない`, `情報なし`, `blank`, `no information`, or similar.
   - Use `general` when the user asks for `一般的な情報入り`, `クイック`, `下書き入り`, `general`, or similar.
   - If the user does not specify a mode, default to `general`; do not ask a follow-up question just to choose the mode.
6. For `general` mode, search the web for general, non-farm-specific information about that vegetable before creating the file. Use reputable sources such as public agricultural extension pages, produce/food education pages, encyclopedic references, or reliable recipe/food sites. Prefer Japanese sources when the output is Japanese, but use English sources when Japanese information is sparse.
7. For `general` mode, create a small JSON profile from the researched facts and include source URLs. Keep 小川農園-specific fields empty unless the user provides those facts.
8. If none exists, create `knowledge/vegetables/<vegetable>.md` from the selected template mode.
9. Tell the user the created file path and mode.

## Preferred Implementation

Use the bundled script so duplicate checks and formatting stay consistent:

```bash
python3 .agents/skills/vegetable-database-template/scripts/create_vegetable_database.py "<vegetable-name>" --workspace "<current-workspace-path>" --mode blank
python3 .agents/skills/vegetable-database-template/scripts/create_vegetable_database.py "<vegetable-name>" --workspace "<current-workspace-path>" --mode general --profile-file "/path/to/researched-profile.json"
```

Run the script from the project root. The script creates `knowledge/vegetables/` when needed. It exits successfully both when it creates a new database and when it finds an existing one.

For `general` mode, do not rely on the model's memory or fixed built-in vegetable facts. Research first, then pass the researched JSON profile to the script. If web access is unavailable, ask whether the user wants a blank template instead. Because `general` is the default, any simple request like `ジャガイモのDBを作成して下さい` should perform web research and create a general-info-filled database.

## Duplicate Rules

Consider a database existing only if a Markdown file under `knowledge/vegetables/` has:

- the same normalized `category_small` frontmatter value as the requested vegetable

Do not use filename, legacy `vegetable`, aliases, body `野菜名`, or the H1 heading for duplicate detection. Do not overwrite or modify an existing vegetable database unless the user explicitly asks to edit it.

If the output path already exists but the file does not have a matching `category_small`, do not overwrite it. Tell the user the path already exists and that `category_small` must be checked or added before the tool can safely decide.

## Template Content

The created file must be a Markdown database note with YAML frontmatter and clear Japanese sections for:

- basic identity
- cultivation and harvest
- flavor and texture body notes
- recommended ways to eat
- storage
- introduction-copy source notes
- cautions and expressions to avoid
- update history

`blank` mode leaves all fields empty except the vegetable name, section headings, and dates.

`general` mode pre-fills ordinary, non-farm-specific culinary and handling information from web research to make a quick first draft. Mark general content as general information, include source URLs in `参考情報源`, and keep 小川農園-specific fields empty unless the user provides those facts.

Write frontmatter arrays on one line with Japanese comma separators, for example `best_uses: [生食、 サラダ]`. Do not use block-list frontmatter such as `best_uses:` followed by `- 生食`.

See `references/template-fields.md` for the field definitions and authoring guidance.

## Research Profile JSON

For frontmatter field selection, read `references/frontmatter-guide.md`. Prefer its controlled vocabulary for `category_large`, `category_medium`, `category_small`, `crop_family`, `edible_part`, `color`, `shape`, `size_class`, and `best_uses`.

In `general` mode, `category_large`, `category_medium`, and `category_small` are required. The script rejects missing required fields. Controlled fields must use only values listed in `references/frontmatter-guide.md`; if a value does not fit, leave optional fields blank or update the guide before using a new controlled value. `category_small` and `aliases` are flexible text fields.

For `general` mode, write a temporary JSON object with any researched keys that are supported by the template:

```json
{
  "category_large": "果菜類",
  "category_medium": "トマト類",
  "category_small": "トマト",
  "crop_family": "ナス科",
  "edible_part": "果実",
  "color": "赤",
  "shape": "丸い",
  "size_class": "中",
  "best_uses": ["生食", "サラダ", "煮る"],
  "family": "ナス科",
  "varieties": "一般的な品種名や種類",
  "uses": "主な用途",
  "taste": "味の一般情報",
  "texture": "食感の一般情報",
  "aroma": "香りの一般情報",
  "cooking_change": "加熱時の変化",
  "raw": "生食での使い方",
  "cooked": "加熱での使い方",
  "pairings": "相性のよい食材・調味料",
  "simple_recipes": "簡単な調理例",
  "storage_room": "常温保存の一般情報",
  "storage_fridge": "冷蔵保存の一般情報",
  "storage_freezer": "冷凍保存の一般情報",
  "eat_soon_state": "早めに食べたい状態",
  "season": "一般的な旬や流通時期",
  "table_ideas": "食卓での楽しみ方",
  "sources": [
    {
      "title": "Source title",
      "url": "https://example.com",
      "note": "used for storage and culinary notes"
    }
  ]
}
```

Omit uncertain keys instead of guessing. Do not include health or medical claims unless the user explicitly requests them and the source is reliable.

## User-Facing Response

When created, answer briefly:

`トマトのデータベーステンプレートを作成しました（空テンプレート）: <path>`

or

`トマトのデータベーステンプレートを作成しました（一般情報入り）: <path>`

When already present, answer briefly:

`トマトのデータベースはすでにあります: <path>`
