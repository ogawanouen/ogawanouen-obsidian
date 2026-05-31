# Vegetable Database Frontmatter Guide

Use this guide when creating or updating vegetable database frontmatter.

Core rules:

- Leave uncertain fields blank or add conservative candidates only.
- Fill 小川農園-specific information only when there is a source in the existing database or the user provides it.
- When using general information, keep source URLs in the body under `参考情報源`.
- Prefer short category words, tags, and use words over prose.
- Use values that are useful for search, filtering, POP writing, SNS writing, and product grouping.
- Write frontmatter arrays on one line with Japanese comma separators: `[値1、 値2]`.
- For controlled fields, choose only from the listed values. If no listed value fits, leave the field blank or update this guide before using a new value.
- In `general` mode, `category_large`, `category_medium`, and `category_small` are required.

## Recommended Frontmatter

```yaml
category_large:
category_medium:
category_small:
market_group: []

crop_family:
edible_part:
color:
shape:
size_class:
best_uses:
```

## Fields

`category_large`: Required controlled field. Choose exactly one from: `果菜類`, `葉菜類`, `根菜類`, `いも類`, `豆類`, `香味野菜`, `ハーブ類`, `山菜・野草`, `穀物・雑穀`, `きのこ類`. Use this for structural produce classification, not cultural or sales grouping.

`category_medium`: Required controlled field. Choose exactly one from: `トマト類`, `ナス類`, `ウリ類`, `ピーマン・唐辛子類`, `葉物`, `結球野菜`, `根もの`, `かぶ・大根類`, `いも類`, `豆・さや豆類`, `香味・薬味`, `ハーブ`, `西洋葉菜`, `茎を食べる野菜`.

`category_small`: Required flexible field. Use the product-level vegetable name, usually the requested vegetable name. Use a more specific product unit only when it matters for sales, such as `ミニトマト`, `水ナス`, `ビーツ`, `ルバーブ`.

This is the only field used to decide whether the same vegetable database already exists. Do not add or rely on legacy `vegetable` frontmatter.

`market_group`: Optional flexible array field for market, cultural, regional, or editorial groupings that should be filterable separately from structural classification. Use one-line array format, such as `[西洋野菜]`. Leave it empty as `[]` when no grouping is useful. Candidate values include `西洋野菜`, `中国野菜`, `イタリア野菜`, `京野菜`, `加賀野菜`, `伝統野菜`, `固定種・在来種`, `珍しい野菜`, `定番野菜`, `ハーブ`, `エスニック野菜`. This field is free-form; add a concise value when it helps search, filtering, article generation, POP planning, or product grouping.

`crop_family`: Optional controlled field. Choose exactly one from: `ナス科`, `ウリ科`, `アブラナ科`, `キク科`, `ヒユ科`, `セリ科`, `ユリ科`, `ヒガンバナ科`, `マメ科`, `イネ科`, `タデ科`, `シソ科`.

`edible_part`: Optional controlled field. Choose one or more from: `果実`, `葉`, `茎`, `根`, `塊茎`, `鱗茎`, `花蕾`, `さや`, `種子`, `新芽`, `香り葉`. Put non-edible cautions in the body, not here.

`color`: Optional controlled field. Choose one or more from: `赤`, `黄`, `オレンジ`, `緑`, `濃緑`, `紫`, `白`, `黒紫`, `ピンク`, `クリーム`, `複色`, `カラフル`.

`shape`: Optional controlled field. Choose exactly one from: `丸い`, `楕円`, `細長い`, `太長い`, `平たい`, `球形`, `円錐形`, `房状`, `さや状`, `葉状`, `茎状`, `ごつごつ`, `しずく形`.

`size_class`: Optional controlled field. Choose exactly one from: `極小`, `小`, `中`, `大`, `特大`, `ミニ`, `一口サイズ`, `細め`, `太め`, `長め`, `規格外あり`.

`best_uses`: Optional controlled field. Choose one or more from: `生食`, `焼く`, `煮る`, `炒める`, `蒸す`, `揚げる`, `漬ける`, `茹でる`, `スープ`, `サラダ`, `ジャム`, `ソース`, `薬味`, `彩り`, `作り置き`, `お弁当`, `子ども向け`, `ギフト向け`.

## AI Fill Rules

Use this order:

1. Existing Ogawa Nouen database facts.
2. The user's current information.
3. Web-confirmed general facts for `general` mode.
4. Blank when uncertain.

Avoid subjective or unsupported frontmatter values such as `おいしい`, `最高`, `絶品`, `安心安全`, `栄養満点`, `健康にいい`, `誰でも好き`.

## Examples

### トマト

```yaml
category_large: 果菜類
category_medium: トマト類
category_small: トマト
market_group: []
crop_family: ナス科
edible_part: 果実
color: 赤
shape: 丸い
size_class: 中
best_uses: [生食、 サラダ、 煮る、 ソース、 彩り]
```

### ルバーブ

```yaml
category_large: 葉菜類
category_medium: 茎を食べる野菜
category_small: ルバーブ
market_group: [西洋野菜]
crop_family: タデ科
edible_part: 茎
color: [赤、 緑]
shape: 茎状
size_class: 長め
best_uses: [煮る、 ジャム、 ソース]
```
