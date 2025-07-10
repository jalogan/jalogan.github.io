---
layout:      project
title:       "Constrained Polymers"
#date:        2 Jan 2014
order: 2
image:
  path:      /assets/img/constrained_polymers/4096_polymer_full.png
  srcset:
    1920w:   /assets/img/constrained_polymers/4096_polymer_full.png
    960w:    /assets/img/constrained_polymers/4096_polymer_half.png
    480w:    /assets/img/constrained_polymers/4096_polymer_quarter.png
caption:     Modeling proteins as constrained polymers
#description: >
#  Hyde is a brazen two-column [Jekyll](http://jekyllrb.com) theme.
#  It's based on [Poole](http://getpoole.com), the Jekyll butler.
#links:
#  - title:   Publication
#    url:     https://doi.org/10.48550/arXiv.2501.02424
#  #- title:   GitHub Repository
#  - icon:    "fab fa-github"
#    url:     https://github.com/jalogan/Constrained-Polymer-Collapse.git
featured:    false
#related_posts: 
---


* this unordered seed list will be replaced by the toc
{:toc}


<!--
# Polymers and Coarse-Grained Proteins
-->


The structural properties of folded proteins are key to understanding their biological function and evolutionary constraints. One of the fundamental descriptors of protein structure is the radius of gyration ($$R_g$$), which quantifies the spatial distribution of atomic mass around the protein’s center of mass. The $$R_g$$ of a protein is influenced by its sequence, secondary structure content, and global packing constraints. A long-standing question in protein physics is how various factors, such as stereochemical constraints and sequence properties, shape the $$R_g$$ of folded proteins.
{:.lead}


## **Why This Work Matters**  
There now exist modern methods using machine learning and AI to obtain the best prediction for the structure of a folded protein. These methods are incredible feats, but they only provide a final folded structure and do not fill in the whole picture of protein folding. Simulations of all-atom models are computationally expensive and require cutting-edge technology to accurately simulate the length of time required for an average sized protein to fold. In addition, proteins typically exist in crowded enviroments inside of cells. To further our understanding of the pathways of protein folding we need to shrink the space of configurations and focus on the most important features. This work focuses on coarse-grained models and searches for the simplest possible model that can recapitulate the average behavior of real folded proteins. In addition to common metrics, such as packing fraction, the fraction of the protein in the core, the end-to-end radius of gyration scaling, and the structure factor, we are the first to study the internal (subpolymer) scaling of the radius of gyration and compare simulated models with real protein X-ray crystal structures. 

This work advances our understanding of what physical ingredients are essential for protein folding, helps distinguish realistic protein structures from computational decoys, and provides a foundation for improving coarse-grained models used in protein design and folding studies​. This will enable future studies to build more efficient, physically realistic coarse-grained models that can simulate folding pathways, misfolding, design, and structural transitions at large scales that are inaccessible to atomistic simulations. It also opens the door to better distinguishing physical principles underlying folding from purely data-driven or machine learning-based structure predictions, helping to unify physics-based modeling with modern predictive tools.



## **What is a protein**

<figure id="fig_protein_schematic">
  <img src="/assets/img/constrained_polymers/protein_skeleton_cartoon.png" alt="schematic_of_protein" width="1000" height="auto">
  <figcaption>Schematic of a chain of amino acids. Each subunit looks identical with an alpha-Carbon (\(C_{\alpha}\)) atom in the center. What gives each amino acid its flavor is the "R" group in yellow. These are called the side chain of the amino acid and they are different for each of the 20 naturally occurring amino acids. </figcaption>
</figure>





A polymer is a chain of monomer units that can be as simple (a single sphere) or as complex (complex molecule, e.g., amino acid) as necessary. Some of the most important and ubiquitous types of polymers are proteins, seen in <a href="#fig_protein_schematic" data-fig-ref>??</a>. In proteins the monomer units are amino acids and the interactions between the amino acids and their surroundings and other parts of the protein, along with the conditions in which they exist, e.g., in a cell, cause the polymer to collapse in a very specific way. This collapse is called protein folding and when a protein folds incorrectly, it can lead to disease and other problems for the organism that relies on it. X-ray Crystallography is often used to probe the folded structures of proteins, so the folded configuration is sometimes called the protein crystal structure.  

