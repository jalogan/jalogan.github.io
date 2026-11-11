from pathlib import Path
r=Path(__file__).resolve().parents[1]
s=r/'src/content/research/symbops.mdx'
t=s.read_text()
t=t.replace('in square-patch assemblies, it can distinguish zig-zag-like fragments associated with honeycomb stacking from square-lattice domains. ', '')
t=t.replace('coherent zig-zag fragments associated with three-dimensional honeycomb stacking', 'coherent fragments of three-dimensional honeycomb stacking')
t=t.replace('The blue and coral groups have identical sixfold bond orientations even though their neighbors occupy vertices at different radii on regular hexagonal guides.', 'The blue and coral neighborhoods have unequal neighbor distances but the same sixfold bond-orientational order. Their regular hexagonal outlines indicate identical bond directions, not equal bond lengths.')
t=t.replace('The method recognizes these fragments through consistent local bond and particle orientations even when they do not form a complete periodic lattice.', 'The method recognizes these structures through their characteristic local bond and particle orientations, including partially formed or spatially separated domains.')
mark='The comparison is especially useful because coherent local motifs can be detected before—or without—long-range translational order.'
insert='''<FigureGroup id="fig-square-ideal" columns={2} caption="Idealized structural motifs of the two competing square-patch assembly morphologies. These drawings illustrate the geometries; the domain classifications above come from bond-level analysis of the simulated assemblies." panels={[
  { label:'a',src:'/figures/square-honeycomb-ideal-user.webp',alt:'Idealized 3D honeycomb stacking of square patch particles and isotropic neighbors',caption:'Honeycomb stacking motif.'},
  { label:'b',src:'/figures/square-square-ideal-user.webp',alt:'Idealized two-dimensional square lattice arrangement of hybrid square-patch particles',caption:'Square-lattice motif.'}
]} />

'''+mark
t=t.replace(mark,insert)
t=t.replace("import Figure from '../../components/Figure.astro';", "import Figure from '../../components/Figure.astro';\nimport FigureGroup from '../../components/FigureGroup.astro';")
s.write_text(t)
# update image caption within SVG source with exact replacement in generator script
p=r/'scripts/make_order_schematic.py'
v=p.read_text().replace('Sixfold bond directions; unequal distances.', 'Unequal neighbor distances; same bond-orientational order.')
p.write_text(v)
# generate svg + png from geometric source
import subprocess
subprocess.run(['python',str(p)],check=True)

p=r/'src/content/research/protein-modeling.mdx'
s=p.read_text()
s=s.replace("import Figure from '../../components/Figure.astro';", "import Figure from '../../components/Figure.astro';\nimport FigureGroup from '../../components/FigureGroup.astro';\nimport VideoFigure from '../../components/VideoFigure.astro';")
s=s.replace('The study uses **2,531 high-resolution X-ray crystal structures** of single-chain proteins selected from a larger database.', 'The study uses **2,531 high-resolution X-ray crystal structures** of single-chain proteins selected from the **Dunbrack 1.8 / PISCES protein-structure database**.')
s=s.replace('A detailed atomistic protein model represents many interactions and degrees of freedom. Such models are powerful, but can be computationally expensive.', 'A detailed atomistic protein model represents many interacting atoms and degrees of freedom. Such models are powerful, but can be computationally expensive.')
needle='A coarse-grained representation sacrifices detail to enable simulations of larger systems or longer time scales.'
insert='''A coarse-grained representation sacrifices detail to enable simulations of larger systems or longer time scales.

<figure className="inline-science-visual"><img src="/figures/protein-atomistic-5tkw.png" alt="All-atom space-filling visualization of protein 5TKW, showing hundreds of overlapping atomic spheres" loading="lazy" /><figcaption>All-atom visualization of protein 5TKW. Even a single protein contains many atomic degrees of freedom; coarse-graining represents selected structural features using far fewer beads.</figcaption></figure>'''
s=s.replace(needle,insert)
start=s.index('<Figure id="fig-protein-scaling"')
end=s.index('\nThe contrast provides', start)
block='''<Figure id="fig-protein-scaling" className="figure-expanded protein-plot-figure" src="/figures/protein-fig1-combined.webp" alt="Three-panel figure showing experimental protein subchain radius of gyration, collapsed polymer scaling, and random-walk scaling comparisons" caption="The full three-panel comparison from the original paper, Fig. 1(a–c): (a) experimental protein subchain scaling; (b) collapsed generic polymer models; (c) ideal and self-avoiding walk scaling. Matching whole-chain size alone cannot reproduce the observed internal geometry." />

### Visualizing radius of gyration along a chain

The animation below moves a five-residue window along a short chain. For each position, its own center of mass and radius of gyration are calculated using the equations above; averaging over windows yields the subchain-size statistic.

<VideoFigure id="fig-protein-rg-window" src="/video/rg-subchain-n5.mp4" poster="/video/rg-subchain-n5-poster.png" caption="Demonstration of a sliding five-monomer window along a polymer chain while evaluating the subchain radius of gyration. This is an explanatory animation, not a trajectory from the protein-model comparison." />

For additional intuition, a **self-avoiding random walk** grows more rapidly than an ideal random walk as the number of steps increases. In the classical Flory approximation, the size scales as $R_g\sim N^{3/(d+2)}$ in spatial dimension $d$; this is a useful reference rather than the full theory of the folded proteins in our dataset.

<VideoFigure id="fig-protein-saw" src="/video/self-avoiding-walk.mp4" poster="/video/self-avoiding-walk-poster.png" caption="An illustrative self-avoiding random walk as its chain length grows; it helps visualize how polymer conformations differ from compact protein structures." />

<Figure id="fig-protein-rg-sketch" src="/figures/protein-random-walk-rg.png" alt="Schematic of a polymer random walk with grid, a center-of-mass star, and a circle illustrating radius of gyration" caption="An illustrative radius-of-gyration construction for a finished random walk. The radius describes the root-mean-square distance of monomers from the center of mass, not the radius of the smallest enclosing circle." />
'''
s=s[:start]+block+s[end:]
s=s.replace('Each subpanel is extracted separately from the paper so the structural differences remain legible at normal reading size.\n\n','')
start=s.index('<div className="protein-panel-grid">')
end=s.index('\n1. **CRW',start)
models=[('a','model-a.webp','CRW: collapsed random walk.'),('b','model-b.webp','BADA: backbone-angle constraints.'),('c','model-c.webp','FJSC: variable side-chain sizes.'),('d','model-d.webp','In Seq: sequence-dependent side chains.'),('e','model-e.webp','MPSC: multibead side chains.'),('f','model-f.webp','Side-chain bead representations used for MPSC and modMPSC.')]
def group(id,caption,items,columns=2):
 lines=[f'<FigureGroup id="{id}" columns={{{columns}}} caption="{caption}" panels={{[']
 for lab,file,desc in items:
  lines.append(f"  {{ label:'{lab}', src:'/figures/protein-panels/{file}', alt:'{desc}', caption:'{desc}' }},")
 lines.append(']} />')
 return '\n'.join(lines)
