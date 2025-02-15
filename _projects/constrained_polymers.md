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

# Polymers and Coarse-Grained Proteins


* this unordered seed list will be replaced by the toc
{:toc}

The structural properties of folded proteins are key to understanding their biological function and evolutionary constraints. One of the fundamental descriptors of protein structure is the radius of gyration ($$R_g$$), which quantifies the spatial distribution of atomic mass around the protein’s center of mass. The $$R_g$$ of a protein is influenced by its sequence, secondary structure content, and global packing constraints. A long-standing question in protein physics is how various factors, such as stereochemical constraints and sequence properties, shape the $$R_g$$ of folded proteins.
{:.lead}





### What is a protein

<figure>
  <img src="/assets/img/constrained_polymers/protein_skeleton_cartoon.png" alt="schematic_of_protein" width="1000" height="auto">
  <figcaption>Figure 1: Schematic of a chain of amino acids. Each subunit looks identical with an alpha-Carbon ($$C_{\alpha}$$) atom in the center. What gives each amino acid its flavor is the "R" group in yellow. These are called the side chain of the amino acid and they are different for each of the 20 naturally occurring amino acids. </figcaption>
</figure>

A polymer is a chain of monomer units that can be as simple (a single sphere) or as complex (complex molecule, e.g., amino acid) as necessary. Some of the most important and ubiquitous types of polymers are proteins, seen in Fig. 1. In proteins the monomer units are amino acids and the interactions between the amino acids and their surroundings and other parts of the protein, along with the conditions in which they exist, e.g., in a cell, cause the polymer to collapse in a very specific way. This collapse is called protein folding and when a protein folds incorrectly, it can lead to disease and other problems for the organism that relies on it. X-ray Crystallography is often used to probe the folded structures of proteins, so the folded configuration is sometimes called the protein crystal structure.  

<figure>
  <img src="/assets/img/constrained_polymers/protein_ribbon_diagram_w_labels.png" alt="ribbon_diagram_w_sphere_core" width="300" height="auto">
  <figcaption>Figure 2: Ribbon diagram of a folded protein. Examples of beta sheet and alpha helix secondary structures are labeled. The core of the protin is shown as space-filling spheres to differentiate it from the surface.</figcaption>
</figure>

While breakthroughs in machine learning have improved our ability to predict the X-ray crystal structures of proteins from their amino acid sequences and to design new protein sequences, modeling the physical process of protein folding remains a challenge. Experimental studies of protein folding have revealed intermediate kinetic traps, fold switching, mechanisms of misfolding and aggregation, allostery, and structural changes in response to mutations.

The radius of gyration $$R_g$$

$$
R^2_g(N) = \frac{1}{N} \sum\limits_{k=1}^N | \vec{r}_k - \vec{r}_{\mathrm{com}} |^2,
$$

where $$N$$ is the number of monomers, $$\vec{r}_k$$ is the position of a monomer, and $$\vec{r}_{\mathrm{com}}$$ is the center of mass of the polymer. has been used for decades to describe the shape and compactness of a polymer configuration. In general, it represents the distance from a rotational axis where the mass could be concentrated to have the same moment of inertia. In polymer physics it is not often thought of in this way, but rather as one of several ways to quantify the size of the polymer. Flory discovered that the radius of gyration $$R_g$$ of polymers follows a simple power-law scaling relation $$R_g \propto N^{\nu}$$, where $$\nu \leq 1$$ depends on the polymer and how compact the configuration is. A value of $$\nu = 1.0$$ would mean that the polymer is perfectly straight, like a rod, whereas $$\nu \approx 0.33 - 0.40$$ corresponds to a collapsed simple polymer or a randomly close-packed structure. An ideal polymer, which allows for overlaps, can be thought of as an ideal random walk, one without constraints on the sequence of points, and follows this scaling relationship with $$\nu=1/2$$.j

Just as $$R_g(N)$$ is the radius of gyration for the entire polymer (average over all $$N$$ monomers), we may define $$R_g(n)$$ (mind the small $$n$$) to be the average radius of gyration over all *subpolymers of length $n$*,

