console.log("custom.js loaded");
// js code to work with css code to make sections expandable and collapsible
document.addEventListener("DOMContentLoaded", () => {
  const headings = document.querySelectorAll("h2, h3");

  headings.forEach(h => {
    const next = h.nextElementSibling;
    if (!next || !next.classList.contains("toggle-content")) return;

    // start collapsed
    h.classList.add("toggle-closed");

    h.addEventListener("click", () => {
      if (h.classList.contains("toggle-closed")) {
        h.classList.remove("toggle-closed");
        h.classList.add("toggle-open");
      } else {
        h.classList.remove("toggle-open");
        h.classList.add("toggle-closed");
      }
    });
  });
});


document.addEventListener("DOMContentLoaded", function () {
  const typedTarget = document.getElementById("typed-role");
  if (!typedTarget) return;

  const phrases = [
    "AI for Science",
    "Scientific Machine Learning",
    "Quantitative Modeling",
    "Computational Physics"
  ];

  let phraseIndex = 0;
  let charIndex = 0;
  let deleting = false;

  function typeLoop() {
    const phrase = phrases[phraseIndex];

    typedTarget.textContent = deleting
      ? phrase.slice(0, charIndex--)
      : phrase.slice(0, charIndex++);

    if (!deleting && charIndex > phrase.length) {
      deleting = true;
      setTimeout(typeLoop, 1200);
      return;
    }

    if (deleting && charIndex < 0) {
      deleting = false;
      phraseIndex = (phraseIndex + 1) % phrases.length;
      charIndex = 0;
    }

    setTimeout(typeLoop, deleting ? 35 : 65);
  }

  typeLoop();
});
