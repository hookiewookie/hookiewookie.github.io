# My personal Blog

my markdown powered blog, using [Zensical](https://zensical.org/docs/create-your-site/)

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
nikola auto
nikola help # for more info
```

### deployment
on gh pages or similar:
```bash
nikola build
```

## blog cheatsheet Nikola

```bash
nikola new_post -e                  # -e for opening the editor of your choice
nikola new_post -e -f markdown      # markdown
```

## Extra Info

* Ich habe in `steffi.py` eine Erweiterung, die dafür sorgt, dass wenn in `posts/` oder Unterordnern davon eine `frontmatter.default.yaml` liegt, diese in das frontmatter der Posts integriert werden:
  * Frontmatter-Settings direkt im Post haben Vorrang
  * `frontmatter.default.yaml` vererbt sich auch in Unterordner (aber je näher dran, desto höherrangig)
* manuell deploy triggern: `git commit --allow-empty -m "Empty-Commit #deploy"`
