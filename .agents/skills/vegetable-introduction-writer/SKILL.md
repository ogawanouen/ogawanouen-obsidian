---
name: vegetable-introduction-writer
description: Create, retrieve, update, and save Japanese vegetable introduction copy for Ogawa Nouen using the Obsidian vault. Use knowledge/vegetables as the factual source, knowledge/style as the writing-style source, and knowledge/introductions as the editable saved-copy store. Use when asked to create or retrieve vegetable introductions, especially Japanese prompts like "トマトの紹介文を作成して下さい", "ナスの商品紹介文を書いて", "キュウリのPOP文を作成", "ルバーブのSNS紹介文を作って", "野菜の紹介文を保存して", or when asked to write, reuse, polish, save, refresh, shorten, lengthen, or prepare product descriptions, farm stand copy, newsletter blurbs, SNS captions, POP text, recipe-adjacent introductions, or customer-facing explanations for vegetables grown by 小川農園.
---

# Vegetable Introduction Writer

## Core Workflow

1. Treat the current Obsidian vault as the source of truth.
2. Read vegetable facts from `knowledge/vegetables/`.
3. Read writing guidance from `knowledge/style/` when present.
4. Store and retrieve reusable introduction copy from `knowledge/introductions/`.
5. If the user writes `knowladge`, interpret it as `knowledge` unless an actual `knowladge/` folder exists.
6. Search first with `rg --files knowledge` and then read only the relevant vegetable, introduction, and style files.

## Retrieval Before Generation

For requests such as `トマトの紹介文を作成して`, first check for `knowledge/introductions/トマト.md`.

If a saved introduction file exists:

- Return the saved copy by default instead of generating a new one.
- Mention the saved file path.
- Regenerate only when the user explicitly asks for a new version, rewrite, refresh, alternate proposal, or update from the vegetable database.

If no saved introduction file exists:

- Read the matching vegetable database under `knowledge/vegetables/`.
- Generate introduction copy from the vegetable facts and style notes.
- Always create `knowledge/introductions/<vegetable>.md` using the saved introduction file format.
- Save the generated `紹介文`, `短い一言`, and `おすすめの食べ方` in that file before responding.
- Return the saved copy and mention the saved file path.

## Saved Introduction Files

Use one Markdown file per vegetable under `knowledge/introductions/`.

Do not add `type` frontmatter. This workflow is file-path based.

Required frontmatter:

```yaml
status: draft
category_small: トマト
source_database: knowledge/vegetables/トマト.md
updated: 2026-05-31
```

`status` is required and must be exactly one of:

- `draft`
- `reviewed`
- `approved`
- `needs_update`

Never generate another `status` value. Never leave `status` empty. Use `draft` for newly generated AI copy unless the user explicitly says a human has reviewed or approved it.

`source_database` only needs to link to the vegetable database in `knowledge/vegetables/`.

Read `references/introduction-file.md` before creating or substantially reorganizing saved introduction files.

## Source Priority

Use facts in this order:

1. The user's latest instructions.
2. Saved copy under `knowledge/introductions/`, when the user asks to retrieve or use existing copy.
3. Matching vegetable facts under `knowledge/vegetables/`.
4. Style and tone instructions under `knowledge/style/`.
5. General culinary knowledge, only for ordinary preparation or storage suggestions and only when not contradicting the notes.

When multiple vegetable notes conflict, mention the conflict briefly and ask which note to trust.

## Generation Rules

- Base generated copy only on information found in the notes or explicitly provided by the user.
- Do not invent cultivar names, growing methods, harvest timing, taste claims, certifications, pesticide practices, or health benefits.
- When source information is missing, either ask for the missing fact or write around it in general language without pretending it is known.
- Do not overwrite human-edited saved copy unless the user explicitly asks to replace it.
- If saved copy exists but the vegetable database has clearly changed, suggest marking the saved copy `needs_update` or generating a refresh, but do not silently replace it.
- When no saved introduction exists and new copy is generated, saving is mandatory. Do not ask whether to save.

## Expected Output

Adapt the shape to the user's request. If unspecified, provide:

- `紹介文`: 120-180 Japanese characters.
- `短い一言`: 30-50 Japanese characters for POP, labels, or SNS lead text.
- `おすすめの食べ方`: 2-3 concise suggestions if the source or common use supports them.

For SNS requests, include a caption-length version and optional hashtags only if requested.

For POP or label requests, keep sentences short and easy to scan. Avoid dense paragraphs.

## Writing Rules

- Write in natural Japanese with a calm, friendly farm voice.
- Prefer sensory details grounded in source facts: texture, aroma, sweetness, bitterness, juiciness, freshness, seasonality, and recommended cooking.
- Make 小川農園 feel present through cultivation context when the notes support it, but avoid exaggerated claims.
- Avoid medical or nutritional promises unless the notes provide a reliable basis and the user explicitly wants that angle.
- Avoid overused sales language such as `こだわり`, `絶品`, `最高`, `安心安全` unless the source or style guide specifically asks for it.
- Keep claims modest: use `〜が特徴です`, `〜を楽しめます`, `〜に向いています` rather than absolute statements.
