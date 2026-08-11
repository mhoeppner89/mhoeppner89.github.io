from __future__ import annotations

import html
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = Path(
    "/Users/mhoeppner/Desktop/Paper/Submitted/rational probability weighting JBEE/current/jbee_theory"
)
SOURCE_TEX = SOURCE_DIR / "paper.tex"
SOURCE_BIB = SOURCE_DIR / "references.bib"
BUILD = Path("/private/tmp/research-landing-rpw-html-build")
OUT_DIR = ROOT / "papers" / "rational-probability-weighting"
OUT_HTML = OUT_DIR / "index.html"

TITLE = "When Linearizing Probability Weights Can Lower Welfare"
DESCRIPTION = (
    "A working paper on probability weighting, ambiguity, and welfare analysis "
    "in rare-loss protection decisions."
)
ABSTRACT = (
    "Probability weighting is frequently interpreted as a behavioral bias, but a "
    "fitted curvature does not constitute a welfare diagnosis. In the context of "
    "a one-shot rare-loss protection model, I show that a linearizing intervention "
    "shifts decision-making from the fitted rare-event weight to a linear application "
    "of a point estimate. While this intervention improves outcome welfare in the "
    "overprotection region under a known-risk benchmark, net welfare only increases "
    "if the gain outweighs the intervention cost. Conversely, when considering an "
    "upper-bound safety benchmark over a credible ambiguity set, this same intervention "
    "can decrease outcome welfare by eliminating protection that the benchmark itself "
    "justifies. This reversal happens when the welfare-relevant risk object exceeds "
    "the point estimate used by the intervention while the weighted baseline still "
    "provides protection. I derive this threshold, map out the policy regions, provide "
    "a Prelec-weighting calibration, and specify treatment-response and diagnostic "
    "objects for an experiment. Thus, rare-loss overweighting is not irrational in "
    "isolation and policy should only alter probability weighting after the welfare "
    "criterion, risk object, damage measure and intervention cost have been fixed."
)
KEYWORDS = [
    "probability weighting",
    "ambiguity",
    "behavioral welfare economics",
    "nudging",
    "risk",
    "insurance",
]


def strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    return " ".join(html.unescape(value).split())


def clean_article(raw: str) -> str:
    body_match = re.search(r"<body>(.*)</body>", raw, flags=re.S)
    if not body_match:
        raise RuntimeError("No <body> block found in converted HTML.")

    body = body_match.group(1)
    start = body.find("<h3 class='sectionHead'><span class='titlemark'>1")
    if start < 0:
        raise RuntimeError("Could not find the first article section.")

    article = body[start:]
    article = re.sub(r"<!--.*?-->", "", article, flags=re.S)
    article = article.replace("\u00a0", " ")
    article = re.sub(r"\n[ \t]+\n", "\n", article)
    article = re.sub(r"\s+(height|width)='[^']*'", "", article)
    article = article.replace("<h3 class='sectionHead'", "<h2 class='sectionHead'")
    article = article.replace("<h3 class='likesectionHead'", "<h2 class='likesectionHead'")
    article = article.replace("</h3>", "</h2>")
    article = article.replace("<h4 class='subsectionHead'", "<h3 class='subsectionHead'")
    article = article.replace("</h4>", "</h3>")
    article = article.replace("<p class='noindent'></p>", "")
    article = article.replace("<p class='indent'></p>", "")
    article = re.sub(r"<p class='(?:noindent|indent)'>\s*</p>", "", article)
    article = re.sub(r"\s{2,}", " ", article)
    return article.strip()


def build_toc(article: str) -> str:
    items: list[str] = []
    pattern = re.compile(
        r"<h2 class='(?:sectionHead|likesectionHead)'>"
        r"(?P<inner>.*?)"
        r"<a id='(?P<id>[^']+)'></a>"
        r"(?P<tail>.*?)</h2>",
        flags=re.S,
    )
    skip_prefixes = (
        "Declaration",
        "Funding",
        "Data availability",
    )
    for match in pattern.finditer(article):
        text = strip_tags(match.group("inner") + match.group("tail"))
        if not text or text.startswith(skip_prefixes):
            continue
        items.append(f"<a href='#{match.group('id')}'>{html.escape(text)}</a>")
    return "\n".join(items)


