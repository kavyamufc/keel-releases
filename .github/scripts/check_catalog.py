#!/usr/bin/env python3
"""Daily check of Keel's source catalog (Batch 14, 14.6): every entry must still answer with a version.
Prints one line per entry and exits 1 with the broken ones listed in broken.txt."""
import json, re, sys, urllib.request

def get(url, accept=None):
    req = urllib.request.Request(url, headers={"User-Agent": "Keel catalog check", **({"Accept": accept} if accept else {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")

def check(entry):
    # {installed} stands for the app's installed version; an old one makes a service answer with its latest.
    kind, source = entry["kind"], entry["source"].replace("{installed}", "1.0.0")
    if kind == "page":
        plain = re.sub(r"<[^>]+>", " ", get(source)).replace("&nbsp;", " ")
        m = re.search(entry["pattern"].replace("(?<", "(?P<"), plain, re.I)
        return m.group("version") if m else None
    if kind == "sparkle":
        m = re.search(r'sparkle:shortVersionString="?>?([^"<]+)', get(source)) or re.search(r'sparkle:version="?>?([^"<]+)', get(source))
        return m.group(1) if m else None
    if kind == "github":
        return json.loads(get(f"https://api.github.com/repos/{source}/releases/latest", "application/vnd.github+json")).get("tag_name")
    if kind == "json":
        cur = json.loads(get(source))
        for key in entry["keyPath"].split("."):
            cur = cur[int(key)] if isinstance(cur, list) else cur[key]
        return str(cur)
    return None

catalog = json.load(open("catalog.json"))
broken = []
for bundle_id, entry in sorted(catalog["apps"].items()):
    try:
        version = check(entry)
    except Exception as e:
        version, why = None, str(e)
    else:
        why = "no version found"
    print(f"{entry['name']} ({bundle_id}): {version or 'BROKEN — ' + why}")
    if not version:
        broken.append(f"- **{entry['name']}** (`{bundle_id}`, {entry['kind']} {entry['source']}): {why}")
if broken:
    open("broken.txt", "w").write("\n".join(broken) + "\n")
    sys.exit(1)
