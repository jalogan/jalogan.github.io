from pathlib import Path
from html import escape
import base64,re
root=Path(__file__).resolve().parents[1]
p=root/'PREVIEW-standalone.html'
s=p.read_text()
# The standalone preview is a compact reading snapshot. The Astro MDX article is the source of truth.
a= 'Symmetry-Adapted Bond Orientational Parameters'
b= 'Symmetrized Bond Orientational Parameters (SymBOPs)'
s=s.replace(a,b)
s=s.replace('A symmetry-aware framework for recognizing coherent orientational order and distinguishing structural domains in complex assemblies.','A symmetry-specific way to measure orientational order, resolve coherent structural domains, and identify order that ordinary scalar descriptors can conceal.')
s=s.replace('Symmetry-specific bond descriptors using reference tensors and group representations.','Co-developed the symmetry-specific order-parameter formulation and computational analysis, including bond-level projections and domain detection.')
s=s.replace('A symmetry-aligned framework for evaluating coherent structural domains.','An approach for locating crystalline domains and compact, coherent non-space-filling clusters.')
s=s.replace('How do we recognize orientational structure hidden by conventional rotationally invariant descriptors?','How do we identify coherent structures that scalar rotational invariants alone can miss?')
img=(root/'public/figures/symbops-user-angle-plot.webp').read_bytes()
imgsrc='data:image/webp;base64,'+base64.b64encode(img).decode()
body='''
<h2 id="context">Research in context</h2>
<p>Particle assemblies may have coherent orientational order even when they lack conventional long-range positional order. SymBOPs use symmetry-adapted bond projections to retain the directional information needed to recognize such structures. The published research connects a mathematical framework in harmonic and tensor spaces to computational analysis of connected domains.</p>
<h2 id="three-types">Three kinds of structural order</h2>
<p><strong>Translational order</strong> concerns periodic positions; <strong>bond-orientational order</strong> concerns neighbor-bond directions; and <strong>particle-orientational order</strong> concerns the alignment of anisotropic building blocks. These properties need not coincide.</p>
<h2 id="group-projector">The symmetry-adapted projection</h2>
<p>Representing bond directions with spherical harmonics gives a space in which point-group operations act as matrices. Averaging over the group projects onto its invariant subspace:</p>
<div class="numbered-equation" id="eq-preview"><span class="eq-math" style="font:italic 23px Georgia,serif;text-align:center;color:#203e5a">𝒫<sup>(ℓ)</sup><sub>G</sub> = (1 / |G|) ∑<sub>g∈G</sub> D<sup>(ℓ)</sup>(g)</span><span class="eq-number">(1)</span></div>
<p>A selected normalized reference vector then defines a rank-one projection within that invariant subspace. This is what allows a chosen symmetry to be tested at the level of individual bonds.</p>
<h2 id="angular">An original angular response figure</h2>
<figure class="scientific-figure" id="fig-preview"><div class="figure-frame"><img src="IMGSRC" alt="Original angular SymBOP response figure" /></div><figcaption><strong>Figure 1.</strong> Angular projection landscape from the original SymBOPs work, supplied for this website rebuild.</figcaption></figure>
<h2 id="applications">Applications to complex assemblies</h2>
<p>The work demonstrates symmetry-sensitive characterization of crystalline domains and compact, non-space-filling coherent clusters. Subsequent applications use the analysis on experimentally reconstructed DNA-assembled nanoparticle lattices.</p>
<h2 id="scope">What the method does—and does not—claim</h2>
<p>SymBOPs complement, rather than replace, rotational invariants. They provide symmetry- and orientation-resolved information, but do not uniquely determine topology or establish a microscopic mechanism of assembly.</p>
<h2 id="papers">Published work</h2>
<p>J. A. Logan, S. Mushnoori, M. Dutt, and A. V. Tkachenko, <em>Journal of Chemical Physics</em> <strong>156</strong>, 054108 (2022). <a href="https://doi.org/10.1063/5.0076915">DOI</a>.</p>
<p><a href="https://jalogan.github.io/projects/SymBOPs/">Original long-form article ↗</a></p>
<p style="font-size:12px;color:#75838a">Preview is abbreviated for convenience. The complete equation-numbered article, references, and original-media import hooks are in the Astro source.</p>
'''.replace('IMGSRC',imgsrc)
pat=r'(<div class="shell article-grid"><article class="article-prose">).*?(</article><aside class="article-toc")'
s,n=re.subn(pat,lambda m:m.group(1)+body+m.group(2),s,count=1,flags=re.S)
if n!=1: raise RuntimeError('Cannot locate article preview')
# Advertise the selective source migration in the publications preview as well.
s=s.replace('A verified publication bibliography will be migrated from my CV and research papers', 'Selected published work is now being migrated from the original papers and research site')
p.write_text(s)
(root.parent/'jalogan-website-v8-preview.html').write_text(s)
print('Wrote preview', p, 'and copied top-level HTML')
# Replace the stale Publications placeholder with the selected verified papers.
s2=(root.parent/'jalogan-website-v8-preview.html').read_text()
publications='''<section class="page-intro"><div class="shell"><div class="section-kicker">Research record</div><h1>Publications</h1><p>Selected published work related to symmetry-specific orientational order and self-assembly. The complete bibliography will follow.</p></div></section>
<section class="page-body shell"><div class="publication-list">
<article class="publication-entry"><time>2022</time><div><h2>Symmetry-specific orientational order parameters for complex structures</h2><p>J. A. Logan, S. Mushnoori, M. Dutt, and A. V. Tkachenko · J. Chem. Phys. 156, 054108 (2022)</p><a href="https://doi.org/10.1063/5.0076915">DOI ↗</a></div></article>
<article class="publication-entry"><time>2022</time><div><h2>Controlling morphology in hybrid isotropic/patchy particle assemblies</h2><p>Related work on programmable self-assembly and symmetry characterization.</p><a href="https://doi.org/10.1063/5.0076914">DOI ↗</a></div></article>
<article class="publication-entry"><time>2023</time><div><h2>Symmetry-specific characterization of bond orientation order in DNA-assembled nanoparticle lattices</h2><p>Related work applying symmetry-specific bond analysis to experimental nanoparticle lattices.</p><a href="https://doi.org/10.1063/5.0168604">DOI ↗</a></div></article>
</div></section>'''
s2,n=re.subn(r'(<div class="view" id="view-publications">).*?(?=<div class="view" id="view-about")',lambda m:m.group(1)+publications+'</div>',s2,count=1,flags=re.S)
if n:
  (root.parent/'jalogan-website-v8-preview.html').write_text(s2)
  p.write_text(s2)
else: print('Could not identify publications-view boundary; keeping the existing preview')