<figure id="fig_ribbon_diagram">
  <img src="/assets/img/constrained_polymers/protein_ribbon_diagram_w_labels.png" alt="ribbon_diagram_w_sphere_core" width="300" height="auto">
  <figcaption>Ribbon diagram of a folded protein. Examples of beta sheet and alpha helix secondary structures are labeled. The core of the protin is shown as space-filling spheres to differentiate it from the surface.</figcaption>
</figure>

While breakthroughs in machine learning have improved our ability to predict the X-ray crystal structures of proteins from their amino acid sequences and to design new protein sequences, modeling the physical process of protein folding remains a challenge. Experimental studies of protein folding have revealed intermediate kinetic traps, fold switching, mechanisms of misfolding and aggregation, allostery, and structural changes in response to mutations.

The radius of gyration $$R_g$$

$$
R^2_g(N) = \frac{1}{N} \sum\limits_{k=1}^N | \vec{r}_k - \vec{r}_{\mathrm{com}} |^2,
$$

where $$N$$ is the number of monomers, $$\vec{r}_k$$ is the position of a monomer, and $$\vec{r}_{\mathrm{com}}$$ is the center of mass of the polymer. has been used for decades to describe the shape and compactness of a polymer configuration. In general, it represents the distance from a rotational axis where the mass could be concentrated to have the same moment of inertia. In polymer physics it is not often thought of in this way, but rather as one of several ways to quantify the size of the polymer. Flory discovered that the radius of gyration $$R_g$$ of polymers follows a simple power-law scaling relation $$R_g \propto N^{\nu}$$, where $$\nu \leq 1$$ depends on the polymer and how compact the configuration is. A value of $$\nu = 1.0$$ would mean that the polymer is perfectly straight, like a rod, whereas $$\nu \approx 0.33 - 0.40$$ corresponds to a collapsed simple polymer or a randomly close-packed structure. An ideal polymer, which allows for overlaps, can be thought of as an ideal random walk, one without constraints on the sequence of points, and follows this scaling relationship with $$\nu=1/2$$.

Just as $$R_g(N)$$ is the radius of gyration for the entire polymer (average over all $$N$$ monomers), we may define $$R_g(n)$$ (mind the small $$n$$) to be the average radius of gyration over all *subpolymers of length $$n$$*,

$$
\begin{align}
    \begin{split}
        R_g(n) &= \frac{1}{N-n} \sum\limits_{i=1}^{N-n} \left\langle R_{g}(i, i+n-1) \right\rangle \\ 
        R_g(i,j) &= \left[ \frac{1}{j-i+1} \sum\limits_{k=i}^{j} \left( \vec{\mathbf{r}}_k - \langle \vec{\mathbf{r}}_k \rangle \right)^2 \right]^{1/2} \\ 
       \langle \vec{\mathbf{r}}_k \rangle &= \frac{1}{j-i+1} \sum\limits_{k=i}^{j} \vec{\mathbf{r}}_k.
    \end{split}
\end{align}
$$


<figure id="vid_Rg(n=5)_example">
  <video width="450" poster="{{ "/assets/img/constrained_polymers/Rg_n_calculation_cover.png" | relative_url }}" autoplay loop muted playsinline>
  <source src="{{ "/assets/videos/constrained_polymers/Rg_n_calculation.mp4" | relative_url }}?v={{ site.time | date: '%s' }}" type="video/mp4">
  Your browser does not support the video tag.
  </video>
  <figcaption data-katex>
    Demonstration of all of the \(n=5\) subpolymers in this small polymer. To compute \(R_g(n=5)\), we first compute the \(R_g\) of each of these subpolymers with five monomers (highlighted in red) and then average over all of their values.
  </figcaption>
</figure>


