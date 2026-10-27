---
date: 2026-10-27
slug: zensical-setup
---
# My Blogging decision and setup as of October 2026

After some research and testing, my markdown powered blog is now powered by [Zensical](https://zensical.org/docs/create-your-site/), the `mkdocs`successor.

Here I am writing about the Why and How.
<!-- more -->
## my needs
* static site generator (simple & secure, no PHP, not databases)
* looking good by default
* easy and uncomplicated usage
* preferably python powered, although this is not a must
* I want to use Obsidian for writing: what looks good on my system (or on my mobile), should also look good after publishing
* multilanguage would be really nice
* I want to integrate my crochet patterns from [Ravelry](https://www.ravelry.com/designers/hookiewookie) for sale in the future. I know that this works with SSGs because I tested it with mkdocs in the past.
* I want to concentrate on content. Design will follow, when I have energy for it.
## what I've tried, but did not work for me
* nikola, pelican: markdown links don't work out of the box. I would have to use extra shortcodes for links that work after publishing. That makes me tool-dependant and disturbes flow when writing. I want to concentrate on content and not on the tools.
* mkdocs: 1.x - unmaintained, 2.x seems to loose community support because no more plugin support (but I want i18n, comments, and maybe more in the future)
* so, I am now working with zensical, an mkdocs fork.

## local setup

```bash
# only once, intial setup
uv venv
source .venv/bin/activate
uv pip install -r requirements
#only for new sites: #zensical new .

# to upgrade
uv pip install --upgrade -r requirements.txt

# local server with live reload
[uv run] zensical serve
[uv run] zensical-i18n serve [--lang de] # ✅ linux ❌ windows

# build
[uv run] zensical build --clean
[uv run] zensical-i18n build --clean  # ✅ linux ❌ windows
```

*  2026-10 use the command `zensical-i18n` instead of `zensical` for everything, until plugins are fully supported

## Blog Configuration

### Multilanguage

* I am using [`zensical-i18n`](https://github.com/hsandmann/zensical-i18n) for the site to become multilanguage.
  * everything as usual, english is default.
  * add that extra pip package and configure [zensical.toml](zensical.toml).
  * for additional german translations of articles, change the file suffix from `.md` to `.de.md` but __keep the same file basename__. 
  * a post or page can also be available only in the extra language, but not in the default language
  * replace the command `[uv run] zensical` by `[uv run] zensical-i18n` &mdash; also in the Github workflow
  * frontmatter data is not inherited between languages
	  * language specific `draft` mode and `date`s
	  * language specific [title](https://zensical.org/docs/authoring/markdown/?h=title#page-title), can come from frontmatter or from first H1 heading
### Comments
* I am using [Giscus](https://giscus.app/) comments, configured in the  [comments partial](overrides/partials/comments.html) and [giscus.json](giscus.json) (interface is always in default language), enabled `custom_dir = "overrides"` in `[project.theme]` of the config
* this was the first system I tried, it works out of the box. It is free and open source, so I did not research alternatives.

### Categories and Tags
* Category index pages for blog posts are auto generated, you get clickable links in the metadata sidebar in content view of the post.
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

### Obsidian Git Sync on Mobile
* Obsidian: enable community plugins, add the Git ("by Vinzent") community plugin and configure it
* `echo .obsidian/ >> .gitignore` (a more finegrained exclude might be possible here, to have some of your settings in sync, but I am too busy for testing that at the moment)
* on your desktop system, copy the whole repository workspace and change the remote from ssh to https
* create a fine grained personal github token to access the repo
* create a zip from that copy and transfer it to your mobile
* on your mobile, unzip, open that vault in obsidian, configure the git community plugin - it will ask for your token