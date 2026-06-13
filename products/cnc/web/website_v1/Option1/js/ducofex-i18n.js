(function () {
  var STORAGE_KEY = "ducofex-language";
  var DEFAULT_LANG = "tr";

  function getCurrentLanguage() {
    try {
      return localStorage.getItem(STORAGE_KEY) || DEFAULT_LANG;
    } catch (error) {
      return DEFAULT_LANG;
    }
  }

  function setStoredLanguage(lang) {
    try {
      localStorage.setItem(STORAGE_KEY, lang);
    } catch (error) {
      return;
    }
  }

  function applyLanguage(lang) {
    var safeLang = (lang === "en") ? "en" : "tr";
    document.documentElement.lang = safeLang;

    var nodes = document.querySelectorAll("[data-i18n-tr][data-i18n-en]");
    nodes.forEach(function (node) {
      var value = node.getAttribute("data-i18n-" + safeLang);
      if (value !== null) {
        node.textContent = value;
      }
    });

    var buttons = document.querySelectorAll("[data-lang-toggle]");
    buttons.forEach(function (button) {
      var isActive = button.getAttribute("data-lang-toggle") === safeLang;
      button.classList.toggle("is-active", isActive);
      button.setAttribute("aria-pressed", isActive ? "true" : "false");
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    var currentLanguage = getCurrentLanguage();

    document.querySelectorAll("[data-lang-toggle]").forEach(function (button) {
      button.addEventListener("click", function () {
        var selectedLanguage = button.getAttribute("data-lang-toggle");
        setStoredLanguage(selectedLanguage);
        applyLanguage(selectedLanguage);
      });
    });

    applyLanguage(currentLanguage);
  });
})();
