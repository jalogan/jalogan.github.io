---
layout:      project
title:       "Superposition entropy"
published:   false

#date:        2 Jan 2014
order: 9
image:
  path:      /assets/img/learned_group_symmetry_D3/hidden_space_heatmap_cover_image.png
  srcset:
    1920w:   /assets/img/learned_group_symmetry_D3/hidden_space_heatmap_cover_image.png
    960w:    /assets/img/learned_group_symmetry_D3/hidden_space_heatmap_cover_image.png
    480w:    /assets/img/learned_group_symmetry_D3/hidden_space_heatmap_cover_image.png
caption:     New interpretation of superposition as a mixing entropy
featured:    false
#related_posts: 
---


* this unordered seed list will be replaced by the toc
{:toc}




## **Why This Work Matters**

The goal of this work is to possibly expand understanding of the phenomenon of superposition in neural networks, and derive physically-motivated knobs that allow us to control it. Much work has been done on superposition, and we only hope to include a new perspective through a lens of the physics of mixtures. There are many parallels between the two fields when aligned correctly, and it feels natural to explore superposition as an entropically-driven effect. 

Below we will derive the well-known physics of mixtures of particle species but with the important distinction that each particle species is thought of as a direction in feature space in an artificial neural network (NN). The mixing of particle species then describes the idea of superposition and how a single input can become a combination of multiple features, obfuscating our ability to interpret the netowrk in human terms. This analogy naturally leads to a superposition entropy, akin to an entropy of mixing, that can be used to 

1. Quantify the amount of superposition in a layer (for a given input or overall for the layer)
2. 
3. Define a novel regularizer that has the power to control (to some extent) how much superposition emerges in training.

Along the way other connections to statistical mechanics can be made with varying importance to our understanding.

We demonstrate these ideas first with a toy NN for clarity, then with a 1-layer encoder transformer trained on single operators from the dihedral $$D_3$$ group of symmetries of the equilateral triangle. We have investigated this group already in ["Emergent dihedral symmetry in a 1-layer Transformer"](/projects/learned_group_symmetry_D3/), and it is a convenient apparatus for experimenting with our new methods. 

Building on prior superposition work that typically measures overlap via cosine similarity or informal notions of feature reuse, our framework treats superposition as a thermodynamic entropy of mixing, which immediately yields quantitative measures, theoretical bounds, stiffness, and differentiable regularizers. This perspective is complementary to existing approaches and recovers their insights, but places them into a unified physical framework.

In our demonstrations we attempt to expose and control the tradeoff between task performance and superposition, and show that significant entropy reductions are achievable at minimal performance cost.




## **Statistical Mechanics Background**

Understanding superposition in neural networks becomes clearer when placed in the language of statistical mechanics. In this section we briefly review the relevant concepts in physics and prepare the ground for the neural analogy that follows.

---

### **Microstates and Microstate Entropy**

A microstate is one of the most important concepts in statistical physics. It is a complete specification of the microscopic degrees of freedom of a system. Examples include:

- the specific spin configuration of every lattice site in a particular Ising model state,
- the precise positions and momenta of particles in a gas.

It represents a single point in phase space. The probability of finding the system in a particular microstate depends on the system and the thermodynamic variables. If a system is in thermal equilibrium with a heat bath at temperature $$T$$, the probability of occupying microstate $$m$$ is

$$
p(m) = \frac{e^{-E(m)/(k_B T)}}{Z}
$$

where $$E(m)$$ is the energy of the microstate and $$Z$$ is the partition function in that ensemble.

The Gibbs entropy

$$
S_{\text{micro}} = -k_B \sum_m p(m)\log p(m)
$$

measures how spread the probability is over all microstates:

- If all weight lies in a single microstate, then $$S_{\text{micro}} = 0$$.  
- If all $$N_m$$ microstates are equally likely, $$p(m) = 1/N_m$$, entropy is maximal $$S = k_B \log N_m$$.

The microstate entropy tells us how likely we are to find the system in any given microstate.


### **Coarse-Grained Macrostates**

One way to think of a macrostate $$M$$ is a set of microstates grouped by a macroscopic observable (energy, magnetization, particle number, etc.). An example is to select all microstates with energy in the range $$[E, E+\delta E]$$. This selects the subset of the phase space that satisfies the constraint.

The probability of macrostate $$M$$ is

$$
P(M) = \sum_{m\in M} p(m),
$$

where we only sum over microstates that satisfy the constraints (e.g., energy lies in a particular interval).

As for the microstate entropy, we can define the macrostate entropy as

$$
S_{\text{macro}} = - \sum_M P(M)\log P(M).
$$

The macrostate entropy tells us how likely we are to find the system in any given macrostate.



### **The Bipartite Matrix Generalization**

Microstates and macrostates can be seen as two sides of the same coin if we combine them into a matrix $$N_{mM}$$ that represents the stastistical weight of microstate $$m$$ in macrostate $$M$$. This matrix allows us to define all of the probabilities necessary to derive the entropies. 

The joint distribution

$$
P(m, M) = \frac{N_{mM}}{\sum_{m',M'} N_{m'M'}},
$$

gives us the probability of being in microstate $$m$$ and macrostate $$M$$.

The marginal distributions

$$
P(m) = \sum_{M'} P(m, M') = \frac{N_{m}}{\sum_{m',M'} N_{m'M'}},
$$

$$
P(M) = \sum_{m'} P(m', M) = \frac{N_{M}}{\sum_{m',M'} N_{m'M'}},
$$

where $$N_m$$ and $$N_M$$ are just sums over the row or column corresponding to $$m$$ or $$M$$, respectively. 

The conditional probability

$$
P(m|M) = \frac{P(m, M)}{P(M)} = \frac{N_{mM}}{N_M}
$$

In the canonical ensemble, considered above, the statistical weight is $$e^{-E(m)/(k_B T)}$$, and we arrive at the same formulas for entropy.

This is nothing new, it's just a convenient way to organize the information.


### **Mixing in a Single Box (Ideal Mixtures)**

Consider a box containing particle species $$i=1,\dots,C$$ with particle counts $$n_i$$ and mole fractions $$x_i = n_i / N$$.

For an ideal mixture (no interactions), the free energy of mixing is (see Appendix A)

$$
F_{\text{mix}} = k_B T N \sum_i x_i \log x_i
$$

and the entropy of mixing is

$$
S_{\text{mix}} = -k_B N \sum_i x_i \log x_i.
$$

The mixing entropy is maximal when $$x_i$$ is distributed uniformly. 
In the neural analogy we will not derive the probabilities $$p_i$$ from an explicit Hamiltonian, but we will treat them as if they were mole fractions obeying the same entropy of mixing structure.


If particle species have different inherent energies $$E_i$$, describing how easy it is for the system to introduce another particle of this type, the total energy is a sum over all particles $$\sum_i n_i E_i$$.
Minimizing the total free energy

$$
F = \sum_i n_i E_i - T S_{\text{mix}}
$$

gives the Boltzmann distribution

$$
x_i = \frac{e^{-\beta E_i}}{\sum_j e^{-\beta E_j}}
$$

Equilibrium compositions balance energetic preference against entropic spreading over species.



