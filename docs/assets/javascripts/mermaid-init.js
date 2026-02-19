(function () {
  function ensureMermaidContainers() {
    // Case 1: Mermaid fences rendered via custom_fences:
    //   <pre class="mermaid"><code>...</code></pre>
    document.querySelectorAll("pre.mermaid").forEach(function (preEl) {
      var codeEl = preEl.querySelector("code");
      var source = (codeEl || preEl).textContent || "";

      var containerEl = document.createElement("div");
      containerEl.className = "mermaid";
      containerEl.textContent = source;

      preEl.replaceWith(containerEl);
    });

    // Case 2: Mermaid fences rendered as regular code blocks with a language class.
    document
      .querySelectorAll("pre > code.language-mermaid, pre > code.lang-mermaid")
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
