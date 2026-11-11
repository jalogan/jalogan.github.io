# V33 release notes — scientific portfolio

This is a **full replacement source archive**, not a partial patch.

## Restored / integrated

- Protein card: final all-atom/Martini overlay (`public/figures/cards/protein-card-overlay.png`).
- Figure-polish patch: SymBOPs figure panel split; protein panel-label crop; sphere packing axis labels; nanorod plot borders; D₃ reader-facing wording.
- Curved manifolds: authentic monodisperse jamming movies for plane and sphere as Figure 3(a–b), with the existing local-coordination images as Figure 4. Original moving-sphere Figure 2 video retained because separate polydisperse jamming MP4 was not supplied.
- Navigation: card and hero video playback retries on Safari back-navigation and tab return, respecting reduced-motion settings.
- About page: description strengthened to emphasize original mathematical models and numerical methods.
- Polymer loop note: latest revised version installed.
- Numbering: `VideoGroup` participates in automatic figure numbering and cross-reference checks.

## Automated validation

- 34 source-level Node tests passed.
- All 91 explicit local media references in source resolve to assets.
- Both uploaded jamming MP4s verified as H.264 streams.

## Outstanding prelaunch checks

1. Migrate 12 D₃ figures linked to the old GitHub Pages repo (`npm run migrate:d3:remote`, while old content exists).
2. Run `npm install`, `npm run launch:check`, and `npm run build` locally with Node 22.12+. Astro dependencies are not available in this assembly environment.
3. Visual-check Safari back navigation, all research cards and articles, mobile pages, and the deployed Formspree contact form.
4. Optional CVs and About photographs are omitted if source files are not provided.

The unavailable local `src` ZIP could not be compared directly; V33 was reconstructed from the verified V32 archive and all available subsequent materials.
