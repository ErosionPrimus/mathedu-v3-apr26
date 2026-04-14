#!/usr/bin/env python3
"""Rebuild all level-4 topic pages with full-depth content. Run from repo root: python3 scripts/build_topic_articles.py"""
from __future__ import annotations
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "public_html"))

ANALYTICS = r"""    <script async src="https://www.googletagmanager.com/gtag/js?id=G-08L01JDD3F"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-08L01JDD3F');
    </script>
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-T34MKQC7');</script>"""

RESPONSIVE_CSS = """
    <style>
      .topic-layout{display:grid;grid-template-columns:1fr 260px;gap:2rem;align-items:start;max-width:1200px;margin:0 auto;padding:1.5rem 1rem;}
      .topic-main{min-width:0;}
      .topic-toc{position:sticky;top:80px;background:var(--secondary,#f8f9fa);border:1px solid var(--border,#dee2e6);border-radius:8px;padding:1.2rem;font-size:0.9rem;}
      .topic-toc h3{margin:0 0 0.8rem;font-size:1rem;font-weight:600;}
      .topic-toc ul{list-style:none;padding:0;margin:0;}
      .topic-toc li{margin:0.35rem 0;}
      .topic-toc a{color:inherit;text-decoration:none;opacity:0.75;}
      .topic-toc a:hover{opacity:1;text-decoration:underline;}
      @media(max-width:860px){
        .topic-layout{grid-template-columns:1fr;}
        .topic-toc{position:static;order:-1;}
      }
      .example-box{background:var(--secondary,#f8f9fa);border-left:3px solid var(--accent,#0d6efd);border-radius:0 6px 6px 0;padding:1rem 1.2rem;margin:1rem 0;}
      .example-box .question{font-weight:600;margin-bottom:0.5rem;}
      .example-box .solution{margin:0;}
      .formula-box{background:var(--secondary,#f8f9fa);border:1px solid var(--border,#dee2e6);border-radius:6px;padding:0.9rem 1.2rem;margin:0.8rem 0;overflow-x:auto;}
      .prop-table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:0.95rem;}
      .prop-table th{background:var(--secondary,#f8f9fa);padding:0.6rem 0.8rem;text-align:left;border-bottom:2px solid var(--border,#dee2e6);}
      .prop-table td{padding:0.55rem 0.8rem;border-bottom:1px solid var(--border,#dee2e6);}
      .content-section{margin-bottom:2rem;}
      .content-section h2{font-size:1.3rem;margin-bottom:0.7rem;padding-bottom:0.3rem;border-bottom:1px solid var(--border,#dee2e6);}
      .content-section h3{font-size:1.1rem;margin:1rem 0 0.5rem;}
      .related-topics ul{display:flex;flex-wrap:wrap;gap:0.5rem;list-style:none;padding:0;}
      .related-topics a{display:inline-block;padding:0.3rem 0.75rem;background:var(--secondary,#f8f9fa);border:1px solid var(--border,#dee2e6);border-radius:20px;font-size:0.88rem;text-decoration:none;color:inherit;}
      .related-topics a:hover{background:var(--accent,#0d6efd);color:#fff;border-color:var(--accent,#0d6efd);}
      .article-byline{display:flex;gap:1.5rem;flex-wrap:wrap;font-size:0.85rem;color:var(--muted-foreground,#6c757d);margin:0.4rem 0 1.5rem;padding-bottom:0.8rem;border-bottom:1px solid var(--border,#dee2e6);}
      .byline-author,.byline-date{display:flex;align-items:center;gap:0.4rem;}
    </style>"""


BYLINE = '<p class="article-byline"><span class="byline-author"><i class="fas fa-user-graduate"></i> By <strong>SkytrailGroup Mathematics Editorial Team</strong></span><span class="byline-date"><i class="fas fa-calendar-alt"></i> <time datetime="2026-04-12">April 12, 2026</time></span></p>'


def head(prefix: str, title: str, desc: str, canon: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | SkytrailGroup Mathematics Academy</title>
    <meta name="author" content="SkytrailGroup Mathematics Editorial Team">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{prefix}css/style.css">
    <link rel="stylesheet" href="{prefix}css/intelligent_academic_widgets.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <meta name="description" content="{desc}">
    <link rel="canonical" href="https://skytrailgroup.com/{canon}">
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
{ANALYTICS}
{RESPONSIVE_CSS}
</head>
<body>
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-T34MKQC7" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <nav class="academic-nav-widget">
        <div class="academic-nav-container">
            <a href="/" class="academic-nav-logo"><i class="fas fa-square-root-alt"></i> SkytrailGroup Mathematics</a>
            <ul class="academic-nav-menu">
                <li><a href="/" class="academic-nav-link">Home</a></li>
                <li><a href="/algebra/" class="academic-nav-link">Algebra</a></li>
                <li><a href="/calculus/" class="academic-nav-link">Calculus</a></li>
                <li><a href="/geometry/" class="academic-nav-link">Geometry</a></li>
                <li><a href="/number-theory/" class="academic-nav-link">Number Theory</a></li>
                <li><a href="/statistics/" class="academic-nav-link">Statistics</a></li>
                <li><a href="/linear-algebra/" class="academic-nav-link">Linear Algebra</a></li>
            </ul>
            <button class="mobile-nav-toggle" aria-label="Toggle navigation" aria-expanded="false"><i class="fas fa-bars"></i></button>
        </div>
    </nav>
    <div class="progress-bar" id="reading-progress"></div>
"""


def foot(prefix: str) -> str:
    return f"""    <footer class="academy-footer">
        <div class="footer-content">
            <h3 style="font-family:'Georgia',serif;margin-bottom:1rem;">SkytrailGroup Mathematics Academy</h3>
            <div style="display:flex;justify-content:center;gap:2rem;flex-wrap:wrap;margin-bottom:1.5rem;">
                <a href="/aboutus" style="color:var(--color-academic-primary,#dee777);text-decoration:none;">About Us</a>
                <a href="/contactus" style="color:var(--color-academic-primary,#dee777);text-decoration:none;">Contact Us</a>
                <a href="/privacy" style="color:var(--color-academic-primary,#dee777);text-decoration:none;">Privacy Policy</a>
                <a href="/terms" style="color:var(--color-academic-primary,#dee777);text-decoration:none;">Terms of Service</a>
            </div>
            <p style="opacity:0.6;font-size:0.9rem;">&copy; 2026 SkytrailGroup Mathematics Academy. All rights reserved.</p>
        </div>
    </footer>
    <script src="{prefix}js/intelligent_academic_widgets.js"></script>
    <script src="{prefix}js/academic_interactions.js"></script>
</body>
</html>
"""


def toc(sections: list[tuple[str, str]]) -> str:
    items = "".join(f'<li><a href="#{sid}">{slabel}</a></li>' for sid, slabel in sections)
    return f'<aside class="topic-toc"><h3>Contents</h3><ul>{items}</ul></aside>'


def examples_html(examples: list[tuple[str, str]]) -> str:
    out = ""
    for i, (q, a) in enumerate(examples, 1):
        out += f"""<div class="example-box">
            <p class="question"><strong>Example {i}.</strong> {q}</p>
            <p class="solution"><strong>Solution.</strong> {a}</p>
        </div>\n"""
    return out


def props_table(rows: list[tuple[str, str]], headers: tuple[str, str] = ("Property", "Statement")) -> str:
    h0, h1 = headers
    body = "".join(f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td></tr>" for r in rows)
    return f'<table class="prop-table"><thead><tr><th>{h0}</th><th>{h1}</th></tr></thead><tbody>{body}</tbody></table>'


def write_page(rel_dir: str, html: str) -> None:
    out = os.path.join(ROOT, rel_dir.replace("\\", "/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", out)


def prefix_for(rel: str) -> str:
    depth = len(rel.strip("/").split("/"))
    return "../" * depth


def page(rel: str, title: str, parent: str, parent_href: str, desc: str, body_fn) -> None:
    pre = prefix_for(rel)
    bc = f'<a href="/">Home</a><span>›</span><a href="{parent_href}">{parent}</a><span>›</span><span>{title}</span>'
    canon = rel.strip("/")
    html = head(pre, title, desc, canon)
    body = body_fn(bc, pre)
    # Inject byline after the first <h1>…</h1>
    import re as _re
    body = _re.sub(r'(<h1>[^<]*</h1>)', r'\1' + BYLINE, body, count=1)
    html += body
    html += foot(pre)
    write_page(rel, html)



# ---------------------------------------------------------------------------
# STATISTICS
# ---------------------------------------------------------------------------

def build_stats():
    S = "statistics"

    def _page(slug, title, desc, body_fn):
        page(f"{S}/{slug}", title, "Statistics", f"/{S}/", desc, body_fn)

    # --- descriptive-statistics ---
    def body_desc(bc, pre):
        secs = [("overview","Overview"),("measures","Measures of Center"),("spread","Measures of Spread"),("shape","Shape of Distributions"),("examples","Examples")]
        return f"""<div class="topic-layout">
<main class="topic-main">
  <nav class="breadcrumb">{bc}</nav>
  <h1>Descriptive Statistics</h1>
  <div class="content-section" id="overview"><h2>Overview</h2>
    <p>Descriptive statistics summarize and describe the main features of a dataset without drawing inferences beyond the data itself. They provide simple summaries about the sample and the measures.</p>
  </div>
  <div class="content-section" id="measures"><h2>Measures of Center</h2>
    {props_table([("Mean","\\(\\bar{{x}}=\\frac{{1}}{{n}}\\sum_{{i=1}}^n x_i\\) — arithmetic average"),("Median","Middle value when data are ordered; robust to outliers"),("Mode","Most frequently occurring value")])}
  </div>
  <div class="content-section" id="spread"><h2>Measures of Spread</h2>
    {props_table([("Range","Max − Min"),("Variance","\\(s^2=\\frac{{1}}{{n-1}}\\sum(x_i-\\bar{{x}})^2\\)"),("Std Dev","\\(s=\\sqrt{{s^2}}\\)"),("IQR","Q3 − Q1")])}
  </div>
  <div class="content-section" id="shape"><h2>Shape of Distributions</h2>
    <p>Skewness measures asymmetry; kurtosis measures tail heaviness. A symmetric, bell-shaped distribution has skewness ≈ 0.</p>
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("Find the mean and standard deviation of {{2,4,4,4,5,5,7,9}}.","Mean = 5. Variance = \\(\\frac{{(2-5)^2+3(4-5)^2+2(5-5)^2+(7-5)^2+(9-5)^2}}{{7}}=4\\). SD = 2.")])}
  </div>
