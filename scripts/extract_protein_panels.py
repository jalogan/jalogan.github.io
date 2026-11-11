"""Extract individual scientific panels from the author's original research PDF."""
from pathlib import Path
import fitz
from PIL import Image, ImageOps, ImageDraw
import io

root=Path(__file__).resolve().parents[1]
pdf=Path('/mnt/data/The effect of stereochemical constraints on the structural properties of folded proteins (2025)(1).pdf')
outdir=root/'public'/'figures'/'protein-panels';outdir.mkdir(parents=True,exist_ok=True)
doc=fitz.open(pdf)
# Rectangles in PDF page points: no paper-level legends/captions should be included.
clips={
 'scaling-a':(1,(52,55,243,245)),
 'scaling-b':(1,(245,54,398,246)),
 'scaling-c':(1,(401,55,560,246)),
 'model-a':(2,(318,56,444,176)),
 'model-b':(2,(441,56,572,176)),
 'model-c':(2,(318,178,444,314)),
 'model-d':(2,(442,178,573,313)),
 'model-e':(2,(315,315,447,417)),
 'model-f':(2,(440,315,572,417)),
 'comparison-a':(5,(48,55,300,205)),
 'comparison-b':(5,(48,207,301,368)),
 'comparison-c':(5,(48,368,300,555)),
 'core-a':(6,(320,245,575,430)),
 'core-b':(6,(320,427,575,601)),
 'residue-a':(7,(48,55,305,173)),
 'residue-b':(7,(48,171,305,274)),
}
images=[]
for name,(page_num,rect) in clips.items():
 pix=doc[page_num].get_pixmap(matrix=fitz.Matrix(4.1,4.1),clip=fitz.Rect(*rect),alpha=False)
 im=Image.open(io.BytesIO(pix.tobytes('png'))).convert('RGB')
 # Lightweight standardization only; do not alter data/colors in actual research plots.
 pad=22
 im=ImageOps.expand(im,border=pad,fill='white')
 im.save(outdir/(name+'.webp'),quality=94,method=6)
 small=im.copy();small.thumbnail((300,220))
 tile=Image.new('RGB',(328,260),'#f1f4f5')
 tile.paste(small,((328-small.width)//2,5))
 ImageDraw.Draw(tile).text((16,232),name,fill='#14243a')
 images.append(tile)
cols=4;rows=(len(images)+cols-1)//cols
contact=Image.new('RGB',(cols*328,rows*260),'#ffffff')
for i,tile in enumerate(images):contact.paste(tile,((i%cols)*328,(i//cols)*260))
contact.save(root/'protein-panels-contact.jpg',quality=92)
print('Extracted',len(clips),'panels;',outdir)
