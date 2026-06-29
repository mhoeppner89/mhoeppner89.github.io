from __future__ import annotations

import html
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT.parent / "joes-html-build-mathml"
RAW_HTML = BUILD / "paper.html"
OUT_DIR = ROOT / "papers" / "models-risk-uncertainty"
ASSET_DIR = OUT_DIR / "assets"
OUT_HTML = OUT_DIR / "index.html"

FIGURE_ALTS = {
    "eu1.png": "Concave utility function illustrating risk aversion.",
    "eu2.png": "Convex utility function illustrating risk-seeking behavior.",
    "eu3.png": "Linear utility function illustrating risk neutrality.",
    "pt.png": "Prospect theory value function with losses steeper than gains.",
    "weights1.png": "Cumulative prospect theory probability weighting function.",
    "weights2.png": "Decision weights and risk preference in a two-state lottery.",
}


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
    article = re.sub(r"\n[ \t\u00a0]+\n", "\n", article)
    article = re.sub(r"\s+(height|width)='[^']*'", "", article)
    article = article.replace("<h3 class='sectionHead'", "<h2 class='sectionHead'")
    article = article.replace("</h3>", "</h2>")
    article = article.replace("<h3 class='likesectionHead'", "<h2 class='likesectionHead'")
    article = article.replace("<h4 class='subsectionHead'", "<h3 class='subsectionHead'")
    article = article.replace("</h4>", "</h3>")
    article = article.replace("<p class='noindent'></p>", "")
    article = article.replace("<p class='indent'></p>", "")

    for filename, alt in FIGURE_ALTS.items():
        article = article.replace(
            f"src='{filename}' alt='PIC'",
            f"src='assets/{filename}' alt='{html.escape(alt, quote=True)}' loading='lazy'",
        )
        article = article.replace(
            f"src='{filename}'",
            f"src='assets/{filename}' loading='lazy'",
        )

    article = article.replace("<span class='lmsy-10x-x-120'>{</span>", "{")
    article = article.replace("<span class='lmsy-10x-x-120'>}</span>", "}")
    article = article.replace(" -combined", " - combined")
    article = article.replace("Risk-seeking bahavior", "Risk-seeking behavior")
    article = article.replace("probability judgements", "probability judgments")
    article = article.replace("probability judgement", "probability judgment")
    article = article.replace("qualitative judgements", "qualitative judgments")
    article = article.replace("qualitative judgement", "qualitative judgment")
    article = re.sub(r"probability\s+judgements", "probability judgments", article)
    article = re.sub(r"probability\s+judgement", "probability judgment", article)
    article = re.sub(r"qualitative\s+judgements", "qualitative judgments", article)
    article = re.sub(r"qualitative\s+judgement", "qualitative judgment", article)
    article = article.replace("href='paper2.html#fn1x0'", "href='#fn1x0'")
    article = article.replace("<a id='x1-13001f1'></a> ,", "<a id='x1-13001f1'></a>,")

    footnote = """
    <section class="footnotes" role="doc-endnotes" aria-label="Footnotes">
      <p id="fn1x0">
        <sup>1</sup> There is literature that discusses the possibility of brains acting as
        quantum processors, but this remains speculative
        (<a href="#Xhameroff2007brain">Hameroff, 2007</a>;
        <a href="#XFISHER2015593">Fisher, 2015</a>). Regardless, QPT works effectively
        as a model, much like <a href="#Xfriedman1953methodology">Friedman (1953)</a>'s
        as-if theories.
      </p>
    </section>
    """
    article = article.replace(
        "<h2 class='likesectionHead'><a id='x1-270006'></a>References</h2>",
        footnote + "\n   <h2 class='likesectionHead'><a id='x1-270006'></a>References</h2>",
    )

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
    for match in pattern.finditer(article):
        text = strip_tags(match.group("inner") + match.group("tail"))
        if text:
            items.append(f"<a href='#{match.group('id')}'>{html.escape(text)}</a>")

    return "\n".join(items)


