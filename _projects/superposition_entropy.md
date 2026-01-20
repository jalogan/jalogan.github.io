---
layout:      project
title:       "Participation Ensembles (In Progress)"
subtitle:    "A Statistical Framework for Interpretable Neural Representations"
header_title: "Participation Ensembles"
header_subtitle:    "A Statistical Framework for Interpretable Neural Representations"
published:   true

#date:        2 Jan 2014
order: 10
image:
  path:      /assets/img/superposition_entropy/cover_image2_cropped.png
  srcset:
    1920w:   /assets/img/superposition_entropy/cover_image2_cropped.png
    960w:    /assets/img/superposition_entropy/cover_image2_cropped.png
    480w:    /assets/img/superposition_entropy/cover_image2_cropped.png
caption:     A Statistical Framework for Interpretable Neural Representations
featured:    false
#related_posts: 
---


* this unordered seed list will be replaced by the toc
{:toc}




## **Why This Work Matters**
The goal of this work is to organize interpretability quantities important for analyzing neural networks (NNs) by developing a unified object $$\mathcal{N}$$. This object combines events and mechanisms---input examples and cmoponents of a neural network in its most basic form---and allows for easy derivation of superposition, polysemanticity, interactions, and entropies. Using this framework entropies derived from dual conditional distributions give measurable superposition and polysemanticity, combining interactions and signature similarity distinguishes redundant vs complementary circuits. The entropies and interactions become targets for regularization, which enables controlled shaping of the internal circuits. We derive physically-motivated knobs that allow us to control such quantities and we hope to include a new perspective through a lens of physics. There are many parallels between the two fields when aligned correctly, and it feels natural to explore superposition as an entropically-driven effect. 


## **Motivating Example: A Unified Statistical Framework**
<div class="toggle-content" markdown="1">
We begin with a minimal motivating example designed to illustrate the core statistical structure underlying superposition, feature reuse, and interactions. The example is intentionally small and fully explicit, allowing all quantities to be computed exactly by hand. No learning or neural network assumptions are made at this stage; the goal is to expose the mechanics of the framework in their simplest form.

---

### **Example System**
Consider a system with a finite set of event group labels $$m$$ and a finite set of mechanisms $$M$$, which would be considered microstates and macrostates in physics. At this stage, these labels carry no semantic meaning and are only used to index the system. We will later interpret events as input examples or groupings of input examples and mechanisms as scalar values measured at components of a neural network, respectively.

We define:

- **Event groups**<br>
$$m \in \{m_0, m_1, m_2, m_3\}$$<br>
- **Mechanisms**<br>
$$M \in \{A, B, C\}$$

---

### **The Primitive Object $$\mathcal{N}$$**
The sole primitive object of the framework is a non-negative matrix of statistical weights with elements $$\mathcal{N}_{mM}$$, which quantifies the statistical weight associated with the joint occurrence of event $$m$$ and mechanism $$M$$. Importantly, $$\mathcal{N}$$ is not assumed to be normalized, probabilistic, or exclusive.

$$
\mathcal{N} = \,
\begin{array}{c|ccc}
      & A & B & C \\
\hline
m_0 & 4 & 0 & 0 \\
m_1 & 2 & 2 & 0 \\
m_2 & 0 & 3 & 1 \\
m_3 & 1 & 1 & 2
\end{array}
$$

$$\mathcal{N}$$ defines an ensemble of joint pairs $$(m, M)$$. The ensemble consists of all event-mechanism pairs, weighted by their statistical weights $$\mathcal{N}_{mM}$$. 

---

### **Joint Distribution**
All probabilistic structure is induced by a single normalization step. Defining 

$$
Z = \sum_{m,M} \mathcal{N}_{mM},
$$ 

we may obtain a joint distribution 

$$p(m, M) = \frac{\mathcal{N}_{mM}}{Z},$$ 

from which all subsequent quantities follow.

$$
p(m,M) = \,
\begin{array}{c|ccc}
      & A & B & C \\
\hline
m_0 & \frac{1}{4} & 0 & 0 \\
m_1 & \frac{1}{8} & \frac{1}{8} & 0 \\
m_2 & 0 & \frac{3}{16} & \frac{1}{16} \\
m_3 & \frac{1}{16} & \frac{1}{16} & \frac{1}{8}
\end{array}
$$