This equation essentially treats the polymer in pieces and computes the $$R_g$$ of each of those pieces. For example, if $$n=5$$, we only look at all subpolymers of five consecutive monomers, as shown in the <a href="#vid_Rg(n=5)_example" data-fig-ref>??</a>, and average over all of their $$R_g$$ values. We do this for all $$2 \leq n \leq N$$ and get a single number for each $$n$$ that allows us to plot $$R_g(n)$$ vs $$n$$. Because $$Rg(n=N) = R_g(N)$$ we not only retain all of the information that the typical average polymer end-to-end size (which is proportional to $$R_g(N)$$) contains, but gain "internal" scaling information for all subpolymer sizes.  As a comparison between $$R_g(N)$$ and $$R_g(n)$$, below we see a plot for collapsed polymers. The polymers do not allow overlaps, but otherwise have no constraints on their connected movement. The inset shows $$R_g(N)$$ vs $$N$$ while the main plot shows $$R_g(n)$$ vs $$n$$. The first thing to notice is that, because the last point of the $$R_g(n)$$ plot is at $$n=N$$, if we trace a line connecting all of the endpionts of the curves we find a line similar to the inset, which has a slope of $$\nu = 1/3$$. This is all $$R_g(N)$$ really tells us, and so when we focus on subpolymers we get more information.


<figure id="fig_Rg_n_collapsed_polymers">
  <img src="/assets/img/constrained_polymers/Fig1b_Rg_vs_n_curves_with_insets.png" alt="Rg_for_collapse_polymers" width="450" height="auto">
  <figcaption> \(R_g(n)\) for collapsed polymers  </figcaption>
</figure>


When it comes to a highly constrained polymer, such as a protein, $$R_g(n)$$ can provide information about specialized ranges of subpolymers like the secondary structure. <a href="#fig_ribbon_diagram" data-fig-ref>??</a> shows an example of the alpha helix and beta strand secondary structures found in proteins. These structures can be variable length, but have typical length scales in the range of 10-15 amino acids for alpha helices and 5-10 amino acids for beta strands. This means that in real proteins we can expect on average that $$R_g(n\approx10)$$ will be growing in size faster than at $$n\approx40$$, for instance. Another way to say this is that, on average, the direction of growth will be correlated over some length called the persistence length. This length gives an idea of how long something can grow before bending. In <a href="#fig_Rg_n_folded_proteins" data-fig-ref>??</a> the $$R_g(n)$$ is plotted for the X-ray crystal structures of 2531 single-chain proteins in black, and we observe some interesting features. The inset shows $$R_g(N)$$, which follows the expected end point scaling for collapsed polymers of $$\nu \approx 1/3$$. The main plot, however, shows that $$R_g(n)$$ does not follow the expected Flory scaling. We see two distinct slopes in the red average curve separated by a clear kink. Proteins are just polymers, so we can firmly state that if we begin with an ideal polymer and add constraints one-by-one, the features that we observe must begin to appear. This leaves one big open question: 

<p align="center"><em><strong>how complex must a polymer model be to capture the features observed in the scaling of proteins?</strong></em></p>


<figure id="fig_Rg_n_folded_proteins">
  <img src="/assets/img/constrained_polymers/Fig1a_Rg_vs_n_curves_with_insets.png" alt="Rg_for_folded_proteins" width="450" height="auto">
  <figcaption>\(R_g(n)\) for over 2500 folded single-chain proteins. </figcaption>
</figure>





## **How complex must a polymer model be to begin to capture critical features of folded proteins**
This is the big question that we aim to answer in this work. We design and employ a C++ molecular dynamics code that will build a polymer model with constraints and collapse it under a central force.

### **What are the critical features of folded proteins?**
We begin with the simplest physical polymer, a freely-jointed chain whose only constraint is for the atoms not to overlap. But where do we go from there? The space of polymer models is vast and if we think of approaching the point in this space that represents a real protein (assuming we even know where that is), there are innumerable directions of approach. To begin to clarify a possible path, we enumerate the key features of proteins. For example, the average distance from residue-to-residue is approximately 3.8$$\r{A}$$, which suggests the possibility to simplify all of the backbone atoms into a single spherical bead of diameter $$\sigma_{\mathrm{bb}} = 3.8\r{A}$$. Proteins have constrained bond angles and dihedral angles along the backbone, but if the backbone of each residue is a single sphere, we can instead define coarse-grained bond and dihedral angles that are defined from $$C_{\alpha}$$-to-$$C_{\alpha}$$ atom in a protein. Another key feature of proteins in the variable side chain that defines the amino acid type. The simplest way to include this is with another single sphere bonded to the backbone sphere. As we add more detail to the models, we can include more atoms in the backbone or side chains. A final key ingredient, which is what defines one protein compared to another, is the amino acid sequence. Somehow the sequence of the protein should be taken into account.

