"""Create the schematic from geometry: regular hexagon guides, disordered radii."""
from pathlib import Path
import math
import svgwrite
from cairosvg import svg2png

root=Path(__file__).resolve().parents[1]
out=root/'public'/'figures'/'order-types-redraw.svg'
W,H=1800,700
bg='#faf9f6'; ink='#162a40'; muted='#5e7281'; light='#dbe4e8'
blue='#457fa8'; coral='#d87f76'; green='#75aa74'
d=svgwrite.Drawing(str(out),size=(W,H),viewBox=f'0 0 {W} {H}')
d.add(d.rect(insert=(0,0),size=(W,H),fill=bg))

def txt(x,y,t,size=20,color=ink,weight='normal',family='Georgia, serif'):
    d.add(d.text(t,insert=(x,y),font_family=family,font_size=size,fill=color,font_weight=weight))

def lin(x1,y1,x2,y2,color=light,w=2,opacity=1):
    d.add(d.line(start=(x1,y1),end=(x2,y2),stroke=color,stroke_width=w,opacity=opacity,stroke_linecap='round'))

def disk(x,y,r,fill,edge='none',sw=1):
    d.add(d.circle(center=(x,y),r=r,fill=fill,stroke=edge,stroke_width=sw))

def pill(x,y,ang=-90,length=55,width=12):
    g=d.g(transform=f'translate({x:.2f},{y:.2f}) rotate({ang})')
    g.add(d.rect(insert=(-length/2,-width/2),size=(length,width),rx=width/2,fill=ink))
    g.add(d.circle(center=(0,0),r=10.0,fill=green,stroke=blue,stroke_width=1))
    d.add(g)

def regular_hexagon(cx,cy,theta,r,color):
    # Each ring is a regular hexagon; never connect the irregularly spaced beads.
    pts=[]
    for k in range(6):
        a=math.radians(theta+60*k)
        pts.append((cx+r*math.cos(a),cy+r*math.sin(a)))
    d.add(d.polygon(points=pts,fill='none',stroke=color,stroke_width=1.7,opacity=.86,stroke_linejoin='round'))

def domain(cx,cy,theta,color,rods=False):
    rings=[63,88,115]
    for r in rings: regular_hexagon(cx,cy,theta,r,color)
    # Different radius for each of the six neighbors, aligned with vertex directions.
    ix=[0,2,1,2,0,1] if theta==0 else [2,1,0,2,1,0]
    coords=[]
    for k,idx in enumerate(ix):
        ang=math.radians(theta+60*k)
        r=rings[idx]
        coords.append((cx+r*math.cos(ang),cy+r*math.sin(ang)))
    # Only the regular hexagons encode sixfold orientational order.
    # Dot-to-dot lines would incorrectly imply a distorted (nonregular) hexagon.
    for x,y in coords:
        if rods: pill(x,y,-68,length=56,width=11)
        else: disk(x,y,11,ink)
    if rods:pill(cx,cy,-68,length=56,width=11)
    else: disk(cx,cy,13,green,blue,1.2)

# Three columns; page-aligned editorial headings (no embedded paper-style title)
for x in [602,1202]:lin(x,85,x,650,light,1.3)
cols=[(52,'01','Bond-orientational order','Unequal neighbor distances; same bond-orientational order.'),
      (650,'02','Nematic order','Aligned particle axes without a lattice.'),
      (1250,'03','Both forms of order','Same bond geometry, now with aligned rods.')]
for x,n,head,desc in cols:
    txt(x,80,n,size=16,color=blue,weight='bold',family='Arial, sans-serif')
    txt(x,130,head,size=27)
    txt(x,166,desc,size=16,color=muted,family='Arial, sans-serif')
    lin(x,190,x+505,190,light,1)

# First panel: local orientation matches a regular hexagonal reference;
# neighbors are deliberately at 3 different radii. No translational lattice.
domain(200,420,0,blue)
domain(412,420,0,coral)

# Nematic director alignment without even approximately lattice-like positions.
coords=[(703,351),(791,299),(897,332),(994,271),(1114,345),
        (713,480),(817,425),(906,496),(1025,427),(1103,509),
        (775,574),(884,564),(990,566),(1083,612)]
for x,y in coords:pill(x,y,-69)

# Exactly the same two sets of particle centers, but with rods instead of spheres.
domain(1397,420,0,blue,rods=True)
domain(1609,420,0,coral,rods=True)

d.save()
svg2png(url=str(out),write_to=str(root/'public'/'figures'/'order-types-redraw-preview.png'),output_width=W,output_height=H)
print(out)
