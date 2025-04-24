---
layout:      project
title:       "Geometric and topological entropy of sphere packing"
header_title: "Exploring Entropy in Sphere Packings: A New Perspective with Statistical Mechanics"
#date:        2 Jan 2014
order: 4
image:
  path:      /assets/img/entropy_of_sphere_packing/packing_entropy_main_full.png
  srcset:
    1920w:   /assets/img/entropy_of_sphere_packing/packing_entropy_main_full.png
    960w:    /assets/img/entropy_of_sphere_packing/packing_entropy_main_half.png
    480w:    /assets/img/entropy_of_sphere_packing/packing_entropy_main_quarter.png
caption:     Modeling proteins as constrained polymers
#description: >
#  Hyde is a brazen two-column [Jekyll](http://jekyllrb.com) theme.
#  It's based on [Poole](http://getpoole.com), the Jekyll butler.
#links:
#  - title:   Publication
#    url:     https://doi.org/10.1103/PhysRevE.105.014117
featured:    false
#related_posts: 
---



Entropy is often associated with disorder, but in physics and mathematics, it is a powerful tool for understanding complexity and structure. In their paper, "Geometric and Topological Entropies of Sphere Packing," Logan and Tkachenko introduce novel ways to quantify the organization and randomness in sphere packings using a statistical mechanics-inspired framework. Instead of working in traditional energy-based ensembles, they construct a **custom entropy-based ensemble**, where entropy itself is the primary variable. Their work extends beyond traditional methods by developing two complementary entropy measures: **geometric entropy** and **topological entropy**. These measures provide deeper insights into the organization of sphere packings, particularly in jammed states, with implications for materials science, soft matter physics, and statistical mechanics.
{:.lead}


### **The System**

We consider a system of $$N$$ hard spherical particles in $$d$$-dimensional space with average particle diameter $$\bar{a}$$. The spheres have similar diameters, and packing is weakly polydisperse. A pair of particles is said to be in contact if the gap between them is less than some small value $$\Delta \ll \bar{a}$$. For any configuration, the topology can be specified by an adjacency matrix $$\mathbf{\hat{C}}$$ with $$C_{ij}=1$$ for all particles $$i\neq j$$ in contact and $$C_{ij}=0$$ otherwise.

One way in which this work is unique is that the average coordination number $$Z = \frac{1}{N} \sum_{i<j} C_{ij}$$ is treated as a thermodynamic variable of the system. The weak polydispersity is introduced to avoid overconstrained topolgoies--those with more than the required bonds to keep the configuration stable. Examples of such configurations include close-packed crystals, e.g., face-centered cubic in 3D or hexagonal in 2D. If we disqualify such topolgies, the only rigid packings remaining are isostatic. These are configurations where the number of contacts is equal to the total number of degrees of freedom of $$N$$ spheres $$Nd$$ minus the number of rigid body degrees of freedom $$d(d+1)/2$$ (global rotations and translations). For a finite system of $$N$$ spheres the mean coordination number for a system to be isostatic is $$Z^* = 2d - d(d+1)/N$$. In the thermodynamic limit ($$N \rightarrow \infty$$) this becomes $$Z^* = 2d$$.

The mathematical framework developed below is applicable to all topolgies of spheres, not just the isostatic case, but we'll see that when the system is isostatic there is a key simplification that allows the equations to be easily solved. Another important point is that the energy of the system comes from the bonding, but if the number of bonds does not change, then the energy of the system does not change. This makes energy essentially useless in this problem. The main  variable is the entropy of the system. For this reason, we reformulate standard statistical mechanics in terms of entropy instead of energy. As shown below, the entropy of the whole packing $$S_{\text{pack}}$$ is broken into two exclusive pieces: geometric entropy $$S_{\text{geo}}$$ and topological entropy $$S_{\text{topo}}$$. 

In order to compute the entropies we use a statistical mechanical thought experiment and a novel Monte Carlo algorithm, developed for this work. The simulations are done for packings in a semi-periodic box (periodic in $$x$$ and $$y$$, closed at $$z=0$$ and open for positive $$z$$) and for packings in free space. Examples of these two types of packings are seen in the figure at the top of the page.


### **Connecting to Traditional Statistical Mechanics**
In equilibrium statistical mechanics, the **partition function** $$\mathcal{Z}$$ is the fundamental quantity that encodes all thermodynamic properties of a system:

$$
\mathcal{Z} = \sum_i e^{-\beta E_i} = \sum_E \Omega(E) e^{-\beta E}
$$

where:
- The first sum runs over all possible **microstates** $$ i $$.
- $$E_i$$ is the energy of the microstate.
- $$\beta = 1/k_B T$$ is the inverse temperature.
- Equivalently, the second sum is over all **macrostates** with energy $$E$$
- $$\Omega(E)$$ is the number of microstates with energy $$E$$

**While these are *equivalent* ways to write the partition function, the latter is more directly comparable to this work.**

The free energy $$F$$ is related to the partition function by:

$$
F = -k_B T \ln \mathcal{Z}.
$$

In contrast, for our work we define an **entropy-based partition function** more akin to the sum over macrostates defined above:

$$
e^{N S_{\text{pack}}(Z)} = \sum_{\mathbf{\hat{C}}} \frac{\delta(Z(\mathbf{\hat{C}}) - Z)}{N!} e^{N S_{\text{geo}}(\mathbf{\hat{C}})}.
$$

This equation sums over **packing configurations** instead of energy states. Here:
- $$Z$$ is the mean coordination number---the average number of bonds for each sphere.
- $$\mathbf{\hat{C}}$$ is the **adjacency matrix** defining a packing topology---a bonding network.
- $$S_{\text{geo}}(\mathbf{\hat{C}})$$ is the **geometric entropy** of that topology.
- $$\delta(Z(\mathbf{\hat{C}}) - Z)$$ enforces a constraint on the **average coordination number**.
- $$Z$$ is used as a thermodynamic variable in this custom ensemble.

If $$e^{N S_{\text{pack}}(Z)}$$ is the equivalent of a partition function, then $$S_{\text{geo}}$$ determines the statistical weight for a specific realization of the packing topology $$\mathbf{\hat{C}}$$.

$$
e^{NS_{\text{geo}}(\mathbf{\hat{C}})} = \int \frac{d^d\vec{r}_2...d^d\vec{r}_N}{\Omega_d \bar{a}^{(N-1)d}} \prod\limits_{i>j,C_{ij}=1} \bar{a} \delta(x_{ij}) \prod\limits_{i>j,C_{ij}=0} \Theta(x_{ij}) 
$$

Here:
- The first sphere $$\vec{r}_1$$ is assumed fixed at the origin to remove global translations.
- Division by $$\Omega_d$$ eliminates contributions from rigid body rotations (specicially, $$\Omega_{2} = 2\pi$$ and $$\Omega_{3} = 2\pi \times 4\pi = 8\pi^2$$).
- <span>$$x_{ij} = |\vec{r}_i - \vec{r}_j| - (a_i + a_j)/2$$</span> is the surface-to-surface distance between spheres $$i$$ and $$j$$ with positions $$\vec{r}_i$$ and $$\vec{r}_j$$.
- The delta function $$\delta(x_{ij})$$ ensures that all contacts recorded in the adjacency matrix are just touching with surface-to-surface distance 0.
- The Heaviside function $$\Theta(x_{ij})$$ ensures that all spheres that are not in contact are not touching.

In the special case of an isostatic packing, the number of constraints is exactly equal to the number of degrees of freedom (minimum number of constraints to make the packing mechanically stable) we may conveniently change variables from the positions $$(\vec{r}_2,...,\vec{r}_N)$$ to the gaps between pairs of particles $$(x_1,...,x_{NZ/2})$$ including the $$d(d-1)/2$$ independent rigid body rotations $$\hat{\theta} = (\theta_1,...,\theta_{d(d-1)/2})$$. The Jacobian determinant of this transformation then provides a very simple way to compute the geometric entropy of a configuration.

$$
NS_{\text{geo}}(\mathbf{\hat{C}}) = \ln \left[ \frac{\partial (\vec{r}_2,...,\vec{r}_N)}{\partial (\hat{\theta}, x_1,...,x_{NZ/2})}  \right].
$$



### **Geometric vs. Topological Entropy: A Free Energy-Like Decomposition**
We may decompose our effective free energy in a similar way to the standard $$ F = E - TS $$:

$$
\begin{align}
- N T S_{\text{pack}} &= (- N T S_{\text{geo}}) - T(N S_{\text{topo}}) \\ 
S_{\text{pack}} &= S_{\text{geo}} + S_{\text{topo}},
\end{align}
$$

