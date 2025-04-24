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
#header-includes:
#  - \renewcommand{\vec}[1]{\mathbf{#1}}
#  - \let\oldhat\hat
#  - \renewcommand{\hat}[1]{\oldhat{\mathbf{#1}}}
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

<figure id="fig_model">
  <img src="{{ 'assets/img/vdW_nanorods/vdW_nanorods_main_full.png' | relative_url }}" alt="Figure 1a" style="width: 37.5%; max-width: 100%;">
  <img src="{{ 'assets/img/vdW_nanorods/Fig2_Secondary_Modelv2.png' | relative_url }}" alt="Figure 1b" style="width: 54.2%; max-width: 100%;">
  <figcaption style="text-align: center; width: 100%;">
    Several views of the model of two identical rods interacting through a vdW potential.
  </figcaption>
</figure>


Our model, shown in <a href="#fig_model" data-fig-ref>??</a>, is two identical rods of length $$L$$ and diameter $$a$$. We utilize non-orthogonal coordinates $$XYZ$$, where $$\mathbf{\hat{n}_x}$$ and $$\mathbf{\hat{n}_y}$$ are the 
"director" vectors directed along the two rods, and $$\mathbf{\hat{n}_z}$$ is perpendicular to both rods. The centers of the rods are denoted $$\mathbf{X}_c$$ and $$\mathbf{Y}_c$$ for the two rods and are defined as 

$$
\begin{aligned}
\mathbf{X}_c &= \mathbf{X}_1 + X_0 \mathbf{\hat{n}_x} \\ 
\mathbf{Y}_c &= \mathbf{Y}_1 + Y_0 \mathbf{\hat{n}_y},
\end{aligned}
$$

where $$X_1$$ and $$Y_1$$ are the two closest points in each rod and $$X_0$$ and $$X_0$$ are their longitudinal displacements from the rod centers.

$$
\begin{aligned}
X_0 &= \frac{\left[ \left( \mathbf{X}_c - \mathbf{Y}_c \right) \cdot \mathbf{\hat{n}}_y \right]\left( \mathbf{\hat{n}}_x \cdot \mathbf{\hat{n}}_y \right) - \left( \mathbf{X}_c - \mathbf{Y}_c \right) \cdot \mathbf{\hat{n}}_x}{\left( \mathbf{\hat{n}}_x \cdot \mathbf{\hat{n}}_y \right)^2 -1} \\
Y_0 &= \frac{\left[ \left( \mathbf{X}_c - \mathbf{Y}_c \right) \cdot \mathbf{\hat{n}}_x \right]\left( \mathbf{\hat{n}}_x \cdot \mathbf{\hat{n}}_y \right) - \left( \mathbf{X}_c - \mathbf{Y}_c \right) \cdot \mathbf{\hat{n}}_y}{1 - \left( \mathbf{\hat{n}}_x \cdot \mathbf{\hat{n}}_y \right)^2}.
\end{aligned}
$$

The axis-to-axis distance between the rods is 

$$
r=\left|\left(\mathbf{X}_c - \mathbf{Y}_c\right)\cdot \mathbf{\hat{n}}_z\right|,
$$

where

$$
\mathbf{\hat{n}}_z = \mathrm{sgn} \left( \left(\mathbf{X}_c-\mathbf{Y}_c \right)\cdot \left( \mathbf{\hat{n}}_x \times \mathbf{\hat{n}}_y \right) \right) \frac{\mathbf{\hat{n}}_x \times \mathbf{\hat{n}}_y}{\left| \mathbf{\hat{n}}_x \times \mathbf{\hat{n}}_y \right|}.
$$

With this definition of $$\mathbf{\hat{n}}_z$$, the origin of the $$XYZ$$ system is at point  $$\mathbf{Y}_1$$, and vector $$\mathbf{\hat{n}}_z$$  points towards the "$$X$$" rod.  The angle between two rods is defined as

$$
\sin \theta = \left| \mathbf{\hat{n}}_x \times \mathbf{\hat{n}}_y \right|.
$$











### **The Approach: Bridging the Gaps**  
The key to the work is recognizing that there are a few limiting cases where the problem becomes much easier. 

**Limiting Cases:**

