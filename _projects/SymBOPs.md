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

Bond-orientational order quantifies how ordered a set of points are based on their angles on a common set of axes. To learn by example, see the left image of <a href="#fig_BOO_vs_nematic" data-fig-ref>??</a>. Focus only on the left green point and the six black points neighboring it. Using the usual polar coordinates we can compute the angle $$\theta_i$$ for each black neighboring partile $$i$$. We sum the phases of all $$N_b$$ neighbors of the green point

$$
\psi_{\ell} = \frac{1}{N_b}\sum\limits_{i=1}^{N_{b}} e^{i\ell \theta_i},
$$

where $$\ell$$ is chosen to look at $$\ell$$-fold orientational order. In the figure I have drawn concentric hexagons to aid the eye in looking for $$\ell=6$$-fold order, called hexatic order. We can easily see that each neighbor lies almost exactly on a vertex of the hexagons, showing that these neighbors have near perfect hexatic order. Notice that translationally, they're a mess; together the points do not form a regular hexagon. Our concern is strictly the orientational order about the central point, and not the translational order. Another thing to note is that this shows that we can have orientational order while maintaining translational symmetry. Translational symmetry implies that there is no preferred distance between points, such as in a crystal-which breaks translational and orientational order. At this point we have a 2D vector $$\psi_\ell$$ which is a property of the neighborhood of the green point. This vector holds information about how the neighboring points are distributed *orientationally* around the green point-how well they approximate $$\ell$$-fold symmetry and also the orientation of this polygon in the chosen coordinate system. If we were to look at the neighborhood of a different point that differs from the previous neighborhood only by a rotation, the $$\psi_\ell$$ vectors will most likely be different.

The seminal paper by Steinhardt et al. in 1983 defined a way to quantify bond-orientational order in three-dimensions and proposed the use of rotational invariants to describe local structure of a set of particles in liquids and glasses. In 3D you may use spherical harmonics in place of a complex field. For each bond vector $$b_{ij}$$ from central particle $$i$$ to neighboring particle $$j$$ we may identify a point on the unit sphere with polar and azimuthal angles $$\left( \theta(\vec{r}_{ij}), \phi(\vec{r}_{ij}) \right)$$. From here traditionally one averages over the spherical harmonics for all neighbors and computes the second-order scalar (rotational invariant)

$$
\begin{align}
  \vec{q}_{\ell m} &= \frac{1}{N_b} \sum\limits_{j=1}^{N_b} Y_{\ell m}\left( \theta(\vec{r}_{ij} \right), \phi(\vec{r}_{ij})) \\ 
  q_\ell &= \left[ \frac{4\pi}{2\ell + 1} \sum\limits_{m=-\ell}^{\ell} |\vec{q}_{\ell m}|^2  \right]^{1/2}.
\end{align}
$$


The neighboring points may be collected within a specified distance or by some weighting function that rapidly goes to zero away from the central particle.

These parameters have been used very successfully over decades as structure descriptors, but cannot be considered an order parameter once they throw away the phase information by forming invariants. These descriptors are widely accepted and are often used to identify neighborhoods of clusters of particles as crystal-like or amorphous-like, and even the local structure as FCC-like, etc. 








## **Coexistence of Different Types of Order**

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
Translational order refers to the periodic arrangement of particle centers in space. In the pentagon lattice, the centers of mass of the particles of one color lie on the vertices of a 2D orthorhombic lattice--easily spotted by noticing the centers form small rectangles with neighbors of the same color. This means their spatial distribution is characterized by regular repetition along two perpendicular directions, which can be described mathematically as a **density wave** with wavevectors $$\vec{k}_x$$ and $$\vec{k}_y$$ corresponding to the lattice spacings $$a$$ along those directions: $$\vert \vec{k} \vert = 2\pi/a$$. This kind of order is present even if the particles are simple circles, making it agnostic to particle anisotropy.

### **Bond-Orientational Order**
Bond-orientational order (BOP) captures the angular structure of how particle centers are arranged relative to each other. It measures the symmetry of the bond directions connecting each particle to its neighbors. In the pentagon crystal, these bonds align strongly along the $$\hat{x}$$ and $$\hat{y}$$ directions, forming a **biaxial symmetry** pattern. This directional information reveals the symmetry axes of the lattice and serves as a natural frame of reference for understanding both the translational and orientational patterns. Even if the particles themselves were replaced with isotropic disks, this underlying bond structure would still persist, making it, again, agnostic to the particle anisotropy.