def page(article: str, toc: str) -> str:
    keyword_tags = "\n".join(f"<span class='tag'>{html.escape(item)}</span>" for item in KEYWORDS)
    abstract = html.escape(ABSTRACT)
    description = html.escape(DESCRIPTION, quote=True)
    title = html.escape(TITLE)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{description}">
  <title>{title} | Martin Höppner</title>
  <style>
    :root {{
      color-scheme: light;
      --ink: #1f2430;
      --muted: #596474;
      --line: #d9dee7;
      --paper: #f6f7f8;
      --surface: #ffffff;
      --accent: #006b67;
      --accent-2: #8f2f44;
      --soft: #e7f0ee;
      --wash: #f2edf0;
      --focus: #b56b00;
      --measure: 780px;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}

    * {{
      box-sizing: border-box;
    }}

    html {{
      scroll-behavior: smooth;
      overflow-x: hidden;
    }}

    body {{
      margin: 0;
      background: var(--paper);
      color: var(--ink);
      line-height: 1.62;
      overflow-x: hidden;
    }}

    a {{
      color: var(--accent);
      text-decoration-thickness: 0.08em;
      text-underline-offset: 0.18em;
    }}

    a:hover {{
      color: var(--accent-2);
    }}

    a:focus-visible {{
      outline: 3px solid var(--focus);
      outline-offset: 3px;
    }}

    .wrap {{
      width: min(1160px, calc(100% - 40px));
      margin: 0 auto;
    }}

    .topbar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      padding: 22px 0;
      font-size: 0.94rem;
    }}

    .brand {{
      font-weight: 750;
      letter-spacing: 0;
    }}

    .nav {{
      display: flex;
      align-items: center;
      gap: 18px;
      flex-wrap: wrap;
    }}

    .nav a {{
      color: var(--ink);
      text-decoration: none;
      border-bottom: 1px solid transparent;
    }}

    .nav a:hover {{
      border-bottom-color: currentColor;
    }}

    .paper-hero {{
      background:
        linear-gradient(115deg, rgba(231, 240, 238, 0.96), rgba(246, 247, 248, 0.92) 58%, rgba(242, 237, 240, 0.94)),
        var(--soft);
      border-bottom: 1px solid var(--line);
    }}

    .hero-body {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) minmax(230px, 0.34fr);
      gap: 42px;
      align-items: end;
      padding: 58px 0 64px;
    }}

    .kicker {{
      margin: 0 0 18px;
      color: var(--accent);
      font-weight: 750;
      font-size: 0.96rem;
    }}

    h1 {{
      margin: 0;
      max-width: 880px;
      font-size: clamp(2.35rem, 5vw, 4.9rem);
      line-height: 1;
      letter-spacing: 0;
      overflow-wrap: break-word;
      hyphens: auto;
    }}

    .byline {{
      margin: 22px 0 0;
      color: var(--muted);
      font-size: clamp(1.02rem, 1.5vw, 1.17rem);
      overflow-wrap: break-word;
    }}

    .meta-panel {{
      border-left: 4px solid var(--accent);
      padding: 4px 0 4px 18px;
    }}

    .meta-panel dl {{
      margin: 0;
      display: grid;
      gap: 11px;
    }}

    .meta-panel dt {{
      color: var(--muted);
      font-size: 0.78rem;
      font-weight: 750;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }}

    .meta-panel dd {{
      margin: 3px 0 0;
      font-weight: 650;
    }}

    .abstract-band {{
      background: var(--surface);
      border-bottom: 1px solid var(--line);
    }}

    .abstract {{
      display: grid;
      grid-template-columns: minmax(180px, 0.32fr) minmax(0, 1fr);
      gap: 38px;
      padding: 34px 0 38px;
    }}

    .abstract h2 {{
      margin: 0;
      font-size: 1.2rem;
      letter-spacing: 0;
    }}

    .abstract p {{
      margin: 0;
      color: var(--muted);
      font-size: 1.05rem;
    }}

    .tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 18px;
    }}

    .tag {{
      border: 1px solid var(--line);
      border-radius: 999px;
      padding: 5px 9px;
      background: color-mix(in srgb, var(--surface) 72%, var(--soft));
      color: var(--ink);
      font-size: 0.86rem;
      font-weight: 700;
    }}

    .article-layout {{
      display: grid;
      grid-template-columns: minmax(190px, 230px) minmax(0, var(--measure));
      gap: 54px;
      align-items: start;
      padding: 48px 0 76px;
    }}

    .paper-toc {{
      position: sticky;
      top: 24px;
      display: grid;
      gap: 5px;
      padding-top: 8px;
      font-size: 0.92rem;
    }}

    .paper-toc h2 {{
      margin: 0 0 10px;
      font-size: 0.84rem;
      color: var(--muted);
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }}

    .paper-toc a {{
      color: var(--ink);
      text-decoration: none;
      border-left: 2px solid transparent;
      padding: 5px 0 5px 10px;
    }}

    .paper-toc a:hover {{
      border-left-color: var(--accent);
      color: var(--accent);
    }}

    article {{
      min-width: 0;
      font-family: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
      font-size: 1.06rem;
      line-height: 1.74;
      overflow-x: clip;
      overflow-wrap: break-word;
    }}

    @supports not (overflow: clip) {{
      article {{
        overflow-x: hidden;
      }}
    }}

    article p {{
      margin: 0;
    }}

    article p + p {{
      margin-top: 1.05em;
    }}

    article h2,
    article h3 {{
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.18;
      letter-spacing: 0;
      scroll-margin-top: 20px;
    }}

    article h2 {{
      margin: 2.4em 0 0.75em;
      font-size: clamp(1.55rem, 2.5vw, 2.15rem);
      border-top: 1px solid var(--line);
      padding-top: 1.05em;
    }}

    article h2:first-child {{
      margin-top: 0;
      border-top: 0;
      padding-top: 0;
    }}

    article h3 {{
      margin: 2em 0 0.65em;
      font-size: 1.22rem;
    }}

    .titlemark {{
      color: var(--accent);
      margin-right: 0.25em;
    }}

    .ec-lmbx-12,
    .ec-lmbx-10x-x-109,
    .ec-lmbx-8 {{
      font-weight: 700;
    }}

    .ec-lmri-12 {{
      font-style: italic;
    }}

    .ec-lmtt-12,
    .ec-lmtt-10x-x-109 {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 0.95em;
    }}

    .newtheorem,
    .proof {{
      margin: 1.9rem 0;
      padding: 1.05rem 1.15rem;
      border-left: 4px solid var(--accent);
      background: var(--surface);
      box-shadow: 0 1px 0 rgba(31, 36, 48, 0.04);
    }}

    .proof {{
      border-left-color: var(--line);
      background: color-mix(in srgb, var(--surface) 78%, var(--paper));
    }}

    .newtheorem .head,
    .proof .head {{
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}

    .paragraphHead,
    .likeparagraphHead {{
      display: inline;
      font-weight: 700;
    }}

    .table {{
      margin: 2rem 0;
      overflow-x: auto;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--surface);
    }}

    figure.float {{
      margin: 0;
      padding: 0;
      min-width: 720px;
    }}

    .tabular table,
    table.tabular {{
      width: 100%;
      border-collapse: collapse;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 0.88rem;
      line-height: 1.45;
    }}

    table.tabular td {{
      min-width: 150px;
      padding: 11px 12px;
      border-top: 1px solid var(--line);
      vertical-align: top;
      white-space: normal !important;
    }}

    table.tabular tr:first-of-type td {{
      border-top: 0;
    }}

    figcaption.caption {{
      margin: 0;
      padding: 12px 14px 14px;
      color: var(--muted);
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 0.9rem;
      line-height: 1.5;
      text-align: left;
      border-top: 1px solid var(--line);
    }}

    figcaption .id {{
      color: var(--ink);
      font-weight: 750;
      margin-right: 0.25em;
    }}

    .thebibliography {{
      font-size: 0.94rem;
      line-height: 1.5;
      overflow-wrap: anywhere;
    }}

    .bibitem {{
      margin: 0.75em 0 0;
      padding-left: 1.15em;
      text-indent: -1.15em;
    }}

    .biblabel,
    .bibsp {{
      display: none;
    }}

    math {{
      font-family: math, "STIX Two Math", "Cambria Math", "Times New Roman", serif;
    }}

    math[display="block"] {{
      max-width: 100%;
      padding: 0.25rem 0;
    }}

    mjx-container[jax="SVG"][display="true"] {{
      max-width: 100%;
      overflow-x: auto;
      overflow-y: hidden;
      padding: 0.12rem 0;
    }}

    table.equation mjx-container[jax="SVG"][display="true"],
    table.equation-star mjx-container[jax="SVG"][display="true"] {{
      margin: 0;
    }}

    table.equation,
    table.equation-star {{
      display: block;
      width: 100%;
      max-width: 100%;
      margin: 1.15em 0;
      border-collapse: collapse;
      overflow-x: auto;
      overflow-y: hidden;
      table-layout: auto;
    }}

    table.equation tbody,
    table.equation tr,
    table.equation td,
    table.equation-star tbody,
    table.equation-star tr,
    table.equation-star td {{
      display: block;
      width: 100%;
    }}

    table.equation td:first-child,
    table.equation-star td:first-child {{
      overflow-x: auto;
      overflow-y: hidden;
      text-align: center;
    }}

    .eq-no {{
      width: 100%;
      margin-top: 0.2rem;
      color: var(--muted);
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 0.9rem;
      text-align: right;
      white-space: nowrap;
    }}

    footer {{
      padding: 28px 0 42px;
      color: var(--muted);
      font-size: 0.92rem;
      border-top: 1px solid var(--line);
    }}

    @media (max-width: 900px) {{
      .hero-body,
      .abstract,
      .article-layout {{
        grid-template-columns: 1fr;
      }}

      .hero-body {{
        align-items: start;
        padding: 44px 0 50px;
      }}

      .paper-toc {{
        position: static;
        display: flex;
        flex-wrap: wrap;
        gap: 8px 12px;
        padding: 0 0 8px;
      }}

      .paper-toc h2 {{
        flex-basis: 100%;
      }}

      .paper-toc a {{
        border-left: 0;
        border-bottom: 1px solid var(--line);
        padding: 2px 0;
      }}
    }}

    @media (max-width: 620px) {{
      .wrap {{
        width: min(100% - 28px, 1160px);
      }}

      .topbar {{
        align-items: flex-start;
        flex-direction: column;
      }}

      h1 {{
        font-size: clamp(2.25rem, 13vw, 3.8rem);
      }}

      article {{
        font-size: 1.02rem;
      }}

      .newtheorem,
      .proof {{
        padding: 0.95rem;
      }}
    }}
  </style>
  <script>
    window.MathJax = {{
      svg: {{
        fontCache: "global"
      }}
    }};
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/mml-svg.js"></script>
</head>
<body>
  <header class="paper-hero">
    <div class="wrap">
      <div class="topbar" aria-label="Site header">
        <div class="brand">Martin Höppner</div>
        <nav class="nav" aria-label="Primary navigation">
          <a href="../../">Home</a>
          <a href="../../#papers">Papers</a>
          <a href="https://orcid.org/0009-0006-7904-295X">ORCID</a>
          <a href="https://github.com/mhoeppner89">GitHub</a>
        </nav>
      </div>
      <div class="hero-body">
        <div>
          <p class="kicker">Working paper</p>
          <h1>{title}</h1>
          <p class="byline">Martin Höppner</p>
        </div>
        <aside class="meta-panel" aria-label="Paper details">
          <dl>
            <div>
              <dt>Status</dt>
              <dd>Working paper</dd>
            </div>
            <div>
              <dt>Topic</dt>
              <dd>Probability weighting and welfare</dd>
            </div>
            <div>
              <dt>JEL Codes</dt>
              <dd>D81, D91, D61</dd>
            </div>
          </dl>
        </aside>
      </div>
    </div>
  </header>

  <section class="abstract-band" aria-labelledby="abstract-title">
    <div class="wrap abstract">
      <div>
        <h2 id="abstract-title">Abstract</h2>
      </div>
      <div>
        <p>{abstract}</p>
        <div class="tags" aria-label="Keywords">
          {keyword_tags}
        </div>
      </div>
    </div>
  </section>

  <main class="wrap article-layout">
    <nav class="paper-toc" aria-label="Paper contents">
      <h2>Contents</h2>
      {toc}
    </nav>
    <article>
      {article}
    </article>
  </main>

  <footer class="wrap">
    <span>&copy; 2026 Martin Höppner.</span>
  </footer>
</body>
</html>
"""


def build_raw_html() -> Path:
    if BUILD.exists():
        shutil.rmtree(BUILD)
    BUILD.mkdir(parents=True)
    shutil.copy2(SOURCE_TEX, BUILD / "paper.tex")
    shutil.copy2(SOURCE_BIB, BUILD / "references.bib")
    subprocess.run(
        ["make4ht", "-u", "-f", "html5", "-m", "draft", "paper.tex", "mathml"],
        cwd=BUILD,
        check=True,
    )
    subprocess.run(["bibtex", "paper"], cwd=BUILD, check=True)
    for _ in range(2):
        subprocess.run(
            ["make4ht", "-u", "-f", "html5", "-m", "draft", "paper.tex", "mathml"],
            cwd=BUILD,
            check=True,
        )
    return BUILD / "paper.html"


def main() -> None:
    raw = build_raw_html().read_text(encoding="utf-8")
    article = clean_article(raw)
    toc = build_toc(article)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_HTML.write_text(page(article, toc), encoding="utf-8")


if __name__ == "__main__":
    main()