$$
\begin{align}
    \begin{split}
        R_g(n) &= \frac{1}{N-n} \sum\limits_{i=1}^{N-n} \left\langle R_{g}(i, i+n-1) \right\rangle \\ 
        R_g(i,j) &= \left[ \frac{1}{j-i+1} \sum\limits_{k=i}^{j} \left( \vec{\mathbf{r}}_k - \langle \vec{\mathbf{r}}_k \rangle \right)^2 \right]^{1/2} \\ 
       \langle \vec{\mathbf{r}}_k \rangle &= \frac{1}{j-i+1} \sum\limits_{k=i}^{j} \vec{\mathbf{r}}_k.
    \end{split}
\end{align}
$$


<figure>
  <video width="450" height="auto" poster="{{ "/assets/img/constrained_polymers/Rg_n_calculation_cover.png" | relative_url }}" autoplay loop muted playsinline>
  <source src="{{ "/assets/videos/constrained_polymers/Rg_n_calculation.mp4" | relative_url }}?v={{ site.time | date: '%s' }}" type="video/mp4">
  Your browser does not support the video tag.
  </video>
  <figcaption data-katex>
    Demonstration of all of the \($$n=5$$\) subpolymers in this small polymer. To compute \(R_g(n=5)\), we first compute the \(R_g\) of each of these subpolymers with five monomers (highlighted in red) and then average over all of their values.
  </figcaption>
</figure>


This equation essentially treats the polymer in pieces and computes the $$R_g$$ of each of those pieces. For example, if $$n=5$$, we only look at all subpolymers with five monomers, as shown in the video below, and average over all of their $$R_g$$ values. We do this for all $$2 \leq n \leq N$$ and get a single number for each $$n$$ that allows us to plot $$R_g(n)$$ vs $$n$$. As a comparison between $$R_g(N)$$ and $$R_g(n)$$, below we see a plot for collapsed polymers. The polymers do no allow overlaps, but otherwise have no constraints on their connected movement. The inset shows $$R_g(N)$$ vs $$N$$ while the main plot shows $$R_g(n)$$ vs $$n$$. The first thing to notice is that, because the last point of the $$R_g(n)$$ plot is at $$n=N$$, if we trace a line connecting all of the endpionts of the curves we find a line similar to the inset, which has a slope of $$\nu = 1/3$$. This is all $$R_g(N)$$ really tells us, and so when we focus on subpolymers we get more information. 


<figure>
  <img src="/assets/img/constrained_polymers/Fig1b_Rg_vs_n_curves_with_insets.png" alt="Rg_for_collapse_polymers" width="450" height="auto">
  <figcaption>Figure 1: Schematic of a chain of amino acids. Each subunit looks identical with an alpha-Carbon ($$C_{\alpha}$$) atom in the center. What gives each amino acid its flavor is the "R" group in yellow. These are called the side chain of the amino acid and they are different for each of the 20 naturally occurring amino acids. </figcaption>
</figure>







Protein folding occurs in a high-dimensional, complicated energy landscape, but, incredibly, some of the most important features necessary for simulating protein structure and dynamics can be captured with relatively *simple coarse-grained models*.
{:.lead}


{%comment%}
You can add a note.
{:.note title="Deeper Look"}

~~~python
import numpy as np

## Define vector x
x = [1,2,3]

## Compute the norm of x
xnorm = np.linalg.norm(x)

## Print the norm
print("xnorm: ", xnorm)
~~~
{%endcomment%}


## How complex must a polymer model be to begin to capture critical features of folded proteins 




### What are the critical features of folded proteins?

#### Key constraints of folded proteins
Discuss the key constraints, such as, bond angles, bond dihedrals, side chains, etc. 
#### Key observables to check how protein-like the model is
Discuss the key observables we want to match, such as, core packing fraction, fraction core, scattering, etc. 

### Models



### Key results


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