### **Orientational Order of Particles**
The third kind of order arises from the intrinsic orientation of anisotropic particles themselves—in this case, the pentagons. Each pentagon has a defined orientation, and in the dense crystal, this orientation **alternates between layers**. This creates a **pattern of anti-nematic order**: neighboring layers contain particles oriented in nearly opposite directions (rotated by $$\pi$$). While the underlying lattice preserves translational and bond-orientational order, the particle orientations break the **10-fold rotational symmetry** that would otherwise exist if all pentagons had the same orientation. This symmetry breaking is subtle and can only be captured using **high-rank tensors** or specialized tools like SymBOPs.



## **Introducing SymBOPs**

Let's begin by providing an intuitive understanding of what a SymBOP is, and what it can do. Given a seemingly messy configuration of particles (the particles can have any shape, but, surprisingly, spheres are a special case), we would like to be able to identify any regions with strong orientational order. Recall that it's possible to have orientational order without translational order, so these regions could be ideal crystalline lattices, or domains that may not look as ordered to the human eye, like <a href="#fig_BOO_vs_nematic" data-fig-ref>??</a>. The way SymBOPs finds these domains is by creating a *reference template* of the order we want to search for and then checking how well each bond matches this template. As an overly simplified example, you can imagine taking a cookie cutter of the order you want to find and running it over the sample; where the shape fits, the score is high. In one pass SymBOPs checks both (i) how neighbors are oriented relative to each other (bond-orientational order) and (ii) how the particles themselves are oriented (particle orientation). Bonds with high scores are then grouped into connected clusters, giving you domains that share the same order. A good default—when you don’t know what to expect—is to use the symmetry of the building block (e.g., a square, pentagon, etc.) as the template. While not always the case, often the order of the domains mimics the geometry of the building blocks that make up the domains.

Below, 2D square particles assemble in a 3D periodic box. The left panel shows the final configuration; the right shows domains SymBOPs pulled out. Each color is a separate domain with its own orientation. The domains in this case mirror the symmetry of the particles and form 2D sheets.

<figure id="vid_2D_squares_domains_example">
  <video width="450" poster="{{ "/assets/img/SymBOPs_general/2D_squares_domains_cover.png" | relative_url }}" autoplay loop muted playsinline>
  <source src="{{ "/assets/videos/SymBOPs_general/2D_squares_domains.mp4" | relative_url }}?v={{ site.time | date: '%s' }}" type="video/mp4">
  Your browser does not support the video tag.
  </video>
  <figcaption data-katex>
    Using SymBOPs to identify ordered domains of 2D square particles in 3D space. Each colored domain is independent and has it's own orientation.
  </figcaption>
</figure>

In this case there are particles in the configuration that were not found to fall in any of the ordered domains. This, of course, makes sense, because not all of the particles in a region of space share the orientational order of its neighbors, and some never assembled correctly, which is very common in simulation and experiment. By design, we only report contiguous domains, so distant matches aren’t grouped together. (In other applications you could relax this to find non-local patterns.)







## **Deeper Understanding of SymBOPs**

The example of the ideal pentagon crystal in <a href="#fig_pentagon_lattice" data-fig-ref>??</a> shows that orthorhombic crystals and their symmetry group constrained the available space. In general, we begin with the full space of symmetric, traceless tensors of rank $$\ell$$ with dimension $$2\ell + 1$$ and the identity is the only "symmetry". As we add symmetries, e.g., rotation by $$180^\circ$$ around the $$X$$-axis, reflection across the $$XY$$-plane, a constraint is added that either zeros elements or equates elements of the symmetric, traceless tensor. The most constrained case is full isotropy (group O(3)), and this forces all $$\ell > 0$$ to vanish and only the scalar $$\ell=0$$ survives. One of the main objects utilized by the SymBOPs method is what we call a *reference tensor* $$\widehat{R}^{(\ell)}$$. It is a traceless $$\ell$$-rank tensor that is invariant to all operations of a chosen point symmetry group and normalized $$\sqrt{\widehat{R}^{(\ell)} \cdot \widehat{R}^{(\ell)}} = 1$$. 

The reference tensor acts as the ideal template of the subspace that satisfies all symmetries we have chosen to search for in our configuration. We define the SymBOP as the projection of our bond tensors into this subspace,

