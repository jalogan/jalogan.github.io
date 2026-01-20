---
layout:      project
title:       "Emergent dihedral symmetry in a 1-layer Transformer"
published:   true

#date:        2 Jan 2014
order: 8
image:
  path:      /assets/img/learned_group_symmetry_D3/hidden_space_heatmap_cover_image.png
  srcset:
    1920w:   /assets/img/learned_group_symmetry_D3/hidden_space_heatmap_cover_image.png
    960w:    /assets/img/learned_group_symmetry_D3/hidden_space_heatmap_cover_image.png
    480w:    /assets/img/learned_group_symmetry_D3/hidden_space_heatmap_cover_image.png
caption:     Interpreting the emergent properties of dihedral symmetry with a 1-layer transformer
featured:    false
#related_posts: 
---


* this unordered seed list will be replaced by the toc
{:toc}




## **Why This Work Matters**

Many neural net models are top-down and explicitly bake in symmetries and invariances to achieve a model that respects physics. Our model is a bottom-up approach that aims to train on the Dihedral group and allow the group structure to emerge without explicitly demanding it. The model we use is a minimal 1-layer transformer because our goal is to identify the group operator circuits (hopefully) as a circuit-representation of the symmetry group. Once the circuits are identified we check the closure property of the group on this representation by composing the circuits attributed to each operator. 

This work combines:
  - Physics intuition (emergence of classical symmetries)
  - Representation theory (group actions)
  - Mechanistic interpretability (circuit composition)


## **Introduction**
<div class="toggle-content" markdown="1">
We train a small 1-layer transformer to apply symmetry operations from the dihedral group $$D_3$$ to a triangle---the symmetries of the equilateral triangle.

The group $$D_3$$ has six elements which consist of rotations and reflections of the equilateral triangle:

  - $$E$$ (identity---do nothing)
  - $$R$$ (Rotate $$120^{\circ}$$)
  - $$R^2$$ (Rotate $$240^{\circ}$$)
  - $$S$$ (Reflect across a chosen axis---vertical axis in <a href="#fig_D3_symmetries" data-fig-ref>??</a>)
  - $$SR$$ (operator R followed by operator S---equivalent to a reflection about axis through green in <a href="#fig_D3_symmetries" data-fig-ref>??</a>)
  - $$SR^2$$ (operator R followed by operator R followed by operator S---equivalent to a reflect about the axis through blue in <a href="#fig_D3_symmetries" data-fig-ref>??</a>)

<figure id="fig_D3_symmetries">
  <img src="/assets/img/learned_group_symmetry_D3/D3_operators.png" alt="group_operations" width="600" height="auto">
  <figcaption>Visual display of the group operations. Vertices 0, 1, and 2 are colored red, green, and blue, respectively. \(E\) is the identity operator, \(R, R^2\) are rotations by \(120^{\circ} and 240^{\circ}\), \(S, SR, SR^2\) are relections about the three lines of mirror symmetry, through the red vertex, green vertex, and blue vertex. </figcaption>
</figure>

Any group satisfies certain properties:

  - The operations are closed---composing group operators is *always* equivalent to a single operator in the group (e.g., $$R R^2 = E$$)
  - The operations are associative (e.g., $$R^2 (S R) = (R^2 S) R = (SR)R = SR^2$$)
  - The operations have inverses (e.g., $$R^2 R = E$$, $$SS = E$$, etc.)
  - The group has an identity (E)

Each of these properties relies on the composition of group operations, e.g., $$R^2 S R$$ means act with R, followed by S, followed by $$R^2$$. If composition fails, the group structure dissolves. 

The input to the model is:
  - the coordinates of three triangle vertices
  - the token telling the model which operator to apply.

The output of the model is:
  - the three vertices of the transformed triangle.

