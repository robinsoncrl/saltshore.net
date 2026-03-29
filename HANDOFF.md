# SaltShore Systems — Project Handoff
_Last updated: 2026-03-29_

---

## What This Is

A static marketing and documentation site for **SaltShore Systems**, a Maine-based software brand. Tagline: *"Where tides meet tech."* The company is pre-launch, building workflow and dashboard tools targeting gig workers, solo operators, and small teams.

The site is a digital presence and brand anchor — no backend, no database, no framework.

---

## Tech Stack

| Layer | Tech |
|---|---|
| Markup | HTML5, semantic |
| Styling | CSS3 — custom properties, Grid, Flexbox, `backdrop-filter` |
| Scripting | Vanilla JS — `fetch` API, scroll-spy, nav toggle |
| Font | Revans Medium (custom, 2026) — WOFF2/WOFF/OTF/TTF in `assets/fonts/` |
| Build | Python 3 (`_bake_dist.py`) — bakes partials into `/dist/` for production |
| Hosting | Static (GitHub-linked) |

---

## Project Structure

```
saltshore.net/
├── index.html               # Homepage
├── about/index.html         # Company story
├── products/index.html      # Product lineup
├── contact/index.html       # Contact info
├── docs/
│   ├── index.html           # Docs hub (scroll-spy sidebar)
│   └── filetree.html        # Project file tree reference
├── assets/
│   ├── css/style.css        # Global stylesheet (single source of truth for design)
│   └── fonts/               # Revans font files
├── partials/
│   ├── header.html          # Shared nav + logo (fetched client-side)
│   └── footer.html          # Shared footer (fetched client-side)
├── dist/                    # Baked production output — DO NOT edit directly
├── _bake_dist.py            # Build script
├── .gitignore
└── saltshore.net.code-workspace
```

`Legacy Artifacts/` and `.vscode/` are gitignored.

---

## How the Partials System Works

**Development (source files):** Each page fetches `header.html` and `footer.html` via JavaScript `fetch()` at runtime. Active nav state is set dynamically per page inside the `.then()` callback. If the fetch fails, a minimal inline fallback is rendered.

**Production (`/dist/`):** Run `python _bake_dist.py` to embed partials directly into each page as static HTML. The dist output has no runtime fetch dependency.

**Rule:** Always edit source files (`index.html`, `about/`, etc.) — never `dist/`. Rebuild dist before deploying.

---

## Design System

All design tokens live in `:root` in `assets/css/style.css`:

```css
--accent: #004466       /* Primary brand teal */
--bg:     #fdfdfd       /* Off-white background */
--text:   #222          /* Body text */
--muted:  #6b7a89       /* Secondary text */

--h1 / --h2 / --h3     /* Type scale */
--space-sm/md/lg/xl    /* Spacing rhythm: 12/24/48/64px */
--content-max: 720px   /* Standard content width */
```

Font is **Revans** (declared via `@font-face`). Reference it as `'Revans', sans-serif` — not `'Revans Medium'` or `serif`.

---

## Deployment Workflow

```bash
# 1. Edit source files
# 2. Rebuild dist
python _bake_dist.py

# 3. Commit
git add .
git commit -m "your message"

# 4. Push
git push
```

---

## Session Changes (2026-03-29)

Everything done in this session, in order:

| Change | Files |
|---|---|
| Added `:focus-visible` outline for keyboard accessibility | `style.css` |
| Added mobile hamburger menu (toggle via `aria-expanded` + CSS) | `header.html`, `style.css` |
| Added `.catch()` fallback to all 12 partial fetch calls | All 6 pages × 2 fetches |
| Removed Google Fonts Inter import; normalized `font-family` to Revans | `index.html` |
| Deleted stale `partials/TODO.txt` | — |
| Added `.gitignore` (excludes `.vscode/`, `Legacy Artifacts/`, Python artifacts) | `.gitignore` |
| Committed `saltshore.net.code-workspace` | — |
| Removed deleted `TODO.txt` from filetree | `docs/filetree.html` |
| Rebuilt `dist/` to reflect all changes | `dist/*` |

---

## Open Recommendations

These were identified but not implemented — judgment calls for the owner:

1. **Rename "Vibe Coding Dashboard Utilities"** — "Vibe coding" is an AI coding term; name likely doesn't reflect intent. Consider "Dashboard Utilities" or "Operations Dashboard."

2. **Remove or replace the construction banner** — the `🚧 Under construction` banner undermines brand confidence before a visitor reads anything. Consider removing it or replacing with a forward-looking note.

3. **Fix hero CTA** — "Contact Us" is a weak primary action when there's nothing to buy yet. Consider a scroll-down link or removing it until there's a signup/waitlist.

4. **Rewrite "Upcoming Project" section** — currently too vague ("a new digital solution designed to simplify complex tasks"). Either be specific or cut it.

5. **Fix mobile hero h1 font size** — `font-size: 1rem` at ≤600px (`index.html` line ~140) is almost certainly too small. Should be at least `1.6rem`.

6. **Remove "SaltShore Roadmap" from product grid** — it reads as a note, not a product. Move messaging to a standalone "What's next" section below the grid.

7. **Add Open Graph meta tags** — `og:title`, `og:description`, `og:image` on all pages. Currently social link previews are blank.

---

## Brand Notes

- **Voice:** Calm, direct, values-driven. Not startup-hype. Not corporate. Maine-coastal pragmatism.
- **Philosophy quote (from About page):** *"Software should feel like a well-built dock: steady, simple, and ready for whatever you bring to it."*
- **Logo:** `assets/SSS_logo_2.png` — circular anchor mark. Used in header and homepage mission section.
- **Audience:** Solo operators, gig workers, small teams. Not enterprise.
- **Status:** Pre-launch. Products described, not yet shipped. Docs are placeholder outlines.
