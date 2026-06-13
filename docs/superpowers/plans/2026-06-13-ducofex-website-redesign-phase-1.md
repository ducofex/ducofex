# Ducofex Website Redesign Phase 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the Ducofex website front end into a strong brand-aligned marketing site focused on machine sales, trust, and future service expansion.

**Architecture:** Keep the site as a static multi-page HTML/CSS/JS project inside `products/cnc/web/website_v1/Option1`, but replace most of the template’s visual language and content structure. Use shared brand assets, one central override stylesheet, standardized shared page chrome, and focused page rewrites for the homepage, machine catalog, product pages, partnership page, and future-service teaser pages.

**Tech Stack:** Static HTML, CSS, existing Bootstrap/jQuery stack, lightweight Python validation script for content/link smoke checks

---

## Scope

This plan covers only Phase 1 from the approved spec:

- homepage redesign
- machine catalog and product pages
- shared navigation/footer/theme
- partner/sponsor positioning
- 3D printing / printable models / LokumAI teaser pages
- content cleanup and broken-path fixes

This plan does **not** implement:

- live checkout
- STL/3MF/OBJ upload flow
- Python pricing integration
- real order printing

## File map

### Existing files to modify

- `products/cnc/web/website_v1/Option1/index.html`
- `products/cnc/web/website_v1/Option1/machines.html`
- `products/cnc/web/website_v1/Option1/gen-1.html`
- `products/cnc/web/website_v1/Option1/gen-2.html`
- `products/cnc/web/website_v1/Option1/about-us.html`
- `products/cnc/web/website_v1/Option1/contact-us.html`
- `products/cnc/web/website_v1/Option1/style.css`
- `products/cnc/web/website_v1/Option1/css/color.css`
- `products/cnc/web/website_v1/Option1/js/functions.js`

### New files to create

- `products/cnc/web/website_v1/Option1/partners.html`
- `products/cnc/web/website_v1/Option1/printing-3d.html`
- `products/cnc/web/website_v1/Option1/printable-models.html`
- `products/cnc/web/website_v1/Option1/lokumai.html`
- `products/cnc/web/website_v1/Option1/css/ducofex-theme.css`
- `products/cnc/web/website_v1/Option1/images/brand/6x3.png`
- `products/cnc/web/website_v1/Option1/images/brand/hello-2.png`
- `tools/validate_ducofex_site.py`

### File responsibilities

- `index.html`: catalog-first landing page and visual flagship
- `machines.html`: machine overview and route into detail pages
- `gen-1.html`, `gen-2.html`: stronger product pages with clear CTA flow
- `partners.html`: sponsor / partner pitch and contact CTA
- `printing-3d.html`: service overview and future order path
- `printable-models.html`: teaser catalog concept page
- `lokumai.html`: coming soon page with brand-consistent framing
- `css/ducofex-theme.css`: brand palette, section styling, buttons, hero, cards, glow mode support
- `style.css` and `css/color.css`: minimal cleanup, mostly to prevent legacy styles from fighting the new theme
- `js/functions.js`: only small JS updates if needed for nav/menu polish or CTA behavior
- `tools/validate_ducofex_site.py`: static verification of required pages, nav labels, logo paths, and banned template words

## Implementation notes

- Prefer replacing weak template sections over editing them line by line.
- Keep shared navigation and footer consistent on every live page.
- Use `shared/branding/logo-design/6x3.png` and `shared/branding/logo-design/hello-2.png` as source assets, copied into the site’s own `images/brand/` folder for stable relative paths.
- Put most new styling into `css/ducofex-theme.css` so the redesign is easy to reason about and easier to toggle between restrained and neon-enhanced visuals.
- Leave old template-only pages alone unless they are linked from the main experience; focus only on the active path.
- Git commit steps are intentionally omitted from this plan because the user will manage commits manually.

### Task 1: Add brand assets and validation harness

**Files:**
- Create: `products/cnc/web/website_v1/Option1/images/brand/6x3.png`
- Create: `products/cnc/web/website_v1/Option1/images/brand/hello-2.png`
- Create: `tools/validate_ducofex_site.py`

- [ ] **Step 1: Copy the approved logo assets into the site**

