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

<p align="center"><strong>We consider two uniform rods of the same length \(L\) and diameter \(a\) and present a high-accuracy approximate formula for the vdW potential as a function of their relative positions and orientation.</strong></p>

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

  <!-- only this inner div is in Markdown mode -->
  <div class="aside-content" markdown="1">

Let's take the limits of the function and compute the values of B and C.
  
#### **The Far-Field Limit:**

This limit is not difficult to calculate and we find 

$$
\lim_{r\to\infty} \frac{C}{(r-a)(r+B)^3} = \frac{C}{r^4}
$$

We know that in this limit $$U = \frac{-A \pi a^4}{32 \,  \,\lvert\sin\theta\rvert \, r^4}$$, so we set them equal and find

$$
C = \frac{-A \pi a^4}{32 \,  \,\lvert\sin\theta\rvert}.
$$


#### **The Near-Field Limit:**

This limit requires a little more work.

We can define $$h = r-a$$ and instead compute 
$$
\lim_{h\to 0} \frac{C}{h(h + a + B)^3}
$$

To do this we factor 

$$
\left(h + (a + B)\right)^3 = (a+B)^3 (1 + \frac{h}{a+B})^3
$$

and expand the second term $$(1 + \frac{h}{a+B})^3$$ to leading order around $$\frac{h}{(a+B)}=0$$ to find

$$
\lim_{h\to 0} \frac{C}{h(h + a + B)^3} \approx \frac{C}{h(a + B)^3} = \frac{C}{(r-a)(a+B)^3}.
$$

Setting the limit equal to the expression in the near-field

$$
\frac{C}{(r-a)(a+B)^3} = \frac{-A a}{12\,  \,\lvert\sin\theta\rvert \, (r-a)}
$$

$$
B = \left( \frac{12 \lvert\sin\theta\rvert C}{-Aa} \right)^{1/3} - a = \left[ \frac{(3\pi)^{1/3}}{2} - 1 \right]a \approx 0.06a
$$

  </div>
</div>






After using the asymptotes to find $$B$$ and $$C$$ we find 

$$
U = \frac{-V_0}{\lvert\sin\theta\rvert (r-a) (r + \epsilon a)^3},
$$

where $$V_0 = A\pi a^4 / 32$$ and $$\epsilon$$ has replaced the $$0.06$$ prefactor of $$a$$ and is instead used as a fine tuning parameter to achieve a near-perfect fit for the value $$\epsilon = 0.12$$. 

With this result we have a compact expression for *non-parallel infinite rods*. From Here we use the same logic for parallel rods in the near- and far-fields. We interpolate between these limits, in the same manner as above, starting with our previous expression, which we know works well for non-parallel rods, but we replace the $$\lvert \sin\theta \rvert$$ with a correction term to match the parallel results in the extreme limits. After repeating the steps above for parallel rods, we arrive at an equation for the vdW potential of interacting infinite rods at arbitrary angle and diameter

$$
U_{\mathrm{rods}} \approx \frac{-V_0}{(\lvert\sin\theta\rvert + 2.35\frac{\sqrt{r(r-a)}}{L}) (r-a) (r + \epsilon a)^3}.
$$


