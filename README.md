# Jack Logan — Scientific Portfolio (V33)

Astro 7 / TypeScript / MDX static website for https://jalogan.github.io.


## V33 release consolidation

V33 is the **complete project**, rebuilt from the last full V32 source with the figure-polish and video-figure patches integrated. It is **not** an incremental patch. In particular it includes:

- Final selected atomistic/coarse-grained overlay for the protein research card (both homepage and Research listing).
- Corrected SymBOPs, protein, sphere-packing and nanorod scientific figure assets and updated article references.
- Two playable original monodisperse jamming movies in a **single Figure 3** with panels (a) flat plane and (b) sphere; the subsequent coordination comparison remains **Figure 4**.
- Restored curved-manifold card animation and a Safari back/forward-cache `pageshow` playback recovery (also applied to the main hero animation).
- Updated polymer-loop note and About text; the publication order, site styling, navigation, and contact form remain intact.
- A regression-test set for these final choices.

Source-level checks: `npm run check:refs` (34 tests) and a static local-asset scan. This does **not** replace a full Astro build, visual review, or live contact-form test.

**Outstanding launch blocker:** 12 D₃ images still reference the **old** GitHub Pages repository. The assets must be migrated before deleting or replacing that repository. Use `npm run migrate:d3:remote` while the old images remain available; then rerun `npm run launch:check` and `npm run build`. If those images are not available online, use the local legacy-repository migration method described below.

## Local setup

Use Node.js 22.12 or newer.

```bash
npm install
npm run dev
```

Review the site locally, then run the automated checks and build:

```bash
npm run check:refs
npm run launch:check
npm run build
npm run preview
```

The deployable static website is generated into `dist/`. Do not deploy the project source as though it were already a built website.

## One-time D₃ media migration before replacing the old website

The existing D₃ Transformer research page includes 12 scientific images still linked from the legacy GitHub repository. Move those files into this new website *before replacing or deleting the old repository contents*:

```bash
npm run migrate:d3:remote
```

This command uses the original public GitHub raw image URLs and requires internet access. Alternatively, migrate from an existing local checkout of the old website:

```bash
npm run migrate:d3 -- /absolute/path/to/old-jalogan-site
```

Both methods replace the remote image references in the D₃ article with local files in `public/figures/d3/`. Run `npm run launch:check` afterward; the check fails while remote dependencies remain.

## Optional CVs and About photographs

Place the exact files below before the final build if you want the corresponding links and images published:

```
public/docs/jack-logan-research-cv.pdf
public/docs/jack-logan-industry-resume.pdf
public/images/about/about-photo-1.jpg
public/images/about/about-photo-2.jpg
```

Missing CVs and photographs are automatically omitted at build time so visitors do not see placeholder messages or broken downloads. The CV navigation appears once either CV is present.

The contact form uses the existing Formspree endpoint; test real email delivery from the deployed domain before promoting the site.

**See `LAUNCH-CHECKLIST.md` for the full pre-publication sequence and outstanding real-world checks.**

## Project structure

- `src/pages/` — homepage, About, Contact, publications, and article routes
- `src/content/research/` — research articles and their metadata
- `src/content/notes/` — Notes & Explorations
- `src/components/` — layout and figure components
- `src/styles/` — styles
- `public/` — static images, video, PDFs, robots.txt and sitemap
- `scripts/` — maintenance and media migration tools
- `tests/` — tests for media links, scientific references, publication metadata and site wiring

The README and launch checklist are source-repository documents, not published site pages.
