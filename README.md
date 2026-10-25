# My personal Blog

## local

```bash
# only once, intial setup
uv venv
source .venv/bin/activate
uv pip install -r requirements
nikola init . # or: uv run nikola ...

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

Ich habe in `steffi.py` eine Erweiterung, die dafür sorget, dass wenn in `posts/` oder Unterordnern davon eine `frontmatter.default.yaml` liegt, diese in das frontmatter der Posts integriert werden:

* Frontmatter-Settings direkt im Post haben Vorrang
* `frontmatter.default.yaml` vererbt sich auch in Unterordner (aber je näher dran, desto höherrangig)
