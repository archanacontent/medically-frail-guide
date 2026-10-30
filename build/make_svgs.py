# Draws the guide's visuals as static SVGs: <name>.svg (light, used by PDF and light mode) and <name>-dark.svg
import sys, textwrap
OUT = sys.argv[1]
THEMES = {
  'light': dict(bg='#f2f7fd', card='#ffffff', edge='#cfe0f3', ink='#0f2236', mute='#4f6478', az='#0078d4', risk='#c8432f', ok='#107c41', warn='#9a5800', deep='#005a9e', arrow='#7f97ad'),
  'dark':  dict(bg='#0f1c2b', card='#132436', edge='#24405e', ink='#e8f1fb', mute='#a7bbcf', az='#4ca8ff', risk='#f0766a', ok='#5fd39a', warn='#f2b45a', deep='#2b7fd0', arrow='#6f88a0'),
}
FONT = 'font-family="IBM Plex Sans, Segoe UI, Arial, sans-serif"'
def svg(w, h, body, c):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" {FONT}><rect width="{w}" height="{h}" rx="14" fill="{c["bg"]}"/>{body}</svg>'
def t(x, y, s, size, fill, weight=400, anchor='start', extra=''):
    s = s.replace('&', '&amp;').replace("'", '&#8217;')
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {extra}>{s}</text>'

def key_numbers(c):
    items = [('Jan 1, 2027', 'Work requirements begin in most states'), ('12 months', 'Of claims data states can use to verify frailty'),
             ('30 days', 'For a member to answer a noncompliance notice'), ('Once', 'Self-declaration allowed per enrollment period from 2028')]
    W, H = 520, 292; b = ''
    for i, (n, d) in enumerate(items):
        x = 16 + (i % 2) * 252; y = 16 + (i // 2) * 136
        b += f'<rect x="{x}" y="{y}" width="236" height="124" rx="12" fill="{c["card"]}" stroke="{c["edge"]}"/><rect x="{x}" y="{y+18}" width="4" height="88" rx="2" fill="{c["az"]}"/>'
        b += t(x+20, y+46, n, 27, c['az'], 700)
        for j, ln in enumerate(textwrap.wrap(d, 25)): b += t(x+20, y+74+j*20, ln, 15, c['mute'])
    return svg(W, H, b, c)

def timeline(c):
    ev = [('JUNE 3, 2026', 'CMS publishes the interim final rule', 'Adds a test that a condition must significantly impair the member\'s ability to comply.', 'az', False),
          ('SEPTEMBER 2026', 'CMS issues frailty guidance', 'An optional three-tier framework for finding frail members in data.', 'az', False),
          ('OCTOBER 29, 2026', 'Federal court strikes down the added test', 'The 12-month data limit and the 2028 self-declaration limit stay in place.', 'risk', False),
          ('JANUARY 1, 2027', 'Work requirements begin', 'In most states.', 'az', True),
          ('JANUARY 1, 2028', 'Self-declaration narrows', 'Once per enrollment period, then data or documentation.', 'az', True)]
    W = 520; y = 40; b = ''; pts = []
    for d, ti, s, col, fut in ev:
        pts.append(y)
        b += t(64, y+5, d, 13, c[col], 600, extra='letter-spacing="0.6"')
        lines = textwrap.wrap(ti, 34); 
        for j, ln in enumerate(lines): b += t(64, y+30+j*22, ln, 18, c['ink'], 600)
        yy = y+30+(len(lines)-1)*22
        sl = textwrap.wrap(s, 48)
        for j, ln in enumerate(sl): b += t(64, yy+24+j*20, ln, 15, c['mute'])
        y = yy+24+(len(sl)-1)*20+40
    H = y-10
    dots = f'<line x1="36" y1="{pts[0]}" x2="36" y2="{pts[-1]}" stroke="{c["edge"]}" stroke-width="2"/>'
    for (d, ti, s, col, fut), py in zip(ev, pts):
        if col == 'risk': dots += f'<circle cx="36" cy="{py}" r="9" fill="{c["risk"]}"/>'
        else: dots += f'<circle cx="36" cy="{py}" r="8" fill="{c["bg"]}" stroke="{c["az"]}" stroke-width="2.5" {"stroke-dasharray=\"3 3\"" if fut else ""}/>' + ('' if fut else f'<circle cx="36" cy="{py}" r="3.5" fill="{c["az"]}"/>')
    return svg(W, H, dots+b, c)

def data_first(c):
    st = [('State condition list', 'Five federal groups, mapped to codes', 'az'), ('12 months of claims', 'Paid, pended and denied, plus encounters', 'az'),
          ('Tier 1 match', 'Exempt with no request', 'ok'), ('Tier 2 or 3', 'More data, then caseworker review', 'warn'), ('Member proof', 'Statement or documentation', 'risk')]
    W, bh, gap = 520, 70, 28; H = 24 + len(st)*(bh+gap) - gap + 16; b = ''
    for i, (ti, s, col) in enumerate(st):
        y = 20 + i*(bh+gap); inset = i*16; x = 16+inset; w = W-32-inset*2
        b += f'<rect x="{x}" y="{y}" width="{w}" height="{bh}" rx="12" fill="{c["card"]}" stroke="{c[col]}" stroke-width="2"/>'
        b += t(W/2, y+31, ti, 18, c['ink'], 600, 'middle') + t(W/2, y+54, s, 15, c['mute'], 400, 'middle')
        if i < len(st)-1: b += f'<path d="M{W/2} {y+bh+5} v{gap-10} m-6 -6 l6 6 l6 -6" fill="none" stroke="{c["arrow"]}" stroke-width="2"/>'
    return svg(W, H, b, c)

def losses(c):
    rows = [('Baseline projection', '6.4M a year', 6.4, 'deep', False), ('With the rule\'s added limits', '8.2M a year', 8.2, 'risk', False), ('Added by the rule', '1.8M a year', 1.8, 'risk', True)]
    W, H = 520, 276; b = f'<defs><pattern id="h" width="10" height="10" patternTransform="rotate(45)" patternUnits="userSpaceOnUse"><rect width="5" height="10" fill="{c["risk"]}"/></pattern></defs>'
    for i, (l, v, n, col, hatch) in enumerate(rows):
        y = 40 + i*80; bw = (W-48)*n/8.2
        b += t(24, y, l, 16, c['ink']) + t(W-24, y, v, 16, c['ink'], 700, 'end')
        b += f'<rect x="24" y="{y+12}" width="{W-48}" height="34" rx="7" fill="{c["card"]}" stroke="{c["edge"]}"/>'
        b += (f'<rect x="24" y="{y+12}" width="{bw}" height="34" rx="7" fill="url(#h)" stroke="{c["risk"]}" stroke-width="1.5"/>' if hatch else f'<rect x="24" y="{y+12}" width="{bw}" height="34" rx="7" fill="{c[col]}"/>')
    return svg(W, H, b, c)

for name, fn in [('key-numbers', key_numbers), ('timeline', timeline), ('data-first', data_first), ('projected-losses', losses)]:
    for theme, c in THEMES.items():
        open(f'{OUT}/{name}{"" if theme=="light" else "-dark"}.svg', 'w').write(fn(c))
print('ok')
