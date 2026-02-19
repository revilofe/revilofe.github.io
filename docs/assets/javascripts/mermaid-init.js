(function () {
  function ensureMermaidContainers() {
    document
      .querySelectorAll("pre > code.language-mermaid")
      .forEach(function (codeEl) {
        var preEl = codeEl.parentElement;
        if (!preEl) return;

        var containerEl = document.createElement("div");
        containerEl.className = "mermaid";
        containerEl.textContent = codeEl.textContent || "";

        preEl.replaceWith(containerEl);
      });
  }

  function initMermaid() {
    if (typeof window.mermaid === "undefined") return;

    ensureMermaidContainers();

    // Render diagrams after navigation changes (works with and without instant loading).
    window.mermaid.initialize({ startOnLoad: false });
    window.mermaid.run({ querySelector: ".mermaid" });
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(initMermaid);
  } else {
    document.addEventListener("DOMContentLoaded", initMermaid);
  }
})();
