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
The goal of this work is to organize interpretability quantities important for analyzing neural networks (NNs) by developing a unified object $$\mathcal{N}$$. This object combines events and internal components---input examples and possible mechanisms of a neural network---and allows for easy derivation of superposition, polysemanticity, interactions, and entropies. Using this framework entropies derived from dual conditional distributions give measurable superposition and polysemanticity, combining interactions and signature similarity distinguishes redundant vs complementary circuits. The entropies and interactions become targets for regularization, which enables controlled shaping of the internal circuits. We derive physically-motivated knobs that allow us to control such quantities and we hope to include a new perspective through a lens of physics. There are many parallels between the two fields when aligned correctly, and it feels natural to explore superposition as an entropically-driven effect. 


## **Motivating Example: A Unified Statistical Framework**
<div class="toggle-content" markdown="1">
We begin with a minimal motivating example designed to illustrate the core statistical structure underlying superposition, feature reuse, and interactions. The example is intentionally small and fully explicit, allowing all quantities to be computed exactly by hand. No learning or neural network assumptions are made at this stage; the goal is to expose the mechanics of the framework in their simplest form.

---

### **Example System**
Consider a system with a finite set of event group labels $$m$$ and a finite set of internal components $$M$$, which would be considered microstates and macrostates in physics. At this stage, these labels carry no semantic meaning and are only used to index the system. We will later interpret events as input examples or groupings of input examples and components as scalar values measured over chosen objects of a neural network, respectively.

We define:

- **Event groups**<br>
$$m \in \{m_0, m_1, m_2, m_3\}$$<br>
- **Internal components**<br>
$$M \in \{A, B, C\}$$

---

### **The Primitive Object $$\mathcal{N}$$**
The sole primitive object of the framework is a non-negative matrix of statistical weights with elements $$\mathcal{N}_{mM}$$, which quantifies the statistical weight associated with the joint occurrence of event $$m$$ and components $$M$$. Importantly, $$\mathcal{N}$$ is not assumed to be normalized, probabilistic, or exclusive.

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

$$\mathcal{N}$$ defines an ensemble of joint pairs $$(m, M)$$. The ensemble consists of all event-component pairs, weighted by their statistical weights $$\mathcal{N}_{mM}$$. 

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

This has the exact same structure as a joint distribution over events and components. 

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

$$p(M)$$ represents how used each component is across the ensemble.

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
Conditioning on a fixed event yields a distribution over components,

$$
p(M|m) = \frac{\mathcal{N}_{mM}}{\sum\limits_{M'} \mathcal{N}_{mM'}}.
$$

This distribution characterizes how representational mass is spread across components for a given event, and provides a natural notion of *superposition*.

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
- $$m_3$$ is spread across all three components


#### **Polysemanticity**
Conversely, conditioning on a fixed component yields a distribution over events,

$$
p(m|M) = \frac{\mathcal{N}_{mM}}{\sum\limits_{m'} \mathcal{N}_{m'M}}.
$$ 

This dual conditional perspective captures the degree to which a given component is reused across different events, a notion referred to as polysemanticity if the components are features.

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


#### **Global component entropy**

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

The maximum $$H(M)$$ possible in this example is $$\log 3 \approx 1.1$$, so the computed value is high, and tells us that the usage is spread almost evenly across all components. 

The entropies above quantify how components are distributed individually. We now turn to correlations between components, which are not captured by entropy alone.

---

### **Interactions**
While conditional entropies capture how features are distributed across events and vice versa, they do not describe correlations between components themselves. To probe whether features tend to co-occur or avoid one another across the ensemble, we introduce pairwise co-usage statistics $$C_{MN}$$ derived from the same joint distribution

$$
C_{MN} = \sum\limits_m p(m) \, p(M|m) \, p(N|m),
$$

and the interaction $$\chi_{MN}$$

$$
\chi_{MN} = \log \frac{C_{MN}}{p(M)p(N)}.
$$

If the components are assigned independently with no knowledge of each other it is the ideal case $$C_{MN}^{\mathrm{ideal}} = p(M)p(N)$$, which provides a useful normalization.

For all pairs of components,

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

Because $$C$$ tells us the probability of co-occurrence of two components within an event: 
- Large $$C_{MN}$$: components $$M$$ and $$N$$ tend to appear together within the same event
- Small $$C_{MN}$$: components $$M$$ and $$N$$ tend to avoid each other within the same event

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

