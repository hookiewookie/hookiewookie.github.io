---
date: 
  created: 2026-11-02
  updated: 2026-11-02
categories:
  - shop
  - patterns
tags:
  - crochet
  - clothing
draft: true
ravelry_pattern_id: 967219
ravelry_cart_id: 5421
ravelry_pattern_slug: children-sweater-1-moss
icon: lucide/braces
links:
  - Zensical Macros: https://github.com/python33r/zensical-docs/blob/master/docs/setup/extensions/macros.md
---

# Ravelry Example and HowTo

* write a `ravelry.py` module in the project root, which provides a `ravelry_block()` jinja shortcode to be used in posts
* provide a `ravelry.yaml` in the project root with default data in project root (overwriteable in per-post frontmatter)
* `zensical.toml`:  make zensical know these:

```toml
[project.markdown_extensions]
zensical.extensions.macros = { module_name = "ravelry", include_yaml = ["ravelry.yaml"]  }
```
* if you don't want to write your own python modules, but want to use jinja inside your markdown documents, you can write  `zensical.extensions.macros = {}`

* Value: {{ 1 + 1 }}
* Cart: {{ ravelry_cart_id }}
* pattern: {{ ravelry_pattern_id }}

{{ ravelry_block() }}

<!-- more -->

The complete post continues here.

{% for tag in page.meta.tags %}

- {{ tag }}

{% endfor %}