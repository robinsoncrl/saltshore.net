import re, pathlib

ROOT = pathlib.Path(".")
DIST = ROOT / "dist"
HEADER = (ROOT / "partials/header.html").read_text(encoding="utf-8")
FOOTER = (ROOT / "partials/footer.html").read_text(encoding="utf-8")

pages = [
    (ROOT / "index.html",                      DIST / "index.html"),
    (ROOT / "about/index.html",                DIST / "about/index.html"),
    (ROOT / "products/index.html",             DIST / "products/index.html"),
    (ROOT / "products/calgen/index.html",      DIST / "products/calgen/index.html"),
    (ROOT / "products/finpro/index.html",      DIST / "products/finpro/index.html"),
    (ROOT / "products/ledgerpro/index.html",   DIST / "products/ledgerpro/index.html"),
    (ROOT / "products/suite/index.html",       DIST / "products/suite/index.html"),
    (ROOT / "contact/index.html",              DIST / "contact/index.html"),
    (ROOT / "docs/index.html",                 DIST / "docs/index.html"),
    (ROOT / "docs/filetree.html",              DIST / "docs/filetree.html"),
    (ROOT / "legal/index.html",                DIST / "legal/index.html"),
    (ROOT / "legal/eula-calgen.html",          DIST / "legal/eula-calgen.html"),
    (ROOT / "legal/eula-finpro.html",          DIST / "legal/eula-finpro.html"),
    (ROOT / "legal/eula-ledgerpro.html",       DIST / "legal/eula-ledgerpro.html"),
    (ROOT / "legal/eula-suite.html",           DIST / "legal/eula-suite.html"),
]

for src, dst in pages:
    html = src.read_text(encoding="utf-8")

    # Replace header placeholder + its fetch script block
    html = re.sub(
        r'\s*<!-- Shared header include -->\s*'
        r'<div id="header-placeholder"></div>\s*'
        r'<script>.*?</script>',
        "\n" + HEADER,
        html, flags=re.DOTALL
    )

    # Replace footer placeholder + its fetch script block
    html = re.sub(
        r'\s*<!-- Shared footer include -->\s*'
        r'<div id="footer-placeholder"></div>\s*'
        r'<script>.*?</script>',
        "\n" + FOOTER,
        html, flags=re.DOTALL
    )

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(html, encoding="utf-8")
    print(f"Baked: {dst}")

print("Done.")
