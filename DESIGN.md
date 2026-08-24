# CLUBHUS — Design System

Reference doc for anyone (human or agent) touching `index.html`, `css/styles.css`,
or `js/script.js`. Values are pulled directly from the CSS custom properties in
`css/styles.css:5-26` — update there first, then reflect changes here.

## Brand direction

- **Positioning:** premium yet authentic, heritage-led, members-only.
- **Reference points:** Aimé Leon Dore, Rapha, Malbon, Copenhagen design studios.
- **Voice:** confident, understated, clubhouse-insider — not shouty DTC.

## Color

| Token | Value | Use |
|---|---|---|
| `--green` | `#0B3D2E` | Primary brand green (British Racing Green) |
| `--green-deep` | `#072A20` | Dark sections, announcement bar |
| `--green-soft` | `#14513D` | Hover/secondary green surfaces |
| `--cream` | `#F4F0E6` | Page background (ecru canvas) |
| `--cream-warm` | `#EFE9D8` | Warm cream surfaces |
| `--paper` | `#FBFAF6` | Card/paper surfaces |
| `--ink` | `#1C1B16` | Body text |
| `--brass` | `#B79055` | Heritage gold accent, focus rings, links |
| `--brass-soft` | `#C9A86E` | Brass hover state |
| `--line` | `rgba(28,27,22,.14)` | Hairline borders on light surfaces |
| `--line-light` | `rgba(244,240,230,.18)` | Hairline borders on dark surfaces |

Don't introduce new colors outside this palette without updating the tokens
in `css/styles.css` first — no one-off hex values in markup or inline styles.

## Type

| Token | Stack | Role |
|---|---|---|
| `--serif` | Fraunces, Georgia, Times New Roman | Heritage display serif — headings (`.display`) |
| `--sans` | Inter, system sans fallback | Body copy, UI labels, eyebrows |
| `--logo` | Gabarito, Inter | Wordmark only |
| `--script` | Caveat, Bradley Hand | Handwritten brand voice / slogans (`.script`) — use sparingly |

Conventions:
- `.display` — serif headings, `clamp(2rem, 4.6vw, 3.6rem)`, tight leading (1.04).
- `.eyebrow` — small uppercase sans label, `.28em` letter-spacing, sits above headings.
- `.num` — italic serif section numbers (e.g. "No. 01").
- `.textlink` — underlined brass inline link.

## Layout

- Max content width: `--maxw: 1240px`.
- Side padding: `--pad: clamp(20px, 5vw, 72px)` — fluid, don't hardcode margins.
- Breakpoints: `980px` (tablet), `560px` (mobile) — see `css/styles.css:604`, `:625`.
- Standard ease: `--ease: cubic-bezier(.22,.61,.36,1)` — use for all transitions, don't invent new curves.

## Components

**Buttons** (`.btn`) — uppercase, `.12em` letter-spacing, 2px radius, subtle lift on hover
(`translateY(-2px)`). Variants: `.btn--gold` (brass fill, primary CTA), `.btn--line`
(outlined, for dark sections), `.btn--ghost` (outlined green, for light sections),
`.btn--block` (full width).

## Motion & accessibility

- Every animation (`marquee`, aurora, hero title reveal, scroll reveals) has a
  matching `@media (prefers-reduced-motion: reduce)` override that disables it.
  New motion must follow the same pattern.
- Visible focus via `:focus-visible` with brass outline — never remove without
  a replacement.
- Skip link present (`.skip-link`) — keep it working when editing nav markup.

## Working with this doc

- `/web-interface-guidelines` reviews UI code against general web-interface best
  practices (accessibility, forms, focus, etc.) — this doc is CLUBHUS-specific
  brand/token guidance, use both together.
- The `design-taste-frontend` skill treats this file's contents as the
  "brand tokens" starting material for any redesign or new section — extend it
  rather than inventing a parallel system.
