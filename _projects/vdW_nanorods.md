---
layout:      project
title:       "Compact interaction potential for vdW nanorods"
header_title: "How Nanorods Stick Together: A Simple Approach to a Tricky Problem"
#date:        2 Jan 2014
order: 5
image:
  path:      /assets/img/vdW_nanorods/vdW_nanorods_main2_full_w_bg.png
  srcset:
    1920w:   /assets/img/vdW_nanorods/vdW_nanorods_main2_full_w_bg.png
    960w:    /assets/img/vdW_nanorods/vdW_nanorods_main2_half.png
    480w:    /assets/img/vdW_nanorods/vdW_nanorods_main2_quarter.png
caption:     Modeling proteins as constrained polymers
#description: >
#  Hyde is a brazen two-column [Jekyll](http://jekyllrb.com) theme.
#  It's based on [Poole](http://getpoole.com), the Jekyll butler.
#links:
#  - title:   Publication
#    url:     https://doi.org/10.1103/PhysRevE.98.032609
featured:    false
#related_posts: 
---


Van der Waals forces are the molecular glue that holds together a surprising number of materials. From geckos sticking to walls to how soot clumps in the air, these weak but omnipresent forces shape the microscopic world. But what happens when the objects involved aren’t simple spheres, but long, thin nanorods? We set out to answer a deceptively simple question: how do these tiny rods attract each other, and can we describe their interactions with a simple formula?  
{:.lead}


---

* this unordered seed list will be replaced by the toc
{:toc}


### **The Challenge: Beyond Spheres**  
For decades, van der Waals (vdW) interactions have been well understood for spherical particles. If you want to model how tiny spheres attract or repel each other, there's a well-established set of equations for that. But nanorods (think tiny, elongated cylinders) have added complications. Their interactions depend not just on distance but also on *orientation*—-two rods can sit parallel, cross at an angle, or barely touch end-to-end. Traditional calculations for these scenarios are complex, computationally expensive, and have no simple closed-form expression.

Despite the difficulty of working with vdW rods, they are incredibly useful and necessary with applications to simulations of self-assembly, carbon nanotubes, liquid crystals, microtubules, and DNA. Their use spans fields such as soft-condensed matter physics, biology, materials science, among others. 

We sought to simplify this mess with a compact formula that captures the essential physics without the need for heavy computation. This compact formula can help computational scientists to avoid time wasting numerical integrations when performing molecular dynamics or Monte Carlo simulations involving rod-like particles interacting through a vdW force.

<p align="center"><strong>We consider two uniform rods of the same length $$L$$ and diameter $$a$$ and present a high-accuracy approximate formula for the vdW potential as a function of their relative positions and orientation.</strong></p>

---

## **vdW Potential Energy**

vdW interactions were first developed by London (London dispersion forces are a type of vdW interaction for non-polar molecules) and are interpreted as an effect of correlated quantum fluctuations of dipole moments. It is generally only effective over several hundred angstroms and then begins to fall off faster for larger distances (known as the retarded regime). Retardation and multi-body effects are often neglected and written as a simple $$1/r^6$$ potential.

$$
U = -\frac{A}{\pi^2} \int \int \frac{d^3\mathbf{r_1}d^3\mathbf{r_2}}{|\mathbf{r_1} - \mathbf{r_2}|^6},
$$

where $$A = \pi^2 C \rho_1 \rho_2$$ is the material-dependent Hamaker constant with $$\rho$$ the number density of interacting particles, and integration is carried out over the the volumes of each object. The potential is negative becuase it is purely attractive.

## **The Model**

<figure style="display: flex; justify-content: center; align-items: center; gap: 15px; flex-wrap: wrap;">
  <img src="{{ "assets/img/vdW_nanorods/vdW_nanorods_main_full.png" | relative_url }}" alt="Figure 1" style="width: 100%; max-width: 45%;">
  <figcaption style="text-align: center; width: 100%;">
    Figure 1: The model of two idential rods interacting through a vdW potential. 
  </figcaption>
</figure>

Our model, shown in Fig. !, is two identical rods of length $$L$$ and diameter $$a$$. We utilize non-orthogonal coordinates $$\mathbf{\hat{n}_x}$$, $$\mathbf{\hat{n}_y}$$, $$\mathbf{\hat{n}_z}$$, where $$\mathbf{\hat{n}_x}$$ and $$\mathbf{\hat{n}_y}$$ are the 
"director" vectors directed along the two rods, and $$\mathbf{\hat{n}_z}$$ is perpendicular to both rods. The centers of the rods are denoted $$\mathbf{X}_c$$ and $$\mathbf{Y}_c$$ for the two rods and are defined as 

$$
\begin{aligned}
\mathbf{X}_c &= \mathbf{X}_1 + X_0 \mathbf{\hat{n}_x} \\ 
\mathbf{Y}_c &= \mathbf{Y}_1 + Y_0 \mathbf{\hat{n}_y},
\end{aligned}
$$

where $$X_1$$ and $$Y_1$$ are the two closest points in each rod and $$X_0$$ and $$X_0$$ are their longitudinal displacements from the rod centers.



### **The Approach: Bridging the Gaps**  
The key to the work was recognizing that there are a few limiting cases where the problem becomes much easier. 

**Limiting Cases:**


* *Infinitely long* rods with *infinitesimal thickness* and *non-parallel*
* *Infinitely long* rods with *finite thickness* and *non-parallel*

* *Infinitely long* rods with *infinitesimal thickness* and *parallel*
* *Infinitely long* rods with *finite thickness* and *parallel*

* *Finite length* in the far-field



We begin with the case of infinitely long, infinitesimally thin rods that are not parallel. 


For example:  
- When two rods are far apart, their interaction behaves like that of two point masses.  
- When they're nearly touching, the force looks more like the interaction between two plates.  
- If they are perfectly aligned, they behave like a set of stacked spheres.  

In this work we interpolate between these known cases to create a general equation that works across a wide range of distances and orientations. 

---

### **What They Found**  
The result? A **compact formula** that accurately describes van der Waals interactions between nanorods in various configurations. This formula provides a quick and efficient way to model these interactions, making it much easier to simulate systems of nanorods in fields like nanomaterials, soft matter physics, and colloidal science.  

The approach is not just theoretical—it’s practical. Instead of running costly simulations for every possible scenario, scientists can now plug values into this formula and get good approximations in a fraction of the time.  

---

### **Why It Matters**  
Understanding how nanorods stick together is critical for many cutting-edge technologies. Think of **nanotube-based electronics**, **self-assembling materials**, or even **biomedical applications** where rod-like particles are used for drug delivery. By providing a simple, computationally light method to calculate these interactions, we have made it easier for other researchers to explore and design new materials.  

---







### **Links**

<a href="https://doi.org/10.1103/PhysRevE.98.032609" class="info-button" target="_blank">
  <span class="icon-book" style="font-size: 32px;"></span> Compact interaction potential for van der Waals nanorods
</a>


<style>
  /* Remove any arrows on external links */
  .info-button::after {
    content: none !important;
  }
</style>