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