In broad strokes, the limiting csaes can be broken into a few parameters: 

  1. Rod Thickness:

      - infinitesemially thin rods (far-field regime)
      - finite thickness rods (near-field regime)

  2. Angle Between Rods:

      - non-parallel rods
      - parallel rods (surprisingly different from non-parallel)

  3. Rod Length:

      - infinitely long rods
      - finite rods of length $$L$$ (requires care)



The general method for finding solutions is as follows. For the simplest cases, we may integrate over the rods to get a closed-form solution, such as with infinitely long rods in the far-field. Given a solutions for, essentially, interacting lines of material, we may integrate this result to build up to a finite thickness, but infinitely long, rod (near-field). For instance, for infinitely long non-parallel rods, the potential in the two extreme limits is 

$$
U_{\mathrm{\times}} \approx \begin{cases}{} 
\frac{-A \pi a^4}{32 \,  \,\left|\sin\theta\right| \, r^4} & \frac{r}{a} \gg 1 \\ \\ 
\frac{-A a}{12\,  \,\left|\sin\theta\right| \, (r-a)} & \frac{r-a}{a} \ll 1
\end{cases} 
$$

Given the results in the near- and far-fields, we may interpolate in between by choosing a rational function that equals these results in the correct limits. This is a common interpolation strategy known as a Padé approximant.

We want something that decays like $$1/r^4$$ in the far-field and like $$1 / (r-a)$$ in the near-field. We choose a rational function such as 

$$
U = \frac{C}{(r-a)(r+B)^3}.
$$


<div class="aside-box">
  <div class="aside-header">Aside: Taking the limits</div>
  <div class="aside-content">
    Let's take the limits of the function and compute the values of B and C.
  
    <div class="math-box">
    $$\mathbf{r\to\infty}$$ \textbf{Limit:}
    </div>

      This limit is not difficult to calculate and we find 
      <div class="math-box">
      $$
      \lim_{r\to\infty} \frac{C}{(r-a)(r+B)^3} = \frac{C}{r^4}
      $$
      </div>
      We know that in this limit $$U = \frac{-A \pi a^4}{32 \,  \,\left|\sin\theta\right| \, r^4}$$, so we set them equal and find

      <div class="math-box">
      $$
      C = \frac{-A \pi a^4}{32 \,  \,\left|\sin\theta\right|}.
      $$

    $$\mathbf{r\to\a^+}$$ \textbf{Limit:}
    </div>
      This limit requires a little more work.

      We can define $$h = r-a$$ and instead compute 
      $$
      \lim_{h\to\0} \frac{C}{h(h + a + B)^3}
      $$

      To do this we factor 

      $$
      \left(h + (a + B)\right)^3 = (a+B)^3 (1 + \frac{h}{a+B})^3
      $$

      and expand the second term $$(1 + \frac{h}{a+B})^3$$ to leading order around $$\frac{h}{(a+B)}=0$$ as

      $$
      (1 + \frac{h}{a+B})^3 \approx 1 + \frac{3h}{a+B} + \mathellipsis
      $$

      Plugging in $$(1 + \frac{h}{a+B})^3 \approx 1$$ we find

      $$
      \lim_{h\to\0} \frac{C}{h(h + a + B)^3} \approx \frac{C}{h(a + B)^3} = \frac{C}{(r-a)(a+B)^3}.
      $$

      Setting the limit equal to the expression in the near-field

      $$
      \begin{aligned}
      \frac{C}{(r-a)(a+B)^3} &= \frac{-A a}{12\,  \,\left|\sin\theta\right| \, (r-a)} \\ 
      B &= \left( \frac{12 |sin\theta| C}{-Aa} \right)^{1/3} - a = \left[ \frac{(3\pi)^{1/3}}{2} - 1 \right]a \approx 0.06a
      \end{aligned}
      $$
  </div>
</div>


After using the asymptotes to find $$B$$ and $$C$$ we find 

$$
U = \frac{-V_0}{|\sin\theta| (r-a) (r + \epsilon a)^3},
$$

where $$\epsilon$$ has replaced the $$0.06$$  prefactor of $$a$$ and is instead used as a fine tuning parameter to achieve a near-perfect fit for the value $$\epsilon = 0.12$$. Finally we have a compact expression for non-parallel infinite rods






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