### **Weak Interactions: Mean-Field (Flory–Huggins Theory)**

Introducing weak (mean-field) interactions, the free energy has the additional term

$$
F_{\text{inter}} = \frac{1}{2} \sum_{i,j} \chi_{ij} n_i n_j
$$

The total free energy

$$
F = \sum_i n_i E_i - T S_{\text{mix}} + F_{\text{inter}}
$$

produces a self-consistent equilibrium condition:

$$
x_i = \frac{1}{Z} \exp\left(-\beta E_i - \beta N \sum_j \chi_{ij} x_j \right)
$$

Interactions shift equilibrium composition. 
Here the interaction matrix $$\chi_{ij}$$ penalizes or favors co-occurrence of species $$i$$ and $$j$$. In the neural setting, we will use a similar matrix to penalize or encourage co-activation of feature directions.



### **Multi-Site Mixing (Occupancy Across Compartments)**

Suppose particles don't just exist anywhere withina box, but must distribute across sites $$i = 1,\dots,D$$. 
Let $$P_i(c)$$ denote the fraction of species $$c$$ at site $$i$$---an occupancy of this species at a particular site. We define

Normalized occupancy:

$$
R_i(c) = \frac{P_i(c)}{\sum_d P_i(d)},
$$

the fraction of particles at site $$i$$ that are of particle species $$c$$,

Per-site entropy:

$$
\tilde{S}_{\text{mix}}(i) = - \frac{1}{\log C} \sum_c R_i(c)\log R_i(c),
$$

the spread in particle species found at site $$i$$. We have normalized by $$\log C$$ to keep the mixing entropy in the range $$[0, 1]$$, and the tilde signifies that it is the normalized quantity.

- If a site is dominated by a single particle species, $$R_i(c) \approx 1$$ for that species (0 for all others) and $$S_{\text{mix}}(i) \approx 0$$
- If a site has equal amounts of each particle species, $$R_i(c) \approx 1/C$$ for all species and $$S_{\text{mix}}(i) \approx 1$$.

From this we are in a position to define the total mixing entropy 

$$
\tilde{S}_{\text{total}} = \frac{1}{D} \sum_{i=1}^D \tilde{S}_{\text{mix}}(i)
$$

The total mixing entropy is the average over all sites. It measures how mixed the particle species are on average across all sites.

- If many species appear together at each site, S_{\text{total}} is high
- If each site is dominated by a single species, S_{\text{total}} is low.

This concept motivates global superposition entropy in neural networks.

<div class="aside-box">
  <div class="aside-header">Aside: Examples of multi-site mixing entropy</div>

  <div class="aside-content" markdown="1">

**Example 1:** *One particle species per site*.

Suppose all sites $$i$$ have exactly one particle species $$c$$:

$$
R_i(c)=
\begin{cases}
1, & c=c_i \\
0, & \text{otherwise}
\end{cases}
$$

Then

$$
\tilde{S}_{\text{mix}}(i)=0, \qquad
\tilde{S}_{\text{total}}=0.
$$

Each site contains a single species → zero mixing entropy.



**Example 2:** *Uniform mixing at every site*.

$$
R_i(c)=\frac{1}{C}
$$

This yields

$$
\tilde{S}_{\text{mix}}(i)=1,\qquad 
\tilde{S}_{\text{total}}=1.
$$

Each site contains all species equally $$\rightarrow$$ maximal mixing entropy.



**Example 3:** *Mixed structure*.

Let $$D=3$$ and $$C=3$$:

- Site 1: uniform mixing → $$\tilde{S}_{\text{mix}}=1$$
- Site 2: pure species → $$\tilde{S}_{\text{mix}}=0$$
- Site 3: two-way mixture $$R=(\frac{1}{2}, \frac{1}{2}, 0) \rightarrow$$ $$\tilde{S}_{\text{mix}} = \frac{\log 2}{\log 3}$$

Total normalized entropy:

$$
\tilde{S}_{\text{total}}
= \frac{1}{3}\left(1 + 0 + \frac{\log 2}{\log 3}\right)
\approx 0.54.
$$

The system is at roughly half the maximum possible mixing entropy.

  </div>
</div>









## **Mapping to Neural Networks**

We now re-interpret microstates, macrostates, particle species, and interactions in the context of neural representations.

Now that we have developed the physical framework of microstates, macrostates, mixing, and mean-field interactions, we can show how each concept maps onto neural network representations.
Every definition above finds its counterpart in network activations, features, and circuits.

At a high level:

- A **neural activation pattern** behaves like a microstate.
- An input **class-average activation signature** behaves like a macrostate.
- The **distribution of semantic features** acts like a multicomponent mixture.
- The **loss function** plays the role of a free energy functional.
- **Superposition** becomes an entropy of mixing.


### **Activations as Microstates and Local Superposition Entropy**

In a neural network layer, a single input $$x$$ produces an activation vector $$a(x)\in\mathbb{R}^D$$.

We define the neural layer microstate probabilities:

$$
p_i(x) = \frac{|a_i(x)|^n}{\sum_j |a_j(x)|^n}.
$$ 

The microstate probability weight of the neural network is the *feature occupation* pattern.

- The *particle species* is represented by the *feature direction* $$i$$
- $$p_i(x)$$ is the normalized activation in feature direction $$i$$
- The vector $$(p_1(x), p_2(x), \dots, p_D(x))$$ is the microstate distribution.

We leave the power $$n$$ in the probability mapping as a choice, depending on the work. In this work we choose to use $$n \in \{1,2\}$$. $$n=1$$ is simple absolute value normed probabilities that do not favor any particular features, while $$n=2$$ is a more physics-flavored choice, where we think of squared projections as probabilites.

The Gibbs entropy of the microstate distribution is what we call the **Local superposition entropy**

$$
\tilde{S}_{\text{local}}(x) = -\frac{1}{\log D}\sum_i p_i(x)\log p_i(x).
$$

measures how spread the activation is over all feature directions:

- If all weight lies in a single feature direction, then $$S_{\text{local}} = 0$$.  
- If all $$D$$ features are equally likely, $$p(m) = 1/D$$, and local superposition entropy is maximal $$\tilde{S}_{\text{local}} = 1$$ (or unnormalized $$S_{\text{local}} = \log D$$).

The local superposition entropy measures how many semantic features are effectively co-active for a single input.



### **Class-level Signatures: Macrostates**

In physics, a coarse-grained macrostate is a subset of microstates, defined by grouping them by some thermodynamic variable.

In neural networks, an individual input $$x$$ is not a complete representation of its input class. To better define a macrostate in neural networks, the natural analog is:

$$
P_i(c) = E_{x \in c}[p_i(x)]
$$

the average activation probability of feature $$i$$ over all examples of input class $$c$$.

The vector $$\vec{P}(c) = (P_1(c), P_2(c), \dots, P_D(c))$$ is the circuit signature of input class $$c$$ at that layer.

$$\vec{P}(c)$$ tells us how strongly class $$c$$ uses each feature direction. 

