# Ducofex Language Switch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Turkish/English language switching with default Turkish plus YouTube integration across the active Ducofex pages.

**Architecture:** Keep the static HTML site structure and add a small client-side i18n layer driven by `data-i18n` attributes and a shared language dictionary. Persist the selected language in `localStorage`, apply it on load across all active pages, and add the language toggle plus YouTube link into the shared header/footer shell.

**Tech Stack:** Static HTML, CSS, existing JavaScript, Python validation script

---

## File map

**Create**
- `products/cnc/web/website_v1/Option1/js/ducofex-i18n.js`
- `tools/validate_ducofex_i18n.py`

**Modify**
- `products/cnc/web/website_v1/Option1/index.html`
- `products/cnc/web/website_v1/Option1/machines.html`
- `products/cnc/web/website_v1/Option1/gen-1.html`
- `products/cnc/web/website_v1/Option1/gen-2.html`
- `products/cnc/web/website_v1/Option1/about-us.html`
- `products/cnc/web/website_v1/Option1/contact-us.html`
- `products/cnc/web/website_v1/Option1/partners.html`
- `products/cnc/web/website_v1/Option1/printing-3d.html`
- `products/cnc/web/website_v1/Option1/printable-models.html`
- `products/cnc/web/website_v1/Option1/lokumai.html`
- `products/cnc/web/website_v1/Option1/css/ducofex-theme.css`
- `products/cnc/web/website_v1/Option1/js/functions.js`

### Task 1: Add failing i18n validator first

**Files:**
- Create: `tools/validate_ducofex_i18n.py`
- Test: `tools/validate_ducofex_i18n.py`

- [ ] **Step 1: Write the failing validation script**

```python
from pathlib import Path

ROOT = Path("products/cnc/web/website_v1/Option1")
PAGES = [
    "index.html",
    "machines.html",
    "gen-1.html",
    "gen-2.html",
    "about-us.html",
    "contact-us.html",
    "partners.html",
    "printing-3d.html",
    "printable-models.html",
    "lokumai.html",
]

def main() -> int:
    errors = []
    for page in PAGES:
        html = (ROOT / page).read_text(encoding="utf-8")
        if 'data-lang-toggle="tr"' not in html:
            errors.append(f"{page}: missing TR toggle")
        if 'data-lang-toggle="en"' not in html:
            errors.append(f"{page}: missing EN toggle")
        if 'js/ducofex-i18n.js' not in html:
            errors.append(f"{page}: missing i18n script include")
        if 'https://www.youtube.com/@Ducofex' not in html:
            errors.append(f"{page}: missing youtube link")
    script_path = ROOT / "js/ducofex-i18n.js"
    if not script_path.exists():
        errors.append("missing js/ducofex-i18n.js")
    if errors:
        print("I18N VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("I18N VALIDATION PASSED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: Run the validator to verify it fails**

Run:

```bash
python3 tools/validate_ducofex_i18n.py
```

Expected:

```text
I18N VALIDATION FAILED
```

- [ ] **Step 3: Keep the existing site validator available**

Run:

```bash
python3 tools/validate_ducofex_site.py
```

Expected:

```text
VALIDATION PASSED
```

### Task 2: Add shared language toggle and YouTube shell

**Files:**
- Modify: `products/cnc/web/website_v1/Option1/index.html`
- Modify: `products/cnc/web/website_v1/Option1/machines.html`
- Modify: `products/cnc/web/website_v1/Option1/gen-1.html`
- Modify: `products/cnc/web/website_v1/Option1/gen-2.html`
- Modify: `products/cnc/web/website_v1/Option1/about-us.html`
- Modify: `products/cnc/web/website_v1/Option1/contact-us.html`
- Modify: `products/cnc/web/website_v1/Option1/partners.html`
- Modify: `products/cnc/web/website_v1/Option1/printing-3d.html`
- Modify: `products/cnc/web/website_v1/Option1/printable-models.html`
- Modify: `products/cnc/web/website_v1/Option1/lokumai.html`
- Modify: `products/cnc/web/website_v1/Option1/css/ducofex-theme.css`

- [ ] **Step 1: Add shared top-strip controls to each active page**

```html
<div class="top-strip-actions">
  <a href="mailto:info@ducofex.com" class="pull-left">info@ducofex.com</a>
  <a href="https://www.youtube.com/@Ducofex" target="_blank" rel="noopener" class="ducofex-social-link">YouTube</a>
  <div class="ducofex-lang-switch" aria-label="Language switcher">
    <button type="button" data-lang-toggle="tr" class="is-active">TR</button>
    <span>/</span>
    <button type="button" data-lang-toggle="en">EN</button>
  </div>
</div>
```

- [ ] **Step 2: Add supporting CSS**

```css
.top-strip-actions{
  display:flex;
  align-items:center;
  gap:14px;
  margin-left:auto;
}

.ducofex-lang-switch{
  display:inline-flex;
  align-items:center;
  gap:8px;
}

