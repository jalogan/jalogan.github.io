---
layout: default
title: "Symmetrized Bond Order Parameters"
#date:        2 Jan 2014
order: 3
image: 
  path:    /assets/img/SymBOPs_general/SymBOPs_main_full_w_bg.png
  srcset:
  1920w:   /assets/img/SymBOPs_general/SymBOPs_main_full_w_bg.png
  960w:    /assets/img/SymBOPs_general/SymBOPs_main_half.png
  480w:    /assets/img/SymBOPs_general/SymBOPs_main_quarter.png
caption: "Exploring SymBOPs with different particle types."
#description: >
#  SymBOPs projects
#links:
#  - title: Publication
#    url:     https://doi.org/10.1063/5.0076915
featured:    false
redirect_from:
  - "/SymBOPs"
---


{%comment%}
<h1>{{ page.title }}</h1>
{%endcomment%}

<div class="grid">
  {% for project in site.projects %}
    {% if project.category == "SymBOPs" %}
      <div class="grid-item">
        <a href="{{ project.url }}">
          {% if project.image %}
            <img src="{{ project.image.path }}" alt="{{ project.title }}">
          {% endif %}
          <h2>{{ project.title }}</h2>
          <p>{{ project.caption }}</p>
        </a>
      </div>
    {% endif %}
  {% endfor %}
</div>



* this unordered seed list will be replaced by the toc
{:toc}



## **Why This Work Matters**

This work is a significant advancement in the characterization of complex self-assembled structures. By introducing symmetry-specific bond orientational order parameters (SymBOPs), we extend the classical framework of bond orientational order to explicitly account for the symmetry of particles and structures, overcoming key limitations of traditional, rotationally invariant bond order parameters (BOPs). This innovation allows researchers to detect both crystalline and amorphous coherent domains with much greater sensitivity, even at the level of individual bonds. The methodology enables the identification of complex forms of order-—such as compact amorphous clusters that lack long-range periodicity, which were previously inaccessible using conventional tools. As a result, this work has the potential to profoundly impact future studies of self-assembly, nanomaterials design, and condensed matter physics by offering more precise tools for analyzing symmetry, order, and defect structures in emerging complex materials.





## **Rotational symmetry**

<figure id="fig_rotational_symm_example">
  <img src="/assets/img/SymBOPs_general/symmetry_of_circle_vs_rod.png" alt="rotational_symm_ex" width="1000" height="auto">
  <figcaption>Difference of rotational symmetry between a circle and a cirlce with two differently colored points. </figcaption>
</figure>

{%comment%}
<figure id="fig_rotational_symm_example" style="max-width: 100%; text-align: center; margin: auto;">
  <img src="{{ "/assets/img/SymBOPs_general/symmetry_of_circle_vs_rod.png" | relative_url }}" alt="Figure Description"
       style="width: 100%; height: auto; max-width: 600px;">
  <figcaption style="font-size: 0.9em; color: #666; margin-top: 5px;">
    Difference of rotational symmetry between a circle and a cirlce with two differently colored points.
  </figcaption>
</figure>
{%endcomment%}




Rotational symmetry is used to describe an object or set of objects (or points, equations, etc.) that is unaffected by rotations. A 2-sphere in three-dimensions, for instance, has the full symmetry of the rotation group SO(3). We can rotate it in any manner that we'd like and it never looks any different. To make things easier to visualize let's think of a circle (1-sphere) in two-dimensions. Any rotation of the circle leaves it unchanged. If we place two differently colored points on opposite ends of a chord that goes through the center of the circle, everything changes. Now any rotation we choose other than a multiple of $$2\pi$$ gives a different picture from what we started with. The symmetry we had has been broken and only repeats when we rotate by $$2\pi n$$, where $$n$$ is an integer.





## **What is Traditionally Done**

<figure id="fig_BOO_vs_nematic">
  <img src="/assets/img/SymBOPs_general/BOP_and_nematic_rods_full.png" alt="BOO_vs_nematic" width="1000" height="auto">
  <figcaption>Simple example using rods to demonstrate the difference between bond-orientational order, nematic order, and the combination of both. </figcaption>
</figure>


{%comment%}
<figure id="fig_BOO_vs_nematic" style="max-width: 100%; text-align: center; margin: auto;">
  <img src="{{ "/assets/img/SymBOPs_general/BOP_and_nematic_rods_full.png" | relative_url }}" alt="Figure Description"
       style="width: 100%; height: auto; max-width: 800px;">
  <figcaption style="font-size: 0.9em; color: #666; margin-top: 5px;">
    Simple example using rods to demonstrate the difference between bond-orientational order, nematic order, and the combination of both.
  </figcaption>
</figure>
{%endcomment%}

Orientational order looks at the rotational symmetry of an object or group of objects around a common point. There are two types of orientational order that we must distinguish between: *bond-orientational order* describes the orientational order of points in the neighborhood of a an origin, and *polyhedral nematic order* describes how aligned anisotropic objects, e.g., polygons and polyhedra, are with each other. 

