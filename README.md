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
```

### deployment
on gh pages or similar:
```bash
nikola build
```


