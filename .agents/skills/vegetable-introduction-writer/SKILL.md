---
name: vegetable-introduction-writer
description: Create Japanese vegetable introduction copy for Ogawa Nouen using the Obsidian vault's knowledge/vegetables notes as the factual source and knowledge/style notes as the writing-style source. Use when asked to write, rewrite, polish, shorten, lengthen, or prepare product descriptions, farm stand copy, newsletter blurbs, SNS captions, POP text, recipe-adjacent introductions, or customer-facing explanations for vegetables grown by 小川農園.
---

# Vegetable Introduction Writer

## Core Workflow

1. Treat the current Obsidian vault as the source of truth. In this workspace, read vegetable facts from `knowledge/vegetables/` and writing guidance from `knowledge/style/`.
2. If the user writes `knowladge`, interpret it as `knowledge` unless an actual `knowladge/` folder exists.
3. Search first with `rg --files knowledge` and then read only the relevant vegetable and style files.
4. Base the introduction only on information found in the notes or explicitly provided by the user. Do not invent cultivar names, growing methods, harvest timing, taste claims, certifications, pesticide practices, or health benefits.
5. When source information is missing, either ask for the missing fact or write around it in general language without pretending it is known.
6. Produce polished Japanese copy that feels warm, concrete, and useful to customers.

## Source Priority

Use facts in this order:

1. The user's latest instructions.
2. Matching files under `knowledge/vegetables/`.
3. Style and tone instructions under `knowledge/style/`.
4. General culinary knowledge, only for ordinary preparation or storage suggestions and only when not contradicting the notes.

When multiple vegetable notes conflict, mention the conflict briefly and ask which note to trust.

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

## Knowledge Notes

Read `references/knowledge-layout.md` when creating or reorganizing the source notes in `knowledge/vegetables/` or `knowledge/style/`.