</main>
{toc(secs)}
</div>"""
    _page("descriptive-statistics","Descriptive Statistics","Learn measures of center, spread, and shape in descriptive statistics.",body_desc)

    # --- probability ---
    def body_prob(bc, pre):
        secs = [("basics","Basics"),("rules","Rules"),("conditional","Conditional Probability"),("examples","Examples")]
        return f"""<div class="topic-layout">
<main class="topic-main">
  <nav class="breadcrumb">{bc}</nav>
  <h1>Probability</h1>
  <div class="content-section" id="basics"><h2>Basics</h2>
    <p>Probability measures the likelihood of an event: \\(P(A)=\\frac{{|A|}}{{|\\Omega|}}\\) for equally likely outcomes.</p>
  </div>
  <div class="content-section" id="rules"><h2>Rules</h2>
    {props_table([("Addition","\\(P(A\\cup B)=P(A)+P(B)-P(A\\cap B)\\)"),("Complement","\\(P(A^c)=1-P(A)\\)"),("Multiplication","\\(P(A\\cap B)=P(A)P(B|A)\\)")])}
  </div>
  <div class="content-section" id="conditional"><h2>Conditional Probability</h2>
    <div class="formula-box">\\[P(A|B)=\\frac{{P(A\\cap B)}}{{P(B)}}\\]</div>
    <p>Bayes' theorem: \\(P(A|B)=\\frac{{P(B|A)P(A)}}{{P(B)}}\\)</p>
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("A fair die is rolled. What is P(even | > 2)?","Even and >2: {{4,6}}, so P = 2/4 = 1/2.")])}
  </div>
</main>
{toc(secs)}
</div>"""
    _page("probability","Probability","Fundamental rules of probability including addition, multiplication, and Bayes' theorem.",body_prob)

    # --- normal-distribution ---
    def body_norm(bc, pre):
        secs = [("definition","Definition"),("properties","Properties"),("zscore","Z-Scores"),("examples","Examples")]
        return f"""<div class="topic-layout">
<main class="topic-main">
  <nav class="breadcrumb">{bc}</nav>
  <h1>Normal Distribution</h1>
  <div class="content-section" id="definition"><h2>Definition</h2>
    <div class="formula-box">\\[f(x)=\\frac{{1}}{{\\sigma\\sqrt{{2\\pi}}}}e^{{-\\frac{{1}}{{2}}\\left(\\frac{{x-\\mu}}{{\\sigma}}\\right)^2}}\\]</div>
  </div>
  <div class="content-section" id="properties"><h2>Properties</h2>
    {props_table([("Symmetry","Symmetric about μ"),("68-95-99.7","68% within 1σ, 95% within 2σ, 99.7% within 3σ"),("Mean=Median=Mode","All equal μ")])}
  </div>
  <div class="content-section" id="zscore"><h2>Z-Scores</h2>
    <div class="formula-box">\\[z=\\frac{{x-\\mu}}{{\\sigma}}\\]</div>
    <p>Standardizes any normal variable to N(0,1).</p>
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("Heights are N(170,10). What % are between 160 and 180?","z = ±1, so 68% by the empirical rule.")])}
  </div>
</main>
{toc(secs)}
</div>"""
    _page("normal-distribution","Normal Distribution","Properties, z-scores, and applications of the normal distribution.",body_norm)

    # --- hypothesis-testing ---
    def body_hyp(bc, pre):
        secs = [("setup","Setup"),("errors","Type I & II Errors"),("tests","Common Tests"),("examples","Examples")]
        return f"""<div class="topic-layout">
<main class="topic-main">
  <nav class="breadcrumb">{bc}</nav>
  <h1>Hypothesis Testing</h1>
  <div class="content-section" id="setup"><h2>Setup</h2>
    <p>State H₀ (null) and H₁ (alternative). Choose significance level α. Compute test statistic and p-value. Reject H₀ if p &lt; α.</p>
  </div>
  <div class="content-section" id="errors"><h2>Type I &amp; II Errors</h2>
    {props_table([("Type I (α)","Reject H₀ when it is true (false positive)"),("Type II (β)","Fail to reject H₀ when it is false (false negative)"),("Power","1 − β")])}
  </div>
  <div class="content-section" id="tests"><h2>Common Tests</h2>
    {props_table([("z-test","Known σ, large n"),("t-test","Unknown σ, small n"),("χ²-test","Categorical data / goodness of fit"),("F-test","Comparing variances / ANOVA")])}
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("A sample of 36 has x̄=52, s=6. Test H₀: μ=50 at α=0.05.","t = (52−50)/(6/√36) = 2. df=35, critical t≈2.03. Fail to reject H₀.")])}
  </div>
</main>
{toc(secs)}
</div>"""
    _page("hypothesis-testing","Hypothesis Testing","Step-by-step guide to hypothesis testing, p-values, and statistical errors.",body_hyp)

    # --- confidence-intervals ---
    def body_ci(bc, pre):
        secs = [("concept","Concept"),("formula","Formula"),("interpretation","Interpretation"),("examples","Examples")]
        return f"""<div class="topic-layout">
<main class="topic-main">
  <nav class="breadcrumb">{bc}</nav>
  <h1>Confidence Intervals</h1>
  <div class="content-section" id="concept"><h2>Concept</h2>
    <p>A confidence interval gives a range of plausible values for a population parameter based on sample data.</p>
  </div>
  <div class="content-section" id="formula"><h2>Formula</h2>
    <div class="formula-box">\\[\\bar{{x}}\\pm z_{{\\alpha/2}}\\frac{{\\sigma}}{{\\sqrt{{n}}}}\\quad\\text{{(known σ)}}\\]</div>
    <div class="formula-box">\\[\\bar{{x}}\\pm t_{{\\alpha/2,n-1}}\\frac{{s}}{{\\sqrt{{n}}}}\\quad\\text{{(unknown σ)}}\\]</div>
  </div>
  <div class="content-section" id="interpretation"><h2>Interpretation</h2>
    <p>A 95% CI means: if we repeated the sampling procedure many times, 95% of the constructed intervals would contain the true parameter.</p>
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("n=25, x̄=100, s=15. Build a 95% CI for μ.","t* ≈ 2.064. CI = 100 ± 2.064·(15/5) = (93.81, 106.19).")])}
  </div>
</main>
{toc(secs)}
</div>"""
    _page("confidence-intervals","Confidence Intervals","Constructing and interpreting confidence intervals for population parameters.",body_ci)

    # --- regression-analysis ---
    def body_reg(bc, pre):
        secs = [("slr","Simple Linear Regression"),("ols","OLS Estimates"),("fit","Goodness of Fit"),("examples","Examples")]
        return f"""<div class="topic-layout">
<main class="topic-main">
  <nav class="breadcrumb">{bc}</nav>
  <h1>Regression Analysis</h1>
  <div class="content-section" id="slr"><h2>Simple Linear Regression</h2>
    <div class="formula-box">\\[y=\\beta_0+\\beta_1 x+\\varepsilon\\]</div>
  </div>
  <div class="content-section" id="ols"><h2>OLS Estimates</h2>
    {props_table([("Slope","\\(\\hat{{\\beta}}_1=\\frac{{\\sum(x_i-\\bar{{x}})(y_i-\\bar{{y}})}}{{\\sum(x_i-\\bar{{x}})^2}}\\)"),("Intercept","\\(\\hat{{\\beta}}_0=\\bar{{y}}-\\hat{{\\beta}}_1\\bar{{x}}\\)")])}
  </div>
  <div class="content-section" id="fit"><h2>Goodness of Fit</h2>
    <p>R² = SSR/SST measures the proportion of variance in y explained by x. Ranges from 0 to 1.</p>
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("x=[1,2,3], y=[2,4,5]. Find the regression line.","x̄=2, ȳ=11/3. β̂₁=(1·(−1/3)+0·(1/3)+1·(2/3))/2 = 1.5. β̂₀ = 11/3−1.5·2 = 0.67. ŷ = 0.67+1.5x.")])}
  </div>
</main>
{toc(secs)}
</div>"""
    _page("regression-analysis","Regression Analysis","Simple linear regression, OLS estimation, and R² goodness of fit.",body_reg)

    # --- correlation ---
    def body_corr(bc, pre):
        secs = [("pearson","Pearson r"),("spearman","Spearman ρ"),("caution","Correlation vs Causation"),("examples","Examples")]
        return f"""<div class="topic-layout">
<main class="topic-main">
  <nav class="breadcrumb">{bc}</nav>
  <h1>Correlation</h1>
  <div class="content-section" id="pearson"><h2>Pearson r</h2>
    <div class="formula-box">\\[r=\\frac{{\\sum(x_i-\\bar{{x}})(y_i-\\bar{{y}})}}{{\\sqrt{{\\sum(x_i-\\bar{{x}})^2\\sum(y_i-\\bar{{y}})^2}}}}\\]</div>
    <p>Ranges from −1 (perfect negative) to +1 (perfect positive).</p>
  </div>
  <div class="content-section" id="spearman"><h2>Spearman ρ</h2>
    <p>Rank-based correlation; robust to outliers and monotone non-linear relationships.</p>
  </div>
  <div class="content-section" id="caution"><h2>Correlation vs Causation</h2>
    <p>A high r does not imply causation. Confounding variables can produce spurious correlations.</p>
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("x=[1,2,3], y=[2,4,6]. Compute r.","Perfect linear relationship, r = 1.")])}
  </div>
</main>
{toc(secs)}
</div>"""
    _page("correlation","Correlation","Pearson and Spearman correlation coefficients and their interpretation.",body_corr)

    # --- inferential-statistics ---
    def body_inf(bc, pre):
        secs = [("overview","Overview"),("estimation","Estimation"),("testing","Testing"),("examples","Examples")]
        return f"""<div class="topic-layout">