where we have defined effective energies and entropies:
- $$ -N T S_{\text{geo}} $$ (geometric entropy) is analogous to an **energy function**.
- $$ N S_{\text{topo}} $$ (topological entropy) plays the role of an **entropy correction**.
- $$ -N T S_{\text{pack}} $$ (packing entropy) is the effective free energy, and the total entropy accounting for both local geometric structure and global connectivity.

This formulation mirrors the **free energy decomposition** in traditional statistical mechanics but within an entropy-driven ensemble:


| **Traditional Statistical Mechanics** | **Logan & Tkachenko Sphere Packing** |
|----------------------------|----------------------------------|
| $$ \mathcal{Z} = \sum_i e^{-\beta E_i} $$ | $$ e^{N S_{\text{pack}}} = \sum_{\hat{C}} e^{N S_{\text{geo}}} $$ |
| $$ F = E - TS $$ | $$ -N T S_{\text{pack}} = -N T S_{\text{geo}} - N T S_{\text{topo}} $$ |
| Energy $$ E $$ | Geometric entropy $$ -N T S_{\text{geo}} $$ |
| Temperature $$ T $$ | Implicit, ensemble-based |
| Entropy $$ S $$ | Topological entropy $$ N S_{\text{topo}} $$ |
| Free energy $$ F $$ | Packing entropy $$ -N T S_{\text{pack}} $$ |

### **Computing $$S_{\text{geo}}$$ Using Novel Isostaticity-Preserving Monte Carlo Methods**

{%comment%}
<figure id="vid_MC_move">
  <img src="/assets/img/entropy_of_sphere_packing/MC_move_cover.png" alt="2D_vp_and_rem" width="400" height="auto">
  <figcaption style="text-align: center; width: 100%;">
  Demonstration of one step in a Monte Carlo move from one isostic packing to another for a cluster of 50 particles in 2D. The bond between the green particles increases and all spheres move along the zero mode introduced until a previously unbound pair of spheres (purple) makes contact. At this point the green bond is broken and a new bond is formed between the purple spheres.
  </figcaption>
</figure>
{%endcomment%}

{%comment%}
<figure id="vid_MC_move">
  <video width="650" height="auto" poster="{{ "/assets/img/entropy_of_sphere_packing/MC_move_cover.png" | relative_url }}" autoplay loop muted playsinline>
  <source src="{{ "/assets/videos/entropy_of_sphere_packing/MC_move.mp4" | relative_url }}?v={{ site.time | date: '%s' }}" type="video/mp4">
  Your browser does not support the video tag.
  </video>
  <figcaption data-katex>
    Demonstration of Monte Carlo move from one isostic packing to another for a cluster of 50 particles in 2D. The bond between the green particles increases and all spheres move along the zero mode introduced until a previously unbound pair of spheres (purple) makes contact. At this point the green bond is broken and a new bond is formed between the purple spheres.
  </figcaption>
</figure>
{%endcomment%}

{%comment%}
<figure id="vid_MC_move">
  <video width="650" poster="{{ "/assets/img/entropy_of_sphere_packing/MC_move_cover.png" | relative_url }}" autoplay loop muted playsinline>
    <source src="{{ "/assets/videos/entropy_of_sphere_packing/MC_move.mp4" | relative_url }}" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <figcaption data-katex>
    Demonstration of Monte Carlo move from one isostatic packing to another for a cluster of 50 particles in 2D.
  </figcaption>
</figure>
{%endcomment%}

<video
  width="650"
  muted autoplay loop playsinline
  preload="auto"
  poster="{{ '/assets/img/entropy_of_sphere_packing/MC_move_cover.png' | relative_url }}"
  onloadedmetadata="this.play().catch(()=>{});"
>
  <source
    src="{{ '/assets/videos/entropy_of_sphere_packing/MC_move.mp4' | relative_url }}"
    type="video/mp4"
  >
</video>


A key challenge in computing entropy in sphere packings is ensuring that the packing remains **mechanically stable**. Traditional Monte Carlo (MC) methods allow random displacements, but these can disrupt the isostatic nature of the packing. Instead, we introduce an **isostaticity-preserving Monte Carlo method**, where moves are constrained to preserve the number of bonds.