- $$\chi_{MN} > 0$$: components $$M$$ and $$N$$ prefer to co-occur--form a component family
- $$\chi_{MN} < 0$$: components $$M$$ and $$N$$ avoid each other
- $$\chi_{MN} = 0$$: components $$M$$ and $$N$$ occur exactly as if they were independent


#### **Redundancy and Complementarity**
If we use the the $$p(m|M)$$ and $$\chi$$ metrics together, we can determine if two components are redundant or complementary of each other. 

If $$\chi_{MN} > 0$$, the components co-occur, but if in addition:
- $$p(m\vert M) \approx p(m\vert N)$$: the components are used in the same events.  
  This is a case of $$M$$ and $$N$$ are doing the same job. It is an overcomplete representation---possible candidates for pruning or merging.

- $$p(m\vert M) \not\approx p(m\vert N)$$ (but possibly overlapping): the components appear together but each carries distinct information.


---


### **Example Summary**
This example demonstrates that superposition, polysemanticity, and feature interactions arise as complementary projections of a *single* normalized participation matrix. No additional assumptions are required beyond the initial choice of $$\mathcal{N}$$.
</div>


## **Mapping to Neural Networks**
<div class="toggle-content" markdown="1">
The motivating example in the previous section laid out the general construction. Now we will formalize this construction in the context of artificial neural networks (NNs) and show how the same statistical object arises naturally from NN activations, and how the quantities defined above can be used to analyze learned representations.

One of the beautiful consequences of this framework is that what we call the event-component pair, as outlined above, can be any degrees of freedom that carry information through the NN. The framework does not prescribe what constitutes the conjugate pair, *input* and *internal component*, such as input classes and features. It provides a **statistical lens** for analyzing joint structure between any two sets of objects. We outline some examples below, with the canonical mapping being the most natural, and others perhaps more useful for LLMs and NNs with more diverse elements.


### **The Primitive Object $$\mathcal{N}$$**

As in the motivating example, we want to define a non-negative matrix of statistical weights of events $$e \in \mathcal{E}$$ as rows and components or components from which we collect measurements as columns $$M \in \mathcal{M}$$. An event is a single observation over which statistics are accumulated. This is commonly a single input example, but could also be a token or something else depending on the NN. A component or component is any reusable internal component that produces a scalar contribution for each event. Common examples of components are a single neuron, SAE feature, attention head, circuit, appropriately aggregated.

$$
\mathcal{N}_{eM} = f(e;M) \geq 0,
$$

where $$f$$ is a chosen transformation on the raw measurements to ensure they are non-negative, monotonic, and align with the task at hand. For a measurement $$a$$, some common forms of $$f$$ might be $$\vert a \vert^p$$ with $$p=1,2$$ when interested in contribution strength, $$\vert \vert h_M(e) \vert \vert^2$$ when components are vector-valued and you want it to be energy-like, $$\exp({a})$$, or any other choice that best highlights what you want to interpret. Different choices of $$f$$ correspond to different measurement lenses, but all downstream quantities are computed identically once $$\mathcal{N}$$ is fixed. Recall, $$\mathcal{N}$$ is not normalized or probabilistic. 


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

and from here all other quantities, per-event superposition $$p(M\vert m)$$, global component usage $$p(M)$$, superposition entropy $$H(M\vert m)$$, polysemanticity conditional $$p(m\vert M)$$, interaction matrix $$\chi_{MN}$$.

All quantities studied in this work are functionals of a single nonnegative event–component weight matrix. Groupings and labels are optional coarse-grainings applied only when interpretability requires them.


### **Canonical Mapping**

The most immediate choice that comes to mind when grouping events and choosing components that are useful quantities in NNs is

- **Events**<br>
$$e$$: inputs/tokens<br>
- **Event Grouping**<br>
$$m$$: input classes/concepts/labels<br>
- **Components**<br>
$$M$$: internal components (neurons at layer $$\ell$$, attention heads, SAE features, circuits, etc.)

This mapping does not introduce a new object; it corresponds to a particular choice of event grouping and interpretation of the same underlying event–component weight matrix $$\mathcal{N}$$. This grouping is one interpretive coarse-graining of the events. 

This is an obvious choice when events are naturally grouped by classes or concepts, e.g., representation of a symmetry group where each event has a single group transformation associated with it.

The components (NN components) can be as simple as the neurons in a single layer, or more complex like aggregated output from attention heads. Whatever the components are, the framework quantifies the superposition, polysematicity, usage, etc. across them.