<main class="topic-main">
  <nav class="breadcrumb">{bc}</nav>
  <h1>Inferential Statistics</h1>
  <div class="content-section" id="overview"><h2>Overview</h2>
    <p>Inferential statistics uses sample data to make conclusions about a population, accounting for sampling variability.</p>
  </div>
  <div class="content-section" id="estimation"><h2>Estimation</h2>
    {props_table([("Point estimate","Single value (e.g. x̄ for μ)"),("Interval estimate","Range of values (confidence interval)")])}
  </div>
  <div class="content-section" id="testing"><h2>Testing</h2>
    <p>Hypothesis tests formalize decisions about population parameters using probability. The p-value quantifies evidence against H₀.</p>
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("Why can't we just use descriptive stats?","Descriptive stats describe the sample only; inferential stats generalize to the population with quantified uncertainty.")])}
  </div>
</main>
{toc(secs)}
</div>"""
    _page("inferential-statistics","Inferential Statistics","Using sample data to draw conclusions about populations.",body_inf)

    # --- random-variables ---
    def body_rv(bc, pre):
        secs = [("discrete","Discrete RVs"),("continuous","Continuous RVs"),("expectation","Expectation & Variance"),("examples","Examples")]
        return f"""<div class="topic-layout">
<main class="topic-main">
  <nav class="breadcrumb">{bc}</nav>
  <h1>Random Variables</h1>
  <div class="content-section" id="discrete"><h2>Discrete RVs</h2>
    <p>Takes countable values. PMF: \\(P(X=x)\\geq 0\\), \\(\\sum P(X=x)=1\\).</p>
  </div>
  <div class="content-section" id="continuous"><h2>Continuous RVs</h2>
    <p>PDF \\(f(x)\\geq 0\\), \\(\\int_{{-\\infty}}^{{\\infty}}f(x)dx=1\\). \\(P(a\\leq X\\leq b)=\\int_a^b f(x)dx\\).</p>
  </div>
  <div class="content-section" id="expectation"><h2>Expectation &amp; Variance</h2>
    {props_table([("E[X]","\\(\\sum x\\,P(X=x)\\) or \\(\\int x\\,f(x)dx\\)"),("Var(X)","\\(E[X^2]-(E[X])^2\\)"),("Linearity","\\(E[aX+b]=aE[X]+b\\)")])}
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("X ~ Bernoulli(p). Find E[X] and Var(X).","E[X] = p. Var(X) = p(1−p).")])}
  </div>
</main>
{toc(secs)}
</div>"""
    _page("random-variables","Random Variables","Discrete and continuous random variables, expectation, and variance.",body_rv)

    # --- statistical-distributions ---
    def body_dist(bc, pre):
        secs = [("discrete","Key Discrete Distributions"),("continuous","Key Continuous Distributions"),("examples","Examples")]
        return f"""<div class="topic-layout">
<main class="topic-main">
  <nav class="breadcrumb">{bc}</nav>
  <h1>Statistical Distributions</h1>
  <div class="content-section" id="discrete"><h2>Key Discrete Distributions</h2>
    {props_table([("Binomial","\\(B(n,p)\\): n trials, success prob p"),("Poisson","\\(\\text{{Pois}}(\\lambda)\\): rare events, mean λ"),("Geometric","Trials until first success")])}
  </div>
  <div class="content-section" id="continuous"><h2>Key Continuous Distributions</h2>
    {props_table([("Normal","\\(N(\\mu,\\sigma^2)\\): bell curve"),("Exponential","Time between Poisson events"),("Uniform","\\(U(a,b)\\): equal density on [a,b]"),("t","Heavy-tailed; used when σ unknown"),("Chi-squared","Sum of squared normals; used in tests")])}
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("X~Poisson(3). Find P(X=2).","P(X=2) = e⁻³·3²/2! = 9e⁻³/2 ≈ 0.224.")])}
  </div>
</main>
{toc(secs)}
</div>"""
    _page("statistical-distributions","Statistical Distributions","Overview of key discrete and continuous probability distributions.",body_dist)

    # --- sampling-methods ---
    def body_samp(bc, pre):
        secs = [("types","Sampling Types"),("clt","Central Limit Theorem"),("examples","Examples")]
        return f"""<div class="topic-layout">
<main class="topic-main">
  <nav class="breadcrumb">{bc}</nav>
  <h1>Sampling Methods</h1>
  <div class="content-section" id="types"><h2>Sampling Types</h2>
    {props_table([("Simple Random","Every subset of size n equally likely"),("Stratified","Population divided into strata; sample from each"),("Cluster","Randomly select clusters; sample all within"),("Systematic","Every k-th element")])}
  </div>
  <div class="content-section" id="clt"><h2>Central Limit Theorem</h2>
    <p>For large n, \\(\\bar{{X}}\\sim N\\!\\left(\\mu,\\frac{{\\sigma^2}}{{n}}\\right)\\) regardless of the population distribution.</p>
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("Population has μ=50, σ=10. n=100. Find P(X̄>52).","SE = 10/10 = 1. z = 2. P(Z>2) ≈ 0.023.")])}
  </div>
</main>
{toc(secs)}
</div>"""
    _page("sampling-methods","Sampling Methods","Random sampling techniques and the Central Limit Theorem.",body_samp)

    # --- bayesian-statistics ---
    def body_bayes(bc, pre):
        secs = [("theorem","Bayes' Theorem"),("prior","Prior & Posterior"),("examples","Examples")]
        return f"""<div class="topic-layout">
<main class="topic-main">
  <nav class="breadcrumb">{bc}</nav>
  <h1>Bayesian Statistics</h1>
  <div class="content-section" id="theorem"><h2>Bayes' Theorem</h2>
    <div class="formula-box">\\[P(\\theta|x)=\\frac{{P(x|\\theta)P(\\theta)}}{{P(x)}}\\]</div>
  </div>
  <div class="content-section" id="prior"><h2>Prior &amp; Posterior</h2>
    {props_table([("Prior P(θ)","Belief about θ before seeing data"),("Likelihood P(x|θ)","Probability of data given θ"),("Posterior P(θ|x)","Updated belief after seeing data")])}
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("Disease prevalence 1%. Test sensitivity 99%, specificity 95%. Positive test — P(disease)?","P(D|+) = (0.99·0.01)/(0.99·0.01+0.05·0.99) ≈ 16.7%.")])}
  </div>
</main>
{toc(secs)}
</div>"""
    _page("bayesian-statistics","Bayesian Statistics","Bayes' theorem, prior and posterior distributions in Bayesian inference.",body_bayes)

# ---------------------------------------------------------------------------
# CALCULUS
# ---------------------------------------------------------------------------

def build_calculus():
    S = "calculus"

    def _page(slug, title, desc, body_fn):
        page(f"{S}/{slug}", title, "Calculus", f"/{S}/", desc, body_fn)

    def body_limit(bc, pre):
        secs = [("def","Definition"),("laws","Limit Laws"),("examples","Examples")]
        return f"""<div class="topic-layout"><main class="topic-main">
  <nav class="breadcrumb">{bc}</nav><h1>Limits</h1>
  <div class="content-section" id="def"><h2>Definition</h2>
    <p>\\(\\lim_{{x\\to a}}f(x)=L\\) means f(x) can be made arbitrarily close to L by taking x sufficiently close to a.</p>
  </div>
  <div class="content-section" id="laws"><h2>Limit Laws</h2>
    {props_table([("Sum","\\(\\lim(f+g)=\\lim f+\\lim g\\)"),("Product","\\(\\lim(fg)=(\\lim f)(\\lim g)\\)"),("Quotient","\\(\\lim f/g=\\lim f/\\lim g\\) (\\(\\lim g\\neq0\\))"),("Squeeze","If \\(g\\leq f\\leq h\\) and \\(\\lim g=\\lim h=L\\) then \\(\\lim f=L\\)")])}
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("Find \\(\\lim_{{x\\to0}}\\frac{{\\sin x}}{{x}}\\).","By the squeeze theorem, the limit equals 1.")])}
  </div>
</main>{toc(secs)}</div>"""
    _page("limit","Limits","Definition, limit laws, and evaluation techniques for limits.",body_limit)

    def body_cont(bc, pre):
        secs = [("def","Definition"),("types","Types of Discontinuity"),("examples","Examples")]
        return f"""<div class="topic-layout"><main class="topic-main">
  <nav class="breadcrumb">{bc}</nav><h1>Continuity</h1>
  <div class="content-section" id="def"><h2>Definition</h2>
    <p>f is continuous at a if: (1) f(a) is defined, (2) \\(\\lim_{{x\\to a}}f(x)\\) exists, (3) \\(\\lim_{{x\\to a}}f(x)=f(a)\\).</p>
  </div>
  <div class="content-section" id="types"><h2>Types of Discontinuity</h2>
    {props_table([("Removable","Limit exists but ≠ f(a)"),("Jump","Left and right limits differ"),("Infinite","Limit is ±∞")])}
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("Is f(x)=sin(x)/x continuous at x=0?","No (undefined), but the removable discontinuity is fixed by defining f(0)=1.")])}
  </div>
</main>{toc(secs)}</div>"""
    _page("continuity","Continuity","Definition of continuity and types of discontinuities.",body_cont)

    def body_deriv(bc, pre):
        secs = [("def","Definition"),("rules","Differentiation Rules"),("examples","Examples")]
        return f"""<div class="topic-layout"><main class="topic-main">
  <nav class="breadcrumb">{bc}</nav><h1>Derivatives</h1>
  <div class="content-section" id="def"><h2>Definition</h2>
    <div class="formula-box">\\[f'(x)=\\lim_{{h\\to0}}\\frac{{f(x+h)-f(x)}}{{h}}\\]</div>
  </div>
  <div class="content-section" id="rules"><h2>Differentiation Rules</h2>
    {props_table([("Power","\\((x^n)'=nx^{{n-1}}\\)"),("Product","\\((fg)'=f'g+fg'\\)"),("Quotient","\\((f/g)'=(f'g-fg')/g^2\\)"),("Chain","\\((f\\circ g)'=(f'\\circ g)\\cdot g'\\)")])}
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("Differentiate \\(f(x)=x^3\\sin x\\).","\\(f'(x)=3x^2\\sin x+x^3\\cos x\\) by the product rule.")])}
  </div>