**Key Point**<br>
We do not train our model on the compositions themselves. We train only on single operators and look inside to see how much of the group structure has been internalized. We want to see if the model has learned an internal structure such as "the current operator is R", and if the model can compose operations. The system is very interpretable because

  - the group behavior is well-defined
  - the network is small---just a 1-layer transformer.

After training **we want to open it up and essentially reverse engineer how the transformer encodes the symmetry group**.
</div>

Throughout this work we use "circuit" in several closely related but distinct senses, following standard usage in mechanistic interpretability. At the lowest level, a neural circuit refers to a concrete subgraph of the model (e.g., attention, MLP, or encoder blocks) through which activations flow. At a higher level, an operator circuit refers to the computation that implements the effect of a symmetry operator on internal representations, potentially spanning multiple layers or modules. At the highest level, we sometimes speak of circuits abstractly, referring to the effective computational pathways or feature combinations that realize group operations in representation space. These uses form a hierarchy: operator circuits are implemented by neural circuits, and feature-level circuits describe how those implementations are composed internally. In what follows, the intended meaning should be clear from context.


## **Experiment 1: Does the model actually compose?**
<div class="toggle-content" markdown="1">
### **Composing operator circuits**
When the model is applying transformations, is it understanding the algebra of the group? One way we test this is by checking closure of operator composition. We choose boundaries in the architecture to act as the "operator implementation circuit", such as just before and just after the encoder transformer (pre- and post-encoder). We run the model on operator $$g_1$$ and record the internal activations after the transformer block (post-encoder) for each vertex token, then we run the model on operator $$g_2$$, but during the forward pass before the encoder boundary (pre-encoder) we inject the activations from the post-encoder output of operator $$g_1$$ to act as the incoming state at the pre-encoder with operator $$g_2$$. A schematic diagram of this composition can be seen in <a href="#fig_circuit_compos_diagram" data-fig-ref>??</a>, where the orange layers represent the supposed circuit. In essence this treats the encoder transformer as the circuit which we hypothesize implements the operation. Composition is implemented by first passing through this circuit with operator $$g_1$$, then using the output with the operator changed to $$g_2$$ to pass through another copy of the circuit. As a comparison we do a single pass of the known composed $$g_2 g_1$$ and compare the final outputs of both. If the model truly represents the algebra of the group, and we have chosen the circuit correctly, the two final outputs should match. We may quantify how much the two outputs mismatch through the mean squared error (MSE) between the single-pass and two-pass outcomes.

<figure id="fig_circuit_compos_diagram">
  <img src="/assets/img/learned_group_symmetry_D3/circuit_composition_diagram.png" alt="composition_diagram" width="1000" height="auto">
  <figcaption> Circuit composition test. In the first pass (\(g_1\)), activations are captured after layer C. In the second pass (\(g_2\)), they are re-injected before C, yielding an effective composed circuit transformation \(\mathrm{C}_1 \mathrm{D}_1 \mathrm{C}_2 \mathrm{D}_2\). If the orange block really is the operator circuit, then running it twice with \(g_1\) then \(g_2\) should match running it once with \(g_2 g_1\). </figcaption>
</figure>

We repeated this for three different test circuits, each a subcircuit of the former: pre-post encoder transformer, pre-post first LayerNorm + attention, pre-post attention only. The results can be seen in <a href="#fig_closure_heatmaps" data-fig-ref>??</a>. What we find is that the closure is not perfect. Some pairs of operators match their composed version better than others. The model has apparently not learned the group algebra. It can output the correct transformation for a single operator, but it cannot compose.

<figure id="fig_closure_heatmaps">
  <img src="/assets/img/learned_group_symmetry_D3/all_CLR_heatmaps.png" alt="group_operations" width="auto" height="500">
  <figcaption> A heatmap visualizing the difference between the output of single operator \(g_2 g_1\) and two-pass \(g_1\) followed by \(g_2\) for three different possible circuits. For perfect group closure, they should all be at or near zero. The boundary around the encoder transformer does the best of the three, but still does not demonstrate that operator composition has emerged through learning individual operator actions.</figcaption>
