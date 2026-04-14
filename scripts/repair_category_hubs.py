#!/usr/bin/env python3
"""Repair hub pages: collapse stacked <article> opens (after bad patch), fix linear algebra Matrix card, apply attrs."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "public_html"


def collapse_stacked_after_grid(html: str, first_sub: str) -> str:
    return re.sub(
        r'(<div class="topics-grid">[\s\S]*?)(?:<article class="topic-card"(?: data-subcategory="[^"]+")?>)+(?=\s*<div class="topic-image">)',
        rf'\1<article class="topic-card" data-subcategory="{first_sub}">',
        html,
        count=1,
    )


def ensure_article_attrs(block: str, sub: str, href: str | None) -> str:
    block = re.sub(
        r'<article class="topic-card"( data-subcategory="[^"]+")?>',
        f'<article class="topic-card" data-subcategory="{sub}">',
        block,
        count=1,
    )
    if href is None:
        return block
    if "read-more" in block and "href=" in block and "topic-expand" not in block:
        return block
    block = re.sub(
        r'<div class="topic-expand">[\s\S]*?</div>\s*<button class="read-more-toggle"[^>]*>.*?</button>',
        "",
        block,
    )
    if href and f'href="{href}"' not in block:
        block = re.sub(
            r"(<p>[^<]*</p>)",
            rf'\1\n                            <a href="{href}" class="read-more">Full article →</a>',
            block,
            count=1,
        )
    return block


def article_block_pattern(title: str) -> str:
    """Match a single topic-card article that contains the given h3 title (no crossing </article>)."""
    return (
        r'<article class="topic-card"[^>]*>'
        rf'(?:(?!</article>)[\s\S])*<h3>{re.escape(title)}</h3>'
        r'(?:(?!</article>)[\s\S])*</article>'
    )


def process_specs(html: str, specs: list[tuple[str, str, str | None]]) -> str:
    for title, sub, href in specs:
        pat = article_block_pattern(title)

        def make_repl(m: re.Match[str]) -> str:
            return ensure_article_attrs(m.group(0), sub, href)

        html, n = re.subn(pat, make_repl, html, count=1)
        if n == 0:
            print("WARN missing", title)
    return html


def fix_linear_algebra_matrix(html: str) -> str:
    return re.sub(
        r'(<h3>Matrix</h3>\s*<p>A rectangular array of numbers arranged in rows and columns\. The fundamental object of study in linear algebra with applications in solving systems of equations, transformations, and data representation\.</p>)[\s\S]*?(?=\s*</div>\s*</div>\s*</article>)',
        r'\1\n                            <a href="/algebra/matrix/" class="read-more">Full article →</a>',
        html,
        count=1,
    )


def main() -> None:
    geom = [
        ("Euclidean Geometry", "foundations", "euclidean-geometry/"),
        ("Point", "foundations", "point-geometry/"),
        ("Line", "foundations", "line-geometry/"),
        ("Plane", "foundations", "plane-geometry/"),
        ("Triangle", "plane", "triangle/"),
        ("Circle", "plane", "circle/"),
        ("Polygon", "plane", "polygon/"),
        ("Quadrilateral", "plane", "quadrilateral/"),
        ("Angle", "plane", "angle/"),
        ("Congruence", "plane", "congruence/"),
        ("Similarity", "plane", "similarity/"),
        ("Analytic Geometry", "coordinate", "analytic-geometry/"),
        ("Coordinate System", "coordinate", "coordinate-system/"),
        ("Distance Formula", "coordinate", "distance-formula/"),
        ("Slope", "coordinate", "slope/"),
        ("Conic Sections", "coordinate", "conic-sections/"),
        ("Ellipse", "coordinate", "ellipse/"),
        ("Parabola", "coordinate", "parabola/"),
        ("Hyperbola", "coordinate", "hyperbola/"),
        ("Solid Geometry", "solid", "solid-geometry/"),
        ("Polyhedron", "solid", "polyhedron/"),
        ("Sphere", "solid", "sphere/"),
        ("Volume", "solid", "volume/"),
        ("Surface Area", "solid", "surface-area/"),
        ("Trigonometry", "plane", "trigonometry/"),
        ("Pythagorean Theorem", "plane", "pythagorean-theorem/"),
        ("Differential Geometry", "advanced", "differential-geometry/"),
        ("Topology", "advanced", "/topology/"),
        ("Transformation Geometry", "advanced", "transformation-geometry/"),
        ("Geometric Constructions", "advanced", "geometric-constructions/"),
    ]
    nt = [
        ("Prime Number", "primes", "prime-number/"),
        ("Composite Number", "divisibility", "composite-number/"),
        ("Modular Arithmetic", "modular", "modular-arithmetic/"),
        ("Congruence", "modular", "congruence/"),
        ("Divisibility", "divisibility", "divisibility/"),
        ("Greatest Common Divisor (GCD)", "divisibility", "greatest-common-divisor/"),
        ("Least Common Multiple (LCM)", "divisibility", "least-common-multiple/"),
        ("Euclidean Algorithm", "divisibility", "euclidean-algorithm/"),
        ("Prime Factorization", "divisibility", "prime-factorization/"),
        ("Sieve of Eratosthenes", "primes", "sieve-of-eratosthenes/"),
        ("Fermat's Little Theorem", "modular", "fermats-little-theorem/"),
        ("Euler's Totient Function", "modular", "euler-totient/"),
        ("Chinese Remainder Theorem", "modular", "chinese-remainder-theorem/"),
        ("Diophantine Equations", "advanced", "diophantine-equations/"),
        ("Perfect Number", "primes", "perfect-numbers/"),
        ("Mersenne Prime", "primes", "mersenne-primes/"),
        ("Twin Prime", "primes", "twin-primes/"),
        ("Goldbach's Conjecture", "primes", "goldbach-conjecture/"),
        ("Riemann Hypothesis", "primes", "riemann-hypothesis/"),
        ("Quadratic Residue", "modular", "quadratic-residue/"),
        ("Primitive Root", "modular", "primitive-root/"),
        ("Arithmetic Function", "advanced", "arithmetic-functions/"),
        ("Möbius Function", "advanced", "mobius-function/"),
        ("P-adic Numbers", "advanced", "p-adic-numbers/"),
        ("Continued Fraction", "advanced", "continued-fractions/"),
        ("Number Theory in Cryptography", "advanced", "number-theory-cryptography/"),
        ("Algebraic Number Theory", "advanced", "algebraic-number-theory/"),
        ("Analytic Number Theory", "advanced", "analytic-number-theory/"),
    ]
    la = [
        ("Matrix", "core", "/algebra/matrix/"),
        ("Vector Space", "core", "/algebra/vector-space/"),
        ("Eigenvalue", "structure", "eigenvalue/"),
        ("Eigenvector", "structure", "eigenvector/"),
        ("Determinant", "structure", "determinant/"),
        ("Linear Transformation", "core", "linear-transformation/"),
        ("Vector", "core", "vectors-in-rn/"),
        ("Linear Systems", "core", "linear-systems/"),
        ("Subspace", "structure", "subspace/"),
        ("Basis", "structure", "basis/"),
        ("Dimension", "structure", "dimension/"),
        ("Rank", "structure", "rank/"),
        ("Null Space", "structure", "null-space/"),
        ("Orthogonality", "geometry", "orthogonality/"),
        ("Inner Product", "geometry", "inner-product/"),
        ("Gram-Schmidt Process", "geometry", "gram-schmidt/"),
        ("Least Squares", "geometry", "least-squares/"),
        ("Singular Value Decomposition", "factor", "singular-value-decomposition/"),
        ("LU Decomposition", "factor", "lu-decomposition/"),
        ("QR Decomposition", "factor", "qr-decomposition/"),
    ]

    gp = ROOT / "geometry" / "index.html"
    ghtml = gp.read_text(encoding="utf-8")
    ghtml = collapse_stacked_after_grid(ghtml, "foundations")
    ghtml = process_specs(ghtml, geom)
    gp.write_text(ghtml, encoding="utf-8")
    print("repaired", gp)

    np = ROOT / "number-theory" / "index.html"
    nhtml = np.read_text(encoding="utf-8")
    nhtml = collapse_stacked_after_grid(nhtml, "primes")
    nhtml = process_specs(nhtml, nt)
    np.write_text(nhtml, encoding="utf-8")
    print("repaired", np)

    lp = ROOT / "linear-algebra" / "index.html"
    lhtml = lp.read_text(encoding="utf-8")
    lhtml = collapse_stacked_after_grid(lhtml, "core")
    lhtml = fix_linear_algebra_matrix(lhtml)
    lhtml = process_specs(lhtml, la)
    lp.write_text(lhtml, encoding="utf-8")
    print("repaired", lp)

    for p in (gp, np, lp):
        t = p.read_text(encoding="utf-8")
        if "category_hub.js" not in t:
            t = t.replace(
                "</body>",
                '    <script src="../js/category_hub.js"></script>\n</body>',
            )
            p.write_text(t, encoding="utf-8")


if __name__ == "__main__":
    main()
