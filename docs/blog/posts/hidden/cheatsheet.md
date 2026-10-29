---
date: 
  created: 2026-10-22
  updated: 2026-10-25
date-alternative-format: 2026-10-22
categories:
  - Hello
  - World
tags:
  - blog
  - template
# realeted links for the sidebar:
links:
  - Getting started: template.md
  - template.md#Notes
  - Resources:
      - Zensical Blog HowTo: https://zensical.org/docs/setup/blog/?h=blog#configuration-zensicaltoml
      - Reference: reference/index.md
icon: lucide/volleyball
slug: cheatsheet
#draft: true # sets draft marker on blog index page
---

# Blog-Howto

* erste primäre Überschrift gibt den Titel und den slug (welcher mit `slug` property überschreibbar ist)
* deutschsprachige Artikel brauchen Dateisuffix `.de.md`!
* [Blog Deploy](https://github.com/steffiland/hookiewookie/actions/workflows/docs.yml)
<!-- more -->

## Features

* Emoji und Icons im Text:
	* :lucide-moon: <--> `\:lucide-moon:`
	* :fontawesome-regular-face-laugh-wink: <--> `\:fontawesome-regular-face-laugh-wink:`
	* [lucide.dev](https://lucide.dev/icons/) und [FontAwesome](https://fontawesome.com/search)
	* in `zensical.toml` können solche Icons auch gesetzt werden für Tags im Schlagwortverzeichnis oder als Icon für den Blog und für einzelne Seiten