</figure>

This opens a deep question: **Why does a circuit representation of the group not close under composition of operators?**

To understand why closure fails, we need to see how the model internally represents each operator and whether different operators are forced to reuse the same subspace.
</div>


## **Uncovering features and superposition**
<div class="toggle-content" markdown="1">
In order to answer this question, we need to go deeper. We must understand the vector space of the activations and what is activated for each operator. 

### **Sparse autoencoder on post-encoder activations**

At the output of the encoder transformer we place a sparse autoencoder (SAE) to expand into a larger vector space ($$\mathrm{SAE_{lat}}$$ dimensions) to allow the activations to disentangle. We keep it sparse (all vectors in the space are mostly zeros) by choosing to limit the nonzero values to the largest $$k$$ activations in each vector. We *could* introduce a $$L_1$$ error term into the loss function, which would act to keep the magnitude of these components small, but it often leads to small, but still nonzero values, so we enforce sparsity by keeping only the top activations ($$k$$). The input of the SAE will be the output activations of the encoder transformer and the SAE must encode these vectors into its latent space, then decode them back to the original space, such that they map back as closely as possible to the original vectors, $$\text{reconstruction loss} = \vert\vert \mathrm{dec}(\mathrm{enc}(h)) - h \vert\vert^2$$. The idea is to represent each original 64-dim activation vector as a sparse linear combination of $$\mathrm{SAE_{lat}}=256$$ learned basis vectors. We train a SAE for each vertex to learn what the recurring internal patterns are for each vertex's representation. We do this per-vertex because each vertex sees a different orbit of the group, so we want to see whether the model reuses the same features or learns vertex-specific features.

Each column of the SAE decoder is a 64-dim vector in the model's hidden space. These columns act like features that the model repeatedly uses, and each row (component) within one column tells us how much each hidden space neuron lights up for that particular feature. In linear algebra terms, the column space of the SAE decoder is a 64-dim space. The set of 256 feature vectors is overcomplete, so the feature vectors necessarily have overlaps, leading to the superposition that we want to measure. Overall, however, the rank of the hidden space is likely less than 64 (we will not find 64 independent vectors).

The sparsity of the SAE forces only $$k$$ features to activate at a time. As a simple example, let's say we input operator $$g$$ and we find that the latent space vector $$z$$ is only nonzero for components 7, 63, 145: $$z = (0,0,\dots,0,z_7,0, \dots, 0,z_{63},0,\dots,0,z_{145},0,\dots) = (0,0,\dots,0,1.2,0, \dots, 0,0.8,0,\dots,0,0.4,0,\dots)$$. This tells us that this vector is a combination of features 7, 63, and 145. We may not know what each of those features represents semantically at this point, but we know that this operator exhibits these features.

We can now use input data for a single vertex and single operator token and ask questions like "For vertex 0, when I apply operator S, which SAE features activate?" We repeat this for thousands of inputs of each operator for each vertex and average the results together to make a set of heatmaps, seen in <a href="#fig_SAE_feature_heatmaps" data-fig-ref>??</a>. Now we can compare what SAE features light up strongly for each operation across vertices.


<figure id="fig_SAE_feature_heatmaps">
  <img src="/assets/img/learned_group_symmetry_D3/all_verts_SAE_feature_heatmap.png" alt="SAE_features" width="1000" height="auto">
  <figcaption> SAE heatmaps that show how strongly each feature activates for operator \(g\) at vertex \(v\) on average. </figcaption>
</figure>

