---
layout: page
title: "CV"
permalink: /cv/
---

{%comment%}
# My CV
{%endcomment%}

<object data="/assets/docs/CV_short.pdf" type="application/pdf" width="100%" height="600px">
  <p>It looks like your browser doesn't support PDFs. You can <a href="/assets/docs/CV_short.pdf">download the file here</a>.</p>
</object>

<div class="pdf-container">
  <object data="/assets/docs/my_cv.pdf" type="application/pdf"></object>
</div>

<style>
.pdf-container {
  width: 100%;
  max-width: 800px; /* Limits the max size on large screens */
  height: 90vh; /* Adjusts height based on screen */
  margin: auto; /* Centers it */
}

.pdf-container object {
  width: 100%;
  height: 100%;
}
</style>





<button onclick="window.location.href='/assets/docs/my_cv.pdf'" class="cv-button">
  <i class="fa fa-download"></i> Download CV
</button>

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


