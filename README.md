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
zensical serve
zensical-i18n serve
```

Hint:
*  20261025 use command `zensical-i18n` instead of `zensical` for everything, until pugins are fully supported

## Extra Info

* ich nutze `zensical-i18n` damit die Site Multilanguage wird.
  * alles bleibt "normal", englisch ist default
  * wenn eine extra deutsche Übersetzung dazukommt, dann Dateiendung `.de.md` statt `.md`
  * extra pip Paket und bisschen Erweiterung der [zensical.toml](zensical.toml).
  * der Befehl `[uv run] zensical` wird ersetzt durch `[uv run] zensical-i18n`, auch im Github Workflow
* Giscus Kommentare: [comments partial](overrides/partials/comments.html) und [giscus.json](giscus.json) (Interface nur englisch)