### **Models**
Given some of the key features that define the structure of folded proteins, we can begin with a simple polymer model and add constraints until we find a model that captures that qualitative scaling observed in Fig. 4.

<figure id="fig_CG_models">
  <img src="/assets/img/constrained_polymers/Fig2_models.png" alt="Rg_for_folded_proteins" width="550" height="auto">
  <figcaption>The coarse-grained models used in this work. For each over 2500 simulations will be done-one for each single-chain protein in the dataset.  </figcaption>
</figure>


<a href="#fig_CG_models" data-fig-ref>??</a> introduces the six polymer models that are studied in this work. We begin with a freely-jointed chain in <a href="#fig_CG_models" data-fig-ref>??</a> (a), where the only constraint is non-overlapping atoms-this is essentially a self-avoiding random walk. As the starting point in model space, we don't expect this model to recapitulate the properties of a folded protein. Next, <a href="#fig_CG_models" data-fig-ref>??</a> (b) introduces bond angle and dihedral angle constraints between three and four consecutive residues, respectively. We find that including these constraints is an enormous step, and we even begin to see a kink in the scaling for this model. The next natural step is to include a simplified side chain as a single atom. Each amino acid type will have a full distriution of side chain size because of the different conformations possible for each amino acid. We account for this by creating distributions of the approximate sizes of the side chains for each amino acid over the whole protein dataset. We also make a single global distribution which accounts for all sizes of every amino acid type. The model seen in <a href="#fig_CG_models" data-fig-ref>??</a> (c) uses this global distribution to randomly select a side chain diameter for each monodisperse backbone atom. The effect of this is to create a protein with a random sequence. The model seen in <a href="#fig_CG_models" data-fig-ref>??</a> (d), on the other hand, makes a random selection from the individual distribution of the amino acid, allowing us to essentially create a model that has the correct sequence. By creating both of these models we are able to compare random sequences to known protein sequences. The final two models are represented by <a href="#fig_CG_models" data-fig-ref>??</a> (e)-(f) are are multi-particle side chain models. <a href="#fig_CG_models" data-fig-ref>??</a> (e) has all the constraints of the previous models, including the correct protein sequence, but includes more geometric detail in the side chains of selected amino acids. The geometry of the side chains is taken from the well-known Martini model. Intra-side chain constraints are included to maintain the correct geometry throughout the simulations, but no additional force fields are included. <a href="#fig_CG_models" data-fig-ref>??</a> (f) shows that the final model is very similar to the previous. It is a modified version of the multi-particle side chain model just described, but with the side chains of amino acids Leucine and Valine updated.

One of our hypotheses is that When a polymer model begins to capture the correct $$R_g(n)$$ scaling of a protein, other structural properties begin to converge as well. To demonstrate this, in addition to $$R_g(n)$$, we also measure the fraction of the protein found in the core $$f_{core}$$, the average packing fraction of the protein cores $$\langle \phi \rangle$$, and the structure factor of the $$C_{\alpha}$$ atoms of the folded polymer $$S(q)$$.




### Links

<a href="https://doi.org/10.48550/arXiv.2501.02424" class="info-button" target="_blank">
  <span class="icon-book" style="font-size: 32px;"></span> The effect of stereochemical constraints on the radius of gyration of folded proteins
</a>

<a href="https://github.com/jalogan/Constrained-Polymer-Collapse.git" class="info-button" target="_blank">
  <span class="icon-github" style="font-size: 32px;"></span>
</a>


<style>
  /* Remove any arrows on external links */
  .info-button::after {
    content: none !important;
  }
</style>