$$
\widehat{q}^{*(\ell)} = \widehat{R}^{(\ell)} \left( \widehat{R}^{(\ell)} \cdot \widehat{b}_{ij}^{\otimes \ell} \right) = \widehat{\mathcal{P}}^{(\ell)} \widehat{b}_{ij}^{\otimes \ell}.
$$

$$\widehat{\mathcal{P}}^{(\ell)} = \widehat{R}^{(\ell)} \otimes \widehat{R}^{(\ell)}$$ is the projection operator associated with the reference tensor and with a symmetry group, when applicable. 

In 3D, high-rank tensors may be replaced with vectors of spherical harmonics. We use a variation of dirac notation to signify use of the spherical harmonic representation, where the reference tensor is now written as $$\vert R)_{\ell}$$, the normalization $$(R\vert R)_{\ell} = 1$$, and the SymBOP becomes

$$
\vert q_{ij}^{*})_{\ell} = \vert R)_{\ell} \, (R \vert \widehat{\mathbf{b}}_{ij})_{\ell} = \tilde{\mathcal{P}} \vert \widehat{\mathbf{b}}_{ij})_{\ell}.
$$


If $$\widehat{b}_{ij}^{\otimes \ell} \in V_\ell$$ is the vector space of all symmetric, traceless tensors of rank $$\ell$$ that holds the bond tensors, the subspace that we want to project our bond tensors into is 

$$
W^G_\ell = \{T \in V_\ell \, \vert \, D^{(\ell)}(g) T = T, \, \forall g \in G\}
$$

the subspace invariant under all operations of group $$G$$ acting on all elements of $$V_\ell$$ with $$D^{(\ell)}(g)$$. To perform this projection we use the projection operator for group $$G$$. 

