"""Article generator for kinyu-engineer blog.
Run: python scripts/gen_article.py
Outputs: articleN.html files based on ARTICLES list below.
"""
import json
import os

BASE = 'https://kinyu-engineer.github.io'
SITE = '金融マンがエンジニアになった話'
TODAY = '2026.05.05'
TODAY_ISO = '2026-05-05'

CATEGORY_TAG_BG = {
    '体験談': 'rgba(196,87,42,0.1); color: var(--accent2)',
    'ノウハウ': 'rgba(26,58,42,0.1); color: var(--accent)',
    '比較': 'rgba(139,105,20,0.1); color: var(--accent3)',
    'データ': 'rgba(28,26,22,0.08); color: var(--text2)',
}


def render_section(s):
    """Render a body section. s is a dict with 'h2' and 'blocks' (list)."""
    out = [f'      <h2>{s["h2"]}</h2>']
    for b in s.get('blocks', []):
        if isinstance(b, str):
            out.append(f'      <p>{b}</p>')
        elif b['type'] == 'h3':
            out.append(f'      <h3>{b["text"]}</h3>')
        elif b['type'] == 'p':
            out.append(f'      <p>{b["text"]}</p>')
        elif b['type'] == 'ul':
            out.append('      <ul>')
            for li in b['items']:
                out.append(f'        <li>{li}</li>')
            out.append('      </ul>')
        elif b['type'] == 'highlight':
            out.append('      <div class="highlight">')
            out.append(f'        <p>{b["text"]}</p>')
            out.append('      </div>')
    return '\n'.join(out)


def render_article(a):
    n = a['num']
    fname = f'article{n}.html'
    url = f'{BASE}/{fname}'
    full_title = f'{a["title"]} | {SITE}'
    cat_color = CATEGORY_TAG_BG[a['category']]
    body_html = '\n\n'.join(render_section(s) for s in a['sections'])

    ld = {
        '@context': 'https://schema.org',
        '@type': 'BlogPosting',
        'headline': a['title'],
        'description': a['description'],
        'url': url,
        'mainEntityOfPage': url,
        'datePublished': TODAY_ISO,
        'dateModified': TODAY_ISO,
        'author': {'@type': 'Person', 'name': 'tamal'},
        'publisher': {'@type': 'Organization', 'name': SITE},
        'articleSection': a['category'],
        'inLanguage': 'ja',
    }
    ld_json = json.dumps(ld, ensure_ascii=False, indent=2)

    prev_link = ''
    next_link = ''
    if a.get('prev'):
        pn, pt = a['prev']
        prev_link = f'<a href="article{pn}.html" class="nav-article-link">← 前の記事：{pt}</a>'
    else:
        prev_link = '<a href="index.html" class="nav-article-link">← 記事一覧へ</a>'
    if a.get('next'):
        nn, nt = a['next']
        next_link = f'<a href="article{nn}.html" class="nav-article-link">次の記事：{nt} →</a>'
    else:
        next_link = '<a href="index.html" class="nav-article-link">記事一覧へ →</a>'

    aff = a['affiliate']

    html = f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-QPKSYX94QP"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag("js", new Date());
  gtag("config", "G-QPKSYX94QP");