Run:

```bash
mkdir -p "products/cnc/web/website_v1/Option1/images/brand" && cp "shared/branding/logo-design/6x3.png" "products/cnc/web/website_v1/Option1/images/brand/6x3.png" && cp "shared/branding/logo-design/hello-2.png" "products/cnc/web/website_v1/Option1/images/brand/hello-2.png"
```

Expected: both brand files exist in `images/brand/`.

- [ ] **Step 2: Write the failing site validation script**

```python
from pathlib import Path
import sys

ROOT = Path("products/cnc/web/website_v1/Option1")
PAGES = [
    "index.html",
    "machines.html",
    "gen-1.html",
    "gen-2.html",
    "about-us.html",
    "contact-us.html",
]
REQUIRED_NAV = [
    "Home",
    "Machines",
    "3D Printing",
    "Printable Models",
    "Partners",
    "About",
    "Contact",
    "LokumAI",
]
BANNED_WORDS = ["Library", "Books", "Authors", "Book Guide"]


def read_text(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def main() -> int:
    errors = []
    for page in PAGES:
        path = ROOT / page
        if not path.exists():
            errors.append(f"missing page: {page}")
            continue
        html = read_text(page)
        for nav_item in REQUIRED_NAV:
            if nav_item not in html:
                errors.append(f"{page}: missing nav item {nav_item}")
        if "images/brand/6x3.png" not in html:
            errors.append(f"{page}: missing brand logo path")
        for banned in BANNED_WORDS:
            if banned in html:
                errors.append(f"{page}: contains banned template word {banned}")
    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 3: Run the validation script to verify it fails**

Run:

```bash
python3 tools/validate_ducofex_site.py
```

Expected: `VALIDATION FAILED` because the current pages still use template words, old navigation, and old logo paths.

### Task 2: Build the shared Ducofex theme layer

**Files:**
- Create: `products/cnc/web/website_v1/Option1/css/ducofex-theme.css`
- Modify: `products/cnc/web/website_v1/Option1/index.html`
- Modify: `products/cnc/web/website_v1/Option1/machines.html`
- Modify: `products/cnc/web/website_v1/Option1/gen-1.html`
- Modify: `products/cnc/web/website_v1/Option1/gen-2.html`
- Modify: `products/cnc/web/website_v1/Option1/about-us.html`
- Modify: `products/cnc/web/website_v1/Option1/contact-us.html`

- [ ] **Step 1: Add the new theme stylesheet with brand tokens and shared components**

```css
:root{
  --ducofex-bg:#05070d;
  --ducofex-bg-soft:#0b1120;
  --ducofex-surface:#10192b;
  --ducofex-surface-2:#15213b;
  --ducofex-line:rgba(126,166,255,.18);
  --ducofex-primary:#4f7cff;
  --ducofex-primary-strong:#76a2ff;
  --ducofex-text:#f4f7ff;
  --ducofex-text-soft:#adb8d6;
  --ducofex-glow:0 0 30px rgba(79,124,255,.25);
  --ducofex-radius:20px;
}

