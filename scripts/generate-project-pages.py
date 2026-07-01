from pathlib import Path
import json

base = Path(__file__).resolve().parent.parent
meta = json.loads((base / "data" / "project-pages.json").read_text())

nav = """      <nav class="site-nav" aria-label="Main navigation">
        <a href="index.html">Home</a>
        <a href="projects.html" class="active">Projects</a>
        <a href="resume.html">Resume</a>
        <a href="about.html">About</a>
        <a href="gallery.html">Gallery</a>
      </nav>"""

template = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Tony Han — {title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="css/styles.css" />
  </head>
  <body>
    <header class="site-header">
{nav}
    </header>
    <main class="page-content">
      <div class="page-frame">
        <img src="assets/projects/{slug}.png" alt="{title}" loading="lazy" />
        <a
          class="back-link"
          href="projects.html"
          aria-label="Back to Projects"
          style="left:{x}%;top:{y}%;width:{w}%;height:{h}%"
        ></a>
      </div>
    </main>
  </body>
</html>
"""

for slug, info in meta.items():
    back = info["back"]
    html = template.format(
        title=info["title"],
        slug=slug,
        nav=nav,
        x=back["x"],
        y=back["y"],
        w=back["width"],
        h=back["height"],
    )
    (base / f"{slug}.html").write_text(html, encoding="utf-8")
    print(f"wrote {slug}.html")
