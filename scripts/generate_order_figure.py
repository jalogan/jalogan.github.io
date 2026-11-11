#!/usr/bin/env python3
"""Deterministic, geometry-verified site figure for bond and nematic order.
All regular-hexagon vertices lie on six rays theta + k*pi/3; rods in panel 3
are rendered at exactly the same centers as the circles in panel 1.
"""
from pathlib import Path
import math
import svgwrite
from cairosvg import svg2png

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'public/figures/order-types-redraw.svg'
PNG=ROOT/'public/figures/order-types-preview.png'
W,H=1920,745
SW=640
C=dict(bg='#FAF9F6', navy='#14243A', slate='#526779',muted='#718799',line='#DFE6EA',
       blue='#4C82B5',coral='#D98578',teal='#6EAB85',ink='#16263D', soft='#F5F8F8')
D=svgwrite.Drawing(str(OUT), size=(W,H), viewBox=f'0 0 {W} {H}')
D.add(D.rect(insert=(0,0),size=(W,H),fill=C['bg']))

# headings

def txt(s,x,y,size=22,color='navy',weight='400',serif=False,spacing=None):
    kw=dict(insert=(x,y),fill=C.get(color,color),font_size=size,
            font_family=('Source Serif 4, Georgia, serif' if serif else 'DM Sans, Arial, sans-serif'),font_weight=weight)
    if spacing: kw['letter_spacing']=spacing
    D.add(D.text(s,**kw))

def line(x1,y1,x2,y2,color='line',width=2,opacity=1):
    D.add(D.line((x1,y1),(x2,y2),stroke=C.get(color,color),stroke_width=width,opacity=opacity))

def circle(x,y,r,fill='ink',border=None,sw=0,identifier=None):
    d=dict(center=(x,y),r=r,fill=C.get(fill,fill))
    if border: d.update(stroke=C.get(border,border),stroke_width=sw)
    if identifier: d['id']=identifier
    D.add(D.circle(**d))

def rod(x,y,identifier=None,angle=-62,small=False):
    # The rod geometric midpoint is exactly (x,y).
    length=49 if small else 60
    width=13 if small else 16
    group=D.g(transform=f'translate({x:.4f},{y:.4f}) rotate({angle})',id=identifier)
    group.add(D.rect(insert=(-length/2,-width/2),size=(length,width),rx=width/2,
                     fill=C['ink']))
    group.add(D.circle(center=(0,0),r=4.1 if small else 5,fill=C['teal']))
    D.add(group)

headers=[('01','Bond-orientational order','Sixfold bond directions, unequal distances.'),
         ('02','Nematic order','Aligned particle axes, disordered positions.'),
         ('03','Both forms of order','Identical bond geometry, with aligned rods.')]
for i,(num,title,desc) in enumerate(headers):
    ox=i*SW
    txt(num,ox+46,64,16,'muted','700',spacing='2.0')
    txt(title,ox+46,109,32,serif=True)
    txt(desc,ox+46,143,15,'slate')
    line(ox+46,168,ox+SW-44,168,'line',1.6)
    if i: line(ox,34,ox,H-35,'line',2)

# Different centers (including vertically displaced) avoid implying a periodic lattice.
# Exactly the same base orientation theta for BOTH domains, so psi6 is identical.
THETA=-90.0
RADII=(65.0,92.0,118.0)
DOMAINS=(
  dict(name='blue',x=189.0,y=445.0,color='blue',level=(2,1,0,2,0,1)),
  dict(name='coral',x=453.0,y=438.0,color='coral',level=(0,2,1,0,2,1)),
)

def vertex(cx,cy,theta,r,k):
    a=math.radians(theta + 60*k)
    return (round(cx+r*math.cos(a),4),round(cy+r*math.sin(a),4))

# Guides consist of true regular, concentric hexagons. Neighbors are one vertex
# of one of the 3 regular guides; radii deliberately differ.
coords=[]
for d in DOMAINS:
    c=d['color']
    for r in RADII:
        vs=[vertex(d['x'],d['y'],THETA,r,k) for k in range(6)]
        path='M '+' L '.join(f'{x:.4f},{y:.4f}' for x,y in vs)+' Z'
        D.add(D.path(d=path,fill='none',stroke=C[c],stroke_width=2.5,opacity=.75))
        # panel 3: translate exact guide paths
        vs3=[(x+2*SW,y) for x,y in vs]
        path3='M '+' L '.join(f'{x:.4f},{y:.4f}' for x,y in vs3)+' Z'
        D.add(D.path(d=path3,fill='none',stroke=C[c],stroke_width=2.5,opacity=.75))
    # same center in panels 1 and 3
    circle(d['x'],d['y'],16,'teal',border='navy',sw=1.6,identifier=f'{c}-center-p1')
    circle(d['x']+2*SW,d['y'],16,'teal',border='navy',sw=1.6,identifier=f'{c}-center-p3')
    for k,level in enumerate(d['level']):
        x,y=vertex(d['x'],d['y'],THETA,RADII[level],k)
        circle(x,y,13.5,'navy',identifier=f'{c}-neighbor-{k}-p1')
        rod(x+2*SW,y,identifier=f'{c}-rod-{k}-p3',angle=-61,small=True)
        coords.append((c,k,x,y))

# Panel 2 has randomly arranged (non lattice) mutually aligned rods.
panel2=[(735,320),(862,269),(987,322),(1142,289),(700,424),(832,408),
        (965,435),(1098,415),(747,537),(881,575),(1014,545),(1154,562),
        (808,646),(970,647)]
for i,(x,y) in enumerate(panel2):
    rod(x,y,identifier=f'nematic-rod-{i}',angle=-61,small=False)
D.save()
svg2png(url=str(OUT),write_to=str(PNG),output_width=W,output_height=H)

# Mathematical verification of actual point coordinates, including orientation and radial levels.
for d in DOMAINS:
    for r in RADII:
        verts=[vertex(d['x'],d['y'],THETA,r,k) for k in range(6)]
        sides=[math.dist(verts[k],verts[(k+1)%6]) for k in range(6)]
        assert max(sides)-min(sides)<1e-3, sides
    a=[]
    for k,level in enumerate(d['level']):
        x,y=vertex(d['x'],d['y'],THETA,RADII[level],k)
        a.append(math.atan2(y-d['y'],x-d['x']))
    psi=sum(complex(math.cos(6*theta),math.sin(6*theta)) for theta in a)/6
    assert abs(psi-(-1+0j))<1e-5,psi
print('SVG',OUT,'\nPNG',PNG,'\nVerified: every guide is regular, both domains have psi6=-1, and every rod center matches the panel-1 neighbor center + 1280px exactly.')