Ideally, the SAE heatmaps would show columns that are bright only for one operator, meaning a particular feature is $$g$$-specific. Reality isn't so clean, and we get certain features lighting up for multiple operators. For instance, for vertex 0, operators $$R^2$$ and $$SR$$ are identical! We see something similar happening for vertex 1 operators $$R^2$$ and $$SR^2$$, and vertex 2 operators $$R^2$$ and $$S$$. Why would this be? This is actually an instance of the group algebraic structure being learned correctly. Certain transformations end with one vertex in the same place. If we begin with E in <a href="#fig_D3_symmetries" data-fig-ref>??</a>, we see that $$R$$ and $$SR^2$$ end with the red vertex (vertex 0) in the same position (bottom left). From the perspective of vertex 0 the transformations $$R$$ and $$SR^2$$ are the same. Let's put a bookmark here and come back to this point soon.

Now that we have the SAE heatmaps, we can also look at how similar different operators are within one vertex by computing the inner product of the 256-dim average SAE vectors in each heatmap.

<figure id="fig_SAE_overlap_heatmaps">
  <img src="/assets/img/learned_group_symmetry_D3/all_SAE_operator_overlap_heatmaps.png" alt="SAE_overlap" width="700" height="auto">
  <figcaption> Overlap of average SAE latent space representations of the operators for each vertex. </figcaption>
</figure>

<a href="#fig_SAE_overlap_heatmaps" data-fig-ref>??</a> shows how similar the average operator SAE vectors are. The main diagonals are the same, by default, and, not surprisingly, there are non-zero off-diagonals. We already discussed why this happens, and how it comes from the real structure of the group, but this highlights these special transformation pairs. We now see clearly that for vertex 0, the operator pairs that share similar (or in some cases the same) circuits are $$R^2$$ and $$SR$$, $$R$$ and $$SR^2$$, and $$S$$ and $$E$$. Each of these pairs leaves vertex 0 in the same position after transformation, as seen in <a href="#fig_D3_symmetries" data-fig-ref>??</a>, and so looks equivalent from vertex 0's perspective. We also have three operator pairs for vertex 1 and vertex 2 that leave the green and blue vertices in the same position, respectively. 


### **Decoding back to hidden space**

SAE latent space allows us to disentangle the operators by expanding each into a larger basis of 256 feature vectors, but we are also interested in looking at how the operators are represented in the model's 64-dim hidden space. SAE heatmaps tell us which features fired, and the hidden space heatmaps will tell us which neurons fired as a linear combination of the features for a given operator-vertex pair. The SAE decoder already handles the map back to the model's hidden space. For each vertex-operator pair we input the 64-dim activation vector $$h$$, we get a sparse 256-dim vector $$z$$ in SAE latent space that tells us exactly the linear combination of feature vectors the $$h$$ vector is made up of, then we apply the SAE decoder and get out a new 64-dim activation vector $$\hat{h}$$ that shows us how the neuron activations for each of these features mix to represent this operator. 

When we use the SAE decoder $$W_d$$ to map the latent vector back to hidden space, we know that this becomes a linear combination of these features $$\hat{h} = W_d \, z = 1.2W_d[:,7] + 0.8W_d[:,63] + 0.4W_d[:,145]$$. The components of each column in $$W_d$$ tell us exactly how much each hidden space neuron activates for that particular feature, which means it tells us exactly the circuit for that feature. When the operator latent space vector is mapped back to hidden space, the neurons will activate exactly in the combination of how the features that make it up activate the neurons. The hidden space representation exhibits *superposition* and blurs our interpretation of what the input does.

We again average over thousands of the output vectors $$\hat{h}$$ from different triangle configurations to get corresponding heatmaps in the model's hidden space.

<figure id="fig_hidden_space_feature_heatmaps">
  <img src="/assets/img/learned_group_symmetry_D3/all_hidden_space_heatmaps.png" alt="hidden_features" width="1000" height="auto">
  <figcaption> Hidden space heatmaps of the decoded representation of each operator-vertex pair averaged over many samples. </figcaption>
</figure>

<a href="#fig_hidden_space_feature_heatmaps" data-fig-ref></a> shows the hidden space feature heatmaps. While the SAE space feature heatmaps in <a href="#fig_SAE_feature_heatmaps" data-fig-ref>??</a> are sparse, the hidden space heatmaps are dense. The SAE essentially created 256 candidate sub-directions in hidden space that act as features directions. This is more directions than the hidden space basis can hold, and so these directions overlap and demonstrate superposition.  

<figure id="fig_hidden_space_overlap_heatmaps">
  <img src="/assets/img/learned_group_symmetry_D3/all_hidden_operator_overlap_heatmaps.png" alt="hidden_overlap" width="700" height="auto">
  <figcaption> Overlap of the average decoded hidden space representations of the operators for each vertex. Many more non-zero squares than the SAE latent space points to superposition. </figcaption>
</figure>

We can continue in the same fashion as for the SAE analysis and look at the inner product of each operator row with all of the others, to see how similar the hidden space activations are for different operators. The overlap between different features can be seen in <a href="#fig_hidden_space_overlap_heatmaps" data-fig-ref>??</a>, and a quick comparison with <a href="#fig_SAE_overlap_heatmaps" data-fig-ref>??</a> shows how the hidden space obfuscates the meaning of each operator. Earlier we saw how the few nonzero off-diagonals in the SAE overlap heatmaps actually arise from the structure of the group and that perspective of each vertex under different transformations. While those same squares are nonzero, we now have more overlapping operators, demonstrating how we do not have distinct neural paths for each operator and we cannot separate the actions of different operators.


### **Geometry of hidden-space representations**

To visualize how the model organizes operator representations in hidden space, we perform principal component analysis (PCA) on the post-encoder activation vectors. Heatmaps tell us which dimensions are shared; PCA tells us how far apart the operators actually lie in the space the model uses.

When we plot the individual hidden activations (for thousands of input triangles per operator and vertex), distinct clusters appear for each operator. These clusters occupy well-defined regions of the hidden space, showing that the model has indeed learned to separate the six symmetry operations internally. However, the clusters for certain operators---particularly $$S$$ and $$R^2$$ for vertex 2---almost completely overlap, mirroring the equivalences seen earlier in the SAE overlap heatmaps. This confirms that these operators are encoded as nearly identical internal directions.

<figure id="fig_hidden_space_PCA_individual_samples">
  <img src="/assets/img/learned_group_symmetry_D3/PCA_hidden_samples_scatter_all_verts.png" alt="hidden_overlap" width="600" height="auto">
  <figcaption> PCA of hidden space activation vectors for many random triangle samples for all operator-vertex pairs. A window into how the model learned the individual operators, and further confirmation of no clear distinction between certain operators in the learned model. </figcaption>
</figure>

Next, averaging the hidden activations for each operator and vertex yields a compact geometric summary. The resulting PCA projection shows that all vertices for a given operator lie nearly on top of each other, while the six operators themselves collapse into three broad groups corresponding roughly to identity, rotations, and reflections. In other words, the transformer compresses the non-abelian dihedral group into a nearly commutative latent geometry, reusing overlapping subspaces for multiple operators.

This geometric compression provides a clear, visual explanation for the closure failure: the model has merged distinct group elements into shared hidden directions.

<figure id="fig_hidden_space_PCA_averaged">
  <img src="/assets/img/learned_group_symmetry_D3/PCA_hidden_means_scatter.png" alt="hidden_overlap" width="700" height="auto">
  <figcaption> PCA of hidden-space activations. Each color represents a symmetry operator, and shapes correspond to vertices. Operators essentially cluster into three main groups (identity, rotations, reflections), revealing compression of the group structure. </figcaption>
</figure>


So far we have examined each vertex independently. But since the group acts globally on all three vertices at once, a consistent internal representation should assign the same hidden-space direction to a given operator across all vertices. To test this, we compute the cosine similarity between the mean hidden-space activation vectors for every vertex–operator pair. The result is the cross-vertex operator overlap matrix shown in <a href="#fig_hidden_space_cross_vertex_overlap_heatmaps" data-fig-ref>??</a>.

