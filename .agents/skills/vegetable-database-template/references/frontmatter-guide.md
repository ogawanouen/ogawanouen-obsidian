# Vegetable Database Frontmatter Guide

Use this guide when creating or updating vegetable database frontmatter.

Core rules:

- Leave uncertain fields blank or add conservative candidates only.
- Fill 小川農園-specific information only when there is a source in the existing database or the user provides it.
- When using general information, keep source URLs in the body under `参考情報源`.
- Prefer short category words, tags, and use words over prose.
- Use values that are useful for search, filtering, POP writing, SNS writing, and product grouping.

## Recommended Frontmatter

```yaml
category_large:
category_medium:
category_small:

crop_family:
edible_part:
color:
shape:
size_class:
texture:
flavor:
best_uses:
sales_angle:
```

## Fields

`category_large`: One broad sales or produce category. Examples: `果菜類`, `葉菜類`, `根菜類`, `いも類`, `豆類`, `香味野菜`, `ハーブ類`, `山菜・野草`, `西洋野菜`, `穀物・雑穀`, `きのこ類`.

`category_medium`: One more specific group under `category_large`. Examples: `トマト類`, `ナス類`, `ウリ類`, `ピーマン・唐辛子類`, `葉物`, `結球野菜`, `根もの`, `かぶ・大根類`, `いも類`, `豆・さや豆類`, `香味・薬味`, `ハーブ`, `西洋葉菜`, `茎を食べる野菜`.

`category_small`: Product-level vegetable name, usually the requested vegetable name. Use a more specific product unit only when it matters for sales, such as `ミニトマト`, `水ナス`, `ビーツ`, `ルバーブ`.

This is the only field used to decide whether the same vegetable database already exists. Do not add or rely on legacy `vegetable` frontmatter.

`crop_family`: Botanical family with `科`, such as `ナス科`, `ウリ科`, `アブラナ科`, `キク科`, `ヒユ科`, `セリ科`, `ユリ科`, `ヒガンバナ科`, `マメ科`, `イネ科`, `タデ科`, `シソ科`.

`edible_part`: Main edible part. Use a scalar for one value or a list for multiple values. Examples: `果実`, `葉`, `茎`, `根`, `塊茎`, `鱗茎`, `花蕾`, `さや`, `種子`, `新芽`, `香り葉`. Put non-edible cautions in the body, not here.

`color`: Main visible color. Use a scalar for one value or a list for mixed-color products. Examples: `赤`, `黄`, `オレンジ`, `緑`, `濃緑`, `紫`, `白`, `黒紫`, `ピンク`, `クリーム`, `複色`, `カラフル`.

`shape`: Representative shape. Examples: `丸い`, `楕円`, `細長い`, `太長い`, `平たい`, `球形`, `円錐形`, `房状`, `さや状`, `葉状`, `茎状`, `ごつごつ`, `しずく形`.

`size_class`: Broad size category for sales and sorting. Examples: `極小`, `小`, `中`, `大`, `特大`, `ミニ`, `一口サイズ`, `細め`, `太め`, `長め`, `規格外あり`.

`texture`: Short texture phrase, 1-3 words. Examples: `みずみずしい`, `しゃきしゃき`, `ぱりっと`, `ほくほく`, `ねっとり`, `とろり`, `やわらかい`, `歯切れがよい`, `肉厚`, `なめらか`, `繊維感あり`.

`flavor`: Short flavor direction, 1-3 words. Examples: `甘い`, `酸味あり`, `甘酸っぱい`, `ほろ苦い`, `香りがよい`, `さっぱり`, `濃い味`, `クセが少ない`, `うまみがある`, `辛みあり`, `青みがある`, `土の香り`.

`best_uses`: List of suitable cooking or sales uses. Prefer these values when possible: `生食`, `焼く`, `煮る`, `炒める`, `蒸す`, `揚げる`, `漬ける`, `茹でる`, `スープ`, `サラダ`, `ジャム`, `ソース`, `薬味`, `彩り`, `作り置き`, `お弁当`, `子ども向け`, `ギフト向け`.

`sales_angle`: List of sales angles that are factual and useful. Prefer these values when possible: `旬`, `珍しい`, `色がきれい`, `食べ比べ`, `料理しやすい`, `香りがよい`, `甘み`, `酸味`, `苦味を楽しむ`, `食感がよい`, `使い切りやすい`, `日持ちしやすい`, `保存しやすい`, `加熱向き`, `生でおいしい`, `子ども向け`, `大人向け`, `ギフト向け`, `セット向き`, `食卓が華やぐ`.

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
crop_family: ナス科
edible_part: 果実
color: 赤
shape: 丸い
size_class: 中
texture: みずみずしい
flavor: 甘酸っぱい
best_uses:
  - 生食
  - サラダ
  - 煮る
  - ソース
  - 彩り
sales_angle:
  - 旬
  - 色がきれい
  - 料理しやすい
```

### ルバーブ

```yaml
category_large: 西洋野菜
category_medium: 茎を食べる野菜
category_small: ルバーブ
crop_family: タデ科
edible_part: 茎
color:
  - 赤
  - 緑
shape: 茎状
size_class: 長め
texture: 繊維感あり
flavor: 酸味あり
best_uses:
  - 煮る
  - ジャム
  - ソース
sales_angle:
  - 珍しい
  - 酸味
  - 食べ比べ
```
