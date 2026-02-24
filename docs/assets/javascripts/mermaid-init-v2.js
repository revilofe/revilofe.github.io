(function () {
  function mermaidConfig() {
    return {
      startOnLoad: false,
      theme: "base",
      themeVariables: {
        fontSize: "11px",
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

  function ensureOverlay() {
    var existing = document.getElementById("mermaid-overlay");
    if (existing && existing.__overlayState) return existing.__overlayState;

    var overlayEl = existing || document.createElement("div");
    overlayEl.id = "mermaid-overlay";
    overlayEl.className = "mermaid-overlay";

    var backdropEl = document.createElement("div");
    backdropEl.className = "mermaid-overlay-backdrop";

    var frameEl = document.createElement("div");
    frameEl.className = "mermaid-overlay-frame";

    var headerEl = document.createElement("div");
    headerEl.className = "mermaid-overlay-header";

    var titleEl = document.createElement("div");
    titleEl.className = "mermaid-overlay-title";
    titleEl.textContent = "Explorar diagrama";

    var actionsEl = document.createElement("div");
    actionsEl.className = "mermaid-overlay-actions";

    var bodyEl = document.createElement("div");
    bodyEl.className = "mermaid-overlay-body";

    headerEl.appendChild(titleEl);
    headerEl.appendChild(actionsEl);
    frameEl.appendChild(headerEl);
    frameEl.appendChild(bodyEl);
    overlayEl.appendChild(backdropEl);
    overlayEl.appendChild(frameEl);

    if (!existing) document.body.appendChild(overlayEl);

    var overlayState = {
      root: overlayEl,
      backdrop: backdropEl,
      frame: frameEl,
      header: headerEl,
      body: bodyEl,
      actions: actionsEl,
      panZoom: null,
      dragging: false,
      dragOffsetX: 0,
      dragOffsetY: 0
    };

    function closeOverlay() {
      overlayState.root.classList.remove("is-open");
      if (overlayState.panZoom && typeof overlayState.panZoom.destroy === "function") {
        overlayState.panZoom.destroy();
      }
      overlayState.panZoom = null;
      overlayState.body.textContent = "";
    }

    function addAction(label, title, onClick) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "mermaid-overlay-btn";
      btn.textContent = label;
      btn.title = title;
      btn.addEventListener("click", function (event) {
        event.preventDefault();
        onClick();
      });
      overlayState.actions.appendChild(btn);
    }

    addAction("+", "Acercar", function () {
      if (overlayState.panZoom) overlayState.panZoom.zoomIn();
    });
    addAction("-", "Alejar", function () {
      if (overlayState.panZoom) overlayState.panZoom.zoomOut();
    });
    addAction("Fit", "Ajustar", function () {
      if (!overlayState.panZoom) return;
      overlayState.panZoom.fit();
      overlayState.panZoom.center();
    });
    addAction("Reset", "Escala 100%", function () {
      if (!overlayState.panZoom) return;
      if (typeof overlayState.panZoom.zoom === "function") overlayState.panZoom.zoom(1);
      if (typeof overlayState.panZoom.center === "function") overlayState.panZoom.center();
    });
    addAction("Cerrar", "Cerrar ventana", closeOverlay);

    overlayState.backdrop.addEventListener("click", closeOverlay);

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") closeOverlay();
    });

    overlayState.header.addEventListener("mousedown", function (event) {
      if (event.target && event.target.closest("button")) return;

      overlayState.dragging = true;
      overlayState.dragOffsetX = event.clientX - overlayState.frame.offsetLeft;
      overlayState.dragOffsetY = event.clientY - overlayState.frame.offsetTop;
      document.body.classList.add("mermaid-overlay-dragging");
    });

    document.addEventListener("mousemove", function (event) {
      if (!overlayState.dragging) return;

      var nextLeft = event.clientX - overlayState.dragOffsetX;
      var nextTop = event.clientY - overlayState.dragOffsetY;

      var maxLeft = Math.max(0, window.innerWidth - overlayState.frame.offsetWidth);
      var maxTop = Math.max(0, window.innerHeight - overlayState.frame.offsetHeight);

      if (nextLeft < 0) nextLeft = 0;
      if (nextTop < 0) nextTop = 0;
      if (nextLeft > maxLeft) nextLeft = maxLeft;
      if (nextTop > maxTop) nextTop = maxTop;

      overlayState.frame.style.left = nextLeft + "px";
      overlayState.frame.style.top = nextTop + "px";
    });

    document.addEventListener("mouseup", function () {
      overlayState.dragging = false;
      document.body.classList.remove("mermaid-overlay-dragging");
    });

    overlayEl.__overlayState = overlayState;
    return overlayState;
  }

  function openOverlayWithDiagram(sourceSvgEl) {
    if (!sourceSvgEl || typeof window.svgPanZoom === "undefined") return;

    var overlayState = ensureOverlay();

    overlayState.root.classList.add("is-open");
    overlayState.body.textContent = "";

    if (overlayState.panZoom && typeof overlayState.panZoom.destroy === "function") {
      overlayState.panZoom.destroy();
    }
    overlayState.panZoom = null;

    var overlaySvg = sourceSvgEl.cloneNode(true);
    if (overlaySvg.style && overlaySvg.style.maxWidth) overlaySvg.style.maxWidth = "";
    overlaySvg.removeAttribute("data-panzoom");
    overlayState.body.appendChild(overlaySvg);

    overlayState.panZoom = window.svgPanZoom(overlaySvg, {
      controlIconsEnabled: false,
      fit: true,
      center: true,
      zoomEnabled: true,
      panEnabled: true,
      dblClickZoomEnabled: true,
      mouseWheelZoomEnabled: true,
      minZoom: 0.2,
      maxZoom: 16,
      zoomScaleSensitivity: 0.3
    });

    if (typeof overlayState.panZoom.resize === "function") overlayState.panZoom.resize();
    overlayState.panZoom.fit();
    overlayState.panZoom.center();
  }

  function setSvgNaturalSize(svgEl) {
    if (!svgEl) return;

    try {
      var vb = svgEl.viewBox && svgEl.viewBox.baseVal ? svgEl.viewBox.baseVal : null;
      if (!vb || !vb.width || !vb.height) return;

      svgEl.style.width = Math.round(vb.width) + "px";
      svgEl.style.height = "auto";
    } catch (e) {
    }
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
        setSvgNaturalSize(svgEl);

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
          fit: false,
          center: false,
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
        addButton("Reset", "Reset zoom (100%)", function () {
          // `resetZoom()` would return to the initial zoom, which is often the same
          // as "fit" because we initialize with fit/center. Make Reset distinct:
          // go to 1:1 zoom and centered.
          if (typeof panZoom.zoom === "function") panZoom.zoom(1);
          if (typeof panZoom.pan === "function") panZoom.pan({ x: 0, y: 0 });
        });
        addButton("Ventana", "Abrir en panel superpuesto", function () {
          openOverlayWithDiagram(svgEl);
        });

        if (typeof panZoom.resize === "function") panZoom.resize();
        if (typeof panZoom.zoom === "function") panZoom.zoom(1);
        if (typeof panZoom.pan === "function") panZoom.pan({ x: 0, y: 0 });
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
