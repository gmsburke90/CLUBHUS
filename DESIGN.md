# CLUBHUS — Design System

Reference doc for anyone (human or agent) touching `index.html` on `main`.
As of the "Promote finalized draft to index.html" commit, `index.html` is a
single self-contained file (inline `<style>`/`<script>`) — the old
`css/styles.css` and `js/script.js` are no longer referenced from it and are
legacy. Values below are pulled directly from the `:root` custom properties
in `index.html`'s `<style>` block — update there first, then reflect changes
here.

> Note for this branch (`claude/add-skill-to-project-xi4qdg`): it forked
> before the "tap redesign" landed on `main`, so files here (`versions/`,
> the old `css/styles.css`) may still reference the earlier racing-green /
> cream / brass / Fraunces system. This doc describes `main`'s current,
> live design — treat it as the source of truth going forward.

## Brand direction

- **Positioning:** a Danish lager for the moment right after the match — understated, not a loyalty program or lifestyle brand.
- **Voice:** short, plain sentences. Confident without being clever. "One lager. One moment." not "Discover a world of exclusive rewards."
- **Signature device:** the "tapline" — a vertical wood-colored rule running the height of the page, like the line down a tap handle. It's the one recurring structural motif; don't add a second one.

## Color

| Token | Value | Use |
|---|---|---|
| `--green-deep` | `#1F3B28` | Manifesto section background, primary heading color |
| `--green` | `#2E5339` | Secondary green (meta labels, SVG line art) |
| `--chalk` | `#F4F1EA` | Page background |
| `--chalk-dim` | `#E7E2D6` | "Find it" section background |
| `--wood` | `#8C6A4F` | Accent — tapline, plaque dots, provenance labels, focus outline |
| `--ink` | `#1A1A1A` | Body text, footer background |
| `--green-line` | `rgba(46,83,57,0.18)` | Hairline borders/rules |

No brass, no cream-warm/paper tiers, no line-light — this is a tighter, five-color system. Don't reintroduce the old racing-green/brass palette into new work on `main`.

## Type

| Token | Stack | Role |
|---|---|---|
| `--display` | Bricolage Grotesque, ui-sans-serif | All headings, wordmark, footer word, fact/provenance values, manifesto text — locked, one treatment scaling from 12px labels to the hero |
| `--body` | Inter, system sans fallback | Body copy, nav, labels |
| `--accent` | Instrument Serif, Georgia | Italic accent only (`<em>` in the hero headline, `.accent`) — used sparingly, never for full lines |

Conventions:
- `h1, h2, h3` get `text-wrap: balance` globally — don't override per-heading.
- `.plaque` — small uppercase eyebrow label with a wood dot, `.16em` letter-spacing.
- Type scale is fully tokenized (`--fs-display` through `--fs-body`) — use the existing steps, don't hardcode new font sizes.

## Layout

- Max content width: `--container: 1160px`.
- Side padding: `--gutter: clamp(22px, 6vw, 96px)`.
- Spacing is one 8px rhythm: `--space-1` (8px) through `--space-6` (64px), plus `--section-y` for vertical section padding. Use these tokens, not arbitrary margins.
- Single stacking breakpoint at `880px` for the two-column grids (hero, beer); `600px` hides nav links; a couple of narrower tweaks at `540px`/`480px`/`460px`.
- Standard ease: `--ease: cubic-bezier(.22,.61,.36,1)`.

## Components

- **Illustrations** — hand-built inline SVG line art only (tap handle + pour, glass), stroked in the three ink colors. No stock icon library, no photography.
- **`.club-tag`** — pill-shaped, hairline border, for the About section's club list.
- **`.club-cta a`** — text link with an arrow that grows its gap on hover; the site's only real "button"-equivalent.

## Motion & accessibility

- Global `@media (prefers-reduced-motion: reduce)` kills all animation/transition duration site-wide (one rule, not per-component overrides) — keep new motion inside that umbrella rather than writing a bespoke reduced-motion variant each time.
- Hero entrance is one quiet staggered rise (opacity + 16px translateY), then still — resist adding more.
- `a:focus-visible, button:focus-visible` get a global wood outline — don't override per-component.
- `section[id] { scroll-margin-top: 88px }` clears the sticky nav on anchor jumps — keep this when adding sections.
- Skip link: not present on `main` as of this writing — added in `versions/tap-refined.html`; worth porting back.

## Working with this doc

- `/web-interface-guidelines` reviews UI code against general web-interface best practices (accessibility, forms, focus, etc.) — this doc is CLUBHUS-specific brand/token guidance, use both together.
- The `design-taste-frontend` skill treats this file's contents as the "brand tokens" starting material for any redesign or new section on `main` — extend it rather than inventing a parallel system, and don't pull colors/type from the old `css/styles.css`.
