---
layout: default
title: "Symmetrized Bond Order Parameters"
date:        2 Jan 2014
image: 
  path:    /assets/img/SymBOPs_general/SymBOPs_main_full.png
  srcset:
  1920w:   /assets/img/SymBOPs_general/SymBOPs_main_full.png
  960w:    /assets/img/SymBOPs_general/SymBOPs_main_half.png
  480w:    /assets/img/SymBOPs_general/SymBOPs_main_quarter.png
caption: "Exploring SymBOPs with different particle types."
description: >
  SymBOPs projects
links:
  - title: Publication
    url:     https://doi.org/10.1063/5.0076915
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
