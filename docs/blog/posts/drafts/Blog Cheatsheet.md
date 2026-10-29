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

* check die Metadaten dieses Artikels
	* Links für die Sidebar
	* `date` entweder direkt oder `created`/`updated` 
* Emoji und Icons im Text:
	* :lucide-moon: <--> `:lucide-moon:` von [lucide.dev](https://lucide.dev/icons/)
	* :tada: <-> ` :tada:` [GitHub Emoji](https://github.com/markdown-templates/markdown-emojis)
	* :panda: :lucide-zoom-in:
	* Lucide und die anderen funktionieren dank [Obsidian Shortcode Icons](https://github.com/kablys/obsidian-shortcode-icons) Plugin auch in Obsidian mit autocomplete ab dem 2. Zeichen nach dem `:` 
	* in Obsidian gehen die Lucide Icons auch ohne `lucide-` Prefix, in Zensical muss man es voranstellen
	* :fontawesome-regular-face-laugh-wink: <--> `:fontawesome-regular-face-laugh-wink:`von [FontAwesome](https://fontawesome.com/search) (geht nur im Blog)
	* in `zensical.toml` können solche Icons auch gesetzt werden für Tags im Schlagwortverzeichnis oder als Icon für den Blog und für einzelne Seiten (out of the Box ohne extra Config), hier gehen noch mehr (aber nicht alle in Obsidian): https://zensical.org/docs/authoring/icons-emojis/?h=icons#included-icon-sets
	* UTF-8 geht sowieso out-of-the-box: 💩🎃
	