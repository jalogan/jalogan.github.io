---
layout: default
title: "Symmetrized Bond Order Parameters"
#date:        2 Jan 2014
order: 3
image: 
  path:    /assets/img/SymBOPs_general/SymBOPs_main_full_w_bg.png
  srcset:
  1920w:   /assets/img/SymBOPs_general/SymBOPs_main_full_w_bg.png
  960w:    /assets/img/SymBOPs_general/SymBOPs_main_half.png
  480w:    /assets/img/SymBOPs_general/SymBOPs_main_quarter.png
caption: "Exploring SymBOPs with different particle types."
#description: >
#  SymBOPs projects
#links:
#  - title: Publication
#    url:     https://doi.org/10.1063/5.0076915
featured:    false
redirect_from:
  - "/SymBOPs"
---


{%comment%}
<h1>{{ page.title }}</h1>
{%endcomment%}

<div class="grid">
  {% for project in site.projects %}
    {% if project.category == "SymBOPs" %}
      <div class="grid-item">
        <a href="{{ project.url }}">
          {% if project.image %}
            <img src="{{ project.image.path }}" alt="{{ project.title }}">
          {% endif %}
          <h2>{{ project.title }}</h2>
          <p>{{ project.caption }}</p>
        </a>
      </div>
    {% endif %}
  {% endfor %}
</div>






### **Brief orientational order overview**


<figure style="max-width: 100%; text-align: center; margin: auto;">
  <img src="{{ "/assets/img/SymBOPs_general/symmetry_of_circle_vs_rod.png" | relative_url }}" alt="Figure Description"
       style="width: 100%; height: auto; max-width: 600px;">
  <figcaption style="font-size: 0.9em; color: #666; margin-top: 5px;">
    Difference of rotational symmetry between a circle and a cirlce with two differently colored points.
  </figcaption>
</figure>




Rotational symmetry is used to describe an object or set of objects (or points, equations, etc.) that is unaffected by rotations. A 2-sphere in three-dimensions, for instance, has the full symmetry of the rotation group SO(3). We can rotate it in any manner that we'd like and it never looks any different. To make things easier to visualize let's think of a circle (1-sphere) in two-dimensions. Any rotation of the circle leaves it unchanged. If we place two differently colored points on opposite ends of a chord that goes through the center of the circle, everything changes. Now any rotation we choose other than a multiple of $$2\pi$$ gives a different picture from what we started with. The symmetry we had has been broken and only repeats when we rotate by $$2\pi n$$, where $$n$$ is an integer.


<figure style="max-width: 100%; text-align: center; margin: auto;">
  <img src="{{ "/assets/img/SymBOPs_general/BOP_and_nematic_rods_full.png" | relative_url }}" alt="Figure Description"
       style="width: 100%; height: auto; max-width: 800px;">
  <figcaption style="font-size: 0.9em; color: #666; margin-top: 5px;">
    Simple example using rods to demonstrate the difference between bond-orientational order, nematic order, and the combination of both.
  </figcaption>
</figure>


Orientational order looks at the rotational symmetry of an object or group of obejcts. There are two types of orientational order that we must distinguish between. 









### Links

<a href="https://doi.org/10.1063/5.0076915" class="info-button" target="_blank">
  <span class="icon-book" style="font-size: 32px;"></span> Symmetry-specific orientational order parameters for complex structures
</a>

<a href="https://doi.org/10.1063/5.0076914" class="info-button" target="_blank">
  <span class="icon-book" style="font-size: 32px;"></span> Controlling morphology in hybrid isotropic/patchy particle assemblies
</a>

<a href="https://doi.org/10.1063/5.0168604" class="info-button" target="_blank">
  <span class="icon-book" style="font-size: 32px;"></span> Symmetry-specific characterization of bond orientation order in DNA-assembled nanoparticle lattices
</a>


<style>
  /* Remove any arrows on external links */
  .info-button::after {
    content: none !important;
  }
</style>


<style>
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
  }
  .grid-item {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
    border: 1px solid #ddd;
    padding: 15px;
    text-align: center;
    transition: transform 0.3s ease;
  }
  .grid-item:hover {
    transform: scale(1.05);
  }
  .grid-item img {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }
  .grid-item h2 {
    margin-top: auto;
  }
</style>