def page(article: str, toc: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Martin Höppner, Models in Decision-Making Under Risk and Uncertainty, Journal of Economic Surveys.">
  <title>Models in Decision-Making Under Risk and Uncertainty | Martin Höppner</title>
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
      --accent-3: #7a5c00;
      --soft: #e7f0ee;
      --wash: #f2edf0;
      --focus: #b56b00;
      --measure: 760px;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}

    * {{
      box-sizing: border-box;
    }}

    html {{
      scroll-behavior: smooth;
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
      grid-template-columns: minmax(0, 1fr) minmax(260px, 0.44fr);
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
      max-width: 860px;
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

    .doi-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px 18px;
      margin-top: 20px;
      color: var(--muted);
      font-size: 0.96rem;
      overflow-wrap: anywhere;
    }}

    .doi-row strong {{
      color: var(--ink);
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
      overflow-wrap: break-word;
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

    .rm-lmbx-12,
    .rm-lmbx-10x-x-109,
    .rm-lmbx-8 {{
      font-weight: 700;
    }}

    .rm-lmri-12 {{
      font-style: italic;
    }}

    .rm-lmtt-8 {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    }}

    figure.figure,
    figure.float {{
      margin: 2.15rem 0;
    }}

    figure.figure {{
      position: relative;
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 16px;
      align-items: start;
    }}

    figure.figure > a[id] {{
      position: absolute;
      inset: 0 auto auto 0;
      width: 0;
      height: 0;
      overflow: hidden;
    }}

    figure.figure > p {{
      margin: 0;
      text-align: center;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: var(--muted);
      font-size: 0.93rem;
      line-height: 1.4;
      min-width: 0;
    }}

    figure.figure > p:empty {{
      display: none;
    }}

    figure.figure img {{
      display: block;
      width: 100%;
      height: auto;
      margin-bottom: 8px;
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 6px;
    }}

    figcaption.caption {{
      grid-column: 1 / -1;
      margin: 0.4rem 0 0;
      color: var(--muted);
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 0.9rem;
      line-height: 1.5;
      text-align: left;
    }}

    figcaption .id {{
      display: inline-block;
      color: var(--ink);
      font-weight: 750;
      margin-right: 0.25em;
    }}

    .table {{
      margin: 2rem 0;
      overflow-x: auto;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--surface);
    }}

    .tabular table,
    table.tabular {{
      width: 100%;
      border-collapse: collapse;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 0.92rem;
      line-height: 1.45;
    }}

    table.tabular td {{
      min-width: 150px;
      padding: 11px 12px;
      border-top: 1px solid var(--line);
      vertical-align: top;
      white-space: normal !important;
    }}

    table.tabular tr:first-of-type td,
    table.tabular tr:nth-of-type(2) td {{
      border-top: 0;
    }}

    table.tabular .hline,
    table.tabular hr {{
      display: none;
    }}

    .thebibliography {{
      font-size: 0.94rem;
      line-height: 1.5;
      overflow-wrap: anywhere;
    }}

    .footnote-mark a,
    .footnotes a {{
      text-decoration-thickness: 0.06em;
    }}

    .footnotes {{
      margin: 2.4rem 0;
      padding-top: 1rem;
      border-top: 1px solid var(--line);
      color: var(--muted);
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 0.92rem;
      line-height: 1.55;
    }}

    .footnotes sup {{
      color: var(--accent);
      font-weight: 800;
      margin-right: 0.25em;
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

    table.equation-star {{
      display: block;
      width: 100%;
      margin: 1.15em 0;
      border-collapse: collapse;
      overflow-x: auto;
      overflow-y: hidden;
    }}

    table.equation-star tbody,
    table.equation-star tr,
    table.equation-star td {{
      display: block;
      text-align: center;
      padding: 0;
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

      figure.figure {{
        grid-template-columns: 1fr;
      }}

      .table {{
        overflow-x: visible;
      }}

      table.tabular {{
        table-layout: fixed;
        font-size: 0.78rem;
      }}

      table.tabular td {{
        min-width: 0;
        width: 33.333%;
        padding: 9px 7px;
      }}

      h1 {{
        max-width: 16ch;
        font-size: clamp(1.95rem, 8.4vw, 2.25rem);
        line-height: 1.04;
        overflow-wrap: normal;
        word-break: normal;
      }}

      .byline {{
        max-width: 31ch;
      }}

      figcaption.caption {{
        grid-column: auto;
      }}

      article {{
        font-size: 1rem;
      }}
    }}
  </style>
</head>
<body>
  <header class="paper-hero">
    <div class="wrap">
      <div class="topbar" aria-label="Site header">
        <div class="brand">Martin Höppner</div>
        <nav class="nav" aria-label="Primary navigation">
          <a href="../../">Research</a>
          <a href="#article">Article</a>
          <a href="#x1-270006">References</a>
        </nav>
      </div>

      <div class="hero-body">
        <div>
          <p class="kicker">Journal of Economic Surveys · 2025</p>
          <h1>Models in Decision-Making Under Risk and Uncertainty</h1>
          <p class="byline">
            Martin Höppner · Brandenburgische Technische Universität Cottbus-Senftenberg,
            Senftenberg, Germany
          </p>
          <div class="doi-row" aria-label="Publication links">
            <span><strong>DOI</strong> <a href="https://doi.org/10.1111/joes.70008">10.1111/joes.70008</a></span>
            <span><strong>Correspondence</strong> <a href="mailto:martin.hoeppner@b-tu.de">martin.hoeppner@b-tu.de</a></span>
          </div>
        </div>

        <aside class="meta-panel" aria-label="Article metadata">
          <dl>
            <div>
              <dt>Received</dt>
              <dd>30 October 2024</dd>
            </div>
            <div>
              <dt>Revised</dt>
              <dd>13 April 2025</dd>
            </div>
            <div>
              <dt>Accepted</dt>
              <dd>25 May 2025</dd>
            </div>
            <div>
              <dt>License</dt>
              <dd>Creative Commons Attribution</dd>
            </div>
          </dl>
        </aside>
      </div>
    </div>
  </header>

  <section class="abstract-band" aria-labelledby="abstract-title">
    <div class="wrap abstract">
      <h2 id="abstract-title">Abstract</h2>
      <div>
        <p>
          This paper systematically compares dominant frameworks for modeling decision-making
          under risk and uncertainty, evaluating their theoretical trade-offs and practical
          relevance for economic research. We establish key criteria for model selection&mdash;including
          predictive accuracy, descriptive realism, computational tractability, and ecological
          validity&mdash;to guide researchers in matching frameworks to specific contexts. While
          classical axiomatic models provide normative benchmarks, our analysis highlights the
          need for context-sensitive models. We propose the following three research frontiers:
          (1) integrating behavioral axioms with machine learning architectures, (2) neuroeconomic
          validation of decision-theoretic assumptions, and (3) dynamic models for evolving
          uncertainty landscapes. The survey provides a structured framework for advancing
          decision theory while maintaining methodological pluralism in behavioral economics.
        </p>
        <div class="tags" aria-label="Keywords">
          <span class="tag">ambiguity</span>
          <span class="tag">decision theory</span>
          <span class="tag">expected utility theory</span>
          <span class="tag">risk</span>
          <span class="tag">uncertainty</span>
          <span class="tag">JEL D81 · D03 · C91</span>
        </div>
      </div>
    </div>
  </section>

  <main class="wrap article-layout">
    <nav class="paper-toc" aria-label="Article contents">
      <h2>Contents</h2>
      {toc}
    </nav>

    <article id="article">
      {article}
    </article>
  </main>

  <footer class="wrap">
    <span>© 2025 Martin Höppner. Journal of Economic Surveys published by John Wiley &amp; Sons Ltd.</span>
  </footer>
</body>
</html>
"""


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ASSET_DIR.mkdir(parents=True, exist_ok=True)

    for filename in FIGURE_ALTS:
        shutil.copy2(BUILD / filename, ASSET_DIR / filename)

    raw = RAW_HTML.read_text(encoding="utf-8")
    article = clean_article(raw)
    toc = build_toc(article)
    OUT_HTML.write_text(page(article, toc), encoding="utf-8")


if __name__ == "__main__":
    main()
