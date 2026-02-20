(function () {
  function mermaidConfig() {
    // Opinionated defaults:
    // - White class/object boxes (high readability in light and dark schemes)
    // - Blue borders/lines for contrast
    return {
      startOnLoad: false,
      theme: "base",
      themeVariables: {
        primaryColor: "#ffffff",
        secondaryColor: "#ffffff",
        tertiaryColor: "#ffffff",

        // Strokes, arrows, borders
        lineColor: "#2563eb",
        primaryBorderColor: "#2563eb",
        secondaryBorderColor: "#2563eb",
        tertiaryBorderColor: "#2563eb",

        // Text
        primaryTextColor: "#0b1220",
        secondaryTextColor: "#0b1220",
        tertiaryTextColor: "#0b1220",
        textColor: "#0b1220",

        // Notes/actors (used in other diagrams too)
        noteBkgColor: "#ffffff",
        noteBorderColor: "#2563eb",
        noteTextColor: "#0b1220",
        actorBkg: "#ffffff",
        actorBorder: "#2563eb",
        actorTextColor: "#0b1220",
        actorLineColor: "#2563eb"
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

    document.querySelectorAll(".mermaid").forEach(function (containerEl) {
      var svgEl = containerEl.querySelector(":scope > svg");
      if (!svgEl) return;

      // Avoid double-init across instant navigation.
      if (svgEl.dataset && svgEl.dataset.panzoom === "1") return;
      if (svgEl.dataset) svgEl.dataset.panzoom = "1";

      try {
        // Create the toolbar *before* initializing svg-pan-zoom so initial fit/center
        // calculations match the final layout (prevents diagrams looking clipped).
        var toolbarEl;
        if (containerEl.dataset && containerEl.dataset.panzoomToolbar === "1") {
          toolbarEl = containerEl.querySelector(":scope > .mermaid-toolbar");
        } else {
          if (containerEl.dataset) containerEl.dataset.panzoomToolbar = "1";
          toolbarEl = document.createElement("div");
          toolbarEl.className = "mermaid-toolbar";
          containerEl.insertBefore(toolbarEl, svgEl);
        }

        var panZoom = window.svgPanZoom(svgEl, {
          controlIconsEnabled: false,
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

        function addButton(label, title, onClick) {
          var btn = document.createElement("button");
          btn.type = "button";
          btn.className = "mermaid-btn";
          btn.textContent = label;
          btn.title = title;
          btn.addEventListener("click", function (e) {
            e.preventDefault();
            onClick();
          });
          toolbarEl.appendChild(btn);
        }

        // Rebuild toolbar contents once (defensive: toolbarEl can be reused on nav).
        if (toolbarEl) toolbarEl.textContent = "";

        addButton("+", "Zoom in", function () {
          panZoom.zoomIn();
        });
        addButton("-", "Zoom out", function () {
          panZoom.zoomOut();
        });
        addButton("Fit", "Fit diagram", function () {
          panZoom.fit();
          panZoom.center();
        });
        addButton("Reset", "Reset zoom", function () {
          panZoom.resetZoom();
          panZoom.fit();
          panZoom.center();
        });

        // Ensure the diagram is fitted after the toolbar affects layout.
        if (typeof panZoom.resize === "function") panZoom.resize();
        panZoom.fit();
        panZoom.center();
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
    var runResult;
    try {
      runResult = window.mermaid.run({ querySelector: ".mermaid" });
    } catch (e) {
      // If Mermaid rendering fails, don't break the whole page.
      return;
    }

    // Mermaid v10 renders asynchronously. Initialize pan/zoom after SVG exists.
    if (runResult && typeof runResult.then === "function") {
      runResult.then(function () {
        enablePanZoom();
      });
    } else {
      enablePanZoom();
    }
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(initMermaid);
  } else {
    document.addEventListener("DOMContentLoaded", initMermaid);
  }
})();