<div class="aside-box">
  <div class="aside-header">Ideal paramagnet</div>

  <div class="aside-content" markdown="1">

A simple example from physics would be an ideal paramagnet.

- **Microstates**<br>
Two non-interacting spins: $$m \in \{\uparrow \uparrow, \uparrow \downarrow, \downarrow \uparrow, \downarrow \downarrow\}$$
- **Macrostates**<br>
Total magnetization: $$M \in \{+2, 0, -2\}$$

$$
\mathcal{N}_{mM} = 
\begin{cases}
e^{-\beta E(m)}, & M = M(m) \\ 
0,               & \text{otherwise}
\end{cases}
$$

$$
Z = \sum \limits_{m,M} \mathcal{N}_{mM}
$$

$$
p(m,M) = \frac{\mathcal{N}_{mM}}{Z}
$$

This has the exact same structure as a joint distribution over events and mechanisms. 

This is a special case where each microstate contributes weight to only one macrostate. The framework does not require this, and $$\mathcal{N}$$ may have multiple nonzero entries per row.

  </div>
</div>


---

### **Marginal Distributions**

The marginal distributions are defined in the usual way as a function of the joint distribution

$$
\begin{aligned}
p(m) &= \sum\limits_{M'} p(m,M') = \frac{1}{Z} \sum\limits_{M'} \mathcal{N}_{mM'} \\ \\ 
p(M) &= \sum\limits_{m'} p(m',M) = \frac{1}{Z} \sum\limits_{m'} \mathcal{N}_{m'M}.
\end{aligned}
$$

$$p(m)$$ represents how much statistical weight event $$m$$ contributes to the ensemble. 

$$
p(m) = \,
\begin{array}{c|c}
m_0 & \frac{1}{4} \\
\hline
m_1 & \frac{1}{4} \\
\hline
m_2 & \frac{1}{4} \\
\hline
m_3 & \frac{1}{4}
\end{array}
$$

In this example, each event contributes equally.

$$p(M)$$ represents how used each mechanism is across the ensemble.

$$
p(M) = \,
\begin{array}{c|c|c}
      A & B & C \\
\hline
\frac{7}{16} & \frac{6}{16} & \frac{3}{16}
\end{array}
$$

This shows:
- $$A$$ is the most frequently used
- $$B$$ is used almost as much as $$A$$
- $$C$$ is rarely used

---

### **Conditional Distributions**

#### **Superposition**
Conditioning on a fixed event yields a distribution over mechanisms,

$$
p(M|m) = \frac{\mathcal{N}_{mM}}{\sum\limits_{M'} \mathcal{N}_{mM'}}.
$$

This distribution characterizes how representational mass is spread across mechanisms for a given event, and provides a natural notion of *superposition*.

$$
p(M|m) = \,
\begin{array}{c|ccc}
      & A & B & C \\
\hline
m_0 & 1.0 & 0.0 & 0.0 \\
m_1 & 0.5 & 0.5 & 0.0 \\
m_2 & 0.0 & 0.75 & 0.25 \\
m_3 & 0.25 & 0.25 & 0.5
\end{array}
$$

From the perspective of $$\mathcal{N}$$, we just divide each row by the sum of all elements in that row.

This shows:
- $$m_0$$ is completely in $$A$$
- $$m_1$$ is evenly spread between $$A$$ and $$B$$
- $$m_2$$ is mostly in $$B$$
- $$m_3$$ is spread across all three mechanisms


#### **Polysemanticity**
Conversely, conditioning on a fixed mechanism yields a distribution over events,

$$
p(m|M) = \frac{\mathcal{N}_{mM}}{\sum\limits_{m'} \mathcal{N}_{m'M}}.
$$ 

This dual conditional perspective captures the degree to which a given mechanism is reused across different events, a notion referred to as polysemanticity if the mechanisms are features.

$$
p(m|M) = \,
\begin{array}{c|ccc}
      & A & B & C \\
\hline
m_0 & \frac{4}{7} & 0 & 0 \\
m_1 & \frac{2}{7} & \frac{1}{3} & 0 \\
m_2 & 0 & \frac{1}{2} & \frac{1}{3} \\
m_3 & \frac{1}{7} & \frac{1}{6} & \frac{2}{3}
\end{array}
$$

From the perspective of $$\mathcal{N}$$, we just divide each column by the sum of all elements in that column.

