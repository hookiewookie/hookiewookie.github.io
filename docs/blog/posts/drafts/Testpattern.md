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
---

# Ravelry patterns inside zensical / mkdocs blog

* `ravelry.py` module in project root, which generates a `{{ ravelry_block() }}` jinja shortcode to be used in posts
* `ravelry.yaml` with default data in project root (overwriteable in per-post frontmatter)

* Value: {{ 1 + 1 }}
* Cart: {{ ravelry_cart_id }}
* pattern: {{ ravelry_pattern_id }}

{{ ravelry_block() }}

<!-- more -->

The complete post continues here.

{% for tag in page.meta.tags %}

- {{ tag }}

{% endfor %}