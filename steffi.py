import os
import yaml

def apply_folder_frontmatter_defaults(site):
    defaults_cache = {}

    # Nikola übergibt hier das Site-Objekt direkt
    for post in site.timeline:
        source_path = post.source_path
        if not source_path:
            continue
        
        current_dir = os.path.dirname(source_path)
        dirs_to_check = []
        d = current_dir
        while d:
            dirs_to_check.append(d)
            parent = os.path.dirname(d)
            if parent == d or not parent:
                break
            d = parent

        dirs_to_check.reverse()

        merged_defaults = {}
        for d in dirs_to_check:
            default_file = os.path.join(d, "frontmatter.default.yaml")
            if os.path.exists(default_file):
                if default_file not in defaults_cache:
                    try:
                        with open(default_file, "r", encoding="utf-8") as f:
                            defaults_cache[default_file] = yaml.safe_load(f) or {}
                    except Exception:
                        defaults_cache[default_file] = {}
                    
                for k, v in defaults_cache[default_file].items():
                    merged_defaults[k] = v

        for key, value in merged_defaults.items():
            if key not in post.meta or not post.meta[key]:
                post.meta[key] = value

        if post.meta.get("status") == "draft":
            post._is_draft = True

# (Wird am Ende der conf.py registriert)