This shows:
- $$A$$ is selective, dominated by $$m_0$$
- $$B$$ is broadly reused $$m_1$$ and $$m_2$$
- $$C$$ is mainly used by $$m_3$$ with some contribution from $$m_2$$

Superposition and polysemanticity are distinct properties, but both arise from the same joint distribution.

---

### **Entropies**
The spread of these conditional distributions can be quantified using Shannon entropy $$H$$. The entropies introduced here are not new definitions, but standard conditional entropies applied to distributions induced by the same underlying object.

#### **Superposition entropy (input-centric)**

$$
H(M|m) = -\sum\limits_{M} p(M|m) \log p(M|m)
$$

$$
H(M|m) = \,
\begin{array}{c|c}
m_0 & 0.0 \\
\hline
m_1 & \log 2 \approx 0.69 \\
\hline
m_2 & 0.56 \\
\hline
m_3 & 1.04
\end{array}
$$

This shows:
- $$m_0$$ is perfectly disentangled
- $$m_3$$ is highly superposed


#### **Polysemanticity entropy (feature-centric)**

$$
H(m|M) = -\sum\limits_{m} p(m|M) \log p(m|M)
$$

$$
H(m|M) = \,
\begin{array}{c|c|c}
      A & B & C \\
\hline
0.96 & 1.01 & 0.64
\end{array}
$$

This shows:
- $$A$$ is relatively polysemantic
- $$B$$ is broadly used--most polysemantic
- $$C$$ specific but not exclusive


#### **Global mechanism entropy (feature-usage)**

$$
H(M) = -\sum\limits_{M} p(M) \log p(M)
$$

For this example,

$$
-p(M)\log p(M) = \,
\begin{array}{c|c|c}
      A & B & C \\
\hline
0.36 & 0.37 & 0.31
\end{array}
$$

$$
H(M) = 1.04.
$$

The maximum $$H(M)$$ possible in this example is $$\log 3 \approx 1.1$$, so the computed value is high, and tells us that the usage is spread almost evenly across all mechanisms. 

The entropies above quantify how mechanisms are distributed individually. We now turn to correlations between mechanisms, which are not captured by entropy alone.

---

### **Interactions**
While conditional entropies capture how features are distributed across events and vice versa, they do not describe correlations between mechanisms themselves. To probe whether features tend to co-occur or avoid one another across the ensemble, we introduce pairwise co-usage statistics $$C_{MN}$$ derived from the same joint distribution

$$
C_{MN} = \sum\limits_m p(m) \, p(M|m) \, p(N|m),
$$

and the interaction $$\chi_{MN}$$

$$
\chi_{MN} = \log \frac{C_{MN}}{p(M)p(N)}.
$$

If the mechanisms are assigned independently with no knowledge of each other it is the ideal case $$C_{MN}^{\mathrm{ideal}} = p(M)p(N)$$, which provides a useful normalization.

For all pairs of mechanisms,

$$
C = \,
\begin{array}{c|ccc}
      & A & B & C \\
\hline
A & 0.33 & 0.08 & 0.03 \\
B & 0.08 & 0.22 & 0.08 \\
C & 0.03 & 0.08 & 0.08
\end{array}
$$

Because $$C$$ tells us the probability of co-occurrence of two mechanisms within an event: 
- Large $$C_{MN}$$: mechanisms $$M$$ and $$N$$ tend to appear together within the same event
- Small $$C_{MN}$$: mechanisms $$M$$ and $$N$$ tend to avoid each other within the same event

$$
\chi = \,
\begin{array}{c|ccc}
      & A & B & C \\
\hline
A & 0.54 & -0.74 & -0.97 \\
B & -0.74 & 0.44 & 0.11 \\
C & -0.97 & 0.11 & 0.80
\end{array}
$$

- $$\chi_{MN} > 0$$: mechanisms $$M$$ and $$N$$ prefer to co-occur--form a mechanism family
- $$\chi_{MN} < 0$$: mechanisms $$M$$ and $$N$$ avoid each other
- $$\chi_{MN} = 0$$: mechanisms $$M$$ and $$N$$ occur exactly as if they were independent


#### **Redundancy and Complementarity**
If we use the the $$p(m|M)$$ and $$\chi$$ metrics together, we can determine if two mechanisms are redundant or complementary of each other. 

