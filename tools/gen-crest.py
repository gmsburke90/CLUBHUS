import math

GREEN = "#0B3D2E"
GREEN_DK = "#072A20"
GOLD = "#B79055"
GOLD_LT = "#C9A86E"
CREAM = "#F4F0E6"

cx, cy, R = 130, 174, 84

def pt(theta):
    return cx + R*math.cos(math.radians(theta)), cy + R*math.sin(math.radians(theta))

def star(scx, scy, r, fill):
    pts = []
    for k in range(5):
        ao = math.radians(-90 + k*72)
        ai = math.radians(-90 + k*72 + 36)
        pts.append((scx + r*math.cos(ao), scy + r*math.sin(ao)))
        pts.append((scx + r*0.42*math.cos(ai), scy + r*0.42*math.sin(ai)))
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"
    return f'<path d="{d}" fill="{fill}"/>'

def ear():
    parts = ['<path d="M0,0 L0,-40"/>',
             '<path d="M0,-40 L-5,-50"/>', '<path d="M0,-40 L0,-54"/>', '<path d="M0,-40 L5,-50"/>']
    for y in (-10, -17, -24, -31):
        parts.append(f'<path d="M0,{y} l-6,-5"/>')
        parts.append(f'<path d="M0,{y} l6,-5"/>')
    return "".join(parts)

def leaf(theta, ang, L, W, fill=GREEN):
    px, py = pt(theta)
    d = f"M0 0 Q {L*0.42:.1f} {-W:.1f} {L:.1f} 0 Q {L*0.42:.1f} {W:.1f} 0 0 Z"
    return f'<path d="{d}" fill="{fill}" transform="translate({px:.1f},{py:.1f}) rotate({ang:.1f})"/>'

def berry(theta, off, fill=GOLD):
    px, py = pt(theta)
    # nudge inward
    ix, iy = px + off*math.cos(math.radians(theta+180)), py + off*math.sin(math.radians(theta+180))
    return f'<circle cx="{ix:.1f}" cy="{iy:.1f}" r="2.2" fill="{fill}"/>'

leaves = []
# LEFT branch: bottom(100) up to top-left(248)
n = 13
for i in range(n):
    th = 100 + (248-100)*i/(n-1)
    size = 1.0 - 0.32*(i/(n-1))      # leaves shrink toward the top
    L, W = 19*size, 7.2*size
    ang = th + 118                    # lean up the branch, toward the opening
    leaves.append(leaf(th, ang, L, W))
# RIGHT branch mirrors the left (reflect across vertical axis x=cx)
for i in range(n):
    th = 80 - (248-100)*i/(n-1)       # 80 down to -68
    size = 1.0 - 0.32*(i/(n-1))
    L, W = 19*size, 7.2*size
    ang = th - 118
    leaves.append(leaf(th, ang, L, W))

# a few gold berries near the base of each branch
berries = []
for th in (104, 113, 122):
    berries.append(berry(th, 9))
for th in (76, 67, 58):
    berries.append(berry(th, 9))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 322" role="img" aria-label="CLUBHUS heritage crest">
  <!-- laurel wreath -->
  <g>
    {"".join(leaves)}
    {"".join(berries)}
  </g>
  <!-- shield body -->
  <path d="M94,108 L166,108 Q172,108 172,114 L172,178 C172,210 150,228 130,240 C110,228 88,210 88,178 L88,114 Q88,108 94,108 Z" fill="{GREEN}"/>
  <!-- chief (gold band) -->
  <path d="M94,108 L166,108 Q172,108 172,114 L172,134 L88,134 L88,114 Q88,108 94,108 Z" fill="{GOLD}"/>
  <!-- chief stars -->
  <g fill="{GREEN}">
    {"".join(star(x,121,5.2,GREEN) for x in (110,130,150))}
  </g>
  <!-- inner border -->
  <path d="M98,114.5 L162,114.5 Q166,114.5 166,118 L166,177 C166,206 147,222 130,233 C113,222 94,206 94,177 L94,118 Q94,114.5 98,114.5 Z" fill="none" stroke="{CREAM}" stroke-width="1.1" opacity="0.85"/>
  <line x1="94" y1="134" x2="166" y2="134" stroke="{CREAM}" stroke-width="1.1" opacity="0.6"/>

  <!-- clubhouse mark (cream, reversed) in the field -->
  <g transform="translate(110.2,150) scale(0.86)" fill="none" stroke="{CREAM}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
    <path d="M7,23 L24,8 L41,23"/>
    <path d="M11,23 L11,40 L37,40 L37,23"/>
    <path d="M20,40 L20,31 a4,4 0 0 1 8,0 L28,40"/>
    <path d="M24,8 L24,3"/>
    <path d="M24,4 C28,4 31,6 34,6 C31,8 28,9 24,9 Z" fill="{CREAM}" stroke="none"/>
  </g>
  <!-- crossed barley (gold) low in the field -->
  <g fill="none" stroke="{GOLD_LT}" stroke-width="1.3" stroke-linecap="round">
    <g transform="translate(130,224) rotate(-20) scale(0.6)">{ear()}</g>
    <g transform="translate(130,224) rotate(20) scale(0.6)">{ear()}</g>
  </g>

  <!-- crown -->
  <path d="M104,98 L108,80 L114,90 L121,76 L130,68 L139,76 L146,90 L152,80 L156,98 Z" fill="{GOLD}" stroke="{GREEN}" stroke-width="1.1" stroke-linejoin="round"/>
  <rect x="103" y="98" width="54" height="9" rx="2" fill="{GOLD}" stroke="{GREEN}" stroke-width="1.1"/>
  <g fill="{GREEN}">
    <circle cx="116" cy="102.5" r="1.7"/><circle cx="130" cy="102.5" r="1.7"/><circle cx="144" cy="102.5" r="1.7"/>
  </g>
  <g fill="{GOLD_LT}" stroke="{GREEN}" stroke-width="0.8">
    <circle cx="108" cy="80" r="3"/><circle cx="121" cy="76" r="3"/><circle cx="130" cy="68" r="3.4"/><circle cx="139" cy="76" r="3"/><circle cx="152" cy="80" r="3"/>
  </g>
  <!-- finial cross -->
  <g stroke="{GREEN}" stroke-width="1.6" stroke-linecap="round"><line x1="130" y1="68" x2="130" y2="60"/><line x1="126" y1="63.5" x2="134" y2="63.5"/></g>

  <!-- motto banner -->
  <path d="M70,272 C100,264 160,264 190,272 L190,288 C160,296 100,296 70,288 Z" fill="{GREEN}"/>
  <path d="M70,272 L52,266 L59,279 L52,293 L70,288 Z" fill="{GREEN_DK}"/>
  <path d="M190,272 L208,266 L201,279 L208,293 L190,288 Z" fill="{GREEN_DK}"/>
  <text x="130" y="285" font-family="'Fraunces','Playfair Display',Georgia,serif" font-weight="600" font-size="15" letter-spacing="3" fill="{GOLD_LT}" text-anchor="middle">CLUBHUS</text>
  <text x="130" y="312" font-family="'Inter',sans-serif" font-size="7.5" letter-spacing="3.5" fill="{GREEN}" text-anchor="middle" opacity="0.9">EST · MMXXVI · DANMARK</text>
</svg>'''

with open('assets/crest-heritage.svg','w') as f:
    f.write(svg)
print("written")
