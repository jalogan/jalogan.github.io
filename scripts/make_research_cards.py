"""Prepare card crops from ORIGINAL user-supplied scientific illustrations.
No scientific data re-rendering; crops/scales only.
"""
from pathlib import Path
from PIL import Image, ImageOps
root=Path(__file__).resolve().parents[1]
out=root/'public'/'figures'/'cards';out.mkdir(exist_ok=True,parents=True)
BG=(245,248,249,255)

def card(p,box,name,scale=.95):
    im=Image.open(p).convert('RGBA').crop(box)
    # Explicit compositing allows transparent original simulation renders to sit on warm offwhite.
    canvas=Image.new('RGBA',(900,940),BG)
    maxw,maxh=int(900*scale),int(940*scale)
    im.thumbnail((maxw,maxh),Image.Resampling.LANCZOS)
    canvas.alpha_composite(im,((900-im.width)//2,(940-im.height)//2))
    canvas.convert('RGB').save(out/name,quality=94,method=6)
    print(name,im.size)

# Crop only the spherical projection from the left of the original two-view figure.
card('/mnt/data/SymBOPs_isotropic_main_full.png',(0,0,806,808),'symbops-sphere.webp',.99)
# Retain the most visually legible dense and branched part of the 4,096-bead simulation.
card('/mnt/data/4096_polymer_full.png',(435,35,1224,660),'protein-4096.webp',.99)
