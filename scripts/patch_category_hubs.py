#!/usr/bin/env python3
"""Add level-3 tabs, data-subcategory, and article links to category hub index.html files."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "public_html"


def patch_calculus() -> None:
    p = ROOT / "calculus" / "index.html"
    t = p.read_text(encoding="utf-8")
    t = t.replace(
        '<div class="topic-grid" id="topicsGrid">',
        """<div class="category-hub-tabs" data-category-hub data-hub-root="#topicsGrid">
                <button type="button" class="category-hub-tab is-active" data-filter="all">All tracks</button>
                <button type="button" class="category-hub-tab" data-filter="limits">Limits &amp; continuity</button>
                <button type="button" class="category-hub-tab" data-filter="derivatives">Derivatives</button>
                <button type="button" class="category-hub-tab" data-filter="integrals">Integrals</button>
                <button type="button" class="category-hub-tab" data-filter="ode">Differential equations</button>
                <button type="button" class="category-hub-tab" data-filter="series">Series</button>
                <button type="button" class="category-hub-tab" data-filter="multivariable">Multivariable</button>
            </div>
            <div class="topic-grid" id="topicsGrid">""",
    )
    rep_cat = {
        "limits": "limits",
        "derivatives": "derivatives",
        "integrals": "integrals",
        "differential-equations": "ode",
        "series": "series",
        "multivariable": "multivariable",
    }
    for k, v in rep_cat.items():
        t = t.replace(f'data-category="{k}"', f'data-category="{k}" data-subcategory="{v}"')

    # h3 title -> slug directory (existing or generated)
    slug_by_title = {
        "Limit": "limit",
        "Continuity": "continuity",
        "Infinite Limits": "infinite-limits",
        "Derivative": "derivative",
        "Differentiation Rules": "differentiation-rules",
        "Implicit Differentiation": "implicit-differentiation",
        "Applications of Derivatives": "applications-of-derivatives",
        "Higher Order Derivatives": "higher-order-derivatives",
        "Integral": "integral",
        "Definite Integral": "definite-integral",
        "Indefinite Integral": "indefinite-integral",
        "Integration Techniques": "integration-techniques",
        "Applications of Integrals": "applications-of-integrals",
        "Differential Equation": "differential-equation",
        "Separable Equations": "separable-equations",
        "Linear Differential Equations": "linear-differential-equations",
        "Second Order Equations": "second-order-equations",
        "Sequences and Series": "sequences-and-series",
        "Convergence Tests": "convergence-tests",
        "Power Series": "power-series",
        "Taylor Series": "taylor-series",
        "Partial Derivatives": "partial-derivatives",
        "Multiple Integrals": "multiple-integrals",
        "Gradient": "gradient",
        "Vector Calculus": "vector-calculus",
    }

    def repl_article(m: re.Match[str]) -> str:
        block = m.group(0)
        hm = re.search(r"<h3>([^<]+)</h3>", block)
        if not hm:
            return block
        title = hm.group(1).strip()
        slug = slug_by_title.get(title)
        if not slug:
            return block
        if f'<a href="{slug}/"' in block or f"<a href='{slug}/'" in block:
            block = re.sub(
                r'<div class="topic-expand">[\s\S]*?</div>\s*<button class="read-more-toggle"[^>]*>.*?</button>',
                "",
                block,
            )
            if f'href="{slug}/"' not in block:
                block = re.sub(
                    r"(<p class=\"topic-description\">[^<]*</p>)",
                    rf'\1\n                        <a href="{slug}/" class="read-more">Full article →</a>',
                    block,
                    count=1,
                )
            return block
        block = re.sub(
            r'<div class="topic-expand">[\s\S]*?</div>\s*<button class="read-more-toggle"[^>]*>.*?</button>',
            f'<a href="{slug}/" class="read-more">Full article →</a>',
            block,
        )
        return block

    t = re.sub(r"<article class=\"topic-card\"[^>]*>[\s\S]*?</article>", repl_article, t)
    t = t.replace(
        """                <a href="./" class="tag">Limits</a>
                <a href="./" class="tag">Derivatives</a>
                <a href="./" class="tag">Integrals</a>
                <a href="./" class="tag">Differential Equations</a>
                <a href="./" class="tag">Series</a>
                <a href="./" class="tag">Multivariable Calculus</a>""",
        """                <a href="limit/" class="tag">Limits</a>
                <a href="derivative/" class="tag">Derivatives</a>
                <a href="integral/" class="tag">Integrals</a>
                <a href="differential-equation/" class="tag">Differential Equations</a>
                <a href="sequences-and-series/" class="tag">Series</a>
                <a href="partial-derivatives/" class="tag">Multivariable</a>""",
    )
    t = t.replace(
        "</body>",
        '    <script src="../js/category_hub.js"></script>\n</body>',
    )
    p.write_text(t, encoding="utf-8")
    print("patched", p)


def patch_geometry() -> None:
    p = ROOT / "geometry" / "index.html"
    t = p.read_text(encoding="utf-8")
    t = t.replace(
        '<h2>Geometry Topics</h2>\n                <div class="topics-grid">',
        """<h2>Geometry Topics</h2>
                <div class="category-hub-tabs" data-category-hub data-hub-root=".topics-grid">
                    <button type="button" class="category-hub-tab is-active" data-filter="all">All</button>
                    <button type="button" class="category-hub-tab" data-filter="foundations">Foundations</button>
                    <button type="button" class="category-hub-tab" data-filter="plane">Plane figures</button>
                    <button type="button" class="category-hub-tab" data-filter="coordinate">Coordinate &amp; conics</button>
                    <button type="button" class="category-hub-tab" data-filter="solid">Solid &amp; measure</button>
                    <button type="button" class="category-hub-tab" data-filter="advanced">Advanced</button>
                </div>
                <div class="topics-grid">""",
    )

    sub_map = [
        ("Euclidean Geometry", "euclidean-geometry", "foundations"),
        ("Point", "point-geometry", "foundations"),
        ("Line", "line-geometry", "foundations"),
        ("Plane", "plane-geometry", "foundations"),
        ("Triangle", "triangle", "plane"),
        ("Circle", "circle", "plane"),
        ("Polygon", "polygon", "plane"),
        ("Quadrilateral", "quadrilateral", "plane"),
        ("Angle", "angle", "plane"),
        ("Congruence", "congruence", "plane"),
        ("Similarity", "similarity", "plane"),
        ("Analytic Geometry", "analytic-geometry", "coordinate"),
        ("Coordinate System", "coordinate-system", "coordinate"),
        ("Distance Formula", "distance-formula", "coordinate"),
        ("Slope", "slope", "coordinate"),
        ("Conic Sections", "conic-sections", "coordinate"),
        ("Ellipse", "ellipse", "coordinate"),
        ("Parabola", "parabola", "coordinate"),
        ("Hyperbola", "hyperbola", "coordinate"),
        ("Solid Geometry", "solid-geometry", "solid"),
        ("Polyhedron", "polyhedron", "solid"),
        ("Sphere", "sphere", "solid"),
        ("Volume", "volume", "solid"),
        ("Surface Area", "surface-area", "solid"),
        ("Trigonometry", "trigonometry", "plane"),
        ("Pythagorean Theorem", "pythagorean-theorem", "plane"),
        ("Differential Geometry", "differential-geometry", "advanced"),
        ("Topology", "/topology/", "advanced"),
        ("Transformation Geometry", "transformation-geometry", "advanced"),
        ("Geometric Constructions", "geometric-constructions", "advanced"),
    ]

    for title, slug, sub in sub_map:
        # insert data-subcategory on article containing <h3>Title</h3>
        pat = rf'(<article class="topic-card">[\s\S]*?<h3>{re.escape(title)}</h3>)'
        t, n = re.subn(pat, rf'<article class="topic-card" data-subcategory="{sub}">\1'.replace("\\1", r"\1"), t, count=1)
        if n == 0:
            continue
        # replace expand+button with link if not triangle/circle (already linked)
        block_pat = rf'(<article class="topic-card" data-subcategory="{sub}">[\s\S]*?<h3>{re.escape(title)}</h3>[\s\S]*?</article>)'

        def fix_block(m: re.Match[str]) -> str:
            blk = m.group(1)
            if "Full article" in blk or "read-more" in blk and "href=" in blk:
                return blk
            href = slug if slug.startswith("/") else f"{slug}/"
            blk = re.sub(
                r'<div class="topic-expand">[\s\S]*?</div>\s*<button class="read-more-toggle"[^>]*>.*?</button>',
                f'<a href="{href}" class="read-more">Full article →</a>',
                blk,
            )
            return blk

        t = re.sub(block_pat, fix_block, t, count=1)

    t = t.replace(
        "</body>",
        '    <script src="../js/category_hub.js"></script>\n</body>',
    )
    p.write_text(t, encoding="utf-8")
    print("patched", p)


def patch_number_theory() -> None:
    p = ROOT / "number-theory" / "index.html"
    t = p.read_text(encoding="utf-8")
    t = t.replace(
        "seed/417/400/225's,little,theorem,mathematics",
        "seed/417/400/225",
    )
    t = t.replace(
        "seed/66/400/225's,totient,function,mathematics",
        "seed/66/400/225",
    )
    t = t.replace(
        "seed/319/400/225's,conjecture,mathematics",
        "seed/319/400/225",
    )
    t = t.replace(
        '<h2>Number Theory Topics</h2>\n                <div class="topics-grid">',
        """<h2>Number Theory Topics</h2>
                <div class="category-hub-tabs" data-category-hub data-hub-root=".topics-grid">
                    <button type="button" class="category-hub-tab is-active" data-filter="all">All</button>
                    <button type="button" class="category-hub-tab" data-filter="divisibility">Divisibility &amp; factorization</button>
                    <button type="button" class="category-hub-tab" data-filter="modular">Modular &amp; congruences</button>
                    <button type="button" class="category-hub-tab" data-filter="primes">Primes &amp; famous problems</button>
                    <button type="button" class="category-hub-tab" data-filter="advanced">Advanced &amp; analytic</button>
                </div>
                <div class="topics-grid">""",
    )

    items = [
        ("Prime Number", "prime-number", "primes", True),
        ("Composite Number", "composite-number", "divisibility", False),
        ("Modular Arithmetic", "modular-arithmetic", "modular", True),
        ("Congruence", "congruence", "modular", False),
        ("Divisibility", "divisibility", "divisibility", False),
        ("Greatest Common Divisor (GCD)", "greatest-common-divisor", "divisibility", False),
        ("Least Common Multiple (LCM)", "least-common-multiple", "divisibility", False),
        ("Euclidean Algorithm", "euclidean-algorithm", "divisibility", False),
        ("Prime Factorization", "prime-factorization", "divisibility", False),
        ("Sieve of Eratosthenes", "sieve-of-eratosthenes", "primes", False),
        ("Fermat's Little Theorem", "fermats-little-theorem", "modular", False),
        ("Euler's Totient Function", "euler-totient", "modular", False),
        ("Chinese Remainder Theorem", "chinese-remainder-theorem", "modular", False),
        ("Diophantine Equations", "diophantine-equations", "advanced", False),
        ("Perfect Number", "perfect-numbers", "primes", False),
        ("Mersenne Prime", "mersenne-primes", "primes", False),
        ("Twin Prime", "twin-primes", "primes", False),
        ("Goldbach's Conjecture", "goldbach-conjecture", "primes", False),
        ("Riemann Hypothesis", "riemann-hypothesis", "primes", False),
        ("Quadratic Residue", "quadratic-residue", "modular", False),
        ("Primitive Root", "primitive-root", "modular", False),
        ("Arithmetic Function", "arithmetic-functions", "advanced", False),
        ("Möbius Function", "mobius-function", "advanced", False),
        ("P-adic Numbers", "p-adic-numbers", "advanced", False),
        ("Continued Fraction", "continued-fractions", "advanced", False),
        ("Number Theory in Cryptography", "number-theory-cryptography", "advanced", False),
        ("Algebraic Number Theory", "algebraic-number-theory", "advanced", False),
        ("Analytic Number Theory", "analytic-number-theory", "advanced", False),
    ]

    for title, slug, sub, skip in items:
        pat = rf'(<article class="topic-card">[\s\S]*?<h3>{re.escape(title)}</h3>)'
        repl = rf'<article class="topic-card" data-subcategory="{sub}">\1'.replace("\\1", r"\1")
        t, c = re.subn(pat, repl, t, count=1)
        if c == 0:
            print("missed", title)
            continue

        block_pat = rf'(<article class="topic-card" data-subcategory="{sub}">[\s\S]*?<h3>{re.escape(title)}</h3>[\s\S]*?</article>)'

        def fix_block(m: re.Match[str]) -> str:
            blk = m.group(1)
            if "href=" in blk and "read-more" in blk:
                blk = re.sub(
                    r'<div class="topic-expand">[\s\S]*?</div>\s*<button class="read-more-toggle"[^>]*>.*?</button>',
                    "",
                    blk,
                )
                return blk
            blk = re.sub(
                r'<div class="topic-expand">[\s\S]*?</div>\s*<button class="read-more-toggle"[^>]*>.*?</button>',
                f'<a href="{slug}/" class="read-more">Full article →</a>',
                blk,
            )
            return blk

        t = re.sub(block_pat, fix_block, t, count=1)

    t = t.replace(
        "</body>",
        '    <script src="../js/category_hub.js"></script>\n</body>',
    )
    p.write_text(t, encoding="utf-8")
    print("patched", p)


def patch_linear_algebra() -> None:
    p = ROOT / "linear-algebra" / "index.html"
    t = p.read_text(encoding="utf-8")
    t = t.replace(
        '<h2>Topics in Linear Algebra</h2>\n                <div class="topics-grid">',
        """<h2>Topics in Linear Algebra</h2>
                <div class="category-hub-tabs" data-category-hub data-hub-root=".topics-grid">
                    <button type="button" class="category-hub-tab is-active" data-filter="all">All</button>
                    <button type="button" class="category-hub-tab" data-filter="core">Core objects</button>
                    <button type="button" class="category-hub-tab" data-filter="structure">Structure &amp; rank</button>
                    <button type="button" class="category-hub-tab" data-filter="geometry">Inner product &amp; orthogonality</button>
                    <button type="button" class="category-hub-tab" data-filter="factor">Factorizations</button>
                </div>
                <div class="topics-grid">""",
    )

    items = [
        ("Matrix", "/algebra/matrix/", "core", True),
        ("Vector Space", "/algebra/vector-space/", "core", True),
        ("Eigenvalue", "eigenvalue", "structure", False),
        ("Eigenvector", "eigenvector", "structure", False),
        ("Determinant", "determinant", "structure", False),
        ("Linear Transformation", "linear-transformation", "core", False),
        ("Vector", "vectors-in-rn", "core", False),
        ("Linear Systems", "linear-systems", "core", False),
        ("Subspace", "subspace", "structure", False),
        ("Basis", "basis", "structure", False),
        ("Dimension", "dimension", "structure", False),
        ("Rank", "rank", "structure", False),
        ("Null Space", "null-space", "structure", False),
        ("Orthogonality", "orthogonality", "geometry", False),
        ("Inner Product", "inner-product", "geometry", False),
        ("Gram-Schmidt Process", "gram-schmidt", "geometry", False),
        ("Least Squares", "least-squares", "geometry", False),
        ("Singular Value Decomposition", "singular-value-decomposition", "factor", False),
        ("LU Decomposition", "lu-decomposition", "factor", False),
        ("QR Decomposition", "qr-decomposition", "factor", False),
    ]

    for title, href, sub, external in items:
        pat = rf'(<article class="topic-card">[\s\S]*?<h3>{re.escape(title)}</h3>)'
        t, c = re.subn(pat, rf'<article class="topic-card" data-subcategory="{sub}">\1'.replace("\\1", r"\1"), t, count=1)
        if c == 0:
            print("missed LA", title)
            continue
        block_pat = rf'(<article class="topic-card" data-subcategory="{sub}">[\s\S]*?<h3>{re.escape(title)}</h3>[\s\S]*?</article>)'

        def fix_block(m: re.Match[str]) -> str:
            blk = m.group(1)
            blk = re.sub(
                r'<div class="topic-expand">[\s\S]*?</div>\s*<button class="read-more-toggle"[^>]*>.*?</button>',
                "",
                blk,
            )
            if external:
                al = f'<a href="{href}" class="read-more">Full article →</a>'
            else:
                al = f'<a href="{href}/" class="read-more">Full article →</a>'
            blk = re.sub(
                r"(<p>[^<]*</p>)",
                rf"\1\n                            {al}",
                blk,
                count=1,
            )
            return blk

        t = re.sub(block_pat, fix_block, t, count=1)

    t = t.replace(
        """                    <a href="./" class="tag">Algebra</a>
                    <a href="./" class="tag">Calculus</a>
                    <a href="./" class="tag">Geometry</a>
                    <a href="./" class="tag">Mathematical Analysis</a>""",
        """                    <a href="/algebra/" class="tag">Algebra</a>
                    <a href="/calculus/" class="tag">Calculus</a>
                    <a href="/geometry/" class="tag">Geometry</a>
                    <a href="/mathematical-analysis/" class="tag">Mathematical Analysis</a>""",
    )
    t = t.replace(
        "</body>",
        '    <script src="../js/category_hub.js"></script>\n</body>',
    )
    p.write_text(t, encoding="utf-8")
    print("patched", p)


def main() -> None:
    patch_calculus()
    patch_geometry()
    patch_number_theory()
    patch_linear_algebra()


if __name__ == "__main__":
    main()