The projection operator may be found in several ways, which breaks SymBOPs into different categories:

  1. *Point Group Symmetries* 

      If there is a particular group of symmetries you want to investigate, the projection operator can be constructed in the usual manner from group theory,

      $$
        \widehat{\mathcal{P}}^{(\ell)}_G = \frac{1}{\vert G \vert}\sum\limits_{g \in G} D^{(\ell)}(g).
      $$

      Or for a specific irreducible representation

      $$
        \widehat{\mathcal{P}}^{(\ell)}_{G, \Gamma} = \frac{d_\Gamma}{\vert G \vert} \sum\limits_{g \in G} \chi_{\Gamma}(g)^* D^{(\ell)}(g),
      $$

      where $$\vert G\vert$$ are the number of elements in $$G$$, $$d_{\Gamma}$$ is the dimension of the irreducible representation $$\Gamma$$, $$D^{(\ell)}(g)$$ is the representation of group operation $$g$$ with character $$\chi_{\Gamma}$$, and the asterisk represents complex conjugation. In general, $$D^{(\ell)}(g)$$ is a $$(2\ell + 1) \times (2\ell + 1)$$ matrix describing how element $$g$$ acts on $$V_\ell$$. In the spherical harmonic basis these are the Wigner $$D$$-matrices $$D^{(\ell)}_{mm'}(g)$$. The first equation is a special case of the latter when the trivial representation, that gives the full $$G$$-invariant subspace, is used, and $$d_{\Gamma} = \chi_{\Gamma}(g) = 1$$.

      If a particle in the system has this symmetry, this operator will be equivalent to that found using the *particle reference* method below.


  2. *Particle Reference*

      If the building blocks in the system are anisotropic then there are two types of orientational order present: bond-orientational order between centers of neighboring particles, and the orientational order of the the particles themselves. It is often, but not always, the case that the order of the bond orientations follows the symmetry of the particle, e.g., self-assmebling cubes or octahedra forming crystals with cubic symmetry. If this is the case, the polyhedral nematic order parameter is a quick, convenient way to construct the projection operator such that it uses the preferred axes of the particle.

      The projection operator can be most easily found by placing the origin at the particle's center of geometry and for each of the $$N_v$$ vertices of the polyhedron use the bond vector $$\hat{b}_{iv}$$ from the chosen origin $$i$$ to the vertex $$v$$. This unit vector defines the polar and azimuthal angles of the vertex with respect to the chosen origin. For each polyhedron you then create the $$2\ell + 1$$-dimensional vector of spherical harmonics based on these angles,

      $$
      \vert \tilde{s}_i )_\ell = \left\{ \frac{1}{N_v} \sum\limits_{v=1}^{N_v} Y_{lm}(\hat{b}_{iv}) \right\}_{m=-\ell \dots \ell}
      $$

      $$
      \vert s_i )_\ell = \frac{\vert \tilde{s}_i )_\ell}{\sqrt{(\tilde{s}_i \vert \tilde{s}_i )_\ell}}
      $$

      Here $$\vert s_i )_\ell$$ is a $$2\ell + 1$$-D vector of spherical harmonics, where each component corresponds to a different $$m$$. 
      
      Given $$\vert s_i )_\ell$$ the projector is 
      
      $$
        \widehat{\mathcal{P}}^{(\ell)} = \vert s_i)(s_i \vert_\ell.
      $$

      This is the preferred method when particles are anisotropic *and* we know the particle orientations--which is often not the case in experiment. In particular, this is demeonstrated in the publication "Controlling morphology in hybrid isotropic/patchy particle assemblies" (linked below). This method is powerful, and it can be used to construct a projector for any orientational geometry you'd like to search for. However, it's important to keep in mind if you want to create a custom projector for, e.g., a stick figure, that this is orientational only and, while the geometry is often constrained by the particle assembly, the geometry and topology of what is discovered may differ from the template.


  3. *Self-consistent Reference*

      In any case when the orientational information about the building blocks is not known or if the particles isotropic, the *particle reference* method is no longer possible, and we must find the projection operator and its preferred axes another way. The coordinate system associated with the projection operator is rotated to maximize the magnitude of the SymBOP signal averaged over a part of the system. Because SymBOPs is defined at the level of a single bond, we may identify individual bonds that belong to the same equivalance class, for the given point group. After bonds are selected, a bond percolation procedure can be used to locate local, coherent domains.

      This method is used in "Symmetry-specific characterization of bond orientation order in DNA-assembled nanoparticle lattices" (linked below).



## **How SymBOPs Improves Traditional BOPs**

Traditional bond-orientational order parameters (BOPs) are rotationally invariant descriptors. While powerful, they lose essential information by averaging out the orientation of the local environment — discarding phase information and symmetry specificity. As a result, they struggle to distinguish between different symmetries (e.g., tetrahedral vs. octahedral) and cannot capture subtle orientational correlations or anisotropies present in disordered or multi-component systems.

SymBOPs (Symmetrized Bond-Orientational Order Parameters) overcome these limitations by explicitly projecting local environments onto the irreducible representations of the symmetry group of interest. Instead of asking “How ordered is this neighborhood?”, SymBOPs ask “How much does this neighborhood look like a perfect copy of symmetry X?” — allowing for targeted detection of structure, whether crystalline, amorphous, or hierarchical.

Moreover, SymBOPs are defined in a group-theoretic framework, allowing them to naturally handle systems with multiple particle types, broken symmetries, or directional interactions — which are increasingly common in modern self-assembly and nanomaterials research.


### *Key Advantages of SymBOPs*

1. **Symmetry Specificity**  
   **What it is:** SymBOPs are built around an explicit reference tensor $$\widehat R^{(l)}$$ that is invariant under exactly the point‐group or space‐group symmetry you care about.  A projection operator $$\widehat P^{(l)} \;=\; \widehat R^{(l)} \otimes \widehat R^{(l)T}$$ then extracts only that symmetry channel from the bond tensor $$b_{ij}^{\otimes l}\,. $$  
   **Why it helps:** Traditional scalar BOPs average over all orientations and lose any memory of *which* symmetry they were testing for. By contrast, SymBOPs vanish identically unless the chosen symmetry is truly present.

2. **Retention of Phase Information**  
   **What it is:** Because SymBOPs project onto a single symmetry mode but keep the full tensor (or complex) output, they preserve both magnitude and *phase* (orientation) of the local order.  
   **Why it helps:** You can not only detect *that* order exists, but also map out the *direction* of each domain (i.e., the local phase of the order parameter), something scalar invariants throw away.

3. **Bond‐Level, Local Assignment**  
   **What it is:** SymBOPs are defined *per bond*—each inter-particle bond $$(i,j)$$ carries its own order parameter  
   $$
   \widehat q_{ij}^{*(l)} \;=\; \widehat P^{(l)} : b_{ij}^{\otimes l}\,.
   $$  
   **Why it helps:** You immediately know which bonds are “good” for that symmetry.  By combining this with simple bond-percolation, you can identify coherent *domains* of any shape or size—even very small or anisotropic clusters that traditional BOPs could never identify.

4. **Built-In Handling of Anisotropic Particles**  
   **What it is:** You can choose the reference tensor from the particle’s own orientational tensor (the polyhedral nematic order parameter) when you know each particle’s orientation, so that SymBOPs measure how bonds align *relative* to the particle axes.

   **Why it helps:** Traditional BOPs treat all particles as isotropic; any “particle orientation” is a separate nematic parameter. SymBOPs merge the two in one step, giving extra sensitivity to bond–particle correlations.

5. **Applicability Even When Orientations Are Unknown**  
   **What it is:** If your building blocks are isotropic (or if you lack orientation data--think experiment), you can instead pick $$\widehat R^{(l)}$$ from the *assumed* symmetry of the expected phase (e.g., octahedral or icosahedral).  
   **Why it helps:** You still get a targeted, symmetry-specific order parameter—even without local director information—leading to better phase identification than blind scalar BOPs.

6. **Unified, Group-Theoretic Framework**  
   **What it is:** Under the hood, SymBOPs are nothing more than projection operators onto irreducible representations of any chosen group $$G$$.  In spherical-harmonic language, one writes  
   $$
   Q_{\ell}^{(\Gamma)}(i)
   = \frac{1}{|G|} \sum_{g \in G}
     \chi^{(\Gamma)}(g)^* \;D^{(\ell)}(g)\;q_{\ell}(i)\,,
   $$  
   but in Cartesian form it reduces to the compact  
   $$
   \widehat P^{(l)}\,b^{\otimes l}\,.
   $$  
   **Why it helps:** The group sum automatically enforces all required sign and multiplicity factors.  This approach imports well-established representation-theory machinery into the bond-order parameter literature in a wholly new way.

7. **Superior Sensitivity in Heterogeneous & Amorphous Systems**  
   **What it is:** Because SymBOPs act locally and retain full tensor/phase information, they pick up even compact amorphous clusters or small crystallites that might be below the detection threshold of global or scalar-averaged BOPs.

   **Why it helps:** In hybrid simulations of patchy + isotropic particles, SymBOPs distinguished both NaCl-type edge-to-edge domains and non-space-filling face-to-face amorphous clusters—whereas traditional $$Q_\ell, W_\ell$$ methods failed to see any order.

8. **Custom Pattern Detection**  
   **What it is:** SymBOPs let you target *any* local bonding motif—crystalline, amorphous, or entirely custom—by supplying a reference tensor $$\widehat R^{(l)}$$ and forming the projector  
   $$  
   \widehat P^{(l)} = \widehat R^{(l)} \otimes \widehat R^{(l)T}  
   $$  
   which then picks out that exact pattern via  
   $$  
   \widehat q_{ij}^{*(l)} = \widehat P^{(l)} : b_{ij}^{\otimes l}\,.  
   $$  
   **Why it helps:** Traditional BOPs are limited to standard point‐group symmetries.  With SymBOPs you can locate any structure you can encode as a reasonable traceless-symmetric tensor of rank $$\ell$$—whether it’s an icosahedral cluster, a compact amorphous motif, or even a user‐defined “stick‐figure” network—simply by defining the appropriate reference tensor. However, it's important to remember that SymBOPs encodes the angular distribution and not necessarily the topology of the structure. It's often the case in assembled structures that a high SymBOPs signal will also find the same bonding connectivity, but it's not guranteed. This is especially important if these methods are applied outside of self-assembled systems, where the nodes and edges may not be constructed through physical principles. 



### Summary of Novel Contributions

- **Reference-tensor/projector approach** to bond order (importing irreducible-representation machinery into soft-matter order parameters).  
- **Particle-referenced vs. self-consistent** reference choices, allowing analysis of both known-orientation and unknown-orientation systems.  
- **Bond percolation** of SymBOP-tagged bonds to automatically extract coherent domains of *any* shape.  
- **Dual Cartesian/spherical formulation**, ensuring applicability in 2D, 3D, and beyond with minimal overhead.  













## **Applications of SymBOPs Beyond Materials**

{%comment%}
  - How can this work be applied to work other than particles? 
  - How can it be used for fields like AI/ML and neural net interpretability?
  - They use high dimensional spaces, but maybe understanding the order of these spaces helps the interpretability. - 
{%endcomment%}






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