body{
  background:
    radial-gradient(circle at top right, rgba(79,124,255,.20), transparent 35%),
    radial-gradient(circle at left center, rgba(44,85,255,.14), transparent 28%),
    linear-gradient(180deg, #04060b 0%, #08101d 55%, #05070d 100%);
  color:var(--ducofex-text);
}

.ducofex-shell{
  background:transparent;
}

.ducofex-section{
  padding:96px 0;
  position:relative;
}

.ducofex-card{
  background:linear-gradient(180deg, rgba(19,29,51,.92), rgba(11,17,32,.96));
  border:1px solid var(--ducofex-line);
  border-radius:var(--ducofex-radius);
  box-shadow:var(--ducofex-glow);
}

.ducofex-btn,
.ducofex-btn-secondary{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  min-height:52px;
  padding:0 24px;
  border-radius:999px;
  font-weight:700;
  letter-spacing:.02em;
  text-transform:uppercase;
}

.ducofex-btn{
  background:linear-gradient(135deg, var(--ducofex-primary), var(--ducofex-primary-strong));
  color:#fff;
  box-shadow:0 18px 40px rgba(79,124,255,.28);
}

.ducofex-btn-secondary{
  border:1px solid rgba(118,162,255,.45);
  color:var(--ducofex-text);
  background:rgba(10,17,31,.65);
}

.ducofex-hero{
  padding:120px 0 92px;
  position:relative;
  overflow:hidden;
}

.ducofex-hero:before{
  content:"";
  position:absolute;
  inset:0;
  background:
    radial-gradient(circle at 75% 20%, rgba(91,138,255,.32), transparent 24%),
    radial-gradient(circle at 15% 30%, rgba(51,94,255,.18), transparent 26%);
  pointer-events:none;
}

.ducofex-pill{
  display:inline-flex;
  align-items:center;
  gap:10px;
  padding:10px 16px;
  border:1px solid var(--ducofex-line);
  border-radius:999px;
  background:rgba(10,17,31,.72);
  color:var(--ducofex-text-soft);
}

.ducofex-nav-badge{
  margin-left:8px;
  padding:4px 8px;
  border-radius:999px;
  background:rgba(79,124,255,.16);
  color:var(--ducofex-primary-strong);
  font-size:11px;
  text-transform:uppercase;
}
```

- [ ] **Step 2: Link the new stylesheet after existing CSS on every live page**

```html
<link href="css/responsive.css" rel="stylesheet">
<link href="css/ducofex-theme.css" rel="stylesheet">
<link href="js/dl-menu/component.css" rel="stylesheet">
```

- [ ] **Step 3: Run a quick search to verify the stylesheet is linked everywhere**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
pages = ["index.html","machines.html","gen-1.html","gen-2.html","about-us.html","contact-us.html"]
root = Path("products/cnc/web/website_v1/Option1")
missing = [p for p in pages if 'css/ducofex-theme.css' not in (root/p).read_text(encoding='utf-8')]
print("missing" if missing else "all linked", missing)
PY
```

Expected: `all linked []`

### Task 3: Standardize shared header, footer, and navigation

**Files:**
- Modify: `products/cnc/web/website_v1/Option1/index.html`
- Modify: `products/cnc/web/website_v1/Option1/machines.html`
- Modify: `products/cnc/web/website_v1/Option1/gen-1.html`
- Modify: `products/cnc/web/website_v1/Option1/gen-2.html`
- Modify: `products/cnc/web/website_v1/Option1/about-us.html`
- Modify: `products/cnc/web/website_v1/Option1/contact-us.html`
- Create: `products/cnc/web/website_v1/Option1/partners.html`
- Create: `products/cnc/web/website_v1/Option1/printing-3d.html`
- Create: `products/cnc/web/website_v1/Option1/printable-models.html`
- Create: `products/cnc/web/website_v1/Option1/lokumai.html`

- [ ] **Step 1: Replace the shared header markup with brand-aligned navigation**

```html
<header class="header-3 ducofex-shell">
  <div class="container">
    <div class="logo-container">
      <div class="row">
        <div class="col-md-3">
          <div class="logo">
            <a href="index.html"><img src="images/brand/6x3.png" alt="Ducofex Industries"></a>
          </div>
        </div>
        <div class="col-md-9">
          <div class="top-strip">
            <div class="pull-left">
              <p>Advanced CNC systems, fabrication solutions, and future-ready manufacturing tools.</p>
            </div>
            <div class="social-icon">
              <a href="mailto:info@ducofex.com" class="pull-left">info@ducofex.com</a>
            </div>
          </div>
          <div class="kode-navigation">
            <ul>
              <li><a href="index.html">Home</a></li>
              <li><a href="machines.html">Machines</a></li>
              <li><a href="printing-3d.html">3D Printing</a></li>
              <li><a href="printable-models.html">Printable Models</a></li>
              <li><a href="partners.html">Partners</a></li>
              <li><a href="about-us.html">About</a></li>
              <li><a href="contact-us.html">Contact</a></li>
              <li><a href="lokumai.html">LokumAI <span class="ducofex-nav-badge">Coming Soon</span></a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</header>
```

- [ ] **Step 2: Replace the footer with a consistent CTA-driven version**

```html
<footer class="footer-2 ducofex-shell">
  <div class="container">
    <div class="lib-copyrights">
      <p>Ducofex Industries builds CNC systems and next-generation fabrication solutions.</p>
      <div class="social-icon">
        <ul>
          <li><a href="https://www.instagram.com/ducofex" title="Instagram"><i class="fa fa-instagram"></i></a></li>
          <li><a href="mailto:info@ducofex.com" title="Email"><i class="fa fa-envelope"></i></a></li>
        </ul>
      </div>
    </div>
    <div class="back-to-top">
      <a href="#top"><i class="fa fa-angle-up"></i></a>
    </div>
  </div>
</footer>
```

- [ ] **Step 3: Create the missing navigated pages with valid shared shell**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Partners | Ducofex Industries</title>
  <link href="style.css" rel="stylesheet">
  <link href="css/bootstrap.css" rel="stylesheet">
  <link href="css/color.css" rel="stylesheet">
  <link href="css/responsive.css" rel="stylesheet">
  <link href="css/ducofex-theme.css" rel="stylesheet">
</head>
<body id="top">
  <!-- shared header here -->
  <section class="ducofex-section">
    <div class="container">
      <div class="ducofex-card" style="padding:48px;">
        <div class="ducofex-pill">Partnerships</div>
        <h1>Build with Ducofex</h1>
        <p>We are open to strategic partnerships, sponsors, and distribution relationships that accelerate industrial innovation.</p>
        <a class="ducofex-btn" href="contact-us.html">Start a Conversation</a>
      </div>
    </div>
  </section>
  <!-- shared footer here -->
</body>
</html>
```

- [ ] **Step 4: Run the validator and verify it still fails only on content/template issues not missing pages**

Run:

```bash
python3 tools/validate_ducofex_site.py
```

Expected: still fails, but no longer reports missing required live pages once they are created and linked.

### Task 4: Rebuild the homepage into a catalog-first Ducofex landing page

**Files:**
- Modify: `products/cnc/web/website_v1/Option1/index.html`

- [ ] **Step 1: Replace the current banner with a Ducofex hero**

```html
<section class="ducofex-hero">
  <div class="container">
    <div class="row">
      <div class="col-md-7">
        <div class="ducofex-pill">
          <img src="images/brand/hello-2.png" alt="" width="28" height="28">
          CNC systems built for serious production
        </div>
        <h1>Precision machines. Stronger manufacturing. A brand built to grow.</h1>
        <p>Ducofex Industries develops advanced CNC systems, scalable fabrication solutions, and future-ready tools for makers, workshops, and industrial partners.</p>
        <div class="caption-btns">
          <a class="ducofex-btn" href="machines.html">View Machines</a>
          <a class="ducofex-btn-secondary" href="contact-us.html">Request Quote</a>
        </div>
      </div>
      <div class="col-md-5">
        <div class="ducofex-card" style="padding:28px;">
          <h3>What Ducofex offers</h3>
          <ul>
            <li>CNC machine lines for different buyer needs</li>
            <li>Future-ready 3D printing solutions</li>
            <li>Partner and sponsor opportunities</li>
            <li>Printable model ecosystem in progress</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Add machine category, featured machine, trust, partner, and future-service sections**

```html
<section class="ducofex-section">
  <div class="container">
    <div class="row">
      <div class="col-md-4">
        <div class="ducofex-card" style="padding:32px;">
          <h3>Starter and workshop systems</h3>
          <p>For makers, independent workshops, and growing fabrication teams.</p>
          <a class="ducofex-btn-secondary" href="gen-1.html">Explore Gen-1</a>
        </div>
      </div>
      <div class="col-md-4">
        <div class="ducofex-card" style="padding:32px;">
          <h3>Higher-output CNC platforms</h3>
          <p>For teams that need more capability, stronger precision, and room to scale.</p>
          <a class="ducofex-btn-secondary" href="gen-2.html">Explore Gen-2</a>
        </div>
      </div>
      <div class="col-md-4">
        <div class="ducofex-card" style="padding:32px;">
          <h3>Custom growth paths</h3>
          <p>For buyers, backers, and partners who want to build with us early.</p>
          <a class="ducofex-btn-secondary" href="partners.html">Partner with Ducofex</a>
        </div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 3: Remove template leftovers and invalid paths from the homepage**

```html
<!-- Remove bxslider, empty anchors, ../../Logo design/... references, and library-specific sections -->
```

- [ ] **Step 4: Run the validator and verify homepage template words are gone**

Run:

```bash
python3 tools/validate_ducofex_site.py
```

Expected: fewer failures, with `index.html` no longer reporting banned template words or missing brand logo path.

### Task 5: Rebuild the machine overview and product pages

**Files:**
- Modify: `products/cnc/web/website_v1/Option1/machines.html`
- Modify: `products/cnc/web/website_v1/Option1/gen-1.html`
- Modify: `products/cnc/web/website_v1/Option1/gen-2.html`

- [ ] **Step 1: Replace `machines.html` with a clearer catalog overview**

```html
<section class="ducofex-section">
  <div class="container">
    <div class="ducofex-pill">Machine Catalog</div>
    <h1>Choose the Ducofex platform that fits your build scale.</h1>
    <div class="row">
      <div class="col-md-6">
        <div class="ducofex-card" style="padding:36px;">
          <h3>Gen-1</h3>
          <p>A practical CNC entry point for workshops, makers, and early adopters.</p>
          <a class="ducofex-btn" href="gen-1.html">View Gen-1</a>
        </div>
      </div>
      <div class="col-md-6">
        <div class="ducofex-card" style="padding:36px;">
          <h3>Gen-2</h3>
          <p>A stronger performance platform for teams that need more capacity and confidence.</p>
          <a class="ducofex-btn" href="gen-2.html">View Gen-2</a>
        </div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Rework each product page into a trust-first product layout**

```html
<section class="ducofex-hero">
  <div class="container">
    <div class="row">
      <div class="col-md-7">
        <div class="ducofex-pill">Ducofex Gen-1</div>
        <h1>Built for hands-on fabrication teams that need a serious first platform.</h1>
        <p>Gen-1 is designed to give buyers an accessible starting point without sacrificing the reliability expected from a real production tool.</p>
        <a class="ducofex-btn" href="contact-us.html">Ask About Gen-1</a>
      </div>
      <div class="col-md-5">
        <div class="ducofex-card" style="padding:28px;">
          <h3>Why it fits</h3>
          <ul>
            <li>Workshop-ready footprint</li>
            <li>Clear upgrade path</li>
            <li>Strong early-stage value</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 3: Remove placeholder/event/template structures from these pages**

```html
<!-- Remove library/event components, placeholder crumbs, and broken CTA links. Keep only product-relevant sections. -->
```

- [ ] **Step 4: Run the validator and verify the machine pages pass**

Run:

```bash
python3 tools/validate_ducofex_site.py
```

Expected: `machines.html`, `gen-1.html`, and `gen-2.html` stop reporting banned template content and missing logo path.

### Task 6: Rebuild the supporting brand pages

**Files:**
- Modify: `products/cnc/web/website_v1/Option1/about-us.html`
- Modify: `products/cnc/web/website_v1/Option1/contact-us.html`
- Modify: `products/cnc/web/website_v1/Option1/partners.html`
- Modify: `products/cnc/web/website_v1/Option1/printing-3d.html`
- Modify: `products/cnc/web/website_v1/Option1/printable-models.html`
- Modify: `products/cnc/web/website_v1/Option1/lokumai.html`

- [ ] **Step 1: Rebuild `about-us.html` around trust and company direction**

```html
<section class="ducofex-section">
  <div class="container">
    <div class="ducofex-pill">About Ducofex</div>
    <h1>We are building more than machines.</h1>
    <p>Ducofex Industries is focused on CNC systems, practical fabrication technology, and a broader production ecosystem that grows with customer needs.</p>
  </div>
</section>
```

- [ ] **Step 2: Rebuild `contact-us.html` around direct inquiry and quote capture**

```html
<section class="ducofex-section">
  <div class="container">
    <div class="row">
      <div class="col-md-6">
        <h1>Talk to Ducofex</h1>
        <p>Request product details, discuss custom needs, or start a partner conversation.</p>
      </div>
      <div class="col-md-6">
        <div class="ducofex-card" style="padding:32px;">
          <p>Email: <a href="mailto:info@ducofex.com">info@ducofex.com</a></p>
          <p>Instagram: <a href="https://www.instagram.com/ducofex">@ducofex</a></p>
        </div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 3: Fill the future-facing pages with honest teaser copy**

```html
<section class="ducofex-section">
  <div class="container">
    <div class="ducofex-card" style="padding:48px;">
      <div class="ducofex-pill">Coming Soon</div>
      <h1>LokumAI</h1>
      <p>LokumAI is an upcoming Ducofex initiative. More details will be shared as the platform takes shape.</p>
      <a class="ducofex-btn-secondary" href="contact-us.html">Ask About Future Plans</a>
    </div>
  </div>
</section>
```

- [ ] **Step 4: Run the validator and verify all required pages pass**

Run:

```bash
python3 tools/validate_ducofex_site.py
```

Expected: `VALIDATION PASSED`

### Task 7: Clean legacy style conflicts and optional neon emphasis

**Files:**
- Modify: `products/cnc/web/website_v1/Option1/style.css`
- Modify: `products/cnc/web/website_v1/Option1/css/color.css`
- Modify: `products/cnc/web/website_v1/Option1/js/functions.js`

- [ ] **Step 1: Neutralize legacy orange-first rules that still override the new palette**

```css
/* append near the end of style.css */
.header-3 .logo-container,
.footer-2,
.lib-count-up-section,
.kode-navigation ul li:before,
.kode-navigation ul li:after{
  background:none;
  border-color:transparent;
}

.kode-navigation ul li a{
  color:var(--ducofex-text);
}

.kode-navigation ul li a:hover{
  color:var(--ducofex-primary-strong);
}
```

- [ ] **Step 2: Replace global orange color tokens with the new primary accent**

```css
/* replace repeated #FF9606 usage in css/color.css with #4F7CFF where the legacy file is still loaded */
```

- [ ] **Step 3: Keep JS changes minimal and only for behavior polish**

```javascript
// Example: ensure back-to-top targets an existing anchor and keep menu behavior intact.
jQuery(function($){
  $('.back-to-top a').attr('href', '#top');
});
```

- [ ] **Step 4: Run one final validation plus a static asset check**

Run:

```bash
python3 tools/validate_ducofex_site.py && python3 - <<'PY'
from pathlib import Path
root = Path("products/cnc/web/website_v1/Option1")
required = [
    "images/brand/6x3.png",
    "images/brand/hello-2.png",
    "css/ducofex-theme.css",
    "partners.html",
    "printing-3d.html",
    "printable-models.html",
    "lokumai.html",
]
missing = [p for p in required if not (root / p).exists()]
print("asset check passed" if not missing else f"missing: {missing}")
PY
```

Expected:

```text
VALIDATION PASSED
asset check passed
```

## Self-review

### Spec coverage

- Brand palette and logo alignment: covered by Tasks 1, 2, and 7
- Catalog-first homepage: covered by Task 4
- Machine overview and product pages: covered by Task 5
- Partners / sponsors: covered by Tasks 3 and 6
- 3D printing / printable models / LokumAI presence: covered by Tasks 3 and 6
- Static-site-first architecture: covered by Tasks 2 through 7
- No fake backend flow: enforced in Scope and Task 6 content guidance
- Neon-enhanced option: covered by Task 2 theme layer and Task 7 styling cleanup

### Placeholder scan

No `TBD`, `TODO`, or fake backend instructions remain in this plan. Places where exact business copy is still unknown are constrained to honest teaser language only.

### Type and naming consistency

All new paths and labels are consistent across tasks:

- `printing-3d.html`
- `printable-models.html`
- `partners.html`
- `lokumai.html`
- `css/ducofex-theme.css`
- `images/brand/6x3.png`

## Execution handoff

Plan complete and saved to `docs/superpowers/plans/2026-06-13-ducofex-website-redesign-phase-1.md`.

Two execution options:

**1. Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints

Which approach?
