import math, cairosvg
GREEN="#0B3D2E"; GOLD="#B79055"; GOLDLT="#C9A86E"; CREAM="#F4F0E6"; PAPER="#FBFAF6"

def c_path(cx, cy, r, gap_deg):
    g=math.radians(gap_deg)
    sx,sy=cx+r*math.cos(g), cy+r*math.sin(g)
    ex,ey=cx+r*math.cos(-g), cy+r*math.sin(-g)
    return f"M{sx:.2f},{sy:.2f} A{r},{r} 0 1 1 {ex:.2f},{ey:.2f}"

def monogram(cx, cy, r, stroke, burgee, sw):
    """C with a mast rising from its top and a burgee flying LEFT (over the solid side)."""
    top = cy - r
    mast_top = top - 8.5
    c = c_path(cx, cy, r, 46)
    parts = [
        f'<path d="{c}" fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round"/>',
        f'<line x1="{cx}" y1="{top:.2f}" x2="{cx}" y2="{mast_top+1.5:.2f}" stroke="{stroke}" stroke-width="{sw*0.62:.2f}" stroke-linecap="round"/>',
        f'<circle cx="{cx}" cy="{mast_top:.2f}" r="{sw*0.42:.2f}" fill="{stroke}"/>',
        # burgee flying left
        f'<path d="M{cx},{mast_top+1.5:.2f} L{cx-13},{mast_top+3.5:.2f} L{cx-9},{mast_top+5.5:.2f} L{cx-13},{mast_top+7.5:.2f} L{cx},{mast_top+8.5:.2f} Z" fill="{burgee}"/>',
    ]
    return "".join(parts)

# ---- 1) Signet seal (beer feature + watermark) — burgee on a standard, flies right ----
seal=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" role="img" aria-label="CLUBHUS members' club seal">
  <defs>
    <path id="top" d="M120,120 m-88,0 a88,88 0 1,1 176,0"/>
    <path id="bot" d="M34,120 A86,86 0 0 0 206,120"/>
  </defs>
  <circle cx="120" cy="120" r="111" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <circle cx="120" cy="120" r="103" fill="none" stroke="{GREEN}" stroke-width="0.8"/>
  <circle cx="120" cy="120" r="62" fill="none" stroke="{GREEN}" stroke-width="1"/>
  <text font-family="'Fraunces',Georgia,'Times New Roman',serif" font-size="21" letter-spacing="6" fill="{GREEN}" text-anchor="middle"><textPath href="#top" startOffset="50%">CLUBHUS</textPath></text>
  <text font-family="'Fraunces',Georgia,serif" font-size="10.5" letter-spacing="5" fill="{GREEN}" text-anchor="middle"><textPath href="#bot" startOffset="50%">MEMBERS’ CLUB · DANMARK</textPath></text>
  <g fill="{GOLD}"><circle cx="30.5" cy="120" r="2"/><circle cx="209.5" cy="120" r="2"/></g>
  <g stroke="{GREEN}" stroke-width="3.2" stroke-linecap="round"><line x1="112" y1="150" x2="112" y2="90"/></g>
  <circle cx="112" cy="89" r="2.6" fill="{GREEN}"/><circle cx="112" cy="150" r="2.6" fill="{GREEN}"/>
  <path d="M112,94 L141,98 L133,102 L141,106 L112,110 Z" fill="{GOLD}"/>
</svg>'''
open("assets/seal.svg","w").write(seal)
cairosvg.svg2png(url="assets/seal.svg", write_to="/tmp/seal_final.png", output_width=300, output_height=300, background_color=PAPER)

# ---- 2) monogram previews (light + dark) ----
mono_light=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">{monogram(24,27,13,GREEN,GOLD,4.2)}</svg>'
cairosvg.svg2png(bytestring=mono_light.encode(), write_to="/tmp/mono.png", output_width=160, output_height=160, background_color=PAPER)
mono_dark=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">{monogram(24,27,13,CREAM,GOLDLT,4.2)}</svg>'
cairosvg.svg2png(bytestring=mono_dark.encode(), write_to="/tmp/mono_dark.png", output_width=160, output_height=160, background_color=GREEN)

# ---- 3) favicon coin (filled) ----
fav=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="11" fill="{GREEN}"/>{monogram(24,27,12,CREAM,GOLDLT,4.4)}</svg>'
open("/tmp/fav.svg","w").write(fav)
cairosvg.svg2png(bytestring=fav.encode(), write_to="/tmp/fav.png", output_width=160, output_height=160)
print("MONO_LIGHT:", monogram(24,27,13,GREEN,GOLD,4.2))
print("---")
print("MONO_DARK:", monogram(24,27,13,CREAM,GOLDLT,4.2))
print("---")
print("FAV_INNER:", monogram(24,27,12,CREAM,GOLDLT,4.4))
print("rendered")
