(function () {
  function mermaidConfig() {
    return {
      startOnLoad: false,
      theme: "base",
      themeVariables: {
        primaryColor: "#ffffff",
        secondaryColor: "#ffffff",
        tertiaryColor: "#ffffff",

        lineColor: "#2563eb",
        primaryBorderColor: "#2563eb",
        secondaryBorderColor: "#2563eb",
        tertiaryBorderColor: "#2563eb",

        primaryTextColor: "#0b1220",
        secondaryTextColor: "#0b1220",
        tertiaryTextColor: "#0b1220",
        textColor: "#0b1220",

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
    document.querySelectorAll("pre.mermaid").forEach(function (preEl) {
      var codeEl = preEl.querySelector("code");
      var source = (codeEl || preEl).textContent || "";

      var containerEl = document.createElement("div");
      containerEl.className = "mermaid";
      containerEl.textContent = source;

      preEl.replaceWith(containerEl);
    });

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

      if (svgEl.dataset && svgEl.dataset.panzoom === "1") return;
      if (svgEl.dataset) svgEl.dataset.panzoom = "1";

      try {
        // Mermaid may inject an inline max-width (e.g. 204px) that makes diagrams tiny.
        if (svgEl.style && svgEl.style.maxWidth) svgEl.style.maxWidth = "";

        (function ensureSvgViewportSize() {
          try {
            var vb =
              svgEl.viewBox && svgEl.viewBox.baseVal
                ? svgEl.viewBox.baseVal
                : null;
            if (!vb || !vb.width || !vb.height) return;

            var containerWidth = containerEl.clientWidth || svgEl.clientWidth;
            if (!containerWidth) return;

            // Height proportional to the viewBox aspect ratio.
            var desiredHeight = Math.round(
              containerWidth * (vb.height / vb.width)
            );

            if (desiredHeight < 240) desiredHeight = 240;

            svgEl.style.height = desiredHeight + "px";
          } catch (e) {
          }
        })();

        // Create the toolbar before initializing svg-pan-zoom so fit/center uses
        // the final layout (otherwise the diagram can look clipped).
        var toolbarEl = containerEl.querySelector(":scope > .mermaid-toolbar");
        if (!toolbarEl) {
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

        toolbarEl.textContent = "";

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
        addButton("Reset", "Reset view", function () {
          panZoom.resetZoom();
          if (typeof panZoom.resetPan === "function") panZoom.resetPan();
          panZoom.center();
        });

        if (typeof panZoom.resize === "function") panZoom.resize();
        panZoom.fit();
        panZoom.center();
      } catch (e) {
      }
    });
  }

  function initMermaid() {
    if (typeof window.mermaid === "undefined") return;

    ensureMermaidContainers();

    window.mermaid.initialize(mermaidConfig());
    var runResult;
    try {
      runResult = window.mermaid.run({ querySelector: ".mermaid" });
    } catch (e) {
      return;
    }

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