</main>{toc(secs)}</div>"""
    _page("derivative","Derivatives","Definition of the derivative and core differentiation rules.",body_deriv)

    def body_diffrules(bc, pre):
        secs = [("trig","Trig Derivatives"),("exp","Exponential & Log"),("examples","Examples")]
        return f"""<div class="topic-layout"><main class="topic-main">
  <nav class="breadcrumb">{bc}</nav><h1>Differentiation Rules</h1>
  <div class="content-section" id="trig"><h2>Trig Derivatives</h2>
    {props_table([("sin","\\(\\cos x\\)"),("cos","\\(-\\sin x\\)"),("tan","\\(\\sec^2 x\\)"),("sec","\\(\\sec x\\tan x\\)")])}
  </div>
  <div class="content-section" id="exp"><h2>Exponential &amp; Log</h2>
    {props_table([("\\(e^x\\)","\\(e^x\\)"),("\\(a^x\\)","\\(a^x\\ln a\\)"),("\\(\\ln x\\)","\\(1/x\\)"),("\\(\\log_a x\\)","\\(1/(x\\ln a)\\)")])}
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("Find \\(\\frac{{d}}{{dx}}[e^{{x^2}}]\\).","Chain rule: \\(2xe^{{x^2}}\\).")])}
  </div>
</main>{toc(secs)}</div>"""
    _page("differentiation-rules","Differentiation Rules","Complete table of differentiation rules including trig, exponential, and logarithmic.",body_diffrules)

    def body_appderiv(bc, pre):
        secs = [("extrema","Extrema"),("mvt","Mean Value Theorem"),("optim","Optimization"),("examples","Examples")]
        return f"""<div class="topic-layout"><main class="topic-main">
  <nav class="breadcrumb">{bc}</nav><h1>Applications of Derivatives</h1>
  <div class="content-section" id="extrema"><h2>Extrema</h2>
    <p>Critical points where f'(x)=0 or undefined. Second derivative test: f''(c)&gt;0 → local min; f''(c)&lt;0 → local max.</p>
  </div>
  <div class="content-section" id="mvt"><h2>Mean Value Theorem</h2>
    <div class="formula-box">\\[f'(c)=\\frac{{f(b)-f(a)}}{{b-a}}\\text{{ for some }}c\\in(a,b)\\]</div>
  </div>
  <div class="content-section" id="optim"><h2>Optimization</h2>
    <p>Find critical points, check endpoints and second derivative to identify global extrema on a closed interval.</p>
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("Maximize area of rectangle with perimeter 20.","A=xy, 2x+2y=20 → y=10−x. A=x(10−x). A'=10−2x=0 → x=5. Max area=25.")])}
  </div>
</main>{toc(secs)}</div>"""
    _page("applications-of-derivatives","Applications of Derivatives","Extrema, MVT, and optimization using derivatives.",body_appderiv)

    def body_indef(bc, pre):
        secs = [("def","Antiderivatives"),("rules","Integration Rules"),("examples","Examples")]
        return f"""<div class="topic-layout"><main class="topic-main">
  <nav class="breadcrumb">{bc}</nav><h1>Indefinite Integrals</h1>
  <div class="content-section" id="def"><h2>Antiderivatives</h2>
    <p>\\(\\int f(x)dx = F(x)+C\\) where \\(F'(x)=f(x)\\).</p>
  </div>
  <div class="content-section" id="rules"><h2>Integration Rules</h2>
    {props_table([("Power","\\(\\int x^n dx=\\frac{{x^{{n+1}}}}{{n+1}}+C\\) (n≠−1)"),("Exponential","\\(\\int e^x dx=e^x+C\\)"),("Trig","\\(\\int\\sin x\\,dx=-\\cos x+C\\)")])}
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("Find \\(\\int(3x^2+2x)dx\\).","\\(x^3+x^2+C\\).")])}
  </div>
</main>{toc(secs)}</div>"""
    _page("indefinite-integral","Indefinite Integrals","Antiderivatives and basic integration rules.",body_indef)

    def body_defint(bc, pre):
        secs = [("ftc","Fundamental Theorem"),("properties","Properties"),("examples","Examples")]
        return f"""<div class="topic-layout"><main class="topic-main">
  <nav class="breadcrumb">{bc}</nav><h1>Definite Integrals</h1>
  <div class="content-section" id="ftc"><h2>Fundamental Theorem of Calculus</h2>
    <div class="formula-box">\\[\\int_a^b f(x)dx=F(b)-F(a)\\]</div>
  </div>
  <div class="content-section" id="properties"><h2>Properties</h2>
    {props_table([("Linearity","\\(\\int_a^b(\\alpha f+\\beta g)=\\alpha\\int f+\\beta\\int g\\)"),("Reversal","\\(\\int_a^b f=-\\int_b^a f\\)"),("Additivity","\\(\\int_a^c f=\\int_a^b f+\\int_b^c f\\)")])}
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("Evaluate \\(\\int_0^2 x^2 dx\\).","\\([x^3/3]_0^2=8/3\\).")])}
  </div>
</main>{toc(secs)}</div>"""
    _page("definite-integral","Definite Integrals","Fundamental theorem of calculus and properties of definite integrals.",body_defint)

    def body_inttech(bc, pre):
        secs = [("sub","Substitution"),("parts","Integration by Parts"),("partial","Partial Fractions"),("examples","Examples")]
        return f"""<div class="topic-layout"><main class="topic-main">
  <nav class="breadcrumb">{bc}</nav><h1>Integration Techniques</h1>
  <div class="content-section" id="sub"><h2>Substitution</h2>
    <p>Let u=g(x), du=g'(x)dx: \\(\\int f(g(x))g'(x)dx=\\int f(u)du\\).</p>
  </div>
  <div class="content-section" id="parts"><h2>Integration by Parts</h2>
    <div class="formula-box">\\[\\int u\\,dv=uv-\\int v\\,du\\]</div>
  </div>
  <div class="content-section" id="partial"><h2>Partial Fractions</h2>
    <p>Decompose rational functions into simpler fractions before integrating.</p>
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("Find \\(\\int x e^x dx\\).","Parts: u=x, dv=eˣdx → xeˣ−eˣ+C.")])}
  </div>
</main>{toc(secs)}</div>"""
    _page("integration-techniques","Integration Techniques","Substitution, integration by parts, and partial fractions.",body_inttech)

    def body_appint(bc, pre):
        secs = [("area","Area Between Curves"),("volume","Volumes of Revolution"),("examples","Examples")]
        return f"""<div class="topic-layout"><main class="topic-main">
  <nav class="breadcrumb">{bc}</nav><h1>Applications of Integrals</h1>
  <div class="content-section" id="area"><h2>Area Between Curves</h2>
    <div class="formula-box">\\[A=\\int_a^b[f(x)-g(x)]dx\\quad(f\\geq g)\\]</div>
  </div>
  <div class="content-section" id="volume"><h2>Volumes of Revolution</h2>
    <p>Disk method: \\(V=\\pi\\int_a^b[f(x)]^2dx\\). Shell method: \\(V=2\\pi\\int_a^b x f(x)dx\\).</p>
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("Area between y=x² and y=x on [0,1].","\\(\\int_0^1(x-x^2)dx=[x^2/2-x^3/3]_0^1=1/6\\).")])}
  </div>
</main>{toc(secs)}</div>"""
    _page("applications-of-integrals","Applications of Integrals","Area between curves and volumes of revolution.",body_appint)

    def body_seq(bc, pre):
        secs = [("sequences","Sequences"),("series","Series"),("tests","Convergence Tests"),("examples","Examples")]
        return f"""<div class="topic-layout"><main class="topic-main">
  <nav class="breadcrumb">{bc}</nav><h1>Sequences and Series</h1>
  <div class="content-section" id="sequences"><h2>Sequences</h2>
    <p>A sequence \\({{a_n}}\\) converges to L if \\(\\lim_{{n\\to\\infty}}a_n=L\\).</p>
  </div>
  <div class="content-section" id="series"><h2>Series</h2>
    <p>\\(\\sum_{{n=1}}^\\infty a_n\\) converges if partial sums converge. Geometric series: \\(\\sum ar^n=\\frac{{a}}{{1-r}}\\) for |r|&lt;1.</p>
  </div>
  <div class="content-section" id="tests"><h2>Convergence Tests</h2>
    {props_table([("Ratio","\\(L=\\lim|a_{{n+1}}/a_n|\\): converges if L&lt;1"),("Integral","Compare to \\(\\int f\\)"),("Comparison","Compare to known series")])}
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("Does \\(\\sum 1/n^2\\) converge?","Yes, p-series with p=2&gt;1.")])}
  </div>
</main>{toc(secs)}</div>"""
    _page("sequences-and-series","Sequences and Series","Convergence of sequences and series with key tests.",body_seq)

    def body_taylor(bc, pre):
        secs = [("def","Taylor Series"),("common","Common Series"),("examples","Examples")]
        return f"""<div class="topic-layout"><main class="topic-main">
  <nav class="breadcrumb">{bc}</nav><h1>Taylor Series</h1>
  <div class="content-section" id="def"><h2>Taylor Series</h2>
    <div class="formula-box">\\[f(x)=\\sum_{{n=0}}^\\infty\\frac{{f^{{(n)}}(a)}}{{n!}}(x-a)^n\\]</div>
  </div>
  <div class="content-section" id="common"><h2>Common Series (a=0)</h2>
    {props_table([("\\(e^x\\)","\\(\\sum x^n/n!\\)"),("\\(\\sin x\\)","\\(\\sum(-1)^n x^{{2n+1}}/(2n+1)!\\)"),("\\(\\cos x\\)","\\(\\sum(-1)^n x^{{2n}}/(2n)!\\)"),("\\(\\ln(1+x)\\)","\\(\\sum(-1)^{{n+1}}x^n/n\\), |x|≤1")])}
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("Approximate \\(e^{{0.1}}\\) using 3 terms.","\\(1+0.1+0.01/2=1.105\\). Exact: ≈1.10517.")])}
  </div>
</main>{toc(secs)}</div>"""
    _page("taylor-series","Taylor Series","Taylor and Maclaurin series expansions and common examples.",body_taylor)

    def body_partial(bc, pre):
        secs = [("def","Partial Derivatives"),("gradient","Gradient"),("examples","Examples")]
        return f"""<div class="topic-layout"><main class="topic-main">
  <nav class="breadcrumb">{bc}</nav><h1>Partial Derivatives</h1>
  <div class="content-section" id="def"><h2>Partial Derivatives</h2>
    <p>\\(\\partial f/\\partial x\\): differentiate f with respect to x, treating all other variables as constants.</p>
  </div>
  <div class="content-section" id="gradient"><h2>Gradient</h2>
    <div class="formula-box">\\[\\nabla f=\\left(\\frac{{\\partial f}}{{\\partial x}},\\frac{{\\partial f}}{{\\partial y}},\\frac{{\\partial f}}{{\\partial z}}\\right)\\]</div>
    <p>Points in the direction of steepest ascent.</p>
  </div>
  <div class="content-section" id="examples"><h2>Examples</h2>
    {examples_html([("Find \\(\\partial f/\\partial x\\) for \\(f=x^2y+y^3\\).","\\(2xy\\).")])}
  </div>