Because both “events” and "components" are abstract indices, superposition and polysemanticity can be defined at any level of description: tokens, sequences, tasks, neurons, heads, features, or circuits.

With this grouping the dictionary of quantities has the following interpretations:

**Probabilities**<br>
&emsp;$$p(m, M)$$: The total statistical weight associated with component $$M$$ when representing inputs in grouping $$m$$ <br>
&emsp;$$p(M)$$: Usage frequency of component $$M$$<br>
&emsp;$$p(m)$$: How much weight each input class contributes<br>
&emsp;$$p(M|m)$$: Measure of *input grouping superposition* across components---distribution of components used to represent a given input grouping. This can also be seen as the *average circuit footprint* for input grouping $$m$$.<br>
&emsp;$$p(m|M)$$: Measure of *component polysemanticity* across input groupings---distribution of inputs that use a given component. This can also be seen as a *component signature* across events or input groupings.<br>

Superposition and polysemanticity are intimately related through one interpretation and its dual. Here we label $$p(M\vert m)$$ as a *input grouping superposition* measure and $$p(m\vert M)$$ as a *component polysemanticity* measure, but in the dual view $$p(M\vert m)$$ is seen as a *input grouping polysemanticity* measure and $$p(m\vert M)$$ as a *component superposition* measure. They are one set of computations, but the meaning depends on interpretation. 

**Entropies**<br>
&emsp;$$H(M|m)$$: *Superposition entropy*---how many of the components are mixed in the representation of a given input grouping<br>
&emsp;&emsp;Low: *disentangled* representation<br>
&emsp;&emsp;High: *highly entangled* superposition<br>
&emsp;$$H(m|M)$$: *Polysemanticity entropy*---how broadly a component is reused across input groupings<br>
&emsp;&emsp;Low: selective component<br>
&emsp;&emsp;High: polysemantic component<br>
&emsp;$$H(M)$$: How evenly components are used overall<br>
&emsp;&emsp;Low: few components dominate<br>
&emsp;&emsp;High: balanced representation across components
&emsp;$$H(m)$$: How evenly groupings are used overall<br>
&emsp;&emsp;Low: few events/groupings dominate<br>
&emsp;&emsp;High: balanced representation across events/groupings

We distinguish local superposition, quantified by $$H(M\vert m)$$, from global superposition, quantified by $$H(M)$$. The former measures how distributed individual representations are, while the latter measures how evenly components are used across the entire dataset.

**Interaction Metrics**<br>
&emsp;$$C_{MN}$$: How often two components appear together with the same input grouping<br>
&emsp;$$\chi_{MN}$$: How often components appear together compared to if they are fully independent<br>
&emsp;&emsp;Positive: components form a family (appear together often)<br>
&emsp;&emsp;Negative: components compete or are exclusive<br>
&emsp;&emsp;Zero: components are independent

**Redundancy and Complementarity**<br>
&emsp;$$\chi_{MN} > 0$$ and $$p(m|M)\approx p(m|N)$$ (distributional similarity: small KL or JS divergence): the two components are doing the same job<br>
&emsp;$$\chi_{MN} > 0$$ and $$p(m|M)\not\approx p(m|N)$$: the two components form part of a circuit

Complementary components form **distributed circuits**. They are co-active, but they specialize in different aspects of the input structure. This cannot be inferred from interaction strength alone. It must be a combination of interaction strength and comparison of component signatures $$p(m\vert M)$$. 

*Looking forward:*<br>
Because all of these quantities are functionals of $$\mathcal{N}$$, they can be directly targeted by regularizers during training, allowing superposition, polysemanticity, and circuit structure to be shaped in a controlled and interpretable way.

The quantities defined above characterize the static structure of a representation. In the following sections, we introduce regularizers and response measures, such as stiffness and curvature, to study how this structure changes under controlled perturbations.


{% comment %}
### **Dual Mapping**

The dual view corresponds to reinterpreting the same joint distribution by swapping the roles of conditioning. Rather than asking which components represent a given input grouping, we ask how input groupings distribute across components. No new grouping or measurement is introduced, only the interpretation of conditionals changes.

Mathematically there are many overlaps between the canonical and dual views. They share the same joint distribution, $$p(m\vert M)_{\text{canonical}} = p(M\vert m)_{\text{dual}}$$, $$p(M\vert m)_{\text{canonical}} = p(m\vert M)_{\text{dual}}$$, by design. However, our interpretations tend to shift and so it's worthwhile going through the dictionary once again.