Bond-orientational order quantifies how ordered a set of points are based on their angles in a common set of axes. To learn by example, see the left image of <a href="#fig_BOO_vs_nematic" data-fig-ref>??</a>. Focus only on the left green point and the black points neighboring it. Using the usual polar coordinates we can compute the angle $$\theta_i$$ for each black neighboring partile $$i$$. We sum the phases of all $$N_b$$ neighbors of the green point

$$
\psi_{\ell} = \frac{1}{N_b}\sum\limits_{i=1}^{N_{b}} e^{i\ell \theta_i},
$$

where $$\ell$$ is chosen to look at $$\ell$$-fold orientational order. In the figure I have drawn concentric hexagons to aid the eye in looking for $$\ell=6$$-fold order, called hexatic order. We can easily see that each neighbor lies almost exactly on a vertex of the hexagons, showing that these neighbors have near perfect hexatic order. Notice that translationally, they're a mess; together the points do no form a regular hexagon. Our concern is strictly the orientational order about the central point, and not the translational order. Another thing to note is that this show that we can have orientational order while maintaining translational symmetry. Translational symmetry implies that there is no preferred distance between points, such as in a crystal-which breaks translational and orientational order. At this point we have a 2D vector $$\psi_\ell$$ which is a property of the neighborhood of the green point. This vector holds information about how the neighboring points are distributed orientationally around the green point-how well they approximate $$\ell$$-fold symmetry and also the orientation of this polygon in the chosen coordinate system. If we were to look at the neighborhood of a different point that differs from the previous neighborhood only be a rotation, the $$\psi_\ell$$ vectors will be different.

The seminal paper by Steinhardt et al. in 1983 defined a way to quantify bond-orientational order in three-dimensions and proposed the use of rotational invariants to describe local structure of a set of particles in liquids and glasses. In 3D you may use spherical harmonics in place of a complex field. For each bond vector $$b_{ij}$$ from central particle $$i$$ to neighboring particle $$j$$ we may identify a point on the unit sphere with polar and azimuthal angles $$\left( \theta(\vec{r}_{ij}), \phi(\vec{r}_{ij}) \right)$$. From here traditionally one averages over the spherical harmonics for all neighbors and computes the second-order scalar (rotational invariant)

$$
\begin{align}
  \vec{q}_{\ell m} &= \frac{1}{N_b} \sum\limits_{j=1}^{N_b} Y_{\ell m}\left( \theta(\vec{r}_{ij} \right), \phi(\vec{r}_{ij})) \\ 
  q_\ell &= \left[ \frac{4\pi}{2\ell + 1} \sum\limits_{m=-\ell}^{\ell} |\vec{q}_{\ell m}|^2  \right]^{1/2}.
\end{align}
$$


The neighboring points may be collected within a specified distance or by some weighting function that rapidly goes to zero away from the central particle.

These parameters have been used very successfully over decades as structure descriptors, but cannot be considered an order parameter once they throw away the phase information by forming invariants. These descriptors are widely accepted and are often used to identify neighborhoods of clusters of particles as crystal-like or amorphous-like, and even the local structure as FCC-like, etc. 








## **Types of Order**

<figure id="fig_pentagon_lattice">
  <img src="/assets/img/SymBOPs_general/ideal_pentagon_lattice_cropped.png" alt="ideal_pentagon_lattice" width="300" height="auto">
  <figcaption>Ideal lattice of pentagons. </figcaption>
</figure>

{%comment%}
If we are to understand how to interpret the order in different configurations, we first need to know the types of order that are possible and how they work together to create the complex mixes observed in reality. A relatively simple example that puts this interplay of types of order on display, and sets the stage for SymBOPs, is a dense ideal crystal of pentagons, seen in <a href="#fig_pentagon_lattice" data-fig-ref>??</a>.

Three types of order are present in this 2D lattice of anisotropic particles: translational order, orientational order of the bonds between particles, and orientational order of the particles. The first two types are agnostic of the actual particle geometry, and we may consider the particles to be isotropic (circles), if we want. The layers are have alternating colors to make the order more apparent. If we consider only green (or red), the centers of the particles form a 2D orthorhombic crystal--their centers all lie on the vertices of rectangles. The translational order can be described as a density wave in space with periodicity dependent on the lattice direction
{%endcomment%}



If we are to interpret the structure of complex materials, we must first understand the **distinct types of order** that may coexist in a configuration and how they interact. A clean example that illustrates this interplay—and sets the stage for the introduction of SymBOPs—is the **dense 2D lattice of ideal pentagons**, shown in <a href="#fig_pentagon_lattice" data-fig-ref>??</a>.

