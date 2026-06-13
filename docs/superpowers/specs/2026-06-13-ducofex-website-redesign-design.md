# Ducofex website redesign design

## Summary

Redesign the current website in `products/cnc/web/website_v1/Option1` into a stronger, more premium Ducofex marketing site. The current build is a reused template with broken brand alignment, leftover library content, weak trust signals, and inconsistent navigation. The first release should focus on trust building and machine sales while clearly opening paths toward partnerships, sponsors, 3D printing services, printable models, and a future LokumAI area.

This is a front-end heavy redesign, not a small cleanup. The site can change almost completely in look and content structure, but it should remain deployable as a static website in the existing project folder. Advanced order automation and Python pricing integration are future-phase features that should be designed for now, not fully implemented in the first visual release unless explicitly re-scoped later.

## Goals

- Replace the generic template feel with a polished Ducofex brand experience.
- Make the site feel trustworthy, technical, modern, and visually memorable.
- Sell CNC machines more effectively through clearer catalog and product presentation.
- Present Ducofex as a company open to partnerships, sponsorship, and growth.
- Add visible paths for 3D printing services, printable model offerings, and LokumAI.
- Establish a reusable brand/theme system based on the real logo palette.
- Keep the codebase structured so a future order flow can plug in cleanly.

## Non-goals for the first release

- No fake checkout or fake upload workflow that pretends to be live.
- No embedded Python pricing logic in the initial front-end-only pass.
- No attempt to preserve every visual pattern from the current template.
- No broad refactor outside the website folder unless required for shared assets.

## Brand direction

The website should be based on the real Ducofex branding assets in `shared/branding/logo-design/`, especially `6x3.png` for the main logo and `hello-2.png` for the scorpion mark. The site should not use the template's orange visual identity.

### Core palette

- Primary accent: electric/scorpion blue derived from the logo
- Base: black / near-black background surfaces
- Support neutrals: cool gray / silver for secondary text, dividers, and UI framing
- High-contrast text: white or near-white on dark surfaces

### Visual personality

The site should feel:

- industrial
- futuristic
- precise
- premium
- confident

It should not feel:

- decorative
- template-like
- overloaded
- playful in a generic startup way

### Visual mode options

Two closely related visual modes should be supported at the design level:

1. `Core industrial`: dark premium presentation with restrained blue accents
2. `Neon industrial`: the same structure plus controlled blue neon / LED glow gradients in hero and selected background surfaces

The redesign should be implemented so these modes are mostly controlled by theme styling rather than requiring structural rewrites. The user wants the neon-enhanced look available as an option once visualized.

## Information architecture

### Primary navigation

- `Home`
- `Machines`
- `3D Printing`
- `Printable Models`
- `Partners`
- `About`
- `Contact`
- `LokumAI` with a clear `Coming Soon` treatment

### First-release page set

1. `index.html`
   - main catalog-first landing page
2. `machines.html`
   - overview of CNC machine lines and buyer paths
3. `gen-1.html`
   - product page for Gen-1
4. `gen-2.html`
   - product page for Gen-2
5. `about-us.html`
   - company story and trust content
6. `contact-us.html`
   - lead capture and contact path
7. New or repurposed partner page
   - sponsor / partnership proposition
8. New or repurposed 3D printing page
   - service overview and future order path
9. New or repurposed printable models page
   - preset model catalog teaser
10. New or repurposed LokumAI page
   - coming soon positioning

Template leftovers like irrelevant event/library/page content can be removed, merged, or repurposed if that produces a cleaner user journey.

## Homepage design

The homepage should be catalog-first, not blog-first and not brochure-only.

### Section order

1. Hero
   - strong machine-led visual
   - short, high-confidence Ducofex value proposition
   - primary actions such as `View Machines` and `Request Quote`
2. Machine categories / buyer paths
   - help visitors identify the right line quickly
3. Featured machines
   - key models with short specs and benefits
4. Trust / proof section
   - build quality, precision, support, engineering, delivery, reliability
5. 3D printing expansion section
   - position Ducofex as expanding into broader fabrication solutions
6. Printable models teaser
   - preset models / toys / starter examples
7. Partnership / sponsor section
   - invite collaborators, sponsors, and growth partners
8. LokumAI teaser
   - clearly marked coming soon
9. Final CTA / contact block
   - push toward inquiry or quote request

### Hero requirements

- Must feel premium and immediate
- Must avoid vague template copy
- Must show what the company does in the first screen
- Must establish trust and seriousness fast
- Should allow either a restrained industrial background or a blue neon gradient enhancement

## Content direction

### Messaging priorities

The website should communicate:

- Ducofex builds CNC machines
- Ducofex is a serious technical brand
- Ducofex is open to customer orders
- Ducofex is evolving into a wider production / fabrication platform
- Ducofex is open to sponsors and strategic partners

### Writing style

- concise
- technical but readable
- confident
- clear for non-expert buyers
- not filled with generic marketing buzzwords

### Content cleanup rules

- Remove template copy related to libraries, books, authors, and unrelated placeholders
- Fix spelling, grammar, and weak wording on current Ducofex copy
- Replace broken or empty CTA links with meaningful destinations
- Use `Coming Soon` honestly where a section is strategic but not yet active

