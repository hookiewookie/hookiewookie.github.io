# setting up a personal Blog

After several my markdown powered blog, using [Zensical](https://zensical.org/docs/create-your-site/), the `mkdocs`successor.

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

### Multilanguage

* I am using [`zensical-i18n`](https://github.com/hsandmann/zensical-i18n) for the site to become multilanguage.
  * everything as usual, english is default.
  * add that extra pip package and configure [zensical.toml](zensical.toml).
  * for additional german transaltions of articles, change the file suffix from `.md` to `.de.md` but __keep the same file basename__. 
	  * a post or page can also be available only in the extra language, but not in the default language
  * replace the command `[uv run] zensical` by `[uv run] zensical-i18n`, also in the Github workflow
  * > [!NOTE] frontmatter data is not inherited between languages
	  * language specific `draft` mode
	  * language specific `title`, can come from frontmatter or from 1.st H1 heading

### Comments
* I am using [Giscus](https://giscus.app/) comments, configured in the  [comments partial](overrides/partials/comments.html) and [giscus.json](giscus.json) (interface is always in default language)

### Categories and Tags
* Category index pages for blog postsare auto generated, you get clickable links in the metadata sidebar in content view of the post.
* tag links in blogposts are shown (after adding `[project.plugins.tags]` to the config), the index page had to be created manually (this is by design).

### Emoji
* for [Emojis](https://zensical.org/docs/authoring/icons-emojis/): i like [Lucide](https://lucide.dev/icons/)  oder FontAwesome

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