# Live-site readiness checklist — V33

This checklist is for the repository owner, not a page published to site visitors.

## Confirmed in consolidated V33

- [x] Published protein paper now cites *Physical Review E* 112, 054405 (2025), DOI `10.1103/9wf9-ywhw`, instead of presenting it as an unreviewed preprint.
- [x] Protein subchain averaging formula matches the published paper: normalization `1/(N-n+1)` and all `N-n+1` contiguous windows.
- [x] Surrogate force article states the actual radial direction convention and explains why its repulsive scalar is negative.
- [x] No visitor-facing "photo coming soon" or "PDF to be added" text. Optional About photographs and CVs are hidden until provided; CV navigation is conditional.
- [x] Removed website-internal phrasing and checked research/notes content for obvious prompt residue or editorial handoff notes.
- [x] Publication list ordered by verified publication dates; corrected van der Waals nanorod publication date.
- [x] Existing scientific media paths and in-article figure references remain covered by automated tests.
- [x] Added static `robots.txt`, `sitemap.xml`, a custom 404 page, social sharing and canonical URL metadata.
- [x] Kept existing site visual design, project content, animations, contact integration, and GitHub/LinkedIn links.
- [x] Restored the chosen protein overlay card on both the homepage and Research list; confirmed it is referenced from the shared research metadata.
- [x] Applied scientific figure corrections: SymBOPs split panels (a)/(b), uncropped protein panel labels, corrected entropy axes, and cleaned nanorod plot edges.
- [x] Integrated the two uploaded jamming MP4s as Figure 3 panels (a) plane and (b) sphere; the static coordination figure now follows as Figure 4.
- [x] Added Safari back/forward-cache video playback recovery for card and hero animations.
- [x] Installed the refined polymer geometry note and refreshed About text emphasizing original mathematical methods.
- [x] All 34 offline source/unit tests pass; 91 explicitly referenced local scientific media paths exist.

## Required before replacing the old GitHub Pages content

- [ ] **Migrate all 12 D₃ figures**: `npm run migrate:d3:remote` (or `npm run migrate:d3 -- /path/to/legacy-repo`). The migration cannot be completed from this offline build environment. `npm run launch:check` will fail until the references are local.
- [ ] Install Node.js 22.12+ and dependencies; run `npm install`, `npm run check:refs`, `npm run launch:check`, `npm run build`, `npm run preview`.
- [ ] Review the actual built site at desktop/tablet/mobile sizes. Confirm no text/image clipping, card-video framing, figure lightboxes, reduced-motion behavior, menu navigation, readable equations, and screen-reader labels.
- [ ] Test a message submitted from the deployed `/contact/` page and confirm that it reaches the intended mailbox through Formspree. This cannot be verified from the source archive alone.
- [ ] If CV or About photos should be public at launch, add files before `npm run build` using the filenames in `README.md`.
- [ ] Verify links to third-party sites on the deployed domain: papers, dissertation, GitHub, LinkedIn, image sources, and optional CVs.
- [ ] Make a backup of the legacy website/repository before deploying `dist/` to the GitHub Pages site. Keep a rollback option until the replacement is confirmed.
- [ ] After deployment check `https://jalogan.github.io/sitemap.xml` and `/robots.txt`, verify HTTPS/canonical URLs, and monitor 404s.

## Optional follow-ups

- Review the publication list against your final research CV to confirm that every paper you want listed is included; six verified journal papers are currently represented.
- Add a favicon/social-preview image if desired. Not required for site functionality.

## Environment limitation

The V33 archive source was checked using Node-based tests and local media-reference audits. A complete Astro build and real browser/deployment checks were not performed in this environment because npm dependencies were unavailable and outbound npm registry access was blocked. Do not treat source-level checks as proof of runtime deployment readiness.