**Events**<br>
$$e$$: inputs/tokens
**Event Grouping**<br>
$$m$$: input classes/concepts/labels<br>
**Components**<br>
$$M$$: internal components (neurons at layer $$\ell$$, attention heads, SAE features, circuits, etc.)

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
&emsp;$$\chi_{MN} > 0$$ and $$p(m|M)\not\approx p(m|N)$$: Both concepts co-occur but have distinct components

{% endcomment %}


</div>


## **Common Templates**
<div class="toggle-content" markdown="1">

### **Events=inputs, Components=neurons**

Let's say we have three input examples that measure over two neurons in a given layer.

- **Events**<br>
$$m \in \{1, 2, 3\}$$<br>
- **Components**<br>
$$M \in \{1, 2\}$$

If the raw activations are:

$$
a_{mM} = \,
\begin{array}{c|cc}
      & M=1 & M=2 \\
\hline
m=1 & 2.0 & 0.0 \\
m=2 & 1.0 & 1.0 \\
m=3 & 0.2 & 1.8
\end{array}
$$

**Choose the lens**<br>
We must choose how to map the activations into non-negative values. An energy-like magnitude is $$\mathcal{N}_{mM} = \vert a_{mM} \vert^2$$,

$$
\mathcal{N} = \,
\begin{array}{c|cc}
      & M=1 & M=2 \\
\hline
m=1 & 4.00 & 0.00 \\
m=2 & 1.00 & 1.00 \\
m=3 & 0.04 & 3.24
\end{array}
$$

**Superposition per event**<br>
This is the row-normalized conditional $$p(M\vert m)$$.

$$
p(M\vert m) = \,
\begin{array}{c|cc}
      & M=1 & M=2 \\
\hline
m=1 & 1.000 & 0.000 \\
m=2 & 0.500 & 0.500 \\
m=3 & 0.012 & 0.988
\end{array}
$$

- Event 1 is fully disentangled on neuron 1
- Event 2 is fully entangled between the neurons
- Event 3 is almost fully disentangled on neuron 2

**Superposition entropy**<br>
We may use the above condition entropies to get a scalar that describes superposition across the neurons for each event.
$$
H(M\vert m) = - \sum\limits_{M} p(M\vert m) \log p(M\vert m)
$$

$$
H(M\vert m) = (0, \log 2, \approx 0)
$$

This matches the interpretation that Events 1 and 3 are disentangled and Event 2 is fully superposed.

**Polysemanticity**<br>
This represents the dual conditional--column normalized.

$$
p(m\vert M) = \,
\begin{array}{c|cc}
      & M=1 & M=2 \\
\hline
m=1 & 0.79 & 0.00 \\
m=2 & 0.20 & 0.24 \\
m=3 & 0.01 & 0.76
\end{array}
$$

- Neuron 1 is mostly selective to Event 1, but shared with Event 2
- Neuron 2 is mostly selective to Event 3, but shared with Event 2

#### **Grouping by input**
If we decide to group events by some equivalence, the results change. 

- Class A: events $$\{1, 2\}$$
- Class B: event $$\{3\}$$

We update $$\mathcal{N}$$ by coarse-graining over events

$$
\mathcal{N}_{mM} = \sum\limits_{e\in Class} \mathcal{N}_{eM}
$$

$$
\mathcal{N} = \,
\begin{array}{c|cc}
      & M=1 & M=2 \\
\hline
A & 5.00 & 1.00 \\
B & 0.04 & 3.24
\end{array}
$$

**Class superposition**<br>

$$
p(M\vert \text{Class}) = \,
\begin{array}{c|cc}
      & M=1 & M=2 \\
\hline
A & 0.833 & 0.167 \\
B & 0.012 & 0.988
\end{array}
$$

Now we have the interpretation of how many internal components each class uses.

**You can control the level of analysis by varying how events are grouped without changing the framework.**


### **Transformer: Events=tokens, Components=attention heads**

The internal components don't need to be neurons. In a transformer, for example, they can be attention heads. 

- **Events**<br>
$$m$$: one token position in one sequence<br>
Example: token *not* at position 7
- **Components**<br>
$$M \in \{1,2,\dots,H\}$$


Part of the current definition of internal components is that they return a *scalar* measurement for each event. Attention heads, however, return a vector. In choosing the lens to map the output to a non-negative value, we must first map the output vector to a scalar.