**Microstate Moves and Computing $$S_{\text{geo}}$$:**
{%comment%}
Each step modifies the configuration by randomly choosing a bond and increasing the bond length while remaining in equilibrium until two previously unbound spheres make contact. At this point the original bond is broken and a new bond is made at the new contact point. 
This preserves the isostaticity of the packing and allows one to explore the space of isostatic packings for $$N$$ spheres and $$NZ/2$$ bonds. When the bond length is increased it introduces a single zero mode into the system which allows the spheres to rearrange until a new isostatic configuration is found.
{%endcomment%}

A packing evolves in a $$Nd$$-dimensional space that can be represented by the positions of the $$N$$ spheres or the $$Nd$$ bond gaps. The constraints for them to be hard spheres in contact are given by <span>$$|\vec{r}_i - \vec{r}_j|^2 = \left(\frac{a_i + a_j}{2}\right)^2$$</span>. The Jacobian of this equation is the rigidity tensor, introduced above as a convenient method of calculating $$S_{\text{geo}}$$. At each step of our simulations a bond is broken and a zero mode enters into the packing. The packing then evolves in such a way that it moves orthogonal to the constraints imposed by the rigidity tensor until contact is made between two unbonded particles, and a new isostatic packing is realized. The rigidity tensor $$R(\vec{r})$$ relates the particle displacements $$\vec{u}_i$$ to the gaps between particles $$x_{ij}$$. If we consider that the bond $$\alpha$$ breaks and opens by an amount $$x_{\alpha}$$, the displacement of any particle $$i$$ can be calculated as $$\vec{u}_{i} = R^{-1}_{i,\alpha} x_{\alpha}$$. However, to avoid the computationally expensive inverse function, we instead use a QR decomposition with column pivoting from the linear algebra library *Eigen* to solve the equation for the displacements $$\vec{u}_i$$ of all particles caused by the opening of $$\alpha$$. By using the equation for $$S_{\text{geo}}$$ defined above, the distribution of $$S_{geo}$$ is computed directly.



### **Computing $$S_{\text{pack}}$$ with Virtual Particle Exchange with a Reference Packing**


<figure id="fig_packing_and_ref_lattice" style="display: flex; justify-content: center; align-items: center; gap: 15px; flex-wrap: wrap;">
  <img src="{{ "/assets/img/entropy_of_sphere_packing/vp_and_rem_2D_full.png" | relative_url }}" alt="Figure 1" style="width: 100%; max-width: 45%;">
  <img src="{{ "/assets/img/entropy_of_sphere_packing/vp_and_rem_3D_full.png" | relative_url }}" alt="Figure 2" style="width: 100%; max-width: 45%;">
  <figcaption style="text-align: center; width: 100%;">
    Examples in 2D and 3D of a packing in equilibrium with a reference lattice (reservoir) with which it can exchange particles. 
  </figcaption>
</figure>


To compute geometric and topological entropy, we propose a **thought experiment** in which a given packing is compared to a **reference packing** with a known entropy.
The simplest reference lattice is a square lattice (in 2D) or cubic lattice (in 3D), because we know $$S_{\text{geo}}=0$$ for these ordered lattices.

This all seems difficult, but, luckily, the system can be treated using equilibrium statistical mechanics.

It all comes down to detailed balance. Detailed balance states that the probability of transitioning $$A \rightarrow B$$ from state $$A$$ to state $$B$$ is balanced by the probability of transitioning $$B \rightarrow A$$:

$$
  P(A)W(A\rightarrow B) = P(B)W(B\rightarrow A),
$$
where $$P(A)$$ is the probability of being in state $$A$$, and $$W(A\rightarrow B)$$ is the transition rate between the two states.

In this case $$A$$ can be the state of the random packing have $$N$$ spheres and $$B$$ is the state of the packing having $$N-1$$ spheres after one sphere was moved to the reference lattice. If we look at <a href="#fig_packing_and_ref_lattice" data-fig-ref>??</a>, we can count the number of positions where a particle can be removed and the number of positions where a particle can be added, such that it remains isostatic. Let the number of ways to add or remove a particle from a configuration be $$N_+$$ and $$N_-$$, respectively. <a href="#fig_packing_and_ref_lattice" data-fig-ref>??</a> shows the particles that may be removed in blue and the positions where a particle may be added as a dashed circle for one particular microstate. Averaging over many microstates, $$\langle N_+ \rangle$$ is proportional to the transition rate from a packing with $$N-1$$ particles to a packing with $$N$$ particles, and similarly for $$\langle N_- \rangle$$ for the reverse transition. From detailed balance this means that the ratio of probabilities is equal to the ratio $$\frac{N_-}{N_+}$$,