If $$\chi_{MN} > 0$$, the mechanisms co-occur, but if in addition:
- $$p(m\vert M) \approx p(m\vert N)$$: the mechanisms are used in the same events.  
  This is a case of $$M$$ and $$N$$ are doing the same job. It is an overcomplete representation---possible candidates for pruning or merging.

- $$p(m\vert M) \not\approx p(m\vert N)$$ (but possibly overlapping): the mechanisms appear together but each carries distinct information.


---


### **Example Summary**
This example demonstrates that superposition, polysemanticity, and feature interactions arise as complementary projections of a *single* normalized participation matrix. No additional assumptions are required beyond the initial choice of $$\mathcal{N}$$.
</div>


## **Mapping to Neural Networks**
<div class="toggle-content" markdown="1">
The motivating example in the previous section laid out the general construction. Now we will formalize this construction in the context of artificial neural networks (NNs) and show how the same statistical object arises naturally from NN activations, and how the quantities defined above can be used to analyze learned representations.

One of the beautiful consequences of this framework is that what we call the event-mechanism pair, as outlined above, can be any degrees of freedom that carry information through the NN. The framework does not prescribe what constitutes the conjugate pair, *input* and *internal mechanism*, such as input classes and features. It provides a **statistical lens** for analyzing joint structure between any two sets of objects. We outline some examples below, with the canonical mapping being the most natural, and others perhaps more useful for LLMs and NNs with more diverse elements.


### **The Primitive Object $$\mathcal{N}$$**

As in the motivating example, we want to define a non-negative matrix of statistical weights of events $$e \in \mathcal{E}$$ as rows and mechanisms or components from which we collect measurements as columns $$M \in \mathcal{M}$$. An event is a single observation over which statistics are accumulated. This is commonly a single input example, but could also be a token or something else depending on the NN. A mechanism or component is any reusable internal component that produces a scalar contribution for each event. Common examples of mechanisms are a single neuron, SAE feature, attention head, circuit, appropriately aggregated.

$$
\mathcal{N}_{eM} = f(e;M) \geq 0,
$$

where $$f$$ is a chosen transformation on the raw measurements to ensure they are non-negative, monotonic, and align with the task at hand. For a measurement $$a$$, some common forms of $$f$$ might be $$\vert a \vert^p$$ with $$p=1,2$$ when interested in contribution strength, $$\vert \vert h_M(e) \vert \vert^2$$ when mechanisms are vector-valued and you want it to be energy-like, $$\exp({a})$$, or any other choice that best highlights what you want to interpret. Different choices of $$f$$ correspond to different measurement lenses, but all downstream quantities are computed identically once $$\mathcal{N}$$ is fixed. Recall, $$\mathcal{N}$$ is not normalized or probabilistic. 


#### **Grouping**

$$\mathcal{N}_{eM}$$ is the finest collection of data; nothing has been washed away or coarse-grained. We have a row for every event, which creates a very large matrix. In some settings, it is useful to aggregate events into groups (e.g., classes, tasks, symmetry elements, or discovered clusters). Grouping is a many-to-one map $$e \rightarrow m(e)$$,

$$
\mathcal{N}_{mM} = \sum\limits_{e \in m} \mathcal{N_{eM}}.
$$

$$\mathcal{N}_{mM}$$ is coarse-grained to discard intra-group variation. We can always go back to $$\mathcal{N}_{eM}$$ and coarse-grain in other ways to probe different ensembles, or we can use $$\mathcal{N}_{eM}$$ without any coarse-graining. 

#### **Normalization**

Any time a new $$\mathcal{N}$$ is created, whether coarse-grained to some ensemble $$\mathcal{mM}$$ or with full detail $$\mathcal{N}_{eM}$$, we must normalize it to make it probabilistic. We do this using the partition function 

$$
Z = \sum\limits_{m,M} \mathcal{N}_{mM},
$$

where $$m=e$$ when $$\mathcal{N}_{eM}$$ is used. 

This leads to the joint distribution

$$
p(m, M) = \frac{\mathcal{N}_{mM}}{Z},
$$

and from here all other quantities, per-event superposition $$p(M\vert m)$$, global mechanism usage $$p(M)$$, superposition entropy $$H(M\vert m)$$, polysemanticity conditional $$p(m\vert M)$$, interaction matrix $$\chi_{MN}$$.

All quantities studied in this work are functionals of a single nonnegative event–mechanism weight matrix. Groupings and labels are optional coarse-grainings applied only when interpretability requires them.


