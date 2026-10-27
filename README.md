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
  * extra pip Paket und bisschen Erweiterung der [zensical.toml](zensical.toml).
  * wenn eine extra deutsche Übersetzung dazukommt, dann Dateiendung `.de.md` statt `.md` und gleicher Basename. 
	  * Ein Artikel kann auch nur auf deutsch verfügbar sein, aber auf englisch nicht
	  * Wenn sich der generierte [Titel](https://zensical.org/docs/authoring/markdown/?h=title#page-title) in den Sprachen unterscheidet, weil z.B. `title` gesetzt ist, oder eine H1-Heading am anfang des Artikels auftaucht, erscheint der Artikel in der non-default Sprache doppelt auf den Indexseiten.
  * der Befehl `[uv run] zensical` wird ersetzt durch `[uv run] zensical-i18n`, auch im Github Workflow
  * > [!NOTE] Frontmatter Metadaten in jeder Übersetzung separat pflegen
	  * sprachspezifischer `draft` möglich
	  * `title` kommt eh aus der 1. Überschrift
* [Giscus](https://giscus.app/) Kommentare: [comments partial](overrides/partials/comments.html) und [giscus.json](giscus.json) (Interface nur englisch)

* im Blog funktionieren Kategorien - es werden automatisch Übersichtsseiten generiert, anklickbare Links zur Kategorie im Blogbeitrag
* tags werden auf blogposts zwar angezeigt (nach Ergänzung von `[project.plugins.tags]`in der config), aber nicht anklickbar, Übersichtsseite, muss explizit angelegt werden.
* [Emoji](https://zensical.org/docs/authoring/icons-emojis/): z.B. [Lucide](https://lucide.dev/icons/)  oder FontAwesome
* Frontmatter `draft: true` ist nur für Blogposts relevant, ansonsten gilt die Konfig (in meinem Fall Ablage in einem `drafts/` Ordner oder Benennung `*.draft.[de.]md`)

### Drafts

TLDR:
* for blogposts, put them into a `drafts/` folder containing a `meta.yml` file with  `draft: true` frontmatter. Move them out, when finished.
* pages: put into a `drafts/` folder or configure a `not_in_nav` matching for hidden access after `build`.

Long:
* in  `[project]` settings: I configured [`draft_docs`](https://zensical.org/docs/setup/basics/?h=draft#draft_docs) to match everything in `draft/` dirs oder with `*.draft.md` names
   * such pages/posts are not published or auto-linked during `zensical build` process, when trying to access them directly via URL, you'll get a 404.
   * `serve` mode:
	   * PAGES are not linked in automatic navigation, but can be opened by URL (a filename part `.draft` also becomes part of the URL)
	   * BLOGPOSTS are linked in the blog index without _draft_ marker  (considering the fact they are linked as a bug, but it's useful and convenient)
	   * content view will contain a _draft_ marker
* frontmatter setting `draft: true` (directly or via `meta.yml` in containing folder or parent polder). 
	* frontmatter setting has no effect for pages, only for blog posts.
	* during `serve`, blog posts will get a _draft_ marker on index pages, but not in their content view.
	* after `build`, blog posts with frontmatter draft won't be published.