</main>{toc(secs)}</div>"""
    _page("partial-derivatives","Partial Derivatives","Computing partial derivatives and the gradient vector.",body_partial)

    # Remaining calculus pages (shorter bodies for brevity)
    simple_pages = [
        ("infinite-limits","Infinite Limits","Limits at infinity and infinite limits.",
         [("def","Definition"),("examples","Examples")],
         "<p>\\(\\lim_{{x\\to\\infty}}f(x)=L\\) if f(x)→L as x grows without bound. Horizontal asymptote at y=L.</p>",
         examples_html([("\\(\\lim_{{x\\to\\infty}}\\frac{{1}}{{x}}\\)","= 0.")])),
        ("higher-order-derivatives","Higher-Order Derivatives","Second and higher derivatives and their applications.",
         [("def","Definition"),("examples","Examples")],
         props_table([("f''(x)","Second derivative; measures concavity"),("f'''(x)","Third derivative"),("f^(n)(x)","nth derivative")]),
         examples_html([("Find f''(x) for f(x)=x\u2074.","f'=4x\u00b3, f''=12x\u00b2.")])),
        ("implicit-differentiation","Implicit Differentiation","Differentiating implicitly defined functions.",
         [("method","Method"),("examples","Examples")],
         "<p>Differentiate both sides with respect to x, applying chain rule to y terms (treating y as a function of x), then solve for dy/dx.</p>",
         examples_html([("Find dy/dx for x²+y²=25.","2x+2y(dy/dx)=0 → dy/dx=−x/y.")])),
        ("gradient","Gradient","The gradient vector and directional derivatives.",
         [("def","Definition"),("directional","Directional Derivative"),("examples","Examples")],
         f"<div class='formula-box'>\\[\\nabla f=\\left(\\frac{{\\partial f}}{{\\partial x_1}},\\ldots,\\frac{{\\partial f}}{{\\partial x_n}}\\right)\\]</div>{props_table([('Directional','\\(D_{{\\mathbf{{u}}}}f=\\nabla f\\cdot\\mathbf{{u}}\\)'),('Max rate','|∇f|, in direction ∇f')])}",
         examples_html([("∇f for f=x²+y².","(2x, 2y).")])),
        ("multiple-integrals","Multiple Integrals","Double and triple integrals over regions.",
         [("double","Double Integrals"),("examples","Examples")],
         "<div class='formula-box'>\\[\\iint_R f(x,y)\\,dA=\\int_a^b\\int_{{g(x)}}^{{h(x)}}f(x,y)\\,dy\\,dx\\]</div>",
         examples_html([("\\(\\int_0^1\\int_0^1 xy\\,dy\\,dx\\)","= \\(\\int_0^1 x/2\\,dx=1/4\\).")])),
        ("vector-calculus","Vector Calculus","Divergence, curl, and integral theorems.",
         [("div","Divergence & Curl"),("theorems","Integral Theorems"),("examples","Examples")],
         f"{props_table([('Divergence','\\(\\nabla\\cdot\\mathbf{{F}}=\\partial F_x/\\partial x+\\partial F_y/\\partial y+\\partial F_z/\\partial z\\)'),('Curl','\\(\\nabla\\times\\mathbf{{F}}\\)'),('Stokes','\\(\\iint(\\nabla\\times\\mathbf{{F}})\\cdot d\\mathbf{{S}}=\\oint\\mathbf{{F}}\\cdot d\\mathbf{{r}}\\)')])}",
         examples_html([("Divergence of F=(x,y,z).","∂x/∂x+∂y/∂y+∂z/∂z = 3.")])),
        ("differential-equation","Differential Equations","Introduction to ODEs and solution methods.",
         [("types","Types"),("examples","Examples")],
         f"{props_table([('Order','Highest derivative present'),('Linear','Coefficients depend only on x'),('Separable','Can write as f(y)dy=g(x)dx')])}",
         examples_html([("Solve dy/dx=y.","Separable: dy/y=dx → ln|y|=x+C → y=Ae^x.")])),
        ("separable-equations","Separable Equations","Solving separable first-order ODEs.",
         [("method","Method"),("examples","Examples")],
         "<p>Rewrite as \\(g(y)dy=f(x)dx\\), integrate both sides, solve for y.</p>",
         examples_html([("dy/dx = xy.","dy/y = x dx → ln|y|=x²/2+C → y=Ae^{{x²/2}}.")])),
        ("linear-differential-equations","Linear Differential Equations","First-order linear ODEs and integrating factors.",
         [("form","Standard Form"),("examples","Examples")],
         "<div class='formula-box'>\\[y'+P(x)y=Q(x),\\quad\\mu=e^{{\\int P\\,dx}}\\]</div><p>Multiply through by μ: \\((\\mu y)'=\\mu Q\\), then integrate.</p>",
         examples_html([("y'+y=e^x.","μ=eˣ. (eˣy)'=e^{{2x}} → y=e^x/2+Ce^{{-x}}.")])),
        ("second-order-equations","Second-Order Equations","Constant-coefficient second-order linear ODEs.",
         [("homogeneous","Homogeneous"),("examples","Examples")],
         f"<p>Characteristic equation: \\(ar^2+br+c=0\\).</p>{props_table([('Two real roots','\\(y=C_1e^{{r_1x}}+C_2e^{{r_2x}}\\)'),('Repeated root','\\(y=(C_1+C_2x)e^{{rx}}\\)'),('Complex roots','\\(y=e^{{\\alpha x}}(C_1\\cos\\beta x+C_2\\sin\\beta x)\\)')])}",
         examples_html([("y''−3y'+2y=0.","r²−3r+2=0 → r=1,2. y=C₁eˣ+C₂e²ˣ.")])),
        ("power-series","Power Series","Radius of convergence and power series solutions.",
         [("def","Definition"),("examples","Examples")],
         "<div class='formula-box'>\\[\\sum_{{n=0}}^\\infty c_n(x-a)^n,\\quad R=\\frac{{1}}{{\\limsup|c_n|^{{1/n}}}}\\]</div>",
         examples_html([("Radius of convergence of \\(\\sum x^n/n\\).","Ratio test: R=1.")])),
        ("convergence-tests","Convergence Tests","All major tests for series convergence.",
         [("tests","Tests"),("examples","Examples")],
         f"{props_table([('Ratio','L=lim|aₙ₊₁/aₙ|; converges if L<1'),('Root','L=lim|aₙ|^{{1/n}}; converges if L<1'),('Integral','Compare ∑aₙ to ∫f'),('Alternating','Converges if aₙ↘0')])}",
         examples_html([("Test \\(\\sum n!/n^n\\).","Ratio test: L=1/e<1, converges.")])),
    ]

    for slug, title, desc, secs, body_html, ex_html in simple_pages:
        def make_body(bc, pre, _secs=secs, _body=body_html, _ex=ex_html):
            inner = ""
            for sid, slabel in _secs:
                if sid == "examples":
                    inner += f'<div class="content-section" id="examples"><h2>Examples</h2>{_ex}</div>'
                elif sid == _secs[0][0]:
                    inner += f'<div class="content-section" id="{sid}"><h2>{slabel}</h2>{_body}</div>'
                else:
                    inner += f'<div class="content-section" id="{sid}"><h2>{slabel}</h2></div>'
            return f'<div class="topic-layout"><main class="topic-main"><nav class="breadcrumb">{bc}</nav><h1>{title}</h1>{inner}</main>{toc(_secs)}</div>'
        _page(slug, title, desc, make_body)

# ---------------------------------------------------------------------------
# GEOMETRY
# ---------------------------------------------------------------------------

def build_geometry():
    S = "geometry"

    def _page(slug, title, desc, body_fn):
        page(f"{S}/{slug}", title, "Geometry", f"/{S}/", desc, body_fn)

    def simple(slug, title, desc, h2, content, exs, extra=""):
        secs = [(slug.replace("-","_")[:10], h2)]
        if extra:
            secs.append(("indepth", "In Depth"))
        secs.append(("examples","Examples"))
        def body(bc, pre, _t=title, _h=h2, _c=content, _e=exs, _s=secs, _x=extra):
            depth_sec = f'<div class="content-section" id="indepth"><h2>In Depth</h2>{_x}</div>' if _x else ""
            return f'<div class="topic-layout"><main class="topic-main"><nav class="breadcrumb">{bc}</nav><h1>{_t}</h1><div class="content-section" id="{_s[0][0]}"><h2>{_h}</h2>{_c}</div>{depth_sec}<div class="content-section" id="examples"><h2>Examples</h2>{examples_html(_e)}</div></main>{toc(_s)}</div>'
        _page(slug, title, desc, body)

    simple("triangle","Triangle","Properties, area formulas, and theorems for triangles.",
        "Key Properties",
        props_table([("Area","\\(\\frac{1}{2}bh\\) or \\(\\frac{1}{2}ab\\sin C\\)"),("Perimeter","a+b+c"),("Angle sum","180°"),("Pythagorean","a²+b²=c² (right triangle)")]),
        [("Find the area of a triangle with base 8 and height 5.","A = ½·8·5 = 20.")])

    simple("circle","Circle","Circumference, area, arc length, and circle theorems.",
        "Formulas",
        props_table([("Area","\\(\\pi r^2\\)"),("Circumference","\\(2\\pi r\\)"),("Arc length","\\(r\\theta\\) (θ in radians)"),("Sector area","\\(\\frac{1}{2}r^2\\theta\\)")]),
        [("Circle with r=7. Find area and circumference.","A=49π≈153.94, C=14π≈43.98.")])

    simple("pythagorean-theorem","Pythagorean Theorem","The Pythagorean theorem and its converse.",
        "Statement",
        "<div class='formula-box'>\\[a^2+b^2=c^2\\]</div><p>In a right triangle, the square of the hypotenuse equals the sum of squares of the legs. Converse: if a²+b²=c², the triangle is right-angled.</p>",
        [("Legs 3 and 4. Find hypotenuse.","c=√(9+16)=5.")])

    simple("polygon","Polygon","Interior angles, area, and properties of polygons.",
        "Key Formulas",
        props_table([("Interior angle sum","(n−2)·180°"),("Regular interior angle","(n−2)·180°/n"),("Diagonals","n(n−3)/2")]),
        [("Sum of interior angles of a hexagon.","(6−2)·180°=720°.")])

    simple("quadrilateral","Quadrilateral","Properties and area formulas for quadrilaterals.",
        "Types & Areas",
        props_table([("Rectangle","A=lw"),("Parallelogram","A=bh"),("Trapezoid","A=½(b₁+b₂)h"),("Rhombus","A=½d₁d₂")]),
        [("Trapezoid with bases 6,10 and height 4.","A=½(6+10)·4=32.")])

    simple("angle","Angles","Types of angles and angle relationships.",
        "Angle Types",
        props_table([("Acute","0°<θ<90°"),("Right","θ=90°"),("Obtuse","90°<θ<180°"),("Supplementary","θ₁+θ₂=180°"),("Complementary","θ₁+θ₂=90°")]),
        [("Two supplementary angles, one is 65°.","Other = 180°−65°=115°.")])

    simple("area","Surface Area","Surface area formulas for common 3D solids.",
        "Formulas",
        props_table([("Cube","6a²"),("Rectangular prism","2(lw+lh+wh)"),("Cylinder","2πr²+2πrh"),("Sphere","4πr²"),("Cone","πr²+πrl")]),
        [("Surface area of a cylinder r=3, h=5.","2π(9)+2π(15)=48π≈150.8.")])

    simple("volume","Volume","Volume formulas for common 3D solids.",
        "Formulas",
        props_table([("Cube","a³"),("Rectangular prism","lwh"),("Cylinder","πr²h"),("Sphere","\\(\\frac{4}{3}\\pi r^3\\)"),("Cone","\\(\\frac{1}{3}\\pi r^2 h\\)")]),
        [("Volume of a sphere with r=3.","V=4π(27)/3=36π≈113.1.")])

    simple("coordinate-system","Coordinate System","Cartesian coordinates, quadrants, and plotting.",
        "Basics",
        "<p>Points (x,y) in the plane. Four quadrants. Distance: \\(d=\\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}\\). Midpoint: \\(\\left(\\frac{x_1+x_2}{2},\\frac{y_1+y_2}{2}\\right)\\).</p>",
        [("Midpoint of (2,4) and (6,8).","(4,6).")])

    simple("distance-formula","Distance Formula","Distance between two points in the plane.",
        "Formula",
        "<div class='formula-box'>\\[d=\\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}\\]</div>",
        [("Distance from (1,2) to (4,6).","d=√(9+16)=5.")])

    simple("slope","Slope","Slope of a line and slope-intercept form.",
        "Definition",
        props_table([("Slope","\\(m=\\frac{y_2-y_1}{x_2-x_1}\\)"),("Slope-intercept","y=mx+b"),("Parallel","Equal slopes"),("Perpendicular","Slopes are negative reciprocals")]),
        [("Slope through (1,2) and (3,8).","m=(8−2)/(3−1)=3.")])

    simple("line-geometry","Lines","Equations of lines and their properties.",
        "Forms",
        props_table([("Slope-intercept","y=mx+b"),("Point-slope","y−y₁=m(x−x₁)"),("Standard","Ax+By=C")]),
        [("Line through (2,3) with slope 4.","y−3=4(x−2) → y=4x−5.")])

    simple("plane-geometry","Plane Geometry","Fundamental theorems of Euclidean plane geometry.",
        "Key Theorems",
        props_table([("Parallel lines","Alternate interior angles equal"),("Triangle","Angle sum = 180°"),("Inscribed angle","Half the central angle")]),
        [("Two parallel lines cut by a transversal. Co-interior angles sum to?","180°.")])

    simple("solid-geometry","Solid Geometry","Properties of 3D solids.",
        "Euler's Formula",
        "<div class='formula-box'>\\[V - E + F = 2\\]</div><p>For any convex polyhedron: vertices − edges + faces = 2.</p>",
        [("Cube: V=8, E=12. Find F.","F=2−8+12=6.")])

    simple("sphere","Sphere","Surface area and volume of a sphere.",
        "Formulas",
        props_table([("Volume","\\(\\frac{4}{3}\\pi r^3\\)"),("Surface area","\\(4\\pi r^2\\)"),("Great circle","Circle with same center and radius as sphere")]),
        [("Sphere r=6. Volume?","V=4π(216)/3=288π≈904.8.")])

    simple("ellipse","Ellipse","Equation, foci, and properties of ellipses.",
        "Standard Form",
        "<div class='formula-box'>\\[\\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1\\quad(a>b)\\]</div>" +
        props_table([("Foci","(±c,0), c²=a²−b²"),("Eccentricity","e=c/a<1")]),
        [("Ellipse a=5, b=3. Find c.","c=√(25−9)=4.")])

    simple("parabola","Parabola","Equation, focus, and directrix of a parabola.",
        "Standard Form",
        "<div class='formula-box'>\\[y=ax^2+bx+c\\quad\\text{or}\\quad(x-h)^2=4p(y-k)\\]</div>" +
        props_table([("Focus","(h, k+p)"),("Directrix","y=k−p"),("Vertex","(h,k)")]),
        [("y=x². Find focus.","4p=1 → p=1/4. Focus at (0,1/4).")])

    simple("hyperbola","Hyperbola","Equation, foci, and asymptotes of hyperbolas.",
        "Standard Form",
        "<div class='formula-box'>\\[\\frac{x^2}{a^2}-\\frac{y^2}{b^2}=1\\]</div>" +
        props_table([("Foci","(±c,0), c²=a²+b²"),("Asymptotes","y=±(b/a)x")]),
        [("Hyperbola a=3, b=4. Find c.","c=√(9+16)=5.")])

    simple("conic-sections","Conic Sections","Unified treatment of circles, ellipses, parabolas, and hyperbolas.",
        "General Equation",
        "<p>Ax²+Bxy+Cy²+Dx+Ey+F=0. Discriminant B²−4AC: &lt;0 ellipse, =0 parabola, &gt;0 hyperbola.</p>",
        [("Classify x²+y²=9.","Circle (A=C, B=0).")])

    simple("trigonometry","Trigonometry","Trig ratios, identities, and the unit circle.",
        "Key Identities",
        props_table([("Pythagorean","sin²θ+cos²θ=1"),("Double angle","sin2θ=2sinθcosθ"),("Law of sines","a/sinA=b/sinB=c/sinC"),("Law of cosines","c²=a²+b²−2ab cosC")]),
        [("Find sin(30°).","1/2.")])

    simple("similarity","Similarity","Similar figures, scale factors, and AA/SAS/SSS criteria.",
        "Criteria",
        props_table([("AA","Two pairs of equal angles"),("SAS","Two sides proportional, included angle equal"),("SSS","All three sides proportional")]),
        [("Triangles with sides 3,4,5 and 6,8,10. Similar?","Yes, SSS ratio 1:2.")])

    simple("congruence","Congruence","Congruent figures and triangle congruence criteria.",
        "Triangle Criteria",
        props_table([("SSS","All three sides equal"),("SAS","Two sides and included angle"),("ASA","Two angles and included side"),("AAS","Two angles and non-included side")]),
        [("Two triangles: sides 5,7,9 each. Congruent?","Yes, by SSS.")])

    simple("transformation-geometry","Transformations","Translations, rotations, reflections, and dilations.",
        "Types",
        props_table([("Translation","(x,y)→(x+a,y+b)"),("Rotation 90°","(x,y)→(−y,x)"),("Reflection (x-axis)","(x,y)→(x,−y)"),("Dilation","(x,y)→(kx,ky)")]),
        [("Reflect (3,4) over x-axis.","(3,−4).")])

    simple("euclidean-geometry","Euclidean Geometry","Euclid's postulates and classical theorems.",
        "Euclid's Postulates",
        props_table([("1","A straight line can be drawn between any two points"),("2","A line segment can be extended indefinitely"),("5","Parallel postulate: exactly one parallel through a point")]),
        [("What does the parallel postulate imply?","The angle sum of a triangle is exactly 180°.")])

    simple("analytic-geometry","Analytic Geometry","Coordinate geometry and algebraic treatment of geometric objects.",
        "Key Tools",
        props_table([("Line","y=mx+b"),("Circle","(x−h)²+(y−k)²=r²"),("Distance","√((Δx)²+(Δy)²)")]),
        [("Center and radius of (x−2)²+(y+3)²=16.","Center (2,−3), r=4.")])

    simple("differential-geometry","Differential Geometry","Curvature, curves, and surfaces.",
        "Curvature",
        "<div class='formula-box'>\\[\\kappa=\\frac{|y''|}{(1+y'^2)^{3/2}}\\]</div><p>Measures how sharply a curve bends at each point.</p>",
        [("Curvature of y=x² at x=0.","κ=|2|/(1+0)^{3/2}=2.")])

    simple("geometric-constructions","Geometric Constructions","Classical compass-and-straightedge constructions.",
        "Constructible Operations",
        props_table([("Bisect segment","Perpendicular bisector construction"),("Bisect angle","Arc intersection method"),("Perpendicular","From point to line")]),
        [("Can you trisect an angle with compass and straightedge?","No — proved impossible by Galois theory.")])

    simple("polyhedron","Polyhedron","Platonic solids and Euler's formula for polyhedra.",
        "Platonic Solids",
        props_table([("Tetrahedron","4 faces, 4 vertices, 6 edges"),("Cube","6 faces, 8 vertices, 12 edges"),("Octahedron","8 faces, 6 vertices, 12 edges"),("Dodecahedron","12 faces, 20 vertices, 30 edges"),("Icosahedron","20 faces, 12 vertices, 30 edges")]),
        [("Verify Euler's formula for a cube.","V−E+F=8−12+6=2. ✓")])

    simple("point-geometry","Points","Collinearity, betweenness, and point relationships.",
        "Key Concepts",
        props_table([("Collinear","Three points on the same line"),("Midpoint","Equidistant from both endpoints"),("Centroid","Average of triangle vertices")]),
        [("Centroid of triangle (0,0),(6,0),(3,6).","((0+6+3)/3,(0+0+6)/3)=(3,2).")])

# ---------------------------------------------------------------------------
# NUMBER THEORY
# ---------------------------------------------------------------------------

def build_number_theory():
    S = "number-theory"

    def _page(slug, title, desc, body_fn):
        page(f"{S}/{slug}", title, "Number Theory", f"/{S}/", desc, body_fn)

    def simple(slug, title, desc, h2, content, exs, extra=""):
        secs = [(slug.replace("-","_")[:10], h2)]
        if extra:
            secs.append(("indepth", "In Depth"))
        secs.append(("examples","Examples"))
        def body(bc, pre, _t=title, _h=h2, _c=content, _e=exs, _s=secs, _x=extra):
            depth_sec = f'<div class="content-section" id="indepth"><h2>In Depth</h2>{_x}</div>' if _x else ""
            return f'<div class="topic-layout"><main class="topic-main"><nav class="breadcrumb">{bc}</nav><h1>{_t}</h1><div class="content-section" id="{_s[0][0]}"><h2>{_h}</h2>{_c}</div>{depth_sec}<div class="content-section" id="examples"><h2>Examples</h2>{examples_html(_e)}</div></main>{toc(_s)}</div>'
        _page(slug, title, desc, body)

    simple("prime-number","Prime Numbers","Definition, properties, and distribution of prime numbers.",
        "Definition & Properties",
        props_table([("Prime","Integer >1 with no divisors other than 1 and itself"),("Infinitude","There are infinitely many primes (Euclid)"),("Prime counting","π(x) ~ x/ln x (Prime Number Theorem)")]),
        [("Is 97 prime?","Yes — not divisible by 2,3,5,7 (√97<10).")])

    simple("prime-factorization","Prime Factorization","Unique factorization and the Fundamental Theorem of Arithmetic.",
        "Fundamental Theorem",
        "<p>Every integer n>1 can be written uniquely as \\(n=p_1^{{a_1}}p_2^{{a_2}}\\cdots p_k^{{a_k}}\\) (up to order).</p>",
        [("Factor 360.","360=2³·3²·5.")])

    simple("divisibility","Divisibility","Divisibility rules and properties.",
        "Rules",
        props_table([("2","Last digit even"),("3","Digit sum divisible by 3"),("4","Last two digits divisible by 4"),("9","Digit sum divisible by 9"),("11","Alternating digit sum divisible by 11")]),
        [("Is 1234 divisible by 4?","Last two digits: 34. 34/4=8.5. No.")])

    simple("greatest-common-divisor","GCD","Greatest common divisor and the Euclidean algorithm.",
        "Euclidean Algorithm",
        "<div class='formula-box'>\\[\\gcd(a,b)=\\gcd(b,a\\bmod b)\\]</div>",
        [("gcd(48,18).","48=2·18+12; 18=1·12+6; 12=2·6+0. gcd=6.")])

    simple("least-common-multiple","LCM","Least common multiple and its relation to GCD.",
        "Formula",
        "<div class='formula-box'>\\[\\text{lcm}(a,b)=\\frac{|ab|}{\\gcd(a,b)}\\]</div>",
        [("lcm(12,18).","gcd=6. lcm=12·18/6=36.")])

    simple("euclidean-algorithm","Euclidean Algorithm","The Euclidean algorithm for computing GCD.",
        "Algorithm",
        "<p>Repeatedly replace (a,b) with (b, a mod b) until b=0. The last nonzero remainder is gcd(a,b).</p>",
        [("gcd(252,105).","252=2·105+42; 105=2·42+21; 42=2·21+0. gcd=21.")])

    simple("modular-arithmetic","Modular Arithmetic","Congruences, residues, and modular operations.",
        "Congruence",
        "<div class='formula-box'>\\[a\\equiv b\\pmod{m}\\iff m\\mid(a-b)\\]</div>" +
        props_table([("Addition","(a+b) mod m"),("Multiplication","(ab) mod m"),("Inverse","ax≡1 (mod m) if gcd(a,m)=1")]),
        [("17 mod 5.","17=3·5+2, so 17≡2 (mod 5).")])

    simple("fermats-little-theorem","Fermat's Little Theorem","Fermat's little theorem and its applications.",
        "Statement",
        "<div class='formula-box'>\\[a^p\\equiv a\\pmod{p}\\quad(p\\text{ prime})\\]</div><p>Equivalently, if p∤a: \\(a^{{p-1}}\\equiv1\\pmod{{p}}\\).</p>",
        [("2¹⁰ mod 11.","By FLT, 2¹⁰≡1 (mod 11).")])

    simple("euler-totient","Euler's Totient Function","φ(n) and Euler's generalization of Fermat's theorem.",
        "Definition",
        "<div class='formula-box'>\\[\\varphi(n)=n\\prod_{p|n}\\left(1-\\frac{1}{p}\\right)\\]</div><p>Euler's theorem: \\(a^{{\\varphi(n)}}\\equiv1\\pmod{{n}}\\) when gcd(a,n)=1.</p>",
        [("φ(12).","12=2²·3. φ=12·(1−1/2)·(1−1/3)=4.")])

    simple("chinese-remainder-theorem","Chinese Remainder Theorem","Solving simultaneous congruences.",
        "Statement",
        "<p>If m₁,…,mₖ are pairwise coprime, the system x≡aᵢ (mod mᵢ) has a unique solution mod M=m₁⋯mₖ.</p>",
        [("x≡2(mod 3), x≡3(mod 5).","x=8 (mod 15).")])

    simple("quadratic-residue","Quadratic Residues","Legendre symbol and quadratic reciprocity.",
        "Definition",
        "<p>a is a QR mod p if x²≡a (mod p) has a solution. Legendre symbol: \\(\\left(\\frac{{a}}{{p}}\\right)=a^{{(p-1)/2}}\\bmod p\\in\\{{0,\\pm1\\}}\\).</p>",
        [("Is 2 a QR mod 7?","2³=8≡1 (mod 7). Yes.")])

    simple("primitive-root","Primitive Roots","Generators of the multiplicative group mod n.",
        "Definition",
        "<p>g is a primitive root mod n if its powers generate all units mod n. Exists when n=1,2,4,pᵏ, or 2pᵏ.</p>",
        [("Is 2 a primitive root mod 5?","2¹=2,2²=4,2³=3,2⁴=1. Yes, order 4=φ(5).")])

    simple("diophantine-equations","Diophantine Equations","Integer solutions to polynomial equations.",
        "Linear Case",
        "<p>ax+by=c has integer solutions iff gcd(a,b)|c. General solution: x=x₀+bt/d, y=y₀−at/d where d=gcd(a,b).</p>",
        [("3x+5y=1.","gcd=1|1. x=2,y=−1 is one solution.")])

    simple("continued-fractions","Continued Fractions","Finite and infinite continued fractions.",
        "Definition",
        "<div class='formula-box'>\\[a_0+\\cfrac{1}{a_1+\\cfrac{1}{a_2+\\cdots}}\\]</div>",
        [("CF of 7/5.","7/5=1+2/5=1+1/(5/2)=1+1/(2+1/2)=[1;2,2].")])

    simple("arithmetic-functions","Arithmetic Functions","Multiplicative functions like σ, τ, and μ.",
        "Key Functions",
        props_table([("τ(n)","Number of divisors"),("σ(n)","Sum of divisors"),("μ(n)","Möbius function"),("φ(n)","Euler totient")]),
        [("τ(12) and σ(12).","Divisors: 1,2,3,4,6,12. τ=6, σ=28.")])

    simple("mobius-function","Möbius Function","The Möbius function and Möbius inversion.",
        "Definition",
        props_table([("μ(1)","1"),("μ(n)","(−1)ᵏ if n is product of k distinct primes"),("μ(n)","0 if n has a squared prime factor")]),
        [("μ(6).","6=2·3, two distinct primes. μ(6)=(−1)²=1.")])

    simple("sieve-of-eratosthenes","Sieve of Eratosthenes","Algorithm for finding all primes up to n.",
        "Algorithm",
        "<p>Mark all multiples of each prime p≤√n as composite. Remaining unmarked numbers are prime.</p>",
        [("Primes up to 20.","2,3,5,7,11,13,17,19.")])

    simple("goldbach-conjecture","Goldbach's Conjecture","Every even integer >2 is the sum of two primes.",
        "Statement",
        "<p>Goldbach (1742): every even integer n>2 can be expressed as the sum of two primes. Verified up to 4×10¹⁸; unproven in general.</p>",
        [("Express 28 as sum of two primes.","5+23=28 or 11+17=28.")])

    simple("twin-primes","Twin Primes","Prime pairs differing by 2.",
        "Definition",
        "<p>Twin primes: pairs (p, p+2) both prime. Examples: (3,5),(5,7),(11,13),(17,19). Twin Prime Conjecture: infinitely many such pairs (unproven).</p>",
        [("Find twin primes between 20 and 40.","(29,31) and (41,43) — wait, (29,31) qualifies.")])

    simple("mersenne-primes","Mersenne Primes","Primes of the form 2ᵖ−1.",
        "Definition",
        "<p>Mₚ=2ᵖ−1 is prime only if p is prime (necessary, not sufficient). Known Mersenne primes: M₂=3, M₃=7, M₅=31, M₇=127, …</p>",
        [("Is M₅=31 prime?","31 is prime. Yes.")])

    simple("perfect-numbers","Perfect Numbers","Numbers equal to the sum of their proper divisors.",
        "Definition",
        "<p>n is perfect if σ(n)=2n. Even perfect numbers: 2ᵖ⁻¹(2ᵖ−1) when 2ᵖ−1 is prime (Euler-Euclid theorem).</p>",
        [("Verify 6 is perfect.","Divisors: 1,2,3. Sum=6. ✓")])

    simple("p-adic-numbers","p-adic Numbers","The p-adic number system and its properties.",
        "Definition",
        "<p>The p-adic absolute value: |pⁿ·(a/b)|ₚ=p⁻ⁿ (p∤a,b). ℚₚ is the completion of ℚ under this metric.</p>",
        [("What is |12|₃?","12=3·4, so |12|₃=3⁻¹=1/3.")])

    simple("riemann-hypothesis","Riemann Hypothesis","The Riemann zeta function and its zeros.",
        "Statement",
        "<p>The Riemann zeta function \\(\\zeta(s)=\\sum_{{n=1}}^\\infty n^{{-s}}\\) has all non-trivial zeros on the critical line Re(s)=1/2. One of the Millennium Prize Problems.</p>",
        [("What are the trivial zeros of ζ(s)?","Negative even integers: −2,−4,−6,…")])

    simple("algebraic-number-theory","Algebraic Number Theory","Number fields, rings of integers, and ideals.",
        "Key Concepts",
        props_table([("Number field","Finite extension of ℚ"),("Ring of integers","Algebraic integers in a number field"),("Ideal","Generalizes prime factorization in rings")]),
        [("What is ℤ[i]?","The Gaussian integers: {a+bi : a,b∈ℤ}.")])

    simple("analytic-number-theory","Analytic Number Theory","Using analysis to study number-theoretic functions.",
        "Key Results",
        props_table([("PNT","π(x)~x/ln x"),("Dirichlet","Infinitely many primes in arithmetic progressions"),("Zeta","ζ(s)=∏(1−p⁻ˢ)⁻¹")]),
        [("What does PNT say about primes near 1000?","π(1000)≈1000/ln(1000)≈145. Actual: 168.")])

    simple("number-theory-cryptography","Number Theory in Cryptography","RSA, discrete logarithm, and cryptographic applications.",
        "RSA",
        props_table([("Key gen","Choose primes p,q; n=pq; e coprime to φ(n); d=e⁻¹ mod φ(n)"),("Encrypt","c=mᵉ mod n"),("Decrypt","m=cᵈ mod n")]),
        [("Why is RSA secure?","Factoring n=pq is computationally hard for large primes.")])

# ---------------------------------------------------------------------------
# LINEAR ALGEBRA
# ---------------------------------------------------------------------------

def build_linear_algebra():
    S = "linear-algebra"

    def _page(slug, title, desc, body_fn):
        page(f"{S}/{slug}", title, "Linear Algebra", f"/{S}/", desc, body_fn)

    def simple(slug, title, desc, h2, content, exs, extra=""):
        secs = [(slug.replace("-","_")[:10], h2)]
        if extra:
            secs.append(("indepth", "In Depth"))
        secs.append(("examples","Examples"))
        def body(bc, pre, _t=title, _h=h2, _c=content, _e=exs, _s=secs, _x=extra):
            depth_sec = f'<div class="content-section" id="indepth"><h2>In Depth</h2>{_x}</div>' if _x else ""
            return f'<div class="topic-layout"><main class="topic-main"><nav class="breadcrumb">{bc}</nav><h1>{_t}</h1><div class="content-section" id="{_s[0][0]}"><h2>{_h}</h2>{_c}</div>{depth_sec}<div class="content-section" id="examples"><h2>Examples</h2>{examples_html(_e)}</div></main>{toc(_s)}</div>'
        _page(slug, title, desc, body)

    simple("vectors-in-rn","Vectors in ℝⁿ","Vector operations, norms, and dot products.",
        "Operations",
        props_table([("Addition","Component-wise"),("Scalar mult","Scale each component"),("Dot product","\\(\\mathbf{u}\\cdot\\mathbf{v}=\\sum u_iv_i\\)"),("Norm","\\(\\|\\mathbf{v}\\|=\\sqrt{\\mathbf{v}\\cdot\\mathbf{v}}\\)")]),
        [("Dot product of (1,2,3) and (4,5,6).","4+10+18=32.")])

    simple("linear-systems","Linear Systems","Gaussian elimination and solution sets.",
        "Gaussian Elimination",
        "<p>Row-reduce the augmented matrix [A|b] to row echelon form. Back-substitute to find solutions. Three cases: unique, infinite, or no solution.</p>",
        [("Solve x+y=3, 2x−y=0.","Add: 3x=3 → x=1, y=2.")])

    simple("determinant","Determinant","Computing determinants and their geometric meaning.",
        "Formulas",
        props_table([("2×2","ad−bc"),("3×3","Cofactor expansion"),("Geometric","|det A| = volume scaling factor"),("Invertible","det A ≠ 0 iff A invertible")]),
        [("det([[1,2],[3,4]]).","1·4−2·3=−2.")])

    simple("eigenvalue","Eigenvalues","Finding eigenvalues via the characteristic polynomial.",
        "Definition",
        "<div class='formula-box'>\\[Av=\\lambda v,\\quad\\det(A-\\lambda I)=0\\]</div>",
        [("Eigenvalues of [[2,1],[0,3]].","det=( 2−λ)(3−λ)=0 → λ=2,3.")])

    simple("eigenvector","Eigenvectors","Computing eigenvectors and eigenspaces.",
        "Method",
        "<p>For each eigenvalue λ, solve (A−λI)v=0. The null space of (A−λI) is the eigenspace.</p>",
        [("Eigenvector of [[2,1],[0,3]] for λ=2.","(A−2I)v=0: [[0,1],[0,1]]v=0 → v=(1,0).")])

    simple("linear-transformation","Linear Transformations","Matrix representations of linear maps.",
        "Definition",
        "<p>T:ℝⁿ→ℝᵐ is linear if T(u+v)=T(u)+T(v) and T(cu)=cT(u). Every linear map has a matrix representation A where T(x)=Ax.</p>",
        [("Is T(x,y)=(x+y, 2x) linear?","Yes — verify additivity and homogeneity.")])

    simple("subspace","Subspaces","Definition and examples of vector subspaces.",
        "Definition",
        "<p>W⊆ℝⁿ is a subspace if: (1) 0∈W, (2) closed under addition, (3) closed under scalar multiplication.</p>",
        [("Is the set of vectors with x+y=0 a subspace?","Yes — it's the null space of [1,1].")])

    simple("basis","Basis","Basis, coordinates, and change of basis.",
        "Definition",
        "<p>A basis is a linearly independent spanning set. Every vector has a unique representation in terms of a basis.</p>" +
        props_table([("Standard basis","e₁=(1,0,…,0), …, eₙ=(0,…,0,1)"),("Coordinates","[v]_B = coefficients in basis B")]),
        [("Is {(1,0),(0,1),(1,1)} a basis for ℝ²?","No — three vectors in ℝ² are linearly dependent.")])

    simple("dimension","Dimension","Dimension of vector spaces and subspaces.",
        "Rank-Nullity Theorem",
        "<div class='formula-box'>\\[\\text{rank}(A)+\\text{nullity}(A)=n\\]</div><p>dim(col A) + dim(null A) = number of columns.</p>",
        [("A is 3×5 with rank 3. Nullity?","5−3=2.")])

    simple("rank","Rank","Row rank, column rank, and their equality.",
        "Definition",
        "<p>rank(A) = dimension of column space = dimension of row space. Computed by counting pivot positions in row echelon form.</p>",
        [("Rank of [[1,2,3],[2,4,6]].","Row 2 = 2·Row 1. Rank = 1.")])

    simple("null-space","Null Space","Kernel of a linear transformation.",
        "Definition",
        "<div class='formula-box'>\\[\\text{null}(A)=\\{x\\in\\mathbb{R}^n : Ax=0\\}\\]</div>",
        [("Null space of [[1,2],[2,4]].","x+2y=0 → x=−2y. Null space: span{(−2,1)}.")])

    simple("inner-product","Inner Products","Inner product spaces, norms, and orthogonality.",
        "Definition",
        "<p>An inner product ⟨·,·⟩ satisfies linearity, symmetry, and positive-definiteness. Induces norm \\(\\|v\\|=\\sqrt{\\langle v,v\\rangle}\\).</p>",
        [("Standard inner product of (1,2) and (3,4).","1·3+2·4=11.")])

    simple("orthogonality","Orthogonality","Orthogonal vectors, projections, and orthogonal complements.",
        "Key Concepts",
        props_table([("Orthogonal","⟨u,v⟩=0"),("Projection","\\(\\text{proj}_v u=\\frac{\\langle u,v\\rangle}{\\langle v,v\\rangle}v\\)"),("Complement","W⊥ = all vectors orthogonal to W")]),
        [("Project (3,4) onto (1,0).","proj=(3,0).")])

    simple("gram-schmidt","Gram-Schmidt","Orthogonalization process.",
        "Process",
        "<p>Given basis {v₁,…,vₙ}, produce orthonormal basis {u₁,…,uₙ}:</p><div class='formula-box'>\\[u_k=\\frac{v_k-\\sum_{{j<k}}\\langle v_k,u_j\\rangle u_j}{\\|v_k-\\cdots\\|}\\]</div>",
        [("Orthogonalize {(1,1),(1,0)}.","u₁=(1,1)/√2. u₂=(1,0)−½(1,1)=(½,−½), normalized=(1,−1)/√2.")])

    simple("least-squares","Least Squares","Least squares solutions to overdetermined systems.",
        "Normal Equations",
        "<div class='formula-box'>\\[A^TAx=A^Tb\\]</div><p>Minimizes \\(\\|Ax-b\\|^2\\). Solution: \\(\\hat{x}=(A^TA)^{{-1}}A^Tb\\).</p>",
        [("Best fit line through (0,1),(1,2),(2,2).","Normal equations give slope≈0.5, intercept≈1.17.")])

    simple("lu-decomposition","LU Decomposition","Factoring a matrix into lower and upper triangular factors.",
        "Definition",
        "<p>A=LU where L is lower triangular (1s on diagonal) and U is upper triangular. Used for efficient solving of Ax=b.</p>",
        [("LU of [[2,1],[4,3]].","L=[[1,0],[2,1]], U=[[2,1],[0,1]].")])

    simple("qr-decomposition","QR Decomposition","Orthogonal-triangular factorization.",
        "Definition",
        "<p>A=QR where Q has orthonormal columns and R is upper triangular. Used in least squares and eigenvalue algorithms.</p>",
        [("Why use QR for least squares?","Q^TQ=I simplifies normal equations to Rx=Q^Tb.")])

    simple("singular-value-decomposition","Singular Value Decomposition","SVD and its applications.",
        "Definition",
        "<div class='formula-box'>\\[A=U\\Sigma V^T\\]</div><p>U,V orthogonal; Σ diagonal with singular values σ₁≥σ₂≥…≥0. Generalizes eigendecomposition to rectangular matrices.</p>",
        [("What do singular values represent?","The 'stretching factors' of the linear transformation A.")])


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    build_stats()
    build_calculus()
    build_geometry()
    build_number_theory()
    build_linear_algebra()
    print("Done.")