.ducofex-lang-switch button{
  background:none;
  border:none;
  color:var(--ducofex-text-soft);
}

.ducofex-lang-switch button.is-active{
  color:var(--ducofex-heading);
}
```

- [ ] **Step 3: Run the i18n validator and confirm it still fails only on missing script and untranslated markup**

Run:

```bash
python3 tools/validate_ducofex_i18n.py
```

Expected: still failing because `js/ducofex-i18n.js` and `data-i18n` behavior are not added yet.

### Task 3: Add the language engine

**Files:**
- Create: `products/cnc/web/website_v1/Option1/js/ducofex-i18n.js`
- Modify: `products/cnc/web/website_v1/Option1/js/functions.js`

- [ ] **Step 1: Write the shared language file**

```javascript
(function () {
  const storageKey = 'ducofex-language';
  const defaultLang = 'tr';

  function getLang() {
    return localStorage.getItem(storageKey) || defaultLang;
  }

  function setLang(lang) {
    localStorage.setItem(storageKey, lang);
    document.documentElement.lang = lang;
    document.querySelectorAll('[data-i18n]').forEach((node) => {
      const key = node.getAttribute('data-i18n');
      const value = window.DUCOFEX_I18N?.[lang]?.[key];
      if (value) node.textContent = value;
    });
    document.querySelectorAll('[data-lang-toggle]').forEach((button) => {
      button.classList.toggle('is-active', button.getAttribute('data-lang-toggle') === lang);
    });
  }

  window.applyDucofexLanguage = setLang;
  window.getDucofexLanguage = getLang;

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-lang-toggle]').forEach((button) => {
      button.addEventListener('click', function () {
        setLang(button.getAttribute('data-lang-toggle'));
      });
    });
    setLang(getLang());
  });
})();
```

- [ ] **Step 2: Load the new script on every active page**

```html
<script src="js/ducofex-i18n.js"></script>
<script src="js/functions.js"></script>
```

- [ ] **Step 3: Re-run the i18n validator**

Run:

```bash
python3 tools/validate_ducofex_i18n.py
```

Expected: still failing because translated content keys are not wired yet.

### Task 4: Wire Turkish and English content on active pages

**Files:**
- Modify: all 10 active HTML files
- Modify: `products/cnc/web/website_v1/Option1/js/ducofex-i18n.js`

- [ ] **Step 1: Mark translatable nodes**

```html
<a href="machines.html" data-i18n="nav.machines">Makineler</a>
<h1 data-i18n="home.hero.title">Büyüyen atölyeler, üretim ekipleri ve iddialı endüstriyel iş ortakları için hassas makineler.</h1>
<a class="ducofex-btn" href="machines.html" data-i18n="home.hero.primaryCta">Makineleri İncele</a>
```

- [ ] **Step 2: Add Turkish and English dictionary entries**

```javascript
window.DUCOFEX_I18N = {
  tr: {
    'nav.home': 'Ana Sayfa',
    'nav.machines': 'Makineler',
    'nav.printing': '3D Baskı',
    'nav.models': 'Basılabilir Modeller',
    'nav.partners': 'İş Ortaklıkları',
    'nav.about': 'Hakkımızda',
    'nav.contact': 'İletişim',
    'home.hero.primaryCta': 'Makineleri İncele'
  },
  en: {
    'nav.home': 'Home',
    'nav.machines': 'Machines',
    'nav.printing': '3D Printing',
    'nav.models': 'Printable Models',
    'nav.partners': 'Partners',
    'nav.about': 'About',
    'nav.contact': 'Contact',
    'home.hero.primaryCta': 'Review Machines'
  }
};
```

- [ ] **Step 3: Run both validators**

Run:

```bash
python3 tools/validate_ducofex_i18n.py && python3 tools/validate_ducofex_site.py
```

Expected:

```text
I18N VALIDATION PASSED
VALIDATION PASSED
```

### Task 5: Verify behavior in the browser

**Files:**
- Test: active live pages in the browser

- [ ] **Step 1: Start a local server**

Run:

```bash
python3 -m http.server 8002
```

Expected: local preview is available.

- [ ] **Step 2: Verify default language**

Check:

```text
Index page opens in Turkish and TR appears active.
```

- [ ] **Step 3: Verify language persistence and YouTube visibility**

Check:

```text
Switch to EN, navigate to another active page, and confirm EN stays active.
Confirm the YouTube link points to https://www.youtube.com/@Ducofex.
```

## Self-review

- Spec coverage: dil seçici, varsayılan TR, kalıcılık, YouTube entegrasyonu ve canlı sayfa kapsamı görevlerde karşılanıyor.
- Placeholder scan: boş `TBD` alanı yok.
- Type consistency: `data-lang-toggle`, `data-i18n`, `window.DUCOFEX_I18N`, `applyDucofexLanguage` isimleri tüm planda tutarlı.

## Execution handoff

Plan complete and saved to `docs/superpowers/plans/2026-06-13-ducofex-language-switch.md`.

Two execution options:

**1. Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints

Which approach?
