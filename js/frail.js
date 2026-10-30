// Theme toggle, phone contents menu, theme-matched figures and scroll position.
(function () {
  var root = document.documentElement;
  if ("scrollRestoration" in history) history.scrollRestoration = "manual";

  function setFigures() {
    var dark = root.dataset.theme === "dark";
    document.querySelectorAll("img[data-light]").forEach(function (img) {
      img.src = dark ? img.dataset.dark : img.dataset.light;
    });
  }

  function init() {
    document.querySelectorAll("figure.fig img").forEach(function (img) {
      var src = img.getAttribute("src");
      if (!/\.svg$/.test(src)) return;
      img.dataset.light = src;
      img.dataset.dark = src.replace(/\.svg$/, "-dark.svg");
    });
    setFigures();

    var themeBtn = document.getElementById("theme-btn");
    if (themeBtn) themeBtn.addEventListener("click", function () {
      root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
      try { localStorage.setItem("frail-theme", root.dataset.theme); } catch (e) {}
      setFigures();
    });

    var menuBtn = document.getElementById("menu-btn");
    if (menuBtn) menuBtn.addEventListener("click", function () {
      var open = document.body.classList.toggle("toc-open");
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
      menuBtn.textContent = open ? "Close" : "Contents";
    });

    if (!location.hash) window.scrollTo(0, 0);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
