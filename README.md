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
* for blogposts set `draft: true` setzen (`meta.yml` works, too).

Long:
* in  `[project]` settings: [`draft_docs`](https://zensical.org/docs/setup/basics/?h=draft#draft_docs) match everything in `draft/` dirs oder with `*.draft.md` names
   * such pages/posts are not published or auto-linked during `zensical build` process, when trying to access them directly via URL, you'll get a 404.
   * `serve` mode:
	   * PAGES are not linked in automatic navigation, but can be opened by URL (a filename part `.draft` also becomes part of the URL)
	   * BLOGPOSTS are linked in the blog index without _draft_ marker  (considering the fact they are linked as a bug, but it's useful)
	   * content view will contain a _draft_ marker
* frontmatter setting `draft: true` (directly or via `meta.yml` in containing folder or parent polder). 
	* frontmatter setting has no effect for pages, only for blog posts.
	* blog posts can have a frontmatter 
	* during `serve`, blog posts will get a _draft_ marker on index pages, but not in their content view.
	* after `build`, blog posts with frontmatter draft won't be published..