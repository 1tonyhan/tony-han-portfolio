# Tony Han Portfolio

Personal portfolio site for [Tony Han](https://github.com/1tonyhan).

## Pages

| Page | File |
|------|------|
| Home | `index.html` |
| Projects | `projects.html` |
| Resume | `resume.html` |
| About | `about.html` |
| Gallery | `gallery.html` |

### Project detail pages

| Project | File |
|---------|------|
| Autonomous Claw | `autonomous-claw.html` |
| Motor Feedback Circuit | `motor-feedback-circuit.html` |
| CRT TV Disassembly | `crt-tv-disassembly.html` |
| Phone Stand | `phone-stand.html` |
| Capacity Claw | `capacity-claw.html` |

All pages share a fixed content width of **1024px**. Page height varies by content.

## Local preview

```bash
python -m http.server 8080
```

Then open [http://localhost:8080](http://localhost:8080).

## Updating project links

Project image links on the Projects page are controlled by `data/projects.json`:

```json
{
  "id": "autonomous-claw",
  "label": "Autonomous Robot claw",
  "href": "autonomous-claw.html"
}
```

## GitHub Pages

This site is configured for GitHub Pages. After pushing to GitHub:

1. Open your repository on GitHub
2. Go to **Settings → Pages**
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**
4. Choose the **main** branch and **/ (root)** folder
5. Save — your site will be live at `https://1tonyhan.github.io/tony-han-portfolio/`

To use a custom domain later, add it under the same Pages settings.

## Regenerating project pages

If you update a project PDF, export a new PNG to `assets/projects/` and re-run:

```bash
python scripts/generate-project-pages.py
```