We have a variety of choices to do this, for example:

- $$L_2$$ norm of the output: $$\vert\vert \text{head output}_{mM} \vert\vert_2$$
- contribution to logit direction: $$\vert \langle\text{head output}_{mM}, v_{\text{logit}}\rangle \vert$$

Then we must define our lens such as $$\mathcal{N}_{mM} = \vert a_{mM} \vert^2$$ or $$\mathcal{N}_{mM} = \vert a_{mM} \vert$$.

For this small example

- **Events**<br>
$$m \in \{not, very, !\}$$<br>
- **Components**<br>
$$M \in \{h_1,h_2\}$$

and we choose the $$L_2$$ norm to get a scalar output and $$\mathcal{N}_{mM} = \vert a_{mM} \vert^2$$.

Given the head outputs for each token

$$
\text{head_output} = \,
\begin{array}{c|cc}
      & h_1 & h_2 \\
\hline
not & (3,0,\dots) & (1,0,\dots) \\
very & (1,0,\dots) & (3,0,\dots) \\
! & (\sqrt{2}, \sqrt{2},0,\dots) & (\sqrt{2}, \sqrt{2},0,\dots)
\end{array}
$$


$$
\text{head_scalar} = \,
\begin{array}{c|cc}
      & h_1 & h_2 \\
\hline
not & 3.0 & 1.0 \\
very & 1.0 & 3.0 \\
! & 2.0 & 2.0
\end{array}
$$

$$
\mathcal{N} = \,
\begin{array}{c|cc}
      & h_1 & h_2 \\
\hline
not & 9.0 & 1.0 \\
very & 1.0 & 9.0 \\
! & 4.0 & 4.0
\end{array}
$$

**Superposition**

$$
p(M\vert m) = \,
\begin{array}{c|cc}
      & h_1 & h_2 \\
\hline
not & 0.9 & 0.1 \\
very & 0.1 & 0.9 \\
! & 0.5 & 0.5
\end{array}
$$

**Polysemanticity**

$$
p(m\vert M) = \,
\begin{array}{c|cc}
      & h_1 & h_2 \\
\hline
not & 0.64 & 0.07 \\
very & 0.07 & 0.64 \\
! & 0.29 & 0.29
\end{array}
$$

- Head 1 specializes in *not* contexts
- Head 2 specializes in *very* contexts
- Both Head 1 and Head 2 contribute to punctuation like *!*

**In real example we could group tokens by context such as negations or punctuation to get a different perspective.**


### **Events=inputs, Components=feature directions**
Given a layer, we can easily adjust the ensemble to analyze how a hidden vector is projected onto feature directions defined though, e.g., a sparse autoencoder (SAE).

- **Events**<br>
$$m \in \{1,2,3\}$$<br>
- **Components**<br>
$$M = \text{feature directions } w_k \in \mathbb{R}^d$$<br>

Just as with the previous example, we first need to transform the vector component into a scalar component. In this case we are interested in the projection of the hidden vector $$h^{(\ell)}(m)$$ at layer $$\ell$$ from input $$m$$. The scalar component is $$z_{mk} = \langle h(m), w_k \rangle$$, or equivalently given by the $$k$$ neuron activation in the SAE.

We choose a lens to observe the ensemble, e.g., $$f=max\{x, 0\}$$, $$f=\vert x \vert^2$$, or $$f=\vert x \vert$$, and the primitive object is defined as

$$
\mathcal{N}_{mk} = f(z_{mk})
$$

Superposition is then given by $$p(M\vert m)$$, polysemanticity by $$p(m\vert M)$$, entropies and interactions may be computed from these probabilities (including p(m)). Interactions gives us a quantitative measure of how much feature directions tend to occur together for an input, providing a sense of feature direction families.  


</div>

## **Demonstration 1: Toy Model**
<div class="toggle-content" markdown="1">
The framework above defines a static statistical description of learned representations. In the following toy model, we introduce explicit regularizers acting on these quantities and study how representations reorganize in response. This allows us to define stiffness, curvature, and phase behavior in a controlled and fully interpretable setting.

</div>

## **Demonstration 2: Dihedral Symmetry in a 1-Layer Transformer**
<div class="toggle-content" markdown="1">
This demonstration uses a model from our previous work ["Emergent dihedral symmetry in a 1-layer Transformer"](/projects/learned_group_symmetry_D3/).

</div>