# Ducofex Premium Futuristic Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rework the active Ducofex website so it feels more elite, spacious, premium-futuristic, and less like a generic AI-generated landing page.

**Architecture:** Keep the current static HTML structure, language switching, and deployable `Option1` folder intact while redesigning the shared visual system first, then rebuilding the flagship pages to use that calmer and more premium language. Treat `css/ducofex-theme.css` as the main control layer, then refine the active pages so the new hierarchy, spacing, and CTA patterns feel intentional rather than templated.

**Tech Stack:** Static HTML, CSS, existing JavaScript, Python validation scripts, local browser preview

---

## File map

**Modify**
- `products/cnc/web/website_v1/Option1/css/ducofex-theme.css`
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

**Test**
- `tools/validate_ducofex_site.py`
- `tools/validate_ducofex_i18n.py`

### Task 1: Redesign the shared visual system

**Files:**
- Modify: `products/cnc/web/website_v1/Option1/css/ducofex-theme.css`

- [ ] **Step 1: Preserve a failing visual checklist**

Write down the intended checks before editing:

```text
- Header should feel lighter and less boxed
- Buttons should stop looking like generic AI landing-page pills
- Section spacing should become more dramatic
- Cards should be reduced in quantity and visual noise
- Typography should feel calmer and more expensive
```

- [ ] **Step 2: Implement the new shared system in `ducofex-theme.css`**

Update:

```css
:root{
  --ducofex-bg:#05070d;
  --ducofex-surface:#0c111d;
  --ducofex-surface-2:#101726;
  --ducofex-line:rgba(124,154,214,.12);
  --ducofex-heading:#e1e8f5;
  --ducofex-text:#c7d1e4;
  --ducofex-text-soft:#98a7c0;
  --ducofex-primary:#6b8dff;
  --ducofex-radius:22px;
}

.ducofex-section{
  padding:148px 0;
}

.ducofex-card{
  background:linear-gradient(180deg, rgba(15,21,33,.82), rgba(10,14,22,.92));
  border:1px solid var(--ducofex-line);
  box-shadow:none;
}

.ducofex-btn,
.ducofex-btn-secondary{
  min-height:54px;
  border-radius:14px;
  text-transform:none;
  letter-spacing:.01em;
}
```

- [ ] **Step 3: Run the validators**

Run:

```bash
python3 tools/validate_ducofex_i18n.py && python3 tools/validate_ducofex_site.py
```

Expected:

```text
I18N VALIDATION PASSED
VALIDATION PASSED
```

### Task 2: Rebuild the homepage into a flagship page

**Files:**
- Modify: `products/cnc/web/website_v1/Option1/index.html`

- [ ] **Step 1: Remove repetitive homepage rhythm**

Reduce or merge:

```text
- stacked equal-weight cards
- duplicated CTA blocks
- filler trust copy that repeats the same message
```

- [ ] **Step 2: Rebuild the home structure with more elite pacing**

Use a calmer structure:

```html
<section class="ducofex-hero">...</section>
<section class="ducofex-flagship-intro">...</section>
<section class="ducofex-machine-paths">...</section>
<section class="ducofex-future-direction">...</section>
<section class="ducofex-final-cta">...</section>
```

And ensure the CTAs separate:

```html
<a class="ducofex-btn" href="machines.html">Review machines</a>
<a class="ducofex-btn-secondary" href="contact-us.html">Request a quote</a>
```

- [ ] **Step 3: Re-run validators**

Run:

```bash
python3 tools/validate_ducofex_i18n.py && python3 tools/validate_ducofex_site.py
```

Expected:

```text
I18N VALIDATION PASSED
VALIDATION PASSED
```

### Task 3: Refine the machine pages into product-first pages

**Files:**
- Modify: `products/cnc/web/website_v1/Option1/machines.html`
- Modify: `products/cnc/web/website_v1/Option1/gen-1.html`
- Modify: `products/cnc/web/website_v1/Option1/gen-2.html`

- [ ] **Step 1: Simplify the catalog overview**

Keep only the blocks that support decision-making:

```text
- overview
- comparison
- trust/buying logic
- next-step CTA
```

- [ ] **Step 2: Make Gen-1 and Gen-2 feel more premium**

Refine:

```html
<section class="ducofex-product-hero">...</section>
<section class="ducofex-product-rationale">...</section>
<section class="ducofex-product-cta">...</section>
```

Reduce:

```text
- identical card repetition
- over-explaining copy
- generic feature-grid feeling
```

- [ ] **Step 3: Re-run validators**

Run:

```bash
python3 tools/validate_ducofex_i18n.py && python3 tools/validate_ducofex_site.py
```

Expected:

```text
I18N VALIDATION PASSED
VALIDATION PASSED
```

### Task 4: Quiet down the support pages

**Files:**
- Modify: `products/cnc/web/website_v1/Option1/about-us.html`
- Modify: `products/cnc/web/website_v1/Option1/contact-us.html`
- Modify: `products/cnc/web/website_v1/Option1/partners.html`
- Modify: `products/cnc/web/website_v1/Option1/printing-3d.html`
- Modify: `products/cnc/web/website_v1/Option1/printable-models.html`
- Modify: `products/cnc/web/website_v1/Option1/lokumai.html`

- [ ] **Step 1: Reduce filler density**

Trim or merge blocks that feel repetitive:

```text
- repeated supporting cards
- duplicate explanation layers
- CTA clutter
```

- [ ] **Step 2: Recompose into quieter support pages**

Target:

```text
- cleaner page openings
- calmer body sections
- stronger spacing
- fewer but more credible CTAs
```

- [ ] **Step 3: Re-run validators**

Run:

```bash
python3 tools/validate_ducofex_i18n.py && python3 tools/validate_ducofex_site.py
```

Expected:

```text
I18N VALIDATION PASSED
VALIDATION PASSED
```

### Task 5: Browser QA and final polish

**Files:**
- Test: active pages in browser preview

- [ ] **Step 1: Start or reuse the local preview server**

Run:

```bash
python3 -m http.server 8002
```

Expected:

```text
Local preview available on http://localhost:8002/
```

- [ ] **Step 2: Manually verify the premium-futuristic direction**

Check:

```text
- homepage feels sparser and more flagship-driven
- machine pages feel more product-led
- header feels lighter
- buttons feel more expensive
- no obvious “AI template” card repetition remains
```

- [ ] **Step 3: Run final validators**

Run:

```bash
python3 tools/validate_ducofex_i18n.py && python3 tools/validate_ducofex_site.py
```

Expected:

```text
I18N VALIDATION PASSED
VALIDATION PASSED
```

## Self-review

- Spec coverage: typography, spacing, header, CTA quality, calmer support pages, and premium-futuristic direction are all covered by tasks 1-5.
- Placeholder scan: there are no `TBD` or incomplete execution notes.
- Type consistency: all file paths and validator commands stay consistent with the current project structure.

## Execution handoff

Plan complete and saved to `docs/superpowers/plans/2026-06-13-ducofex-premium-futuristic-redesign.md`.

Two execution options:

**1. Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints

Which approach?
