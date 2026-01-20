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
