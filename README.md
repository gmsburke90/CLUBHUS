# CLUBHUS — The Clubhouse Lager

Landing page for **CLUBHUS**, a premium Danish lager brewed exclusively for
membership-only sports clubhouses — beginning with golf clubs in Denmark.

## Brand direction

- **Positioning:** premium yet authentic, heritage-led, members-only.
- **Creative reference points:** Aimé Leon Dore, Rapha, Malbon, Copenhagen design studios.
- **Palette:** British Racing Green `#0B3D2E` · Cream `#F4F0E6` · Brass `#B79055`.
- **Type:** Fraunces (heritage display serif) + Inter (clean grotesque body).

## The page tells the full story

1. **Hero** — the lager as hero product, with a custom racing-green can.
2. **Heritage** — why a clubhouse deserves a lager of its own.
3. **The Lager (No. 01)** — tasting notes and the CLUBHUS crest.
4. **Membership** — join via a partnered club, 10% off, earn points.
5. **Rewards Locker** — jersey merch + partners (travel, lounges, car hire, fashion, sport).
6. **The Long Game** — cocktails in a can, members' events, the app.
7. **Invitation** — membership request form + clubhouse partnership enquiry.

## Tech

Static site — no build step. Just open `index.html`, or serve the folder:

```bash
python3 -m http.server 8000   # then visit http://localhost:8000
```

```
index.html        markup + content
css/styles.css    design system + layout
js/script.js      sticky nav, scroll reveals, mobile menu, form, can parallax
assets/           crest.svg, can.svg
```

The membership form is front-end only for now and ready to be wired to an
email/CRM endpoint when the backend is chosen.