### **Canonical Mapping**

The most immediate choice that comes to mind when grouping events and choosing mechanisms that are useful quantities in NNs is

- **Events**<br>
$$e$$: inputs/tokens<br>
- **Event Grouping**<br>
$$m$$: input classes/concepts/labels<br>
- **Mechanisms**<br>
$$M$$: internal mechanisms (neurons at layer $$\ell$$, attention heads, SAE features, circuits, etc.)

This mapping does not introduce a new object; it corresponds to a particular choice of event grouping and interpretation of the same underlying event–mechanism weight matrix $$\mathcal{N}$$. This grouping is one interpretive coarse-graining of the events. 

This is an obvious choice when events are naturally grouped by classes or concepts, e.g., representation of a symmetry group where each event has a single group transformation associated with it.

The mechanisms (NN components) can be as simple as the neurons in a single layer, or more complex like aggregated output from attention heads. Whatever the mechanisms are, the framework quantifies the superposition, polysematicity, usage, etc. across them.

Because both “events” and “mechanisms” are abstract indices, superposition and polysemanticity can be defined at any level of description: tokens, sequences, tasks, neurons, heads, features, or circuits.

With this grouping the dictionary of quantities has the following interpretations:

**Probabilities**<br>
&emsp;$$p(m, M)$$: The total statistical weight associated with mechanism $$M$$ when representing inputs in grouping $$m$$ <br>
&emsp;$$p(M)$$: Usage frequency of mechanism $$M$$<br>
&emsp;$$p(m)$$: How much weight each input class contributes<br>
&emsp;$$p(M|m)$$: Measure of *input grouping superposition* across mechanisms---distribution of mechanisms used to represent a given input grouping. This can also be seen as the *average circuit footprint* for input grouping $$m$$.<br>
&emsp;$$p(m|M)$$: Measure of *mechanism polysemanticity* across input groupings---distribution of inputs that use a given mechanism. This can also be seen as a *mechanism signature* across events or input groupings.<br>

Superposition and polysemanticity are intimately related through one interpretation and its dual. Here we label $$p(M\vert m)$$ as a *input grouping superposition* measure and $$p(m\vert M)$$ as a *mechanism polysemanticity* measure, but in the dual view $$p(M\vert m)$$ is seen as a *input grouping polysemanticity* measure and $$p(m\vert M)$$ as a *mechanism superposition* measure. They are one set of computations, but the meaning depends on interpretation. 

**Entropies**<br>
&emsp;$$H(M|m)$$: *Superposition entropy*---how many of the mechanisms are mixed in the representation of a given input grouping<br>
&emsp;&emsp;Low: *disentangled* representation<br>
&emsp;&emsp;High: *highly entangled* superposition<br>
&emsp;$$H(m|M)$$: *Polysemanticity entropy*---how broadly a mechanism is reused across input groupings<br>
&emsp;&emsp;Low: selective mechanism<br>
&emsp;&emsp;High: polysemantic mechanism<br>
&emsp;$$H(M)$$: How evenly mechanisms are used overall<br>
&emsp;&emsp;Low: few mechanisms dominate<br>
&emsp;&emsp;High: balanced representation across mechanisms
&emsp;$$H(m)$$: How evenly groupings are used overall<br>
&emsp;&emsp;Low: few events/groupings dominate<br>
&emsp;&emsp;High: balanced representation across events/groupings

We distinguish local superposition, quantified by $$H(M\vert m)$$, from global superposition, quantified by $$H(M)$$. The former measures how distributed individual representations are, while the latter measures how evenly mechanisms are used across the entire dataset.

**Interaction Metrics**<br>
&emsp;$$C_{MN}$$: How often two mechanisms appear together with the same input grouping<br>
&emsp;$$\chi_{MN}$$: How often mechanisms appear together compared to if they are fully independent<br>
&emsp;&emsp;Positive: mechanisms form a family (appear together often)<br>
&emsp;&emsp;Negative: mechanisms compete or are exclusive<br>
&emsp;&emsp;Zero: mechanisms are independent

**Redundancy and Complementarity**<br>
&emsp;$$\chi_{MN} > 0$$ and $$p(m|M)\approx p(m|N)$$ (distributional similarity: small KL or JS divergence): the two mechanisms are doing the same job<br>
&emsp;$$\chi_{MN} > 0$$ and $$p(m|M)\not\approx p(m|N)$$: the two mechanisms form part of a circuit

