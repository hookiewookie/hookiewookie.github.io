# My personal Blog

my markdown powered blog, using [Zensical](https://zensical.org/docs/create-your-site/), the `mkdocs`successor.

## what I've tried tooo, but did not work for me
* nikola, pelican: markdown links don't work out of the box
* mkdocs:1.x - unmaintained, 2.x seems to loose community support because no more plugin support
* preferring python based tools


## local

```bash
# only once, intial setup
uv venv
source .venv/bin/activate
uv pip install -r requirements
zensical new .

# to upgrade
uv pip install ...

# local server with live reload
[uv run] zensical serve
[uv run] zensical-i18n serve [--lang de]

# build
[uv run] zensical build --clean
[uv run] zensical-i18n build --clean
```

Hint:
*  20261025 use command `zensical-i18n` instead of `zensical` for everything, until pugins are fully supported

## Extra Info

* ich nutze [`zensical-i18n`](https://github.com/hsandmann/zensical-i18n) damit die Site Multilanguage wird.
  * alles bleibt "normal", englisch ist default
  * wenn eine extra deutsche Übersetzung dazukommt, dann Dateiendung `.de.md` statt `.md`
  * extra pip Paket und bisschen Erweiterung der [zensical.toml](zensical.toml).
  * der Befehl `[uv run] zensical` wird ersetzt durch `[uv run] zensical-i18n`, auch im Github Workflow
  * > [!NOTE] Frontmatter Metadaten in jeder Übersetzung separat pflegen
* [Giscus](https://giscus.app/) Kommentare: [comments partial](overrides/partials/comments.html) und [giscus.json](giscus.json) (Interface nur englisch)

* im Blog funktionieren Kategorien - es werden automatisch Übersichtsseiten generiert, anklickbare Links zur Kategorie im Blogbeitrag
* tags werden auf blogposts zwar angezeigt (nach Ergänzung von `[project.plugins.tags]`in der config), aber nicht anklickbar, Übersichtsseite, muss explizit angelegt werden.
* [Emoji](https://zensical.org/docs/authoring/icons-emojis/): z.B. [Lucide](https://lucide.dev/icons/)  oder FontAwesome
* Frontmatter `draft: true` ist nur für Blogposts relevant, ansonsten gilt die Konfig (in meinem Fall Ablage in einem `drafts/` Ordner oder Benennung `*.draft.[de.]md`)

### Drafts

TLDR:
* setze für Blogposts im Frontmatter `draft: true` setzen (oder verzeichnisweise in der `meta.yml`), das funktioniert zuverlässig

Lange Info:
* in  `[project]` gesetzt: `draft_docs` auf alles in `draft/` Verzeichnissen oder mit `*.draft.md` Namen
   * solche PAGES sind nicht in Indexseiten verlinkt, aber über ihre direkte URL erreichbar (`.draft` wird dabei Teil der URL, wenn die Datei `.draft.md` heißt)
   * solche BLOGPOSTS sind im `serve` Modus auf Blogindexseiten ohne Draft-Markierung verlinkt
   * sie haben eine fette `DRAFT` Markierung im Content - beim lokalen `serve` funktioniert das, auf GH Pages ist das CSS zerschossen, oder es kommt 404.
* Blog-Posts können im Frontmatter `draft: true` setzen (oder verzeichnisweise in der `meta.yml`), in Pages hat dies keine Wirkung. Sie sind dann lokal beim `serve` auf Indexseiten mit `DRAFT` markiert (aber nicht direkt auf der content-Seite, da sieht man sie wie "später in echt"), beim Build sind sie nicht verlinkt, aber direkt über ihre URL aufrufbar (mit kaputtem CSS).