Moving to finite length rods is done using a finite-size correction term $$\gamma$$ which is modified to work for non-parallel and parallel configurations, and, in fact, $$U_{\mathrm{rods}} \gamma$$ works well in the far-field regime. The terminals of the rods are more complicated because they add a "shadow effect" that makes the rods appear longer than they are, which comes from the divergence of the $$1/(r-a)$$ term. To fix this shadow effect we include a term $$\gamma_a$$ in $$1 / (r - \gamma_a a)$$ that allows the user to define the shape of the rods (perhaps you'd like to simulate ellipsoidal rods) and how they shrink to zero at their ends. Alternatively, $$\gamma_a$$ can be set to unity and made to decay as $$\gamma$$ goes to zero to, ensuring that the rod diameter is uniform but will go to zero when they rods should not collide.

The **final vdW interaction potential:** 


<div class="math-box wide-math">
{% raw %}
$$
\begin{gathered}
\boxed{U_{\mathrm{vdW}}(X_0, Y_0, r, L,\theta) = \frac{-A \pi a^4 \, \gamma\left(X_\pm, Y_\pm \right)}{32 \, (\left| \sin \theta \right|+2.35 \frac{\sqrt{r(r-\gamma_a a)}}{L}) \, (r- \gamma_{a} a) \, (r+0.12 \, a)^3}}
\\[5mm]
\hline
\hline
\\[5mm]
\begin{aligned}
\gamma(x\pm, y\pm)&=\mathrm{min}\left\{\left[g\left(x_+ \right)-g\left(x_-\right) \right], \left[g\left(y_+ \right)-g\left(y_-\right) \right]\right\}&g(x)&=\frac{1}{2} \, \mathrm{sgn}\left(x\right) \, \mathrm{min}\left\{ 1, \frac{3}{2}\left|x\right| \right\}&\gamma_a&=\gamma\left(X_\pm^a, Y_\pm^a \right)
\end{aligned}
\\[7mm]
{\scriptstyle
\begin{aligned}
X_\pm&=\left(X_0 \pm \frac{L}{2}\right)\left(\frac{\left|\sin \theta \right|}{r+a}+\frac{4 \left| \cos \theta \right|}{3L}\right) - \frac{4Y_0 \cos \theta}{3L}&Y_\pm&=\left(Y_0 \pm \frac{L}{2}\right)\left(\frac{\left|\sin \theta \right|}{r+a}+\frac{4 \left| \cos \theta \right|}{3L}\right) - \frac{4X_0 \cos \theta}{3L}
\end{aligned}
}
\\[7mm]
\begin{aligned}
X_\pm^a &= \frac{(X_0\pm \frac{L}{2})}{a} \pm \frac{2(r+a)(L\mp 2Y_0\cos \theta)}{4a(r+a) \left|\cos \theta\right| + 3La \left|\sin \theta\right|} \mp 1.4&Y_\pm^a &= \frac{(Y_0\pm \frac{L}{2})}{a} \pm \frac{2(r+a)(L\mp 2X_0\cos \theta)}{4a(r+a) \left|\cos \theta\right| + 3La \left|\sin \theta\right|} \mp 1.4
\end{aligned}
\end{gathered}
$$
{% endraw %}
</div>




<p align="center"><strong>The paper includes derivations of force and torque, and even includes a version of the interaction potential to be used in 2D.</strong></p>




<figure id="fig_results_heat_maps" class="stack-vertical">
  <img src="{{ '/assets/img/vdW_nanorods/Fig9a_gamma_0_and_90_deg_with_L50_a2_r2_2.png' | relative_url }}" alt="Figure a" style="width: 75%;">
  <img src="{{ '/assets/img/vdW_nanorods/Fig9b_gamma_0_and_90_deg_with_L50_a2_r2_2.png' | relative_url }}" alt="Figure b" style="width: 75%;">
  <img src="{{ '/assets/img/vdW_nanorods/Fig10_Uvdw_Xr_heatmap_L50_a2_m90_y0_rpos.png' | relative_url }}" alt="Figure c" style="width: 75%;">
  <figcaption style="text-align: center; width: 100%;">
    Heat map of \(\gamma(X_\pm, Y_\pm)\) with \(\frac{L}{a}=25\), for (top) \(\theta=\frac{\pi}{2}\) and (middle) \(\theta=0\). As the angle between the rods changes from perpendicular to parallel, the non-zero region in the 2D plot transforms from a closed square to an infinitely long linear region, illustrating that \(\gamma(X_\pm, Y_\pm)\) becomes proportional to the overlap \(\Delta\) as the angle goes to zero.
    (bottom) Two-dimensional plot of \(\frac{\left|U_{\mathrm{vdW}}\right|}{A}\) with \(\frac{Y_0}{a}=0\), \(\theta=\frac{\pi}{2}\), and \(\frac{L}{a}=25\). The red region diverges as the rods make contact and it essentially outlines the rod. The area inside of the rod, where the other rod cannot physically penetrate is colored in white.
  </figcaption>
</figure>


In <a href="#fig_results_heat_maps" data-fig-ref>Figure ??</a> we see 2D heat maps of $$\gamma$$ for different displacements from the centers of each rod $$X_0$$ and $$Y_0$$ for orthogonal (top) and parallel (middle) rods of uniform radius $$a$$ and idential lengths $$L$$. At $$X_0 = Y_0 = 0$$ The closest points between the two rods are their centers, and the heat maps show that the interaction is strongest. As We increase $$X_0$$, for instance, the "$$X$$" rod moves along the its longitudinal axis without chanign the angle between the rods and the interaction strength begins to decay. When the rods are orthgonal, the decay begins once the end of the $$X$$ rod nears the center of the $$Y$$ rod. When the rods are parallel, the interaction begins to decay almost immediately and reaches zero once the ends have passed each other. We can interpolate between orthogonal and parallel rods by looking at the top and middle plots. For orthogonal rods the non-zero interaction region is square for equal length rods, and for parallel rods it is an infinitely long linear region as the rods move together parallel to each other. For intermediate angles, the square distorts and transforms slowly as the angle decreases to zero, moving toward the infinite lienar region seen in the middle plot. The bottom plot shows how the interactions decays as orthogonal rods keep the same angle but move away from each other in the Z-direction. 




### **Why This Work Matters**  
The result is a **compact formula** that accurately describes van der Waals interactions between nanorods in arbitrary configurations. This formula provides a quick and efficient way to model these interactions, making it much easier to simulate systems of nanorods in fields like nanomaterials, soft matter physics, and colloidal science.  

The approach is not just theoretical—it’s practical. Instead of running costly simulations for every possible scenario, scientists can now plug values into this formula and get good approximations in a fraction of the time.  

Understanding how nanorods stick together is critical for many cutting-edge technologies. Think of **nanotube-based electronics**, **self-assembling materials**, or even **biomedical applications** where rod-like particles are used for drug delivery. By providing a simple, computationally light method to calculate these interactions, we have made it easier for other researchers to explore and design new materials.  









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