Complementary mechanisms form **distributed circuits**. They are co-active, but they specialize in different aspects of the input structure. This cannot be inferred from interaction strength alone. It must be a combination of interaction strength and comparison of mechanism signatures $$p(m\vert M)$$. 

*Looking forward:*<br>
Because all of these quantities are functionals of $$\mathcal{N}$$, they can be directly targeted by regularizers during training, allowing superposition, polysemanticity, and circuit structure to be shaped in a controlled and interpretable way.

The quantities defined above characterize the static structure of a representation. In the following sections, we introduce regularizers and response measures, such as stiffness and curvature, to study how this structure changes under controlled perturbations.


{% comment %}
### **Dual Mapping**

The dual view corresponds to reinterpreting the same joint distribution by swapping the roles of conditioning. Rather than asking which mechanisms represent a given input grouping, we ask how input groupings distribute across mechanisms. No new grouping or measurement is introduced, only the interpretation of conditionals changes.

Mathematically there are many overlaps between the canonical and dual views. They share the same joint distribution, $$p(m\vert M)_{\text{canonical}} = p(M\vert m)_{\text{dual}}$$, $$p(M\vert m)_{\text{canonical}} = p(m\vert M)_{\text{dual}}$$, by design. However, our interpretations tend to shift and so it's worthwhile going through the dictionary once again.

**Events**<br>
$$e$$: inputs/tokens
**Event Grouping**<br>
$$m$$: input classes/concepts/labels<br>
**Mechanisms**<br>
$$M$$: internal mechanisms (neurons at layer $$\ell$$, attention heads, SAE features, circuits, etc.)

**Probabilities**<br>
&emsp;$$p(m, M)$$: How much does this feature belong to the circuit of input class $$M$$<br>
&emsp;$$p(M)$$: How dominant is the input class or concept $$M$$ internally<br>
&emsp;$$p(m)$$: How much weight a feature contributes across all input classses<br>
&emsp;$$p(M|m)$$: Which input classes does this feature contribute to<br>
&emsp;$$p(m|M)$$: Which features make up this input class (circuit signature)

**Entropies**<br>
&emsp;$$H(M|m)$$: *Polysemanticity entropy*---how spread a feature is across input classes<br>
&emsp;&emsp;Low: feature used by few input classes<br>
&emsp;&emsp;High: polysemantic feature<br>
&emsp;$$H(m|M)$$: *Superposition entropy*---how spread the input class representation is across features<br>
&emsp;&emsp;Low: *disentangled* representation<br>
&emsp;&emsp;High: *highly entangled* superposition<br>
&emsp;$$H(M)$$: How evenly input classes are used overall<br>
&emsp;&emsp;Low: *concept collapse*---few input classes/concepts dominate<br>
&emsp;&emsp;High: *conceptually diverse*---balanced representation across input classes/concepts

**Interaction Metrics**<br>
&emsp;$$C_{MN}$$: *circuit overlap*---how often two input classes overlap internally<br>
&emsp;$$\chi_{MN}$$: circuit overlap compared to independent input classes/concepts<br>
&emsp;&emsp;Positive: concepts share circuit structure<br>
&emsp;&emsp;Negative: concepts have separate circuit structure<br>
&emsp;&emsp;Zero: concepts are independent from each other

**Redundancy and Complementarity**<br>
&emsp;$$\chi_{MN} > 0$$ and $$p(m|M)\approx p(m|N)$$ (distributional similarity: small KL or JS divergence): The two input classes/concepts have the same or similar circuits<br>
&emsp;$$\chi_{MN} > 0$$ and $$p(m|M)\not\approx p(m|N)$$: Both concepts co-occur but have distinct mechanisms

{% endcomment %}


</div>


## **Demonstration 1: Toy Model**
<div class="toggle-content" markdown="1">
The framework above defines a static statistical description of learned representations. In the following toy model, we introduce explicit regularizers acting on these quantities and study how representations reorganize in response. This allows us to define stiffness, curvature, and phase behavior in a controlled and fully interpretable setting.

</div>

## **Demonstration 2: Dihedral Symmetry in a 1-Layer Transformer**
<div class="toggle-content" markdown="1">
This demonstration uses a model from our previous work ["Emergent dihedral symmetry in a 1-layer Transformer"](/projects/learned_group_symmetry_D3/).

</div>