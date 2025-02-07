---
layout:      project
title:       "Constrained Polymers"
date:        2 Jan 2014
image:
  path:      /assets/img/constrained_polymers/4096_polymer_full.png
  srcset:
    1920w:   /assets/img/constrained_polymers/4096_polymer_full.png
    960w:    /assets/img/constrained_polymers/4096_polymer_half.png
    480w:    /assets/img/constrained_polymers/4096_polymer_quarter.png
caption:     Modeling proteins as constrained polymers
description: >
  Hyde is a brazen two-column [Jekyll](http://jekyllrb.com) theme.
  It's based on [Poole](http://getpoole.com), the Jekyll butler.
links:
  - title:   Publication
    url:     https://doi.org/10.48550/arXiv.2501.02424
  #- title:   GitHub Repository
  - icon:    fa-github
    url:     https://github.com/jalogan/Constrained-Polymer-Collapse.git
featured:    false
#related_posts: 
---

# Polymers and Coarse-Grained Proteins

{:toc}

A polymer is a chain of monomer units that can be as simple (a single sphere) or as complex (complex molecule, e.g., amino acid) as necessary. 
{:.lead}

You can add a note.
{:.note title="Deeper Look"}

~~~python
import numpy as np

## Define vector x
x = [1,2,3]

## Compute the norm of x
xnorm = np.linalg.norm(x)

## Print the norm
print("xnorm: ", xnorm)
~~~

## How complex must a polymer model be to begin to capture critical features of folded proteins 

### What are the critical features of folded proteins?

#### Key constraints of folded proteins
Discuss the key constraints, such as, bond angles, bond dihedrals, side chains, etc. 
#### Key observables to check how protein-like the model is
Discuss the key observables we want to match, such as, core packing fraction, fraction core, scattering, etc. 

### Models



### Key results