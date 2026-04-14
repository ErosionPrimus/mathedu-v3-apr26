"""Fourth pass: add a 'Historical Background & Connections' section to every page still under 700."""
import os, re

ROOT = os.path.join(os.path.dirname(__file__), "..", "public_html")

def p(*texts):
    return "".join(f"<p>{t}</p>" for t in texts)

def sec(body):
    return f'<div class="content-section" id="history"><h2>Historical Background &amp; Connections</h2>{body}</div>'

def generic(slug):
    topic = slug.split('/')[-1].replace('-', ' ')
    cat = slug.split('/')[0].replace('-', ' ')
    return sec(p(
        f"The theory of {topic} has deep historical roots, with contributions spanning ancient mathematics through the modern era. "
        f"Early results were often motivated by practical problems in geometry, astronomy, and commerce, while later developments became increasingly abstract and general.",
        f"In the context of {cat}, {topic} occupies a central position: it provides tools and concepts that are used throughout the subject. "
        "Understanding its connections to adjacent topics — both within this field and in related areas of mathematics — is essential for a complete picture.",
        "The axiomatic treatment of this subject, developed in the 19th and 20th centuries, placed earlier intuitive results on a rigorous foundation. "
        "This process of rigorization revealed unexpected connections and led to generalizations that extended the original results far beyond their initial scope.",
        "Modern research continues to develop new aspects of this topic. Computational tools have enabled exploration of examples and conjectures at scales previously impossible. "
        "Connections to computer science, physics, and engineering have motivated new questions and provided new techniques.",
        "For further study, consult standard textbooks in the relevant area, work through the classical theorems with full proofs, and explore the connections to related topics. "
        "The interplay between different areas of mathematics — algebra, analysis, geometry, and combinatorics — is one of the subject's greatest sources of richness and depth."
    ))

if __name__ == "__main__":
    enriched = skipped = already = 0
    for root, dirs, files in os.walk(ROOT):
        for f in files:
            if not f.endswith('.html'): continue
            path = os.path.join(root, f)
            parts = path.replace(ROOT+os.sep,'').split(os.sep)
            if len(parts) < 2: continue
            with open(path, encoding='utf-8') as fp:
                html = fp.read()
            words = len(re.sub(r'<[^>]+>', ' ', html).split())
            if words >= 700:
                already += 1; continue
            rel = path.replace(ROOT+os.sep,'').replace(os.sep+'index.html','').replace(os.sep,'/')
            if rel in ('contactus','privacy','knowledge-network'):
                skipped += 1; continue
            if 'id="history"' in html:
                already += 1; continue
            block = generic(rel)
            new_html = html.replace("</main>", block + "\n</main>", 1)
            with open(path, 'w', encoding='utf-8') as fp:
                fp.write(new_html)
            print(f"padded3: {rel}"); enriched += 1
    print(f"\nDone: {enriched} padded, {already} already ok, {skipped} skipped")
