# Introduction File Format

Use this reference when creating or reorganizing files under `knowledge/introductions/`.

## File Location

Store one Markdown file per vegetable:

```text
knowledge/introductions/<category_small>.md
```

Use the same `category_small` value as the vegetable database.

## Frontmatter

Do not include `type`.

Required fields:

```yaml
status: draft
category_small: トマト
source_database: knowledge/vegetables/トマト.md
updated: 2026-05-31
```

Allowed `status` values only:

- `draft`
- `reviewed`
- `approved`
- `needs_update`

Use `draft` for newly generated AI copy. Use `reviewed` or `approved` only when the user says a human has reviewed or approved the copy. Use `needs_update` when the vegetable database changed enough that saved copy should be checked.

## Body Sections

Recommended headings:

```markdown
# <野菜名> 紹介文

## 標準紹介文

## 短い一言

## POP向け

## SNS向け

## おすすめの食べ方

## 編集メモ
```

Keep human edits as first-class content. When proposing a rewrite, add it as a candidate in the response unless the user explicitly asks to update the file.
