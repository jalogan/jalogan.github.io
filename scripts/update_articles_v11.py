from pathlib import Path
root=Path(__file__).resolve().parents[1]
protein=root/'src/content/research/protein-modeling.mdx'
s=protein.read_text()
s=s.replace("image: '/figures/protein-card-models.webp'", "image: '/figures/cards/protein-4096.webp'")
s=s.replace("imageAlt: 'Three original research illustrations showing the progression from polymer backbone to sequence-informed and multibead side-chain representations'", "imageAlt: 'Original 4,096-bead coarse-grained polymer simulation, colored by particle properties'")
needle="<Equation id=\"eq-protein-subchain\" latex={String.raw`\\langle R_g(n)\\rangle=\\frac{1}{N-n}\\sum_{i=1}^{N-n}R_g(i,i+n-1)`}/>"
assert needle in s
s=s.replace(needle,needle+'''

Here, the subchain radius of gyration and its subchain center of mass (the paper's Eqs. 3–4) are defined by

<Equation id="eq-protein-segment" latex={String.raw`R_g(i,j)=\\left[\\frac{1}{j-i+1}\\sum_{k=i}^{j}\\left|\\mathbf r_k-\\langle\\mathbf r\\rangle_{i:j}\\right|^2\\right]^{1/2}`}/>

<Equation id="eq-protein-segment-center" latex={String.raw`\\langle\\mathbf r\\rangle_{i:j}=\\frac{1}{j-i+1}\\sum_{k=i}^{j}\\mathbf r_k`}/>

Thus, the first equation averages a well-defined structural observable over contiguous subchains of length $n$. These expressions follow Eqs. (2)–(4) of the original paper.
''')

scaling='''<Figure id="fig-protein-scaling" className="protein-plot-figure" src="/figures/protein-panels/scaling-a.webp" alt="Subchain radius of gyration across 2531 experimentally resolved proteins, showing a crossover in scaling and contrasting the one-third power law" caption="Protein structures show a crossover in subchain-size scaling rather than one universal power law. Original paper Fig. 1(a), extracted without the paper's caption." />

<div className="protein-panel-grid protein-panel-grid-supporting">
  <Figure id="fig-protein-scaling-collapsed" src="/figures/protein-panels/scaling-b.webp" alt="Subchain radii of gyration from collapsed excluded-volume bead-spring polymers of different chain lengths" caption="Collapsed generic polymers have a different internal scaling profile. Paper Fig. 1(b)." />
  <Figure id="fig-protein-scaling-random" src="/figures/protein-panels/scaling-c.webp" alt="Subchain radius of gyration for excluded-volume and ideal random-walk polymers" caption="Random-walk polymer comparison. Paper Fig. 1(c)." />
</div>'''
import re
s,n=re.subn(r'<Figure id="fig-protein-scaling".*?/>',scaling,s,count=1,flags=re.S)
assert n==1
models='''Each subpanel is extracted separately from the paper so the structural differences remain legible at normal reading size.

<div className="protein-panel-grid">
  <Figure id="fig-protein-model-crw" src="/figures/protein-panels/model-a.webp" alt="Collapsed random-walk polymer made of backbone beads" caption="CRW: excluded-volume backbone chain. Original paper Fig. 2(a)." />
  <Figure id="fig-protein-model-bada" src="/figures/protein-panels/model-b.webp" alt="Polymer backbone with bend and dihedral constraints marked" caption="BADA: backbone bend- and dihedral-angle constraints. Paper Fig. 2(b)." />
  <Figure id="fig-protein-model-fjsc" src="/figures/protein-panels/model-c.webp" alt="Polymer with randomly sized side-chain beads" caption="FJSC: randomly sampled side-chain sizes. Paper Fig. 2(c)." />
  <Figure id="fig-protein-model-inseq" src="/figures/protein-panels/model-d.webp" alt="Polymer with sequence-dependent side-chain bead sizes" caption="In Seq: residue-dependent side-chain sizes. Paper Fig. 2(d)." />
  <Figure id="fig-protein-model-mpsc" src="/figures/protein-panels/model-e.webp" alt="Protein model with multiple spherical beads per side chain" caption="MPSC and modMPSC: multibead side-chain geometry. Paper Fig. 2(e)." />
  <Figure id="fig-protein-model-sidechains" src="/figures/protein-panels/model-f.webp" alt="Comparison of amino acid side-chain structures used in MPSC and modified MPSC models" caption="Side-chain representations, including the modified leucine and valine models. Paper Fig. 2(f)." />
</div>'''
s,n=re.subn(r'<Figure id="fig-protein-models".*?/>',models,s,count=1,flags=re.S);assert n==1
comparisons='''<Figure id="fig-protein-comparison-size" className="protein-plot-figure" src="/figures/protein-panels/comparison-a.webp" alt="Comparison of subchain radius of gyration across six coarse-grained protein models and experimental crystal structures" caption="Subchain scaling versus experimental references: including realistic side chains improves the shape and crossover of $\\langle R_g(n)\\rangle$. Original paper Fig. 5(a)." />

<Figure id="fig-protein-comparison-error" className="protein-plot-figure" src="/figures/protein-panels/comparison-b.webp" alt="Normalized mean-squared error of subchain radius of gyration for the six protein models" caption="Normalized error in subchain radius of gyration across the six models. Paper Fig. 5(b)." />

<Figure id="fig-protein-comparison-structure" className="protein-plot-figure" src="/figures/protein-panels/comparison-c.webp" alt="Structure factor plotted against wavevector for six coarse-grained models and experimental reference structures" caption="Structure factors reveal which models capture spatial correlations across length scales. Paper Fig. 5(c)." />'''
s,n=re.subn(r'<Figure id="fig-protein-comparison".*?/>',lambda m: comparisons,s,count=1,flags=re.S);assert n==1
core='''<div className="protein-panel-grid protein-panel-grid-supporting">
  <Figure id="fig-protein-core-packing" src="/figures/protein-panels/core-a.webp" alt="Mean core packing fraction compared against experimental folded protein structures for six coarse-grained model variants" caption="Core packing fraction across models and experiment. Original paper Fig. 6(a)." />
  <Figure id="fig-protein-core-fraction" src="/figures/protein-panels/core-b.webp" alt="Core amino-acid fraction for six coarse-grained models compared to experiment" caption="Core fraction, which simple models fail to reproduce. Paper Fig. 6(b)." />
</div>'''
s,n=re.subn(r'<Figure id="fig-protein-core".*?/>',core,s,count=1,flags=re.S);assert n==1