Geometrically, $$\vec{P}(c)$$ is a point in the $$D$$-dimensional feature simplex: nearby $$\vec{P}(c)$$ and $$\vec{P}(c')$$ correspond to classes that rely on similar circuits.

$$P_i(c)$$ is the analog of a macrostate probability distribution over coarse-grained states.

Microstate distribution: $$p_i(x)$$  
Macrostate distribution: $$P_i(c)$$


### **Mixing Across Sites: Global Feature Sharing (Circuit Superposition)**

In physics, mixing across lattice sites is characterized by the per-site composition:

$$
R_i(c) = \frac{P_i(c)}{\sum_d P_i(d)}
$$

the fraction of the content of site $$i$$ that comes from species $$c$$.

In the global neural analogy:

- Each feature direction $$i$$ is a lattice site.
- The input classes $$c$$ are the particle species.
- $$R_i(c)$$ measures how shared feature $$i$$ is across classes.

A concentrated feature (used mostly by one class) has low mixing entropy.  
A polysemantic feature (shared by many classes) has high mixing entropy.  

The per-feature **global superposition entropy** is then:

$$
\tilde{S}_{\text{mix}}(i) = -\frac{1}{\log C} \sum_c R_i(c)\,\log R_i(c)
$$

and the total global superposition is the average:

$$
\tilde{S}_{\text{global}} = \frac{1}{D}\sum_{i=1}^{D} \tilde{S}_{\text{mix}}(i)
$$

This quantity measures how entangled the circuits of different classes are.

Low $$S_{\text{global}}$$: distinct circuits, low polysemanticity  
High $$S_{\text{global}}$$: shared circuits, high polysemanticity  

These are direct analogs of the normalized occupancy and per-site entropy defined for multi-site mixing, now reinterpreted for superposition.

In practice, $$\tilde{S}_{\text{global}}$$ is a scalar that tells us how polysemantic the layer is as a whole: $$\tilde{S}_{\text{global}} \approx 0$$ means nearly disjoint circuits, while $$\tilde{S}_{\text{global}} \approx 1$$ means extensive sharing of features across classes.


### **Mean-Field Interactions: Superposition Regularizers**

The Flory–Huggins mean-field interaction term

$$
\frac{1}{2} \sum_{i,j} \chi_{ij}\, x_i x_j
$$

penalizes or encourages mixing of species.

The neural analog is immediate:

**Local interaction regularizer (Tier-1)**

$$
L_{\chi}^{\text{local}} = \sum_{i,j} \chi_{ij}\, p_i(x)\, p_j(x)
$$

This lets us:

- *discourage superposition* between specific features through matrix $$\chi$$  
- encourage modularity or disentangling  
- shape the learned representation geometry  

This is a local regularizer between feature interactions. It affects how the activation is distributed across the features at a layer.  
If $$\chi_{ij}$$ is nonzero, depending on the sign, it can be used to have more or less superposition between features $$i$$ and $$j$$.  


**Circuit-level interaction regularizer (Tier-2)**

Operating at the macrostate level:

{% comment %}
$$
L_{\chi}^{\text{global}} = \sum_{i,j} \chi_{ij}\, P_i(c)\, P_j(c')
$$
{% endcomment %}

$$
L_{\text{inter}}^{(2)} = \lambda_\chi^{\text{global}} \sum_{c,c'} \Gamma_{cc'} \langle P(c), P(c') \rangle
$$

$$\Gamma_{cc'}$$ lets us selectively penalize or encourage overlap between particular pairs of classes (e.g., repel the circuits for two confusing labels, or attract circuits within a semantic family).

Together with the entropy terms, these produce thermodynamically motivated knobs to control both local and global superposition.






## **Bounds and Superposition Stiffness**
Superposition is not unlimited, and must have bounds on how much the features can be entangled or disentangled. We cannot expect an arbitrary layer to have the capacity for orthogonal or near-orthogonal input class representations. This implies the existence of bounds and stiffness of superposition.  

### **Theoretical Limits**

**Local:**

$$
S_{\text{local}}(x) = -\sum_i p_i(x)\log p_i(x)
$$

Maximal when distribution over features is uniform.

- *Upper Bound:* $$S_{\text{local,max}} = \log D$$, attained for a uniform distribution over features.  
- *Lower Bound per input:* $$S_{\text{local}}(x) \ge 0$$.  
- *Layer-specific lower bound:* if the layer’s activations effectively live in an $$r$$-dimensional subspace (rank $$r$$), then the average local entropy across inputs cannot be pushed below $$\log r$$. In practice we estimate this floor using the effective rank of the activation matrix. 

When the normalized local superposition entropy $$\tilde{S}_{\text{local}}$$ is used, the bounds become $$[0, 1]$$. 

The minimum local layer-specific superposition entropy that can be achieved is exactly how many degrees of freedom we have to use. This can be computed by creating the activation matrix---a $$N_{\text{ex}} \times D$$ matrix, where each of the $$N_{\text{ex}}$$ rows is the activation vector from an input example---and finding the effective rank of the matrix using singular value decomposition or another method.



**Global:**

The unnormalized global superposition entropy 

$$
S_{\text{global}} = \frac{1}{D} \sum_{i=1}^D \left[-\sum_{c=1}^C R_i(c)\log R_i(c)\right]
$$

measures sharing of features across classes.

- *Upper Bound:* $$S_{\text{global}} = \log C$$  
- *Lower Bound:* $$S_{\text{global}} = 0$$  

When the normalized global superposition entropy $$\tilde{S}_{\text{global}}$$ is used, the bounds become $$[0, 1]$$.


### **Stiffness and Response**

In our analogy superposition entropy is the order parameter, and the loss function is the free energy functional. The regularizers defined won't always be able to separate input classes/features--there is always some restoring force or resistance to this change. This stiffness can be measured as the change in the loss given by a small change in the superposition entropy. We can even define response functions/susceptibility as the curvature.

- Let $$L_{\text{task}}$$ be the task loss (e.g., cross entropy loss) without regularizers
- $$\lambda$$ is a knob used to reduce superposition

$$
L = L_{\text{task}} + \lambda S_{\text{global}}
$$

**Stiffness:**

$$
\text{stiffness} = -\frac{dL_{\text{task}}}{dS_{\text{global}}}
$$

*Low stiffness:*
- task loss barely changes when superposition is reduced
- input classes can be separated without hurting performance. 
- this is "accidental" entanglement.  

*High stiffness:*
- task loss is large when you attempt to reduce superposition
- the model needs these classes to share circuits
- this is semantic coupling.

A high stiffness can be interpreted to mean the input classes are semantically coupled, and should not (or cannot) be disentangled. When the stiffness is low, the superposition is just an artifact of the learning and there is no true coupling between the input classes, and they can be separated (to a point). We must keep in mind that nothing is free, and separating one pair must be accounted for elsewhere.

The stiffness can be used to **discover semantic families of input classes**. Choose a pair of classes $$c, c'$$ and apply a repulsive penalty for that pair only using $$\Gamma_{cc'} > 0$$ with all other entries zero, and measure the stiffness. If the stiffness is large they share a real semantic structure. This can be repeated for all pairs creating a stiffness matrix that can be used to single out semantic families by clustering. 

**Curvature:**

$$
\kappa = \frac{d^2 L_{\text{task}}}{d S_{\text{global}}^2}
$$

While the stiffness can determine if two input classes and semantically linked, the curvature can express how strong that link is. Given two pairs of classes, the stiffnesses might be equal, but the curvature shows how fast that stiffness increases, with the strong link having a higher curvature.  

These quantify how costly it is to reduce superposition. These are exact analogs of stiffness and response functions in physics, and a model-intrinsic semantic structure measure through a thermodynamic lens.

These same ideas can be applied to local superposition to better understand feature-level entanglement. 


### **Summary of Regularizers**

#### **Local Entropy Regularizer**

$$
L_{\text{ent}}^{(1)} = -\lambda_{\text{ent}}\, S_{\text{local}}(x)
$$


#### **Local Interaction Regularizer**

$$
L_{\text{inter}}^{(1)} = \lambda_\chi \sum_{i,j} \chi_{ij} p_i(x)p_j(x)
$$


#### **Global Entropy Regularizer**

$$
L_{\text{ent}}^{(2)} = -\lambda_{\text{ent}}^{\text{global}} S_{\text{global}}
$$


#### **Global Interaction Regularizer**

$$
L_{\text{inter}}^{(2)} = \lambda_\chi^{\text{global}} \sum_{c,c'} \Gamma_{cc'} \langle P(c), P(c') \rangle
$$



### **What we mean by superposition in this work**

We follow the standard notion of superposition used in interpretability: 
many concepts (or input classes) being linearly represented in shared feature 
directions. We do *not* redefine superposition; instead we provide a new way 
to *measure* it using the entropy of mixing from statistical mechanics.

**Local superposition** $$S_{\text{local}}(x)$$ quantifies how many semantic features are co-active for a 
single input. 

**Global superposition** $$S_{\text{global}}$$ quantifies how strongly different input 
classes reuse the same features. Both become precise, scalar quantities in 
this thermodynamic framework.





## **Demonstration 1: Toy Model**

Our first demonstration of the ideas laid out above uses a simple, fully connected network 
- Input dimension 5 (one-hot classes)
- Hidden layer with dimension 2
- Output layer with dimensinon 5 features

This model was designed to mirror the physics---it returns the logits of the output layer scaled by temperature, the analog of $$-E_i / T$$, and uses them to define the loss function. The "temperature" in the neural network is really a convenient way to probe how strongly the network prefers certain features over others. At large $$T$$ the $$D$$ feature curves merge to $$1/D$$, which just tells us that if the "energy gaps" between features (how preferred they are) were made negligible, the model would learn to activate them uniformly. This has no affect on the neural network, and the operating regime of the actual model is at $$T=1$$. That said, sweeping $$T$$ gives us a clearer picture of the landscape and the relative preference of the feature space.


### **Local Superposition**

#### **Local Superposition Entropy Per Input Class**

#### **Effect of the local entropy regularizer $$\lambda_{ent}$$**


### **Feature Interactions: Local Interaction Regularizer**

#### **Including $$\chi$$ Matrix Interactions**

#### **Effects on Circuits**


### **Global Superposition**

#### **Class-Level Signatures $$P(c)$$**

#### **Normalized Occupancy and Global Superposition Entropy**


### **Circuit-Level Interaction: Global Interaction Regularizers**

#### **Including Class-Class Interaction Matrix $$\Gamma$$**


### **Do the Regularizers Ruin Model Performance?**
We see that the local and global superposition can be modified at will, to some extent, but it's only useful if doing so doesn't destroy the original model performance. 



### **Stiffness and Semantic Families**



## **Demonstration 2: Dihedral Symmetry in a 1-Layer Transformer**
This proof of principle uses a model from our previous work ["Emergent dihedral symmetry in a 1-layer Transformer"](/projects/learned_group_symmetry_D3/).

### **Local Superposition**

#### **Local Superposition Entropy Per Input Class**

#### **Effect of the local entropy regularizer $$\lambda_{ent}$$**

### **Feature Interactions: Local Interaction Regularizer**

#### **Including $$\chi$$ Matrix Interactions**

#### **Effects on Circuits**

### **Global Superposition**

#### **Class-Level Signatures $$P(c)$$**

#### **Normalized Occupancy and Global Superposition Entropy**

### **Circuit-Level Interaction: Global Interaction Regularizers**

#### **Including Class-Class Interaction Matrix $$\Gamma$$**

### **Stiffness and Semantic Families**











## **Appendix A**

**Physics of mixing**
We begin with some number $$C$$ of particle species at fixed volume and temperature. For each species there exist $$n_i$$ such particles and the total number of particles is fixed $$\sum_{i} n_i = N$$. At first we treat the gas as ideal (no interactions) and then add a weakly interacting term that will piggy-back off of the ideal gas results.

**Ideal**
If we assume ideal gases, no particles interact. Physically, because the particles have no interactions, the hamiltonian is just the kinetic energy $$H=\sum_i p^2_i / 2 m_i$$ and we use classical statistical mechanics to define the partition function as integration of $$\exp(-H / k_B T)$$ over the positions and momenta. The hamiltonian is easily separated into each particle species, so the partition function factorizes and we get a product of the single species partition function over all particle species 

$$
Z = \prod_i \frac{1}{N_i!} \left(\frac{V}{\lambda^3_i}\right)^{N_i}.
$$ 

After applying the Stirling approximation on the free energy $$F = -k_B T \log Z$$ and using $$x_i = N_i / N$$ we find the mixing free energy 

$$
F = (\text{Non-mixing terms}) + k_B T N \sum_i x_i \log x_i.
$$ 

The entropy of mixing is then easily found as $$S_{\mathrm{mix}} = -\left( \frac{\partial F_{\mathrm{mix}}}{\partial T}\right)$$,

$$
S_{\mathrm{mix}} = -k_B N \sum_i x_i \log x_i.
$$

Each particle species has an inherent energy $$E_i$$ associated with it that represents how favorable it is to have a particle of that type; lower energies are more favorable than higher. We may then define the total system energy as the sum of energies of all particles $$E = \sum_i n_i E_i$$. While $$N$$ is fixed, $$n_i$$ (and $$x_i=n_i/N$$) can change--the concetration of one type of particle may be adjusted to reach equilibrium. To find the equilibrium concentrations we first write a general free energy functional

$$
\begin{align}
F &= E - TS_{\mathrm{mix}} + \lambda \left(\sum_i n_i - N_0\right) \\ 
F &= \sum_i n_i E_i - T -k_B \sum_i n_i \log \frac{n_i}{N} + \lambda \left(\sum_i n_i - N_0\right),
\end{align}
$$

where $$E$$ is the total energy, $$T$$ is the temperature, $$S_{\mathrm{mix}}$$ is the mixing entropy (that we just derived above), $$N_0$$ is the constant number of total particles of all species, and $$\lambda$$ is a largrange multiplier that lets us enforce the constraint on the constant number of particles.

We want to minimize the free energy with respect to the particle fractions $$n_i$$.

$$
\frac{\partial F}{\partial n_i} = E_i + k_B T (\log x_i + 1) + \lambda + \mathrm{const} = 0.
$$

Rearranging and grouping terms that are constant for all $$i$$ results in

$$
x_i = \frac{e^{-\beta E_i}}{\sum_j e^{-\beta E_j}}.
$$

The fractions of each particle species at equilibrium is distributed according to the Boltzmann distribution. Lower energy particle species tend to have higher fractions or probabilities.

**Weak interactions**
We can easily push the physics to be more realistic by adding weak interactions following the the work of Flory-Huggins. A weakly interacting mean-field term in the free energy functional can be written as 

$$
F_{\mathrm{inter}} = \frac{1}{2} \sum_{i,j} \chi_{ij} n_i n_j,
$$

where $$\chi$$ is a matrix that holds the strengths of interactions between all $$i$$ and $$j$$.

This term is used to modify the free energy functional used above

$$
\begin{align}
F &= E - TS_{\mathrm{mix}} + \lambda \left(\sum_i n_i - N_0\right) + F_{\mathrm{inter}} \\ 
F &= \sum_i n_i E_i - T -k_B \sum_i n_i \log \frac{n_i}{N_0} + \lambda \left(\sum_i n_i - N_0\right) + \frac{1}{2} \sum_{i,j} \chi_{ij} n_i n_j.
\end{align}
$$

We follow the same steps and minimize the free energy functional with respect to $$n_i$$,

$$
\frac{\partial F}{\partial n_i} = E_i + k_B T (\log x_i + 1) + \lambda + N_0\sum_j \chi_{ij} x_j = 0.
$$

Solving for $$x_i$$ we find

$$
x_i = \frac{1}{Z} \exp\left(-\frac{E_i}{k_B T} - \frac{N_0}{k_B T} \sum_j \chi_{ij}x_j \right),
$$

where $$Z$$ is found using the condition $$\sum_i x_i = 1$$, as before. This is implicit in $$x_i$$ and must be solved self-consistently. This can be done by choosing a guess $$x^{(0)}_i$$ for each particle species (maybe uniform mixing $$1/C$$ for each) and plugging into the right-hand side to get the next iteration $$x^{(1)}_i$$. Check for convergence $$\vert x^{(n+1)}_i - x^{(n)}_i \vert$$. Continue until it converges below some acceptable tolerance. 




































{% comment %}
## **PHysics background: microstates, macrostates, and entropy of mixing**

Let's breakdown the physics that will be directly applied to neural networks to better understand and control superposition. 

### **Microstates**

One of the central objects in statistical mechanics is the microstate $$m$$.  
A microstate is a complete specification of the microscopic degrees of freedom of the system—for example:

- positions and momenta of all particles in a classical gas,
- spin configuration in an Ising model.

The system has a probability $$p(m)$$ of occupying microstate $$m$$.  
The Gibbs entropy is

$$
S = -k_B \sum_m p(m)\,\log p(m).
$$

This measures how spread-out the probability weight is over all microstates:

- If all weight lies in a single microstate, then $$S = 0$$.  
- If all $$N_m$$ microstates are equally likely, $$p(m) = 1/N_m$$, then

$$
S = k_B \log N_m.
$$

This entropy is defined at the finest level of description.

---

### **Macrostates**

A coarse-grained macrostate $$M$$ is a group of microstates sharing some observable property (e.g., energy, magnetization, particle number).

For example, we may define a macrostate as  
“all microstates with energy in $$[E, E+\delta E]$$.”

The probability of macrostate $$M$$ is

$$
P(M) = \sum_{m \in M} p(m).
$$

The entropy associated with the coarse-grained description is

$$
S_{\text{macro}} = - \sum_M P(M)\,\log P(M).
$$

This entropy measures how broadly the system explores macrostates, after collapsing many microstates into meaningful groups.

---

### **Mixing as a Coarse-Graining by Species**

So far, macrostates were defined by grouping microstates according to a thermodynamic variable.  
We now apply the same idea, but group microstates instead by particle species.

Suppose the system contains $$C$$ particle species.  
Let $$n_i$$ be the number of particles of species $$i$$, and let

$$
x_i = \frac{n_i}{N}
$$

be the mole fraction of species $$i$$.

Coarse-graining by composition defines a macrostate described only by the fractions $$\{x_i\}$$.  
The associated entropy of mixing is

$$
S_{\text{mix}} = - \sum_{i=1}^{C} x_i \log x_i.
$$

This is the entropy that arises when we collapse all microstates into composition-only macrostates.

This idea will directly correspond to Tier-1 local superposition.

---

### **Mixing on Multiple Sites: Bridge to Global Superposition**

Now consider a lattice with $$D$$ distinct sites.  
Each site $$i$$ contains a mixture of the same $$C$$ species.  
Let $$P_i(c)$$ be the fraction of species $$c$$ at site $$i$$.

To obtain relative occupancy per site, define

$$
R_i(c) = \frac{P_i(c)}{\sum_d P_i(d)}.
$$

The mixing entropy at site $$i$$ is

$$
S_{\text{mix}}(i)
= - \sum_{c=1}^{C} R_i(c)\,\log R_i(c).
$$

and the total mixing entropy across the lattice is

$$
S_{\text{global}}
= \frac{1}{D} \sum_{i=1}^{D} S_{\text{mix}}(i).
$$

This quantity asks:

**How shared are the lattice sites across the different species?**

In the neural analogy, this will become the global superposition entropy.




## **Mapping to Neural Networks**

The statistical mechanics framework has clean and direct analogues in neural networks once we interpret:

- microstates → individual activation patterns  
- species → semantic features  
- sites → feature directions  
- coarse-grained species distributions → input-class–averaged circuits  

This mapping yields two complementary notions of superposition: **local** and **global**.

---

### **Tier-1: Local Superposition (Microstate Entropy)**

For a given input $$x$$, let the activation vector at a particular layer be $$a(x) \in \mathbb{R}^D$$.

Choose a feature basis (e.g., via an SAE) with feature directions indexed by $$i = 1, \ldots, D$$.  
Define the per-feature probability

$$
p_i(x) = \frac{|a_i(x)|}{\sum_j |a_j(x)|}.
$$

This is the neural analogue of microstate probabilities.  
The local superposition entropy is then

$$
S_{\text{local}}(x) = - \sum_i p_i(x)\,\log p_i(x).
$$

which measures how broadly the activation of a single input spreads across the feature space.

#### Interpretation

- Low $$S_{\text{local}}$$ → activation uses few features → **interpretable**  
- High $$S_{\text{local}}$$ → activation uses many features → **polysemantic**

This mirrors microstate entropy exactly.

---

### **Tier-2: Global Superposition (Species Mixing Across Sites)**

Consider now a set of input classes (or concept classes) indexed by $$c = 1, \ldots, C$$.

For each class, average the normalized activations across many samples to obtain the class-level feature usage:

$$
P_i(c) = \mathbb{E}_{x \in \text{class } c}\, p_i(x).
$$

This is the analogue of “species fraction at site $$i$$.”

To compute mixing per feature direction, normalize across classes:

$$
R_i(c) = \frac{P_i(c)}{\sum_d P_i(d)}.
$$

The global superposition entropy per feature is then

$$
S_{\text{mix}}(i)
= - \sum_{c=1}^{C} R_i(c)\,\log R_i(c).
$$

and the layer-wide global superposition entropy is

$$
S_{\text{global}}
= \frac{1}{D} \sum_{i=1}^{D} S_{\text{mix}}(i).
$$

#### Interpretation

- Low $$S_{\text{global}}$$  
  → each feature is specialized to one class  
  → circuits are disentangled  

- High $$S_{\text{global}}$$  
  → features are heavily shared by many classes  
  → circuits are polysemantic and entangled  

This matches the multi-site species mixing entropy from statistical mechanics.












## **Theoretical background**
When a neural network is given input samples from multiple input classes the network represents the input as an activation vector at each layer. This activation vector, like any vector, can be viewed in any basis of our choosing, but if we know a feature basis--through sparse autoencoder (SAE), for example--that represents the activation vector for the input class along interpretable axes, the vector becomes a mixture of semantic features that help us interpret its meaning and function. The trouble is, different input classes will generally not be near-orthogonal and may learn very similar vectors, making interpretation and differentiation of the input classes very difficult. The idea of activation vectors mixing across feature directions is much like the mixing of different atomic species in a box or across a lattice. In the general chemistry experiment of two gases separated by a barrier, they are initially unmixed but when the barrier is removed, they begin to mix until they come to equilibrium. We believe that this simple framework can be used to quantify superposition in neural networks. 

In this work, we introduce a thermodynamic framework for neural circuit superposition based on entropy of mixing. We first go through the well-known physics and explain how it will be mirrored for neural netowrks. Next, we formalize definitions of *local* and *global* superposition and derive corresponding entropy measures, bounds on superposition, and differentiable regularizers that naturally arise from the thermodynamics. We demonstrate, using both a toy model and a small transformer, that these regularizers can be used to globally or selectively reduce superposition while preserving task performance. 


### **Physics of mixing**
We begin with some number $$C$$ of particle species at fixed volume and temperature. For each species there exist $$n_i$$ such particles and the total number of particles is fixed $$\sum_{i} n_i = N$$. We begin by treating the gas as ideal (no interactions) and then add a weakly interacting term that will piggy-back off of the ideal gas results.

#### **Ideal**
If we assume ideal gases, no particles interact. Physically, because the particles have no interactions, the hamiltonian is just the kinetic energy $$H=\sum_i p^2_i / 2 m_i$$ and we use classical statistical mechanics to define the partition function as integration of $$\exp(-H / k_B T)$$ over the positions and momenta. The hamiltonian is easily separated into each particle species, so the partition function factorizes and we get a product of the single species partition function over all particle species 

$$
Z = \prod_i \frac{1}{N_i!} \left(\frac{V}{\lambda^3_i}\right)^{N_i}.
$$ 

After applying the Stirling approximation on the free energy $$F = -k_B T \log Z$$ and using $$x_i = N_i / N$$ we find the mixing free energy 

$$
F = (\text{Non-mixing terms}) + k_B T N \sum_i x_i \log x_i.
$$ 

The entropy of mixing is then easily found as $$S_{\mathrm{mix}} = -\left( \frac{\partial F_{\mathrm{mix}}}{\partial T}\right)$$,

$$
S_{\mathrm{mix}} = -k_B N \sum_i x_i \log x_i.
$$

Each particle species has an inherent energy $$E_i$$ associated with it that represents how favorable it is to have a particle of that type; lower energies are more favorable than higher. We may then define the total system energy as the sum of energies of all particles $$E = \sum_i n_i E_i$$. While $$N$$ is fixed, $$n_i$$ (and $$x_i=n_i/N$$) can change--the concetration of one type of particle may be adjusted to reach equilibrium. To find the equilibrium concentrations we first write a general free energy functional

$$
\begin{align}
F &= E - TS_{\mathrm{mix}} + \lambda \left(\sum_i n_i - N_0\right) \\ 
F &= \sum_i n_i E_i - T -k_B \sum_i n_i \log \frac{n_i}{N} + \lambda \left(\sum_i n_i - N_0\right),
\end{align}
$$

where $$E$$ is the total energy, $$T$$ is the temperature, $$S_{\mathrm{mix}}$$ is the mixing entropy (that we just derived above), $$N_0$$ is the constant number of total particles of all species, and $$\lambda$$ is a largrange multiplier that lets us enforce the constraint on the constant number of particles.

We want to minimize the free energy with respect to the particle fractions $$n_i$$.

$$
\frac{\partial F}{\partial n_i} = E_i + k_B T (\log x_i + 1) + \lambda + \mathrm{const} = 0.
$$

Rearranging and grouping terms that are constant for all $$i$$ results in

$$
x_i = \frac{e^{-\beta E_i}}{\sum_j e^{-\beta E_j}}.
$$

The fractions of each particle species at equilibrium is distributed according to the Boltzmann distribution. Lower energy particle species tend to have higher fractions or probabilities.

#### **Weak interactions**
We can easily push the physics to be more realistic by adding weak interactions following the the work of Flory-Huggins. A weakly interacting mean-field term in the free energy functional can be written as 

$$
F_{\mathrm{inter}} = \frac{1}{2} \sum_{i,j} \chi_{ij} n_i n_j,
$$

where $$\chi$$ is a matrix that holds the strengths of interactions between all $$i$$ and $$j$$.

This term is used to modify the free energy functional used above

$$
\begin{align}
F &= E - TS_{\mathrm{mix}} + \lambda \left(\sum_i n_i - N_0\right) + F_{\mathrm{inter}} \\ 
F &= \sum_i n_i E_i - T -k_B \sum_i n_i \log \frac{n_i}{N_0} + \lambda \left(\sum_i n_i - N_0\right) + \frac{1}{2} \sum_{i,j} \chi_{ij} n_i n_j.
\end{align}
$$

We follow the same steps and minimize the free energy functional with respect to $$n_i$$,

$$
\frac{\partial F}{\partial n_i} = E_i + k_B T (\log x_i + 1) + \lambda + N_0\sum_j \chi_{ij} x_j = 0.
$$

Solving for $$x_i$$ we find

$$
x_i = \frac{1}{Z} \exp\left(-\frac{E_i}{k_B T} - \frac{N_0}{k_B T} \sum_j \chi_{ij}x_j \right),
$$

where $$Z$$ is found using the condition $$\sum_i x_i = 1$$, as before. This is implicit in $$x_i$$ and must be solved self-consistently. This can be done by choosing a guess $$x^{(0)}_i$$ for each particle species (maybe uniform mixing $$1/C$$ for each) and plugging into the right-hand side to get the next iteration $$x^{(1)}_i$$. Check for convergence $$\vert x^{(n+1)}_i - x^{(n)}_i \vert$$. Continue until it converges below some acceptable tolerance. 


### **Mapping to neural networks**
The well-established physics has now been laid out, and we just need to map it into our neural framework. The physics remains exactly the same, just the interpretation of each variable is modified. We break it into ideal and weakly interacting, just as we did above. The analog of the free energy functional is the loss function we minimize in training.

#### **Ideal**
Let's rephrase the same physics in the language of neural networks by treating the semantic features as the particle species. For an input $$x$$, the model produces an activation vector $$a(x) \in \mathbb{R}^C$$ over $$D$$ feature directions that mix to create the equilibrium state. The probabilities 

$$
p_i = \frac{e^{a_i(x)/T}}{\sum_j e^{a_j(x)/T}}
$$

are the analog of mole fractions ($$x_i$$ above), and represent the distribution of the features present in the activation vector $$a(x)$$, where for a feature direction $$f$$, $$a_i(x) = \langle f, a \rangle$$. Evidently, $$a_i(x) \rightarrow -E_i $$, and "energy" of the feature direction tells us how favorable the feature is to include in the mixture.

#### **Weak Interactions**
In reality the features do interact in some nonlinear way, and we can begin to describe this using a similar mean-field interaction term as introduced above

$$
L_{\mathrm{inter}} = \frac{1}{2} \sum_{i,j} \chi_{ij} p_i p_j,
$$

where the matrix $$\chi$$ holds the strengths of interactions between all feature pairs $$i$$ and $$j$$. We can follow the physics faithfully and define the weakly interacting feature probabilities

$$
p_i = \frac{1}{Z} \exp\left(-\frac{E_i}{T} - \frac{N_0}{T} \sum_j \chi_{ij}p_j \right).
$$


#### **Local superposition**
The above mapping naturally leads to the question of how the activation $$a(x)$$ for input $$x$$ is distributed across the features. This idea is what we call **local superposition**. If the activation is spread across many features then it is highly superposed, while if it is represented by one or very few feature directions, then it has low local superposiition. This idea is not just qualitative, but can be quantified naturally by defining the entropy of mixing in direct analogy with the physics. We define the **local superposition entropy** as

$$
S_{\mathrm{mix}} = - \sum_i p_i \log p_i.
$$

The local superposition entropy will be large when an activation is spread across many features, maximal for a uniform distribution across features, and small when the activation is specialized on one, or few, features.

### Tier-1 (Local Superposition): Mixing in One Box

| Physics Concept        | Meaning in Physics                 | Neural Analogy                   | Meaning in NN                                    |
|------------------------|------------------------------------|----------------------------------|--------------------------------------------------|
| Particle species       | Distinct types of molecules        | Feature directions $$i$$         | Semantic features of the layer                   |
| Mole fraction $$p_i$$  | Fraction of species $$i$$          | Normalized activation $$p_i(x)$$ | How much activation lies in feature $$i$$        |
| Energy $$E_i$$         | Energy of species $$i$$            | Negative logit / feature “cost”  | Lower energy → more activation                   |
| Temperature $$T$$      | Softness of Boltzmann distribution | Softmax temperature              | Degree of spread across features                 |
| Entropy of mixing      | $$-\sum_i p_i\log p_i$$            | Local superposition entropy      | Spread of a single activation across features    |
|            -           |                  -                 | $$C$$ input classes              |                         -                        |
|            -           |                  -                 | $$D$$ feature directions         |                         -                        |



#### **Global superposition**
The local superposition is concerned with a single input from one input class and how the activation vector at a layer is distrbuted across the feature directions. Another very useful perspective is a single feature is shared between the different input classes. Technically, if we have a matrix where the rows are input classes and the columns are features, local superposition looks at the distribution along one row for a single input. The global superposition can be interpreted as the transpose of this matrix; the distribution of the input classes for a single feature. It gives us a sense of how shared a feature direction is.

Previously we have described the physics analogy as a zero-dimensional mixing--just mixing of particle species in a box, where we interpret the particle species as the feature directions. The global superposition requires us to step up to a multi-compartment mixing problem. We now imagine a lattice with sites labeled by $$i$$ and occupancy of different particle species $$c$$ on each site. In our neural mapping, the particle species are the input classes, and the lattice sites are the feature directions. The different input classes distribute themselves among the feature directions, as the particles distribute themselves among the lattice sites. Before we had probabilities $$p_i$$ for the distribution of the activation vector among features, but now we have a vector $$\vec{p}_i = (p^{(1)}_i, p^{(2)}_i, \dots, p^{(C)}_i)$$ of values that describe the probability (mole fraction) of input classes along each feature direction. We first average over many input samples from a single input class and define the normalized vector $$\hat{P}(c)$$ of dimension $$D$$ representing how much input class $$c$$ occupies each feature $$i$$ on average. In some sense, this is the signature of input class $$c$$ at this layer, and this is related to the circuit defined by this input class.

We can further define the occupancy fraction

$$
R_i(c) = \frac{P_i(c)}{\sum_d P_i(d)},
$$

which tells us among all usage of feature $$i$$, how much comes from input class $$c$$. This just the other side of the coin. If we think of the matrix where each row is the signature of class $$c$$, $$\hat{P}(c)$$, then $$R_i(c)$$ is the column vector, the distribution of classes inside feature $$i$$. 

This has a natural entropy of mixing associated with it

$$
\tilde{S}_{\mathrm{mix}}(i) = \frac{-\sum_c R_i(c) \log R_i(c)}{\log C}.
$$

We have normalized this entropy of mixing by the maximum entropy, so that $$\tilde{S}_{\mathrm{mix}}(i) \in [0, 1]$$. We can average the entropy across features to obtain the **global superposition entropy**

$$
S_{\mathrm{global}} = \frac{1}{D} \sum_i \tilde{S}_{\mathrm{mix}}(i).
$$

Low $$S_{\mathrm{global}}$$, peaked $$R_i(c)$$:
  - Each feature is primarily used by a *single* input class
  - Circuits are specialized with little sharing

High $$S_{\mathrm{global}}$$, distributed $$R_i(c) \approx \frac{1}{C}$$:
  - Features are used equally be many input classes
  - Circuits are shared $$\rightarrow$$ high polysemanticity

This quantity gives a thermodynamic measure of circuit-level superposition across concept classes.


### Tier-2 (Global Superposition): Mixing Across Many Compartments

| Physics Concept            | Meaning in Physics                      | Neural Analogy                            | Meaning in NN                                          |
|----------------------------|-----------------------------------------|-------------------------------------------|--------------------------------------------------------|
| Particle species $$c$$     | Different molecule types                | Input classes $$c$$                       | Different semantic categories of inputs                |
| Lattice sites $$i$$        | Compartments or spatial sites           | Feature directions $$i$$                  | Shared representational axes                           |
| Occupancy $$P_i(c)$$       | Fraction of species $$c$$ at site $$i$$ | Class-average activation in feature $$i$$ | Circuit signature of class $$c$$                       |
| Normalized occupancy       | Fraction of species per site            | $$R_i(c)=\frac{P_i(c)}{\sum_d P_i(d)}$$   | Relative usage of feature $$i$$ by class $$c$$         |
| Entropy of mixing per site | $$-\sum_c R_i(c)\log R_i(c)$$           | Global superposition entropy per feature  | How shared each feature is across classes              |
| Total mixing entropy       | Average across all sites                | $$S_{\mathrm{global}}$$                   | Overall circuit-level polysemanticity                  |
|              -             |                     -                   | $$C$$ input classes                       |                            -                           |
|              -             |                     -                   | $$D$$ feature directions                  |                            -                           |



#### **Regularizers, stiffness, theoretical limits**
Discuss the new regularizers this method introduces, how a definition of stiffness falls out of it, and theoretical minima and maxima definitions of superposition entropy.




## **Toy model**





## **Applying to small group theoretic transformer model**










## **Notes**

Things to note:
- When we penalize the superposition between two features using the interaction regularizer, we necessarily increase superposition elsewhere. THe regularizer penalizes superposition between a pair $$i$$ and $$j$$, and reduces $$p_i p_j$$, but the constraint $$\sum p_i = 1$$ must hold, and implies redistribution of probability.
- The space is finite and features cannot all be made orthogonal, so there is no way to completely remove superposition. This implies the existence of a minimum superposition possible for the model (or layer, etc.). We can compute this minimum superposition and maybe use it as a normalizing factor.
- Using multiple nonzero values in the interaction matrix (chi) can lead to complicated non-linear effects. We are asking $$i$$ to maybe penalize superposition with multiple other features and may not be possible, so there becomes a tension as change in one pair influence others. The network will try to satisfy all parts of the loss function, but may struggle. This could lead some features to collapse and go to zero probability and others to become hubs. Some operators could reorganize their circuits and the results may not be totally predictable and may not lead to the desired outcome.
- Direct physics analogy (really just equilibrium stat mech). 
  Given an activation vector h for a layer:
  - Energy: (negative) components of h projected onto each feature vector $$<f_i|h> = z_i$$
  - mole fraction (fraction of mixture--probability): softmax of z_i/T. This is just the Boltzmann distribution in the Canonical ensemble.
  - Temperature: This is really a probe and not a know to be used in practice (set to 1). Sweep T to look at the energy landscape, visualize mixing of features, etc.
  - microstate/macrostate: Each individual feature activation (for a single input) is a microstate--a complete configuration of the system. Observables and probabilities are defined over the ensemble of microstates. The SAE-projected vector $$p_i(x,g)$$ for a single input triangle x and opeator g in group NN. Each input x gives a different activation pattern (different microstate). We end up with a set of microstates which when averaged over allows us to define the macrostate, $$P_i = E[p_i(x,g)]$$.
  - Partition function: softmax of z_i/T.
  - Entropy of macrostate: This IS the superposition entropy of an operator in the Group NN model, S = - \sum P_i log P_i
  - Ensemble of activations: canonical ensemble. The input sampling over traingles in Group NN model is identical to sampling microstates from an ensemble. The operator superposition entropy is the thermodynamics entropy of a canonical ensemble where each microstate is a feature-activation pattern induced by operator g. And the interaction regularizer is a mean-field interaction term.
  - Superposition idea is: 
    - scalar
    - interpretable
    - universal
    - architecture agnostic
    - compatible with SAEs
    - trains with gradients
    - has a meaningful lower bound
    - has direct physics interpretation
    - The idea of minimum is like Carnot efficiency limit. It allows comparison between models. 
    - the interaction regularizer is a mean-field thermodynamic regularizer that targets specific feature pairs. It could be used to:
      - disentable circuits
      - force modularity
      - intentially shape representations
- We must separate between 
  - local superposition (tier 1): Superposition of a single input class. Tells us how spread out a input is across the semantic features.
  - global superposition (tier 2): Superposition of many input classes with each other. Tells us how much circuits overlap for different input types.
- There are times when two input classes naturally point in a similar direction in feature space or MUST contain a large component of some feature directions.
  For instance, if two input classes are "bird's wing" and "bee's wing" and a feature direction is interpreted as the concept of flight, then they both MUST maintain
  a large component in that direction. This is good and correct, and our superposition entropy naturally preserves this. This leads to the concept of 
  superposition entropy stiffness.
- Global superposition entropy stiffness: if two input classes are entangled, but are not semantically related they will be easy to separate using our global superposition
  entropy regularizers. This means that the loss function term for global superposition entropy \lambda_chi * S_super (or \lambda_ent * S_super^local) will decrease and the standard
  loss function task loss term L_task that is trying to make the model correct (cross entropy in this case) will not change much. If, however, we try to decrease \lambda_chi * S_super
  and it leads to a large increase in L_task, then we're sacrificing the correctness of the model to separate these input classes and they will fight each other in the loss
  function, meaning there is a nonzero stiffness that increases dramatically when two input classes are naturally semantically connected (bird's wing and bee's wing being in the flight family).
  This leads to another natural way of discovering families of input classes or concepts. The stiffness in this way can be though of as the negative derivative of the task loss (cross-entropy) with
  respect to the global superposition entropy: stiffness = - dL_task / dS_super. In this case, small stiffness means it's easy to change and probably correct because L_task doesn't fight S_super.
  stiffness = how much task loss you pay per unit decrease in superposition entropy. Entropy is the natural order parameter and stiffness is the curvaturve of the task loss around it. This is the
  same as many physics concepts of how much free energy does it cost to change the order parameter. 
- Superposition entropy tell us how mixed things are, superposition entropy stiffness tells us how connected concepts are (is the superposition accidental or real).
- If we do a second derivative of L_task wrt S_super (free energy vs order parameter) we get a response function. It can tell us about phase transitions in this space.


Local Superposition:

Physics:
System: A box containing multicomponent mixture
Species: molecule types $$i = 1\dots K$$
Energy: per-species energy $$E_i$$
Temperature: controls how sharply the system prefers low-energy species
Mole fractions: $$x_i = \frac{e^{-E_i/T}}{\sum_j e^{-E_j/T}}$$
Entropy of mixing: $$S = -\sum_i x_i \log x_i$$
Interactions from Flory-Huggins: $$E_{int} = \frac{1}{2} \sum_{i,j} \chi_{ij} x_i x_j$$
Free energy: $$F = \sum_i x_i E_i + \frac{1}{2} \sum_{i,j} \chi_{ij} x_i x_j + T \sum_i x_i \log x_i$$

NN:
System: One input class into a specific layer
Species: Features $$i$$, neurons, SAE directions, basis vectors
Energy: negative of the activation magnitude (higher activations = lower energies)
Temperature: probing parameter that controls how concentrated or diffuse the softmax distribution is.
Mole fractions: Defined the same but called $$p_i$$, now show distribution of input class over features
Local superposition entropy: Defined the same, Measures how many features are co-active for a single input (high = more features active)
Interactions: Defined the same, penalize or encourage co-activation of features $$i$$ and $$j$$
Free energy (Loss function): $$L = CE - \lambda_{ent} S_{local} + \lambda_{\chi} \sum_{i,j} \chi_{ij} p_i p_j$$



Global Superposition:

Physics:
System: Set of boxes (lattice sites) indexed by $$i$$
Species: Distinct chemical species now correspond to input classes $$c = 1, \dots, C$$
Energy:
Temperature:
Mole fraction:
Occupancy: FOr each container, the concentration of species $$c$$ is $$R_i(c) = \text{fraction of container i's contents that coe from species c}$$
Entropy of mixing: Defined the same using $$R_i(c)$$ instead of $$p_i$$ or $$x_i$$
Total entropy: $$S_{global} = \frac{1}{K} \sum_{i=1}^K S_{mix}(i)$$
Interactions:
Free energy:

NN:
System:
Species:
Energy:
Temperature:
Mole fraction:
Entropy of mixing:
Interactions:
Free energy:

{% endcomment %}