### **Translational Order**
Translational order refers to the periodic arrangement of particle centers in space. In the pentagon lattice, the centers of mass of the particles lie on the vertices of a 2D orthorhombic lattice. This means their spatial distribution is characterized by regular repetition along two perpendicular directions, which can be described mathematically as a **density wave** with wavevectors $$\vec{k}_x$$ and $$\vec{k}_y$$ corresponding to the lattice spacings along those directions: $$\vec{k} = 2\pi/a$$. This kind of order is present even if the particles were simple circles, making it agnostic to particle anisotropy.

### **Bond-Orientational Order**
Bond-orientational order (BOP) captures the angular structure of how particle centers are arranged relative to each other. It measures the symmetry of the bond directions connecting each particle to its neighbors. In the pentagon crystal, these bonds align strongly along the $$\hat{x}$$ and $$\hat{y}$$ directions, forming a **biaxial symmetry** pattern. This directional information reveals the symmetry axes of the lattice and serves as a natural frame of reference for understanding both the translational and orientational patterns. Even if the particles themselves were replaced with isotropic disks, this underlying bond structure would still persist.

### **Orientational Order of Particles**
The third kind of order arises from the intrinsic orientation of anisotropic particles themselves—in this case, the pentagons. Each pentagon has a defined orientation, and in the dense crystal, this orientation **alternates between layers**. This creates a **pattern of anti-nematic order**: neighboring layers contain particles oriented in nearly opposite directions (rotated by $$\pi$$). While the underlying lattice preserves translational and bond-orientational order, the particle orientations break the **10-fold rotational symmetry** that would otherwise exist if all pentagons had the same orientation. This symmetry breaking is subtle and can only be captured using **higher-rank tensors** or specialized tools like SymBOPs.







## **Introducing SymBOPs**

The example of the ideal pentagon crystal in the previous section shows that orthorhombic crystals and the symmetry group constrained the available space. In general we begin with the full space of symmetric, traceless tensors of rank $$\ell$$ with dimension $$2\ell + 1$$ and the identity is the only "symmetry". As we add symmetries, e.g., rotation by $$180^\circ$$ around the $$X$$-axis, reflection across the $$XY$$-plane, a constraint is added that either zeros elements or equates elements of the symmetric, traceless tensor. One of the main objects utilized by the SymBOPs method is what we call a *reference tensor* $$\widehat{R}^{(\ell)}$$. It is a traceless $$\ell$$-rank tensor that is invariant to all operations of a chosen point symmetry group and normalized to 1 $$\sqrt{\widehat{R}^{(\ell)} \cdot \widehat{R}^{(\ell)}} = 1$$. 





## **How SymBOPs Improves Traditional BOPs**

Traditional bond-orientational order parameters (BOPs) are rotationally invariant descriptors. While powerful, they lose essential information by averaging out the orientation of the local environment — discarding phase information and symmetry specificity. As a result, they struggle to distinguish between different symmetries (e.g., tetrahedral vs. octahedral) and cannot capture subtle orientational correlations or anisotropies present in disordered or multi-component systems.

SymBOPs (Symmetrized Bond-Orientational Order Parameters) overcome these limitations by explicitly projecting local environments onto the irreducible representations of the symmetry group of interest. Instead of asking “How ordered is this neighborhood?”, SymBOPs ask “How much does this neighborhood look like a perfect copy of symmetry X?” — allowing for targeted detection of structure, whether crystalline, amorphous, or hierarchical.

This approach retains symmetry-sensitive phase information, enabling:

  - Distinction between multiple competing local orders

  - Detection of complex or partial symmetry motifs

  - Quantification of structural similarity between neighborhoods and known reference structures

  - Compatibility with both isotropic and anisotropic particles

Moreover, SymBOPs are defined in a group-theoretic framework, allowing them to naturally handle systems with multiple particle types, broken symmetries, or directional interactions — which are increasingly common in modern self-assembly and nanomaterials research.














### Links

<a href="https://doi.org/10.1063/5.0076915" class="info-button" target="_blank">
  <span class="icon-book" style="font-size: 32px;"></span> Symmetry-specific orientational order parameters for complex structures
</a>

<a href="https://doi.org/10.1063/5.0076914" class="info-button" target="_blank">
  <span class="icon-book" style="font-size: 32px;"></span> Controlling morphology in hybrid isotropic/patchy particle assemblies
</a>

<a href="https://doi.org/10.1063/5.0168604" class="info-button" target="_blank">
  <span class="icon-book" style="font-size: 32px;"></span> Symmetry-specific characterization of bond orientation order in DNA-assembled nanoparticle lattices
</a>


<style>
  /* Remove any arrows on external links */
  .info-button::after {
    content: none !important;
  }
</style>


<style>
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
  }
  .grid-item {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
    border: 1px solid #ddd;
    padding: 15px;
    text-align: center;
    transition: transform 0.3s ease;
  }
  .grid-item:hover {
    transform: scale(1.05);
  }
  .grid-item img {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }
  .grid-item h2 {
    margin-top: auto;
  }
</style>







