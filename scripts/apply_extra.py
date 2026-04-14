"""Apply extra_data_1, extra_data_2, and extra_data_3 to public_html pages."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from extra_data_1 import EXTRA2 as E1
from extra_data_2 import EXTRA2 as E2
from extra_data_3 import EXTRA3 as E3

ROOT = os.path.join(os.path.dirname(__file__), "..", "public_html")

COMBINED = {**E1, **E2, **E3}

def inject(html, sections):
    extra = "\n".join(sections)
    return html.replace("</main>", extra + "\n</main>", 1)

def run():
    for slug, sections in COMBINED.items():
        path = os.path.join(ROOT, slug, "index.html")
        if not os.path.exists(path):
            print(f"SKIP: {slug}")
            continue
        with open(path, encoding="utf-8") as f:
            html = f.read()
        if 'id="indepth"' in html or 'id="bg"' in html or 'id="background"' in html or 'id="overview"' in html:
            print(f"already done: {slug}")
            continue
        with open(path, "w", encoding="utf-8") as f:
            f.write(inject(html, sections))
        print(f"enriched: {slug}")

if __name__ == "__main__":
    run()