</script>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{full_title}</title>
<meta name="description" content="{a['description']}">
<meta property="og:title" content="{a['title']}">
<meta property="og:description" content="{a['description']}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="{SITE}">
<meta property="og:locale" content="ja_JP">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{a['title']}">
<meta name="twitter:description" content="{a['description']}">
<link rel="canonical" href="{url}">
<script type="application/ld+json">
{ld_json}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@400;700;900&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg: #F5F0E8; --bg2: #EDE8DC; --card: #FDFAF4;
    --accent: #1A3A2A; --accent2: #C4572A; --accent3: #8B6914;
    --text: #1C1A16; --text2: #5C5648; --text3: #9C9080;
    --border: rgba(28,26,22,0.12); --border2: rgba(28,26,22,0.06);
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: var(--bg); color: var(--text); font-family: 'Noto Serif JP', serif; line-height: 1.9; }}
  nav {{ position: sticky; top: 0; z-index: 100; background: rgba(245,240,232,0.92); backdrop-filter: blur(8px); border-bottom: 1px solid var(--border); padding: 0 2rem; display: flex; align-items: center; justify-content: space-between; height: 52px; }}
  .nav-logo {{ font-size: 13px; font-weight: 700; color: var(--accent); text-decoration: none; }}
  .nav-back {{ font-family: 'DM Mono', monospace; font-size: 12px; color: var(--text2); text-decoration: none; }}
  .nav-back:hover {{ color: var(--accent); }}
  .article-wrap {{ max-width: 720px; margin: 0 auto; padding: 4rem 2rem 6rem; }}
  .article-meta {{ display: flex; align-items: center; gap: 12px; margin-bottom: 1.5rem; }}
  .article-tag {{ font-family: 'DM Mono', monospace; font-size: 10px; padding: 2px 8px; border-radius: 2px; background: {cat_color}; }}
  .article-date {{ font-family: 'DM Mono', monospace; font-size: 11px; color: var(--text3); }}
  .article-title {{ font-size: clamp(1.6rem, 4vw, 2.4rem); font-weight: 900; color: var(--accent); line-height: 1.3; margin-bottom: 1rem; letter-spacing: -0.02em; }}
  .article-lead {{ font-size: 1rem; color: var(--text2); border-left: 3px solid var(--accent2); padding-left: 1.2rem; margin-bottom: 3rem; line-height: 2; }}
  .article-body h2 {{ font-size: 1.3rem; font-weight: 700; color: var(--accent); margin: 2.5rem 0 1rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--border); }}
  .article-body h3 {{ font-size: 1.1rem; font-weight: 700; color: var(--text); margin: 2rem 0 0.8rem; padding-left: 0.8rem; border-left: 3px solid var(--accent3); }}
  .article-body p {{ font-size: 14px; color: var(--text2); margin-bottom: 1.2rem; line-height: 2; }}
  .article-body ul {{ margin: 1rem 0 1.2rem 1.5rem; }}
  .article-body ul li {{ font-size: 14px; color: var(--text2); margin-bottom: 0.5rem; line-height: 1.8; }}
  .highlight {{ background: rgba(196,87,42,0.08); border-radius: 4px; padding: 1.2rem 1.5rem; margin: 1.5rem 0; border-left: 3px solid var(--accent2); }}
  .highlight p {{ margin-bottom: 0; font-size: 14px; color: var(--text); }}
  .affiliate-box {{ background: var(--card); border: 1px solid var(--border); border-radius: 4px; padding: 1.5rem; margin: 2rem 0; }}
  .affiliate-box h4 {{ font-size: 14px; font-weight: 700; color: var(--accent); margin-bottom: 0.5rem; }}
  .affiliate-box p {{ font-size: 12px; color: var(--text2); margin-bottom: 1rem; }}
  .affiliate-btn {{ display: inline-flex; align-items: center; gap: 6px; background: var(--accent2); color: white; font-size: 13px; font-weight: 700; padding: 8px 20px; border-radius: 2px; text-decoration: none; transition: opacity 0.2s; }}
  .affiliate-btn:hover {{ opacity: 0.85; }}
  .affiliate-note {{ font-size: 11px; color: var(--text3); margin-top: 8px; font-family: 'DM Mono', monospace; }}
  .nav-articles {{ display: flex; justify-content: space-between; margin-top: 4rem; padding-top: 2rem; border-top: 1px solid var(--border); gap: 1rem; flex-wrap: wrap; }}
  .nav-article-link {{ font-size: 13px; color: var(--accent); text-decoration: none; font-weight: 700; }}
  .nav-article-link:hover {{ color: var(--accent2); }}
  footer {{ background: var(--accent); padding: 2rem; text-align: center; font-family: 'DM Mono', monospace; font-size: 11px; color: rgba(245,240,232,0.5); }}
  footer a {{ color: rgba(245,240,232,0.7); text-decoration: none; }}
  html {{ scroll-behavior: smooth; }}
  .reading-progress {{ position: fixed; top: 0; left: 0; height: 3px; background: var(--accent2); width: 0; z-index: 200; transition: width 0.1s ease-out; pointer-events: none; }}
</style>
</head>
<body>
<div class="reading-progress" id="readProgress" aria-hidden="true"></div>

<nav>
  <a href="index.html" class="nav-logo">{SITE}</a>
  <a href="index.html" class="nav-back">← 記事一覧</a>
</nav>

<div class="article-wrap">
  <div class="article-meta">
    <span class="article-tag">{a['category']}</span>
    <span class="article-date">{TODAY}</span>
  </div>

  <h1 class="article-title">{a['title']}</h1>

  <p class="article-lead">
    {a['lead']}
  </p>

  <div class="article-body">

{body_html}

    <div class="affiliate-box">
      <h4>{aff['h4']}</h4>
      <p>{aff['p']}</p>
      <a href="#" class="affiliate-btn" target="_blank" rel="sponsored noopener">{aff['btn']} →</a>
      <p class="affiliate-note">※ アフィリエイトリンクです。サービスの品質は変わりません。</p>
    </div>

  </div>

  <div class="nav-articles">
    {prev_link}
    {next_link}
  </div>
</div>

<footer>
  <p>© 2025-2026 {SITE} · <a href="index.html">トップへ</a></p>
</footer>

<script>
  (function() {{
    var bar = document.getElementById('readProgress');
    if (!bar) return;
    function update() {{
      var h = document.documentElement;
      var height = h.scrollHeight - h.clientHeight;
      var pct = height > 0 ? (h.scrollTop / height) * 100 : 0;
      bar.style.width = pct + '%';
    }}
    window.addEventListener('scroll', update, {{ passive: true }});
    window.addEventListener('resize', update);
    update();
  }})();
</script>
</body>
</html>
'''
    return fname, html


def main(articles):
    out_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    written = []
    for a in articles:
        fname, html = render_article(a)
        path = os.path.join(out_dir, fname)
        with open(path, 'w', encoding='utf-8', newline='\n') as fp:
            fp.write(html)
        written.append(fname)
    return written