s=s[:start]+group('fig-protein-models','Six coarse-grained model representations (a–f) from the original paper Fig. 2. Model complexity grows from a simple backbone chain through side-chain and backbone stereochemistry to multiple beads per residue.',models,2)+s[end:]
start=s.index('<Figure id="fig-protein-comparison-size"')
end=s.index('\nThe minimal CRW',start)
comparison=[('a','comparison-a.webp','Subchain radius of gyration for six models and experiment.'),('b','comparison-b.webp','Normalized subchain-size error.'),('c','comparison-c.webp','Static structure factor across wavevectors.')]
s=s[:start]+group('fig-protein-comparison','Model comparison (a–c), from the original paper Fig. 5. The panels test complementary aspects of chain-scale structure and spatial correlations.',comparison,1)+s[end:]
start=s.index('<div className="protein-panel-grid protein-panel-grid-supporting">',s.index('The FJSC and In Seq models')) if '<div className="protein-panel-grid protein-panel-grid-supporting">' in s[s.index('The FJSC and In Seq models'):] else s.index('<div className="protein-panel-grid protein-panel-grid-supporting">')
end=s.index('\nMatching the',start)
core=[('a','core-a.webp','Average packing fraction of buried residues.'),('b','core-b.webp','Fraction of residues in the protein core.')]
s=s[:start]+group('fig-protein-core','Protein-core measurements (a–b), from the original paper Fig. 6. Together these establish whether a model reproduces not just global size, but the internal packing of the folded state.',core,2)+s[end:]
start=s.index('<Figure id="fig-protein-residue-packing"')
end=s.index('\nThe **modMPSC**',start)
res=[('a','residue-a.webp','Residue-specific packing fraction.'),('b','residue-b.webp','Residue-specific model differences, weighted by abundance.')]
s=s[:start]+group('fig-protein-residue','Amino-acid-resolved core packing (a–b), from the original paper Fig. 7. This catches compensating errors that would be hidden in the average packing fraction.',res,1)+s[end:]
s=s.replace("In particular, the paper's reported approximately $3$ Å core $C_\\alpha$ RMSD comes from an additional near-reference initialization and relaxation study, **not from de novo folding of arbitrary sequences**.", "The paper reports an **average $C_\\alpha$ root-mean-square deviation (RMSD) of approximately $3$ Å for core residues** in a separate study initialized close to the corresponding X-ray structures and then minimized. This describes a positional deviation *from the experimental structure*, not the roughly **$3.8$ Å average separation between successive backbone $C_\\alpha$ atoms** used to define bead spacing. Neither result demonstrates de novo folding of an arbitrary sequence.")
p.write_text(s)