anchor='''The **modMPSC** model reproduces all four ensemble-level measures—subchain radius of gyration, structure factor, fraction of core residues, and average core packing—to **within 4%** of the reference values reported in the paper.'''
assert anchor in s
s=s.replace(anchor,'''Matching the **overall** mean core packing fraction can hide systematic errors in specific residue types. To test this, we also calculated the average local packing fraction separately for each of the 20 amino-acid types. The trend is informative: refined side-chain representations bring these residue-resolved packing fractions closer to the experimental values, rather than merely matching a single overall average.

<Figure id="fig-protein-residue-packing" className="protein-plot-figure" src="/figures/protein-panels/residue-a.webp" alt="Twenty-amino-acid comparison of packing fraction in In Seq, MPSC, modMPSC and experimental protein structures" caption="Packing fraction resolved by amino-acid type for the different side-chain models and experimental structures. Original paper Fig. 7(a)." />

<Figure id="fig-protein-residue-errors" className="protein-plot-figure" src="/figures/protein-panels/residue-b.webp" alt="Residue-abundance-weighted differences in packing fraction between model variants and X-ray structures" caption="Residue-abundance-weighted packing fraction differences highlight which amino acids improve as the side-chain descriptions become more detailed. Paper Fig. 7(b)." />

'''+anchor)
protein.write_text(s)

sym=root/'src/content/research/symbops.mdx'
s=sym.read_text().replace("image: '/figures/symbops-user-angle-plot.webp'", "image: '/figures/cards/symbops-sphere.webp'").replace("imageAlt: 'SymBOP symmetry-axis response heatmap calculated from spherical-harmonic projections'", "imageAlt: 'Original spherical SymBOP angular response visualized in rainbow colors'")
s=s.replace('alt="Three vector illustrations: periodic particle centers, aligned bond directions, and aligned anisotropic particle axes"', 'alt="Three scientifically precise schematics showing regular hexagonal guides with unequal bond lengths, disordered aligned rods, and their coexistence"')
s=s.replace('caption="Original vector schematic of bond-orientational order, nematic (particle-axis) order, and their coexistence. In the first panel the neighbors lie at deliberately different distances from their centers: aligned bond directions do not imply a translational lattice."', 'caption="Bond-orientational and nematic order are distinct: the blue and coral regular hexagons show perfect sixfold directions in both the first and last panels, but individual particles occupy vertices at different radii. Panel three repeats the first panel with aligned rods in place of circles; none of these configurations requires translational order."')
# Remove damaged, truncated paper labels from the square-patch reference; text about it stays.
s,n=re.subn(r'<Figure id="fig-square-ideal".*?/>\n\n','',s,count=1,flags=re.S)
assert n==1
sym.write_text(s)
print('Edited research pages')
