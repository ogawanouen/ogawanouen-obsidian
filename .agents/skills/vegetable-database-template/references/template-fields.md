# Vegetable Database Template Fields

Use these fields when creating or reviewing vegetable database templates.

For frontmatter-specific controlled vocabulary and examples, see `frontmatter-guide.md`.

## YAML Frontmatter

- `type`: always `vegetable-database`
- `aliases`: alternate names or spellings
- `status`: use `draft` for blank templates and `general-draft` for general-info-filled templates
- `template_mode`: either `blank` or `general`
- `created`: ISO date if known
- `updated`: ISO date if known
- `category_large`, `category_medium`, `category_small`: search and sales grouping fields from `frontmatter-guide.md`
- `crop_family`, `edible_part`, `color`, `shape`, `size_class`, `texture`, `flavor`: compact classification fields from `frontmatter-guide.md`
- `best_uses`, `sales_angle`: list fields from `frontmatter-guide.md`

## Body Sections

Use Japanese headings:

- `# <野菜名>`
- `## 基本情報`
- `## 栽培情報`
- `## 収穫・出荷`
- `## 味・食感・香り`
- `## おすすめの食べ方`
- `## 保存方法`
- `## 紹介文に使える素材`
- `## 避けたい表現・注意点`
- `## メモ`
- `## 参考情報源`
- `## 更新履歴`

Keep empty placeholders easy to fill in. Prefer list items and short prompts over long explanations.

`category_small` is the only duplicate-detection identity field. Do not add legacy `vegetable` frontmatter to newly created databases.

## Template Modes

`blank` mode:

- Fill only the vegetable name, headings, frontmatter dates, `status`, and `template_mode`.
- Leave item values empty so the user can enter only confirmed Ogawa Nouen facts.

`general` mode:

- Pre-fill ordinary culinary, storage, and handling information from web research.
- Keep farm-specific cultivation, harvest, and field details empty unless the user provides them.
- Include a note that general content should be checked and replaced with Ogawa Nouen-specific facts.
- Include source titles and URLs under `参考情報源`.
- Omit uncertain facts instead of filling them from memory.