$$
\frac{W_{\text{remove}}}{W_{\text{add}}} = \frac{P_{\text{pack}}(N-1)}{P_{\text{pack}}(N)} = \frac{N_-}{N_+} = \frac{\frac{e^{S_{\text{pack}}(N-1)}}{\mathcal{Z}_{pack}}}{\frac{e^{S_{\text{pack}}(N)}}{\mathcal{Z}_{pack}}} = e^{\left[S_{\text{pack}}(N-1) - S_{\text{pack}}(N)\right]} = e^{-\mu} = e^{S_{\text{pack}}}
$$

where we have approximated $$S_{\text{pack}}(N) - S_{\text{pack}}(N-1) \approx \frac{\partial S_{\text{pack}}}{\partial N} = \frac{\partial F}{\partial N} = \mu$$.

Finally, we have a way to compute $$S_{\text{pack}}$$. Really this is an indirect way of computing $$S_{\text{topo}}$$ because we know how to find $$S_{\text{geo}}$$ and $$S_{\text{topo}} = S_{\text{geo}} + S_{\text{topo}}$$.


{% comment %}
We can approximate $$S_{\text{pack}}(N) - S_{\text{pack}}(N-1) \approx \frac{\partial S_{\text{pack}}}{\partial N} = \frac{\partial F}{\partial N} = \mu$$, which leads to $$\mu = \frac{\partial (-N S_{\text{pack}})}{\partial N} = -S_{\text{pack}}$$, using $$T=1$$. Finally we find 

$$
\frac{W_{\text{remove}}}{W_{\text{add}}} = \frac{P_{\text{pack}}(N-1)}{P_{\text{pack}}(N)} = e^{S_{\text{pack}}}.
$$

If the average number of ways to add a particle to the random packing and remove a particle from the random packing is, respectively, $$\langle N_+ \rangle$$ and $$\langle N_- \rangle$$, we can define them using detailed balance as

$$
\begin{align}
N_+ &= P(N-1) W_{\text{add}} = P(N) e^{S_{\text{pack}}} W_{\text{add}} \\ 
N_- &= P(N) W_{\text{remove}}
\frac{N_+}{N_-} &= e^{S_{\text{pack}}} \frac{W_{\text{add}}}{W_{\text{remove}}} \\ 
\end{align}
$$


In equilibrium the rate of transfer of particles between the system and the reference lattice must be equal, which translates to the chemical potentials being equal $$\mu_{\text{ref}} = \mu_{\text{pack}}$$. 
In other words, the probabilities of adding a particle to the packing or removing a particle from the packing must be the same.




1. **Geometric Entropy Calculation**
   - For a given adjacency matrix $$\mathbf{\hat{C}}$$, count the number of distinct spatial configurations preserving the contacts.
   - Compute the local phase-space volume associated with each configuration using **Voronoi tessellations**.

2. **Topological Entropy Calculation**
   - Consider a virtual exchange process where individual spheres are swapped between different adjacency matrices.
   - Track how frequently these exchanges occur and use that to estimate the entropy contribution.
   - Use **persistent homology** techniques to quantify the number of distinct adjacency matrices consistent with a given $$ Z $$.

{% endcomment %}

By combining these two computations, we obtain a complete measure of entropy.



### **Summary and Future Research**
- We proposed a statistical mechanical description of sphere packings based on treating the  coordination number $$Z$$ as a macroscopic thermodynamic parameter, and  identified two contributions to the packing entropy: geometric and topological. They correspond to the statistical weight of a particular topological configuration, and the number of non-equivalent arrangements, respectively.
- An important difference of our approach is that it is built entirely within the framework of equilibrium statistical mechanics, and does not impose a requirement on the individual configurations to be jammed.
- Our results are directly applicable to systems with tensile short-range forces, such as sticky spherical colloids.
- We developed an MC scheme to compute the geometric and topological entropies of isostatic packings in both 2D and 3D.

The work has implications for:
- **Glassy Systems:**
- **Granular Media:**
- **Colloidal Assembly:**















### Links

<a href="https://doi.org/10.1103/PhysRevE.105.014117" class="info-button" target="_blank">
  <span class="icon-book" style="font-size: 32px;"></span> Geometric and Topological Entropies of Sphere Packing
</a>


<style>
  /* Remove any arrows on external links */
  .info-button::after {
    content: none !important;
  }
</style>