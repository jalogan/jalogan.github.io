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



### **Connecting to Traditional Statistical Mechanics**
In equilibrium statistical mechanics, the **partition function** $$\mathcal{Z}$$ is the fundamental quantity that encodes all thermodynamic properties of a system:

$$
\mathcal{Z} = \sum_i e^{-\beta E_i}
$$

where:
- The sum runs over all possible **microstates** \( i \).
- $$E_i$$ is the energy of the microstate.
- $$\beta = 1/k_B T$$ is the inverse temperature.

The free energy $$F$$ is related to the partition function by:

$$
F = -k_B T \ln Z.
$$

In contrast, Logan and Tkachenko define an **entropy-based partition function**:

$$
e^{N S_{\text{pack}}(Z)} = \sum_{\hat{C}} \delta(Z(\hat{C}) - Z) \frac{1}{N!} e^{N S_{\text{geo}}(\hat{C})}.
$$

This equation sums over **packing configurations** instead of energy states. Here:
- $$\hat{C}$$ is the **adjacency matrix** defining a packing topology.
- $$S_{\text{geo}}(\hat{C})$$ is the **geometric entropy** of that topology.
- $$\delta(Z(\hat{C}) - Z)$$ enforces a constraint on the **average coordination number**.
- The factorial $$1/N!$$ accounts for indistinguishable particles, similar to the Gibbs correction in traditional statistical mechanics.

### **Geometric vs. Topological Entropy: A Free Energy-Like Decomposition**
Instead of decomposing free energy as $$ F = E - TS $$, the authors define:

$$
N S_{\text{pack}} = N S_{\text{geo}} - N S_{\text{topo}}.
$$

where:
- $$ S_{\text{geo}} $$ (geometric entropy) is analogous to an **energy function**.
- $$ S_{\text{topo}} $$ (topological entropy) plays the role of an **entropy correction**.
- $$ S_{\text{pack}} $$ (packing entropy) is the total entropy accounting for both local geometric structure and global connectivity.

This formulation mirrors the **free energy decomposition** in traditional stat mech but within an entropy-driven ensemble:

| **Traditional Statistical Mechanics** | **Logan & Tkachenko Sphere Packing** |
|----------------------------|----------------------------------|
| $$ Z = \sum_i e^{-\beta E_i} $$ | $$ e^{N S_{\text{pack}}} = \sum_{\hat{C}} e^{N S_{\text{geo}}} $$ |
| $$ F = E - TS $$ | $$ N S_{\text{pack}} = N S_{\text{geo}} - N S_{\text{topo}} $$ |
| Energy $$ E $$ | Geometric entropy $$ N S_{\text{geo}} $$ |
| Temperature $$ T $$ | Implicit, ensemble-based |
| Entropy $$ S $$ | Topological entropy $$ N S_{\text{topo}} $$ |
| Free energy $$ F $$ | Packing entropy $$ N S_{\text{pack}} $$ |

### **Novel Isostaticity-Preserving Monte Carlo Methods**
A key challenge in computing entropy in sphere packings is ensuring that the packing remains **mechanically stable**. Traditional Monte Carlo (MC) methods allow random displacements, but these can disrupt the isostatic nature of the packing. Instead, the authors introduce an **isostaticity-preserving Monte Carlo method**, where moves are constrained to preserve local force balance.

1. **Microstate Moves:** Each step modifies the configuration while ensuring that all particles remain in force-balanced positions.
2. **Acceptance Criterion:** Instead of a Boltzmann weight based on energy, moves are accepted based on how they contribute to the entropy calculation.
3. **Reweighting Method:** The entropy contribution of each move is determined via a statistical reweighting scheme, analogous to **Wang-Landau sampling** in energy-based ensembles.

### **Thought Experiment: Virtual Exchange with a Reference Packing**
To compute geometric and topological entropy, the authors propose a **thought experiment** in which a given packing is compared to a **reference packing** with a known entropy. The idea is to measure how many ways a system can transition between distinct geometric configurations without changing its contact topology.

1. **Geometric Entropy Calculation**
   - For a given adjacency matrix \( \hat{C} \), count the number of distinct spatial configurations preserving the contacts.
   - Compute the local phase-space volume associated with each configuration using **Voronoi tessellations**.

2. **Topological Entropy Calculation**
   - Consider a virtual exchange process where individual spheres are swapped between different adjacency matrices.
   - Track how frequently these exchanges occur and use that to estimate the entropy contribution.
   - Use **persistent homology** techniques to quantify the number of distinct adjacency matrices consistent with a given \( Z \).

By combining these two computations, they obtain a complete measure of entropy.

### **Results and Key Insights**
- **Packing disorder contains hidden structure:** Even random packings exhibit local motifs appearing more frequently than expected.
- **Different packings with the same average coordination number can have different entropy:** The adjacency matrix structure determines entropy beyond simple coordination counting.
- **A new classification scheme for disordered packings:** Traditional metrics like packing fraction are insufficient; entropy-based classification provides deeper insight.

### **Why This Matters for Future Research**
This study lays the foundation for applying **statistical mechanics to non-equilibrium, jammed, and disordered materials**. It has implications for:

- **Glassy Systems:** Understanding configurational entropy in amorphous solids.
- **Granular Media:** Characterizing mechanically stable packings.
- **Colloidal Assembly:** Predicting self-organization in soft matter physics.

### **Final Thoughts**
Logan and Tkachenko’s work is a significant step forward in understanding entropy in disordered systems. By introducing **geometric and topological entropy** as distinct but complementary measures, they provide a framework that captures both **local and global disorder** in a way that previous methods could not. Their new simulation techniques further enhance our ability to explore and classify packings, opening the door to future research in soft matter physics, statistical mechanics, and beyond.

Next time you see a pile of stacked oranges at the store or think about how atoms arrange in a glass, remember: it’s not just about how dense the packing is, but also how its **local structure and global connectivity** contribute to the overall entropy of the system!












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