Each $$6\times6$$ block on the diagonal corresponds to a single vertex (comparing operators within that vertex), while the off-diagonal blocks compare how the same operator appears across vertices. Ideally, entries along the corresponding operator diagonals (e.g., $$R$$ vs. $$R$$, $$S$$ vs. $$S$$ across vertices) would be bright, indicating that all vertices encode the same operator in a consistent direction.

However, we observe that these off-diagonal blocks are irregular: while the rotations ($$R$$, $$R^2$$) and reflections ($$S$$, $$SR$$, $$SR^2$$) tend to cluster together, their cross-vertex overlaps vary strongly. This means that each vertex has partially learned its own local embedding of the group operators. In effect, the model has not discovered a single global representation of the dihedral group, but three partially aligned subrepresentations—another form of aliasing that contributes to closure failure.


<figure id="fig_hidden_space_cross_vertex_overlap_heatmaps">
  <img src="/assets/img/learned_group_symmetry_D3/global_cross_vertex_overlap_hidden.png" alt="hidden_overlap" width="700" height="auto">
  <figcaption> Cross-vertex operator similarity matrix. Each \((i,j)\) entry gives the cosine similarity between averaged hidden activations for vertex–operator pairs. Bright diagonal blocks indicate within-vertex consistency, off-diagonal structure shows cross-vertex alignment of the same operators. </figcaption>
</figure>

</div>


## **Why group closure fails**
<div class="toggle-content" markdown="1">
Recall the nonzero overlaps in <a href="#fig_SAE_overlap_heatmaps" data-fig-ref>??</a>. Even though they seem to respect the group structure for specific vertices, they are trouble. To see why, we look at the consequences of this for composition of operations, visualized in <a href="#fig_equiv_ops_fails_comp" data-fig-ref>??</a>. Here we use the example that for vertex 2 (blue) operators $$S$$ and $$R^2$$ are equivalent. The top row of the figure repeats the identity $$E$$ and one of the reflections $$SR^2$$. From the perspective of the model's learned code for vertex 2, $$SR^2 = SS (= E) = R^2R^2 (= R)$$. But, from <a href="#fig_equiv_ops_fails_comp" data-fig-ref>??</a> we can easily see that this is not true. From vertex 2's learned representation, $$S$$ and $$R^2$$ collapse to nearly the same internal code. This is harmless for single step operations, but once we compose, the model can't tell whether it should follow the $$S$$ branch or the $$R^2$$ branch, so the composed operation fails.

<figure id="fig_equiv_ops_fails_comp">
  <img src="/assets/img/learned_group_symmetry_D3/NN_equiv_ops_fails_composition.png" alt="group_operations" width="400" height="auto">
  <figcaption> Outcome using the real \(D_3\) group multiplication table if operarators \(S\) and \(R^2\) were treated as being identical. This shows partially why group closure fails in the learned model. </figcaption>
</figure>

The symmetry group $$D_3$$ that we have been investigating is a relatively simple, finite group, but, even so, it is a non-abelian group, which means that not all of the operators commute. The cyclic group $$C_3$$ represents rotations of an equilateral triangle, and is an abelian subgroup of $$D_3$$. Would we observe the same problems if we had chosen to study $$C_3$$? Most likely not, or at least not to the same extent. The property, or lack thereof, of non-commutativity means that one subcircuit reused for more than one operator cannot succeed. In a small group where the operators commute, this is much less crucial.

