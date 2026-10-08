"""Keep only assets reachable from the generated website's pages and styles."""

import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

TEXT_TYPES = {".html", ".xml", ".css", ".js", ".json", ".svg"}
QUOTED = re.compile(r'''["']([^"'<>\s]+)["']''')
ASSET_PATH = re.compile(r"(?:https://[Ww]en[Tt]ian1111\.github\.io)?/assets/[^\s\"'<>`)]+")
CSS_URL = re.compile(r"url\(\s*([^)]*)\)")
SOURCE_MAP = re.compile(r"sourceMappingURL=([^\s*]+)")


def references(path, root):
    """Follow URLs, module imports, srcsets, CSS URLs and source maps."""
    if path.suffix not in TEXT_TYPES:
        return set()
    text = path.read_text(encoding="utf-8")
    tokens = ASSET_PATH.findall(text) + QUOTED.findall(text)
    tokens += [value.strip("\"' ") for value in CSS_URL.findall(text)]
    tokens += SOURCE_MAP.findall(text)
    found = set()
    for token in tokens:
        # srcset can contain multiple URLs; each absolute asset URL is also
        # captured above. Commas terminate a URL in a generated srcset.
        token = token.rstrip(",;")
        url = urlsplit(token)
        if url.scheme or url.netloc:
            if url.hostname != "wentian1111.github.io":
                continue
        name = unquote(url.path)
        if not name:
            continue
        target = root / name.lstrip("/") if name.startswith("/") else path.parent / name
        target = target.resolve()
        if target.is_relative_to(root) and target.is_file():
            found.add(target)
    return found


def prune(root, apply=False):
    root = root.resolve()
    if not (root / "index.html").is_file() or not (root / "assets").is_dir():
        raise ValueError("Expected a built website with index.html and assets/")
    if (root / "_config.yml").exists():
        raise ValueError("Refusing to prune the source repository")
    files = {path.resolve() for path in root.rglob("*") if path.is_file()}
    if any(not path.is_relative_to(root) for path in files):
        raise ValueError("A file resolves outside the generated website")
    # All published pages remain, including news URLs and the 404 page.
    # Start with index pages and feeds, then follow their asset dependencies.
    reachable = {path for path in files if path.suffix in {".html", ".xml"}}
    reachable |= {root / name for name in ("robots.txt", ".nojekyll", "CNAME") if (root / name).is_file()}
    pending = list(reachable)
    while pending:
        path = pending.pop()
        for target in references(path, root) - reachable:
            reachable.add(target)
            pending.append(target)
    removed = sorted(files - reachable)
    for path in removed:
        print(("REMOVE " if apply else "UNUSED ") + path.relative_to(root).as_posix())
        if apply:
            path.unlink()
    print(f"Kept {len(reachable)} files; {'removed' if apply else 'would remove'} {len(removed)} unused files.")
    return reachable, removed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    prune(args.site, args.apply)
