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






### **Rotational symmetry**


<figure style="max-width: 100%; text-align: center; margin: auto;">
  <img src="{{ "/assets/img/SymBOPs_general/symmetry_of_circle_vs_rod.png" | relative_url }}" alt="Figure Description"
       style="width: 100%; height: auto; max-width: 600px;">
  <figcaption style="font-size: 0.9em; color: #666; margin-top: 5px;">
    Difference of rotational symmetry between a circle and a cirlce with two differently colored points.
  </figcaption>
</figure>




Rotational symmetry is used to describe an object or set of objects (or points, equations, etc.) that is unaffected by rotations. A 2-sphere in three-dimensions, for instance, has the full symmetry of the rotation group SO(3). We can rotate it in any manner that we'd like and it never looks any different. To make things easier to visualize let's think of a circle (1-sphere) in two-dimensions. Any rotation of the circle leaves it unchanged. If we place two differently colored points on opposite ends of a chord that goes through the center of the circle, everything changes. Now any rotation we choose other than a multiple of $$2\pi$$ gives a different picture from what we started with. The symmetry we had has been broken and only repeats when we rotate by $$2\pi n$$, where $$n$$ is an integer.





### **What is Traditionally Done**


<figure style="max-width: 100%; text-align: center; margin: auto;">
  <img src="{{ "/assets/img/SymBOPs_general/BOP_and_nematic_rods_full.png" | relative_url }}" alt="Figure Description"
       style="width: 100%; height: auto; max-width: 800px;">
  <figcaption style="font-size: 0.9em; color: #666; margin-top: 5px;">
    Simple example using rods to demonstrate the difference between bond-orientational order, nematic order, and the combination of both.
  </figcaption>
</figure>


Orientational order looks at the rotational symmetry of an object or group of objects around a common point. There are two types of orientational order that we must distinguish between: *bond-orientational order* describes the orientational order of points in the neighborhood of a an origin, and *polyhedral nematic order* describes how aligned anisotropic objects, e.g., polygons and polyhedra, are with each other. 

Bond-orientational order quantifies how ordered a set of points are based on their angles in a common set of axes. To learn by example, see the left image of Fig.2. Focus only on the left green point and the black points neighboring it. Using the usual polar coordinates we can compute the angle $$\theta_i$$ for each black neighboring partile $$i$$. We sum the phases of all $$N_b$$ neighbors of the green point

$$
\psi_{\ell} = \frac{1}{N_b}\sum\limits_{i=1}^{N_{b}} e^{i\ell \theta_i},
$$

where $$\ell$$ is chosen to look at $$\ell$$-fold orientational order. In the figure I have drawn concentric hexagons to aid the eye in looking for $$\ell=6$$-fold order, called hexatic order. We can easily see that each neighbor lies almost exactly on a vertex of the hexagons, showing that these neighbors have near perfect hexatic order. Notice that translationally, they're a mess; together the points do no form a regular hexagon. Our concern is strictly the orientational order about the central point, and not the translational order. Another thing to note is that this show that we can have orientational order while maintaining translational symmetry. Translational symmetry implies that there is no preferred distance between points, such as in a crystal--which breaks translational and orientational order. At this point we have a 2D vector $$\psi_\ell$$ which is a property of the neighborhood of the green point. This vector holds information about how the neighboring points are distributed orientationally around the green point--how well they approximate $$\ell$$-fold symmetry and also the orientation of this polygon in the chosen coordinate system. If we were to look at the neighborhood of a different point that differs from the previous neighborhood only be a rotation, the $$\psi_\ell$$ vectors will be different.

The seminal paper by Steinhardt et al. in 1983 defined a way to quantify bond-orientational order in three-dimensions and proposed the use of rotational invariants to describe local structure of a set of particles in liquids and glasses. In 3D you may use spherical harmonics in place of a complex field. For each bond vector $$b_{ij}$$ from central particle $$i$$ to neighboring particle $$j$$ we may identify a point on the unit sphere with polar and azimuthal angles $$\left( \theta(\vec{r}_{ij}), \phi(\vec{r}_{ij}) \right)$$. From here traditionally one averages over the spherical harmonics for all neighbors and computes the second-order scalar (rotational invariant)

$$
\begin{align}
  \vec{q}_{\ell m} &= \frac{1}{N_b} \sum\limits_{j=1}^{N_b} Y_{\ell m}\left( \theta(\vec{r}_{ij} \right), \phi(\vec{r}_{ij})) \\ 
  q_\ell &= \left[ \frac{4\pi}{2\ell + 1} \sum\limits_{m=-\ell}^{\ell} |\vec{q}_{\ell m}|^2  \right]^{1/2}.
\end{align}
$$


The neighboring points may be collected within a specified distance or by some weighting function that rapidly goes to zero away from the central particle.

These parameters have been used very successfully over decades as structure descriptors, but cannot be considered an order parameter once they throw away the phase information by forming invariants. These descriptors are widely accepted and are often used to identify neighborhoods of clusters of particles as crystal-like or amorphous-like, and even the local structure as FCC-like, etc. 



### **How SymBOPs improves this**








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







