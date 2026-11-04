"""Finishing pass over the DITA-OT HTML5 output: links the theme script, fixes header paths,
adds the dark versions of figures and builds the home page from the topic pages."""
import glob, html, os, re, shutil, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from meta import fix as fix_meta

out, src, build = sys.argv[1], sys.argv[2], sys.argv[3]
SITE = "https://archanacontent.github.io/medically-frail-guide/"

os.makedirs(f"{out}/js", exist_ok=True)
shutil.copy(f"{build}/html/frail.js", f"{out}/js/frail.js")
for f in glob.glob(f"{src}/images/*-dark.svg"):
    shutil.copy(f, f"{out}/images/")
if os.path.exists(f"{build}/og.png"):
    shutil.copy(f"{build}/og.png", f"{out}/og.png")
open(f"{out}/.nojekyll", "w").close()

def finish(page, rel, title, desc, url):
    page = page.replace('href="ROOT/', f'href="{rel}/')
    og = (f'<meta property="og:title" content="{html.escape(title)}">'
          f'<meta property="og:description" content="{html.escape(desc)}">'
          f'<meta property="og:type" content="article"><meta property="og:url" content="{url}">'
          f'<meta property="og:image" content="{SITE}og.png"><meta name="twitter:card" content="summary_large_image">'
          f'<script src="{rel}/js/frail.js" defer></script>')
    return page.replace("</head>", og + "</head>", 1)

topics = {}
for path in sorted(glob.glob(f"{out}/topics/*.html")):
    page = open(path, encoding="utf-8").read()
    title = re.search(r"<title>(.*?)</title>", page).group(1)
    m = re.search(r'<meta name="description" content="(.*?)">', page)
    desc = html.unescape(m.group(1)) if m else ""
    name = os.path.basename(path)
    page = fix_meta(page, name)
    topics[name] = (title, desc)
    open(path, "w", encoding="utf-8").write(finish(page, "..", title, desc, SITE + "topics/" + name))

# Home page: reuse a topic page's frame, replace the article with a hero and topic cards.
frame = open(f"{out}/topics/overview.html", encoding="utf-8").read()
frame = frame.replace('href="../', 'href="').replace('src="../', 'src="').replace(' class="active"', "")
frame = frame.replace('href="who-counts.html', 'href="topics/who-counts.html')
order = [("overview.html", "Start here"), ("who-counts.html", "Concept"), ("october-ruling.html", "Concept"),
         ("find-in-data.html", "Task"), ("data-falls-short.html", "Task"), ("rules-and-dates.html", "Reference")]
cards = "".join(
    f'<li><a href="topics/{n}"><span class="k">{k}</span><span class="t">{topics[n][0]}</span><span class="d">{html.escape(topics[n][1])}</span></a></li>'
    for n, k in order)
hero = (
    '<main role="main"><article class="hero" aria-labelledby="home-title">'
    '<p class="eyebrow">Medicaid 2027 Series - Part 2</p>'
    "<h1 id=\"home-title\">Medically Frail: The Exemption States Can't Afford To Get Wrong</h1>"
    '<p class="lede">Members who are medically frail are exempt from Medicaid work requirements, but only if the state can find them in its own data. '
    "Here is who qualifies, what the October 29, 2026 ruling changed, and how to identify frail members before a notice ever goes out.</p>"
    '<a class="cta" href="topics/overview.html">Start reading</a> <a class="cta ghost" href="medically-frail.pdf">Download PDF</a> <a class="cta ghost" href="is-this-member-exempt.pdf">Caseworker one-pager</a>'
    '<p class="meta">For state eligibility and policy teams, and the vendors who build their systems. Updated November 2026.</p>'
    f'<ul class="cards">{cards}</ul></article></main>')
frame = re.sub(r"<main role=\"main\">.*?</main>", lambda _: hero, frame, flags=re.S)
frame = frame.replace('<body id="overview">', '<body id="home" class="home">')
frame = re.sub(r"<title>.*?</title>", "<title>Medically Frail Guide</title>", frame)
desc = "Who counts as medically frail, what the October 29, 2026 ruling changed, and how states can find frail members in their own data."
frame = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', frame)
frame = re.sub(r'<meta property="og:.*?<script src="\.\./js/frail\.js" defer></script>', "", frame, flags=re.S)
frame = frame.replace('href="../', 'href="')
open(f"{out}/index.html", "w", encoding="utf-8").write(
    finish(frame.replace('href="ROOT/', 'href="./'), ".", "Medically Frail: The Exemption States Can't Afford To Get Wrong", desc, SITE))
print("finished", len(topics), "topics")