From a representation theoretic perspective, we're asking the model to learn a representation of $$D_3$$ in $$\mathbb{R}^{64}$$, a mapping $$\rho: D_3 \rightarrow GL(64, \mathbb{R})$$, such that $$\rho(g_2 g_1) = \rho(g_2)\rho(g_1)$$. For abelian groups, you can diagonalize all $$\rho(g)$$ simultaneously (because commuting matrices share eigenvectors). So the model could encode operators as scalings along shared axes. For non-abelian groups, there is no basis in which all $$\rho(g)$$ are simultaneously diagonalizable. In other words, $$D_3$$'s non-abelian nature mathematically guarantees that no single orthogonal basis can represent all operators simultaneously. But the model still tries to reuse one basis, so it fails to distinguish certain pairs of operations. This means that an abelian group may have the ability to represent operators with the same, or similar, subcircuits, but for non-abelian groups this is impossible outright. The model has tried to *compress* the non-commutative structure into a simple commutative latent space, which has caused it to fail when certain operators are composed and destroys the closure property, thus failing to create a faithful representation of the group. **This exposes the non-abelian nature of $$D_3$$ as one of the root causes behind the closure failure, and the superposition observed in the model**. 




<div class="aside-box">
  <div class="aside-header">Aside: Abelian groups and closure under superposition</div>

  <div class="aside-content" markdown="1">

Even in an **abelian** group, shared feature directions are not automatically a problem — it depends on how the group is represented internally.  
Below we contrast the cyclic group $$C_3$$ (rotations) and the modular addition group $$\mathbb{Z}_3$$.


### **1. The cyclic group $$C_3 = \{E, R, R^2\}$$**
$$C_3$$ describes rotations of an equilateral triangle by $$0^\circ, 120^\circ,$$ and $$240^\circ$$.  
A faithful representation in $$\mathbb{R}^2$$ is given by rotation matrices

$$
\rho(R^k) =
\begin{bmatrix}
\cos(\frac{2\pi k}{3}) & -\sin(\frac{2\pi k}{3}) \\
\sin(\frac{2\pi k}{3}) & \cos(\frac{2\pi k}{3})
\end{bmatrix}.
$$

All three operators act within the same two axes (X and Y), so their “features” are completely shared---yet closure is exact:

$$
\rho(R)\rho(R) = \rho(R^2), \quad \rho(R^2)\rho(R) = \rho(E).
$$

Because the representation is *linear* and the operators commute, composition corresponds exactly to addition of rotation angles.  
This shows that **shared axes are harmless in a true linear representation**.


### **2. The modular group $$\mathbb{Z}_3 = \{0, 1, 2\}$$**
Now consider a model that tries to represent the same group additively:

$$
\begin{aligned}
\rho(0)&=(0,0) \\ 
\rho(1)&=(1,0) \\ 
\rho(2)&=(\cos(0.2), \sin(0.2)) \approx (0.98, 0.20).
\end{aligned}
$$

Composition is supposed to follow addition mod 3:

$$
1+1 = 2 \pmod 3, \qquad 1+2 = 0 \pmod 3.
$$

But in the learned space, addition of the encoded vectors gives

$$
\rho(1)+\rho(1) = (2,0) \neq (0.98, 0.20) = \rho(2),
$$

so closure fails — even though the group itself is abelian.  
Here the operators $$1$$ and $$2$$ share almost the same latent direction (the X-axis), and composition “double-counts” that shared feature instead of rotating into a new one.


In short:  
- $$C_3$$ shows that an abelian group can share axes and still maintain closure,  
- $$Z_3$$ shows that if those shared axes are *entangled* (superposed feature directions), closure fails.

The transformer used here encodes everything as a vector ($$\in \mathbb{V}$$) , but to be faithful to the group we need linear maps ($$\in \mathbb{V} \otimes \mathbb{V^*}$$). In a sense, our transformer never had a chance.

  </div>
</div>


</div>


### Links

<a href="https://github.com/jalogan/emergent-dihedral-symmetry-transformer" class="info-button" target="_blank">
  <span class="icon-github" style="font-size: 32px;"></span>
</a>


<style>
  /* Remove any arrows on external links */
  .info-button::after {
    content: none !important;
  }
</style>




