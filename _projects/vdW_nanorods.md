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

---

### **The Approach: Bridging the Gaps**  
The key to the work was recognizing that there are a few limiting cases where the problem becomes much easier. For example:  
- When two rods are far apart, their interaction behaves like that of two point masses.  
- When they're nearly touching, the force looks more like the interaction between two plates.  
- If they are perfectly aligned, they behave like a set of stacked spheres.  

In this work we interpolate between these known cases to create a general equation that works across a wide range of distances and orientations. 

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