"""Keep every page's meta description within 155 characters, in whole sentences.

Used by postprocess.py during a build. Run it directly on a built site folder
(python3 build/meta.py out/site) to apply the same rule to existing pages.
"""
import glob, html, os, re, sys

LIMIT = 155
WRITTEN = {
    "glossary.html": "Definitions of the Medicaid eligibility and medical frailty terms used in the Medically Frail guide.",
}


def trim(desc):
    desc = re.sub(r"\s+", " ", desc).strip()
    if len(desc) <= LIMIT:
        return desc
    out = ""
    for s in re.split(r"(?<=[.!?])\s+", desc):
        nxt = (out + " " + s).strip()
        if len(nxt) > LIMIT:
            break
        out = nxt
    return out or desc[:LIMIT].rsplit(" ", 1)[0] + "."


def fix(page, name):
    m = re.search(r'<meta name="description" content="(.*?)">', page)
    current = html.unescape(m.group(1)) if m else ""
    desc = WRITTEN.get(name) if not current else trim(current)
    if not desc:
        return page
    tag = f'<meta name="description" content="{html.escape(desc)}">'
    if m:
        return page[:m.start()] + tag + page[m.end():]
    return page.replace("</title>", "</title>" + tag, 1)


if __name__ == "__main__":
    root = sys.argv[1]
    for path in glob.glob(os.path.join(root, "**", "*.html"), recursive=True):
        page = open(path, encoding="utf-8").read()
        new = fix(page, os.path.basename(path))
        if new != page:
            open(path, "w", encoding="utf-8").write(new)
            print("updated", os.path.relpath(path, root))
