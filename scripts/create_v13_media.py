from pathlib import Path
from PIL import Image
import fitz, subprocess
ROOT=Path(__file__).resolve().parents[1]
fig=ROOT/'public/figures'; fig.mkdir(exist_ok=True)
vid=ROOT/'public/video'; vid.mkdir(exist_ok=True)
pr=fitz.open('/mnt/data/The effect of stereochemical constraints on the structural properties of folded proteins (2025)(1).pdf')
sp=fitz.open('/mnt/data/Geometric and topological entropies of sphere packing (Logan, Tkachenko, 2022)(2).pdf')
def export(page,rect,name,scale=3):
 pix=page.get_pixmap(matrix=fitz.Matrix(scale,scale),clip=fitz.Rect(*rect),alpha=False)
 im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
 im.save(fig/name,'WEBP',quality=93,method=5)
 print(name,im.size)
# Entire three-part original figure; no paper caption or footer; nonuniform vertical scaling avoided
export(pr[1],(44,60,570,246),'protein-fig1-combined.webp',3.2)
# Sphere-packing figures from the original paper, not illustrations
export(sp[3],(45,54,285,337),'sphere-fig3-original.webp',3.2)
export(sp[4],(314,59,591,313),'sphere-entropy-data.webp',3.2)
export(sp[5],(314,62,593,261),'sphere-sticky-phase.webp',3.2)
export(sp[2],(49,50,294,224),'sphere-geometric-illustration.webp',3.2)
# Images from original supplied vector PDF files
for name,src in [('square-honeycomb-ideal-user.webp','ideal_lattices_sq_honeycomb.pdf'),('square-square-ideal-user.webp','ideal_lattices_sq_square.pdf')]:
 doc=fitz.open('/mnt/data/'+src);page=doc[0];pr=page.rect;clip=fitz.Rect(5,5,pr.width-5,pr.height-5)
 export(page,clip,name,2.3)
# 5TKW provided screenshot: retain alpha and transparency; don't fake a new protein rendering
Image.open('/mnt/data/image.png').save(fig/'protein-atomistic-5tkw.png')
Image.open('/mnt/data/image(1).png').save(fig/'protein-random-walk-rg.png')
for source,target in [('Rg_n_calculation.mp4','rg-subchain-n5.mp4'),('ideal_random_walk.mp4','self-avoiding-walk.mp4')]:
 dest=vid/target
 dest.write_bytes((Path('/mnt/data')/source).read_bytes())
 # video first frame poster
 out=vid/target.replace('.mp4','-poster.png')
 subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(dest),'-frames:v','1',str(out)],check=False)
 print(dest.name,dest.stat().st_size)
