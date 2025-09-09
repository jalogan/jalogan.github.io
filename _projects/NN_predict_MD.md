---
layout:      project
title:       "Coming Soon!"
#date:        2 Jan 2014
order: 8
image:
  path:      /assets/img/NN_predict_MD/spheres_moving_on_surface.png
  srcset:
    1920w:   /assets/img/NN_predict_MD/spheres_moving_on_surface.png
    960w:    /assets/img/NN_predict_MD/spheres_moving_on_surface.png
    480w:    /assets/img/NN_predict_MD/spheres_moving_on_surface.png
caption:     Using Artificial Neural Networks to Predict MD Forces
#description: >
#  Hyde is a brazen two-column [Jekyll](http://jekyllrb.com) theme.
#  It's based on [Poole](http://getpoole.com), the Jekyll butler.
#links:
#  - title:   Publication
#    url:     https://doi.org/10.48550/arXiv.2501.02424
#  #- title:   GitHub Repository
#  - icon:    "fab fa-github"
#    url:     https://github.com/jalogan/Constrained-Polymer-Collapse.git
featured:    false
#related_posts: 
---


* this unordered seed list will be replaced by the toc
{:toc}


## **Defining Goals and Tempering Expectations**

Molecular dynamics (MD) is one of the most common computational science techniques and the one that most closely seems to resemble the reality of many physical processes. The basic implementation of a MD algorithm is straightforward and mirrors our intuition: some representation of particles (simple spheres or complex geometries, although the difference comes from how pair interactions are defined) experience forces from other particles, obstacles, walls, external fields, etc., which leads to a displacement and change in momentum. At each step the net force on every particle determines how its position and momentum changes. The computation of the net force on each particle is typically the most intensive part of the algorithm, and it can lead to an extreme slow-down of the simulation, depending on the interactions involved---usually $$\mathcal{O}(N^2)$$ for pair interactions of $$N$$ particles plus other types of interactions (3-particle, 4-particle) that may be necessary. 

## **Prediction with MLP**

### **Limitations of MLP**

## **Moving to a GNN**

### **GNN strengths over MLP**

## **Model Comparisons**

