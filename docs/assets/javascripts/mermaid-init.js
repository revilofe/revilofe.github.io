(function () {
  function isDarkScheme() {
    // Material sets this attribute on <html>
    var scheme = document.documentElement.getAttribute("data-md-color-scheme");
    if (scheme) return scheme === "slate";

    return (
      window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches
    );
  }

  function mermaidConfig() {
    // Keep diagrams readable over dark backgrounds (white-ish strokes).
    // If you want this also in light mode, set both branches to the same values.
    var dark = isDarkScheme();
    return {
      startOnLoad: false,
      theme: "base",
      themeVariables: dark
        ? {
            // Higher contrast on dark backgrounds
            lineColor: "#ffffff",
            primaryBorderColor: "#ffffff",
            secondaryBorderColor: "#ffffff",
            tertiaryBorderColor: "#ffffff",
            noteBorderColor: "#ffffff",
            actorBorder: "#ffffff",
            actorLineColor: "#ffffff"
          }
        : {
            // Neutral, readable defaults on light backgrounds
            lineColor: "#1f2937",
            primaryBorderColor: "#1f2937",
            secondaryBorderColor: "#1f2937",
            tertiaryBorderColor: "#1f2937",
            noteBorderColor: "#1f2937",
            actorBorder: "#1f2937",
            actorLineColor: "#1f2937"
          }
    };
  }

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

  function enablePanZoom() {
    if (typeof window.svgPanZoom === "undefined") return;

    document.querySelectorAll(".mermaid > svg").forEach(function (svgEl) {
      // Avoid double-init across instant navigation.
      if (svgEl.dataset && svgEl.dataset.panzoom === "1") return;
      if (svgEl.dataset) svgEl.dataset.panzoom = "1";

      try {
        window.svgPanZoom(svgEl, {
          controlIconsEnabled: true,
          fit: true,
          center: true,
          zoomEnabled: true,
          panEnabled: true,
          dblClickZoomEnabled: true,
          mouseWheelZoomEnabled: true,
          minZoom: 0.2,
          maxZoom: 12,
          zoomScaleSensitivity: 0.35
        });
      } catch (e) {
        // If a diagram fails to init, don't break the whole page.
      }
    });
  }

  function initMermaid() {
    if (typeof window.mermaid === "undefined") return;

    ensureMermaidContainers();

    // Render diagrams after navigation changes (works with and without instant loading).
    window.mermaid.initialize(mermaidConfig());
    window.mermaid.run({ querySelector: ".mermaid" });

    // Attach pan/zoom controls to generated SVGs.
    enablePanZoom();
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(initMermaid);
  } else {
    document.addEventListener("DOMContentLoaded", initMermaid);
  }
})();
