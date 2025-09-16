---
layout: page
title: "About Me"
#permalink: /about-me/
permalink: /         # ← becomes the home page
redirect_from:
  - /about-me/       # keep the old URL working (requires jekyll-redirect-from)
cover: true
#section: true
#order: 1
---

<div id="about"></div>


{%comment%}
# About Me
{%endcomment%}




<div style="max-width: 800px; margin: 0 auto; padding: 0 1rem;">
  <div style="display: flex; justify-content: center; align-items: center; gap: 12px;">
    <img src="/assets/img/about_me/about_me_photo_1.jpg" alt="Me"
         style="display:block; height: clamp(220px, 40vh, 420px); width: auto;">
    <img src="/assets/img/about_me/about_me_photo_2.jpg" alt="Me 2"
         style="display:block; height: clamp(220px, 40vh, 420px); width: auto;">
  </div>
</div>




## Background
I am a PhD physicist with expertise in mathematical modeling, computational modeling, data analysis, and high-performance computing. I have specialized in theoretical soft-condensed matter physics working on everything from order parameters, sphere packings to the structure of proteins and protein folding dynamics. My PhD in physics was completed at Stony Brook University, and my PhD research was done with Dr. Alexei V. Tkachenko as part of the Center for Funcitonal Nanomaterials' Theory and Computation Group at Brookhaven National Laboratory. My post-doctoral work was completed at Yale University with Dr. Corey O'Hern.

On this site you will find some of my past research with summaries or differing perspectives on the work and links to the publications, along with ongoing or current work.

My current interests include, but are not limited to, understanding artificial neural networks through the lens of mathematical physics to better understand how they internal connections and circuits emerge. Elimintating this black box is a key to developing future technologies that will revolutionize society and are, above all, safe for use.


{%comment%}
## Contact Info
📧 Email: myemail@example.com  
🔗 GitHub: [My GitHub](https://github.com/myprofile)  
🔗 LinkedIn: [My LinkedIn](https://linkedin.com/in/myprofile)
{%endcomment%}

## Other Resources

<div class="info-buttons">
  <a href="/cv/" class="info-button">
    <img src="/assets/img/buttons/cv_button_3.png" alt="View My CV" height="100">
  </a>

  <a href="https://github.com/jalogan" class="info-button">
    <img src="/assets/img/buttons/github_logo_lego_button.png" alt="GitHub" height="100">
  </a>

  <a href="https://www.linkedin.com/in/jacklogan-physicist/" class="info-button">
    <img src="/assets/img/buttons/linkedin_logo_lego_button.png" alt="LinkedIn" height="100">
  </a>

  <a href="https://jalogan.github.io/contact_me" class="info-button">
    <img src="/assets/img/buttons/contact_button_envelope.png" alt="Contact" height="100">
  </a>
</div>

<style>
.info-buttons {
  display: flex;
  justify-content: left; /* Centers the buttons */
  gap: 15px; /* Adds spacing between buttons */
}

.info-button img {
  height: 100px;
  width: auto;
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.info-button img:hover {
  transform: scale(1.1);
  opacity: 0.8;
}

/* Remove any arrows on external links */
.info-button::after {
  content: none !important;
}

</style>





{%comment%}
## My CV
[📄 View My CV](/cv/)  
<button onclick="window.location.href='/cv/'" class="cv-button">
  <i class="fa fa-file-pdf"></i> View My CV
</button>
{%endcomment%}


{%comment%}

<a href="/cv/" class="cv-image-button">
  <img src="/assets/img/buttons/cv_button_2.png" alt="View My CV">
</a>

<style>
.cv-image-button {
  display: inline-block;
  border: 3px solidrgb(255, 255, 255);
  border-radius: 10px;
  padding: 5px;
  transition: background 0.3s ease, transform 0.3s ease;
}

.cv-image-button img {
  display: block;
  width: 100px; /* Adjust size as needed */
  height: auto;
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.cv-image-button:hover {
  background: rgba(0, 115, 230, 0.1);
  transform: scale(1.05);
}

.cv-image-button img:hover {
  opacity: 0.8;
}
</style>

{%endcomment%}



{%comment%}

<style>
.cv-button {
  display: inline-flex;
  align-items: center;
  padding: 10px 15px;
  font-size: 16px;
  background-color: #0073e6;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  margin-top: 10px;
  transition: background 0.3s;
}

.cv-button:hover {
  background-color: #005bb5;
}

.cv-button i {
  margin-right: 8px;
}
</style>

{%endcomment%}