## Page-specific expectations

### Machines page

- Present machine families clearly
- Support comparison or scanning behavior
- Show use cases and audience fit
- Route users into Gen-1 and Gen-2 pages

### Gen-1 / Gen-2 pages

- Clear product framing
- Better layout for specs, use cases, benefits, and inquiry actions
- More trust-oriented presentation than the current template pages

### Partners page

- Explain collaboration, distribution, sponsorship, or investment interest
- Present Ducofex as ambitious but credible
- Provide a direct contact path

### 3D Printing page

This page should exist in the first release, but it can start as a strong service overview if the full order flow is not implemented yet.

It should introduce:

- 3D printing as a Ducofex solution area
- future file-based quoting and ordering
- materials / quality / speed direction at a high level if content is available later

### Printable Models page

This page should present the idea of preset printable models, toys, or starter items. It can initially work as a teaser/catalog concept page rather than a full e-commerce system.

### LokumAI page

This page should clearly say `Coming Soon` and position LokumAI as an upcoming Ducofex initiative without inventing unconfirmed product details.

## Future order flow design constraints

The user described a future upload-and-pricing workflow. This is not the core first-release scope, but the redesign should leave room for it.

### Future capabilities to support later

- upload `STL`, `3MF`, and `OBJ` files
- send file/job details into Python pricing software
- display calculated price in checkout
- offer quality presets renamed for marketing clarity:
  - `Regular` for low
  - `High` for mid
  - `Ultra` for high
- offer turnaround choices:
  - `2-3 days`
  - `3-5 days`
  - `5-7 days`
- allow order printing / print-friendly output after submission

### First-release rule

If these features are not truly connected to working backend logic, the UI should not pretend the system is live. It can preview the path, explain upcoming capability, or provide a manual quote request flow instead.

## Technical direction

### Current-state issues

The current site includes:

- broken relative asset references
- template logos still present
- mixed navigation quality
- leftover pages and structures from a different domain/theme
- weak shared styling consistency

### Technical strategy

- keep the website deployable as static HTML/CSS/JS in the current folder
- reuse only what still helps; do not preserve template sections for their own sake
- centralize shared branding/styling so page updates remain consistent
- standardize header, footer, CTAs, and navigation across pages
- remove or repurpose dead pages and irrelevant sections
- prefer a smaller set of stronger sections over many shallow template blocks

### Architecture note

The site should be shaped so a later app-like order flow can be added cleanly as:

- a dedicated order page, or
- a separate mini-app linked from the main site

This avoids scattering pricing logic through many static pages.

## Assets

### Brand assets to use

- `shared/branding/logo-design/6x3.png` as the main logo
- `shared/branding/logo-design/ducofex-final.png`, `ducofex.png`, or related alternates only if needed for fallback/comparison
- `shared/branding/logo-design/hello-2.png` and the uploaded `hello-2.png` as the mascot mark

### Asset guidance

- Do not rely on unrelated template images if they weaken brand credibility
- Reuse existing images only if they fit the Ducofex story
- Preserve logo sharpness and contrast on dark backgrounds

## UX requirements

- The first screen must explain what the company does
- Navigation must be cleaner and easier to scan
- CTA hierarchy must be obvious
- Product browsing must feel easier than in the current template
- Contact and inquiry actions must be visible without hunting
- The site must stay readable even if neon treatment is enabled
- Mobile navigation and section stacking must be respected during implementation

## Error handling and integrity

- Broken links and empty anchors should be removed or replaced
- Missing assets should be fixed, not silently ignored
- Pages marked as future-facing should say so clearly
- No invented specifications, prices, or capabilities should be inserted without source content

## Testing expectations for implementation

Implementation should verify:

- pages render without broken layout
- shared navigation works across pages
- brand colors are applied consistently
- logo assets display correctly
- no obvious template/library copy remains
- core pages look coherent on desktop and mobile widths
- neon-enhanced option remains readable and not overdone

## Open items intentionally left out of implementation scope

These are acknowledged but should not be hallucinated into the first release:

- exact machine specifications if not already provided
- final sponsor / partner business copy beyond safe positioning
- live checkout behavior
- real file parsing and price calculation integration details
- full printable model catalog data
- exact LokumAI product definition

## Recommended implementation phases

### Phase 1

Brand/theme redesign and core marketing site:

- homepage
- machine catalog pages
- trust sections
- partnership section
- about/contact improvements
- 3D printing / printable models / LokumAI placeholders with strong framing

### Phase 2

Order experience and pricing integration:

- file upload
- quote calculation
- checkout logic
- print-friendly order output

### Phase 3

Catalog depth and ecosystem growth:

- printable model catalog depth
- richer 3D printing service options
- LokumAI activation

## Acceptance criteria for the redesign

The first release is successful if:

- the site no longer feels like a generic library template
- the visual identity clearly matches the Ducofex logo palette
- the homepage is stronger, clearer, and more trust-building
- machine sales paths are easier to follow
- partnership / sponsor intent is visible
- future service areas are introduced cleanly without fake functionality
- the codebase remains a practical base for later pricing/order integration
