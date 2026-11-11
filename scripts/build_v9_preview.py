"""Generate a self-contained scientific article preview from MDX for local design review.
The Astro-rendered MDX site remains authoritative; raw TeX is text in standalone mode.
"""
from pathlib import Path
import re,base64,html
import mistune
ROOT=Path(__file__).resolve().parents[1]
raw=(ROOT/'src/content/research/symbops.mdx').read_text()
body=re.sub(r'^---\n.*?\n---\n','',raw,count=1,flags=re.S)
body=re.sub(r'^import .*?;\s*$','',body,flags=re.M)
figs={}
fig_num=0
for m in list(re.finditer(r'<Figure\s+[^>]*?\s*/>',body,flags=re.S)):
 fig_num+=1
 f=m.group(0)
 get=lambda k: re.search(rf'\b{k}="([^"]*)"',f).group(1)
 figs[get('id')]=fig_num

def figure(m):
 text=m.group(0)
 get=lambda k: re.search(rf'\b{k}="([^"]*)"',text).group(1)
 id,src,alt,caption=[get(k) for k in ('id','src','alt','caption')]
 p=ROOT/'public'/src.lstrip('/')
 med={'svg':'image/svg+xml','webp':'image/webp','png':'image/png','jpg':'image/jpeg'}
 typ=med[p.suffix[1:]]
 uri='data:'+typ+';base64,'+base64.b64encode(p.read_bytes()).decode()
 return f'<figure class="scientific-figure" id="{id}"><div class="figure-frame"><img src="{uri}" alt="{html.escape(alt,quote=True)}" loading="lazy"></div><figcaption><strong>Figure {figs[id]}.</strong> {html.escape(caption)}</figcaption></figure>'
body=re.sub(r'<Figure\s+[^>]*?\s*/>',figure,body,flags=re.S)
body=re.sub(r'<FigRef id="([^"]+)"\s*/>',lambda m:f'<a href="#{m.group(1)}">Figure {figs[m.group(1)]}</a>',body)

eqs={};n=0
for m in re.finditer(r'<Equation id="([^"]+)" latex=\{String.raw`(.*?)`\}\s*/>',body,flags=re.S):
 n+=1;eqs[m.group(1)]=n

def eq(m):
 id,expr=m.group(1),m.group(2)
 return f'<div class="numbered-equation" id="{id}" style="grid-template-columns:minmax(0,1fr) 55px"><code style="white-space:pre-wrap;overflow-wrap:anywhere;color:#253f57;font-size:14px;">{html.escape(expr)}</code><span class="eq-number">({eqs[id]})</span></div>'
body=re.sub(r'<Equation id="([^"]+)" latex=\{String.raw`(.*?)`\}\s*/>',eq,body,flags=re.S)
body=re.sub(r'<EqRef id="([^"]+)"\s*/>',lambda m:f'<a href="#{m.group(1)}">Eq. ({eqs[m.group(1)]})</a>',body)
content=mistune.html(body)
old=(ROOT/'PREVIEW-standalone.html').read_text()
# Replace article section
begin='<div class="shell article-grid"><article class="article-prose">';end='</article><aside class="article-toc"'
a=old.index(begin)+len(begin); b=old.index(end,a)
old=old[:a]+content+old[b:]
# Replace article title and deck wherever written
old=old.replace('Symmetrized Bond Orientational Parameters (SymBOPs)','Symmetrized Bond Order Parameters (SymBOPs)')
# Remove placeholder reviewer prose that may be on About; no editorial notes are public.
old=re.sub(r'<div class="placeholder-note">.*?</div>','',old,flags=re.S)
# Update metadata summary when present
old=old.replace('A symmetry-specific way to measure orientational order, resolve coherent structural domains, and identify order that ordinary scalar descriptors can conceal.','A symmetry-aware mathematical framework for revealing coherent order in complex particle assemblies—even when conventional bond-order scalars or visual inspection miss it.')
old=old.replace('Co-developed the symmetry-specific order-parameter formulation and computational analysis, including bond-level projections and domain detection.','Led theory, symmetry projections, computational algorithms, analysis, and visualizations. Collaborators performed the experimental measurements and hybrid-system LAMMPS simulations.')
old=old.replace('An approach for locating crystalline domains and compact, coherent non-space-filling clusters.','SymBOPs distinguish crystalline domains and coherent non-space-filling amorphous clusters; later applications resolve experimental domains, defects, and interpenetrating sublattices.')
# Keep standalone preview on a separate file; do not overwrite source-generated preview within the zip.
p=(ROOT/'PREVIEW-standalone.html');p.write_text(old)
top=ROOT.parent/'jalogan-website-v9-preview.html';top.write_text(old)
print('Preview:',top,'bytes:',top.stat().st_size,'figures:',len(figs),'equations:',len(eqs))
