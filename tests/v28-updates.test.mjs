import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';

const source = p => readFileSync(resolve(process.cwd(), p), 'utf8');
const asset = p => existsSync(resolve(process.cwd(), 'public', p));

test('publication order follows the finalized public-site sequence', () => {
  const pub = source('src/pages/publications.astro');
  const entries = [...pub.matchAll(/title:'([^']+)'/g)].map(m => m[1]);
  assert.deepEqual(entries, [
    'Effect of stereochemical constraints on the structural properties of folded proteins',
	'Protein folding as a jamming transition',
    'Symmetry-specific characterization of bond orientation order in DNA-assembled nanoparticle lattices',
    'Geometric and topological entropies of sphere packing',
    'Controlling morphology in hybrid isotropic/patchy particle assemblies',
    'Symmetry-specific orientational order parameters for complex structures',
    'Compact interaction potential for van der Waals nanorods',
	'Near-field spectroscopic investigation of dual-band heavy fermion metamaterials',
  ]);
});

test('professional profiles appear in About and footer and use exact user URLs', () => {
  for (const path of ['src/pages/about.astro','src/components/SiteFooter.astro']) {
    const t = source(path);
    assert.ok(t.includes('https://github.com/jalogan'));
    assert.ok(t.includes('https://linkedin.com/in/jacklogan-physicist/'));
    assert.match(t, /rel="noopener noreferrer"/);
  }
});

test('contact and About use broad collaboration and opportunity language', () => {
  const contact = source('src/pages/contact.astro');
  const about = source('src/pages/about.astro');
  assert.ok(contact.includes('research and professional opportunities'));
  assert.ok(!contact.includes('without my email address being displayed publicly'));
  assert.ok(about.includes('collaborations or professional opportunities'));
});

test('final card media assets are installed and contained treatments remain in place', () => {
  const research = ['md-surrogate','protein-modeling','sphere-packing','packing-on-curved-manifolds'].map(s => source(`src/content/research/${s}.mdx`));
  const assets = [
    'figures/cards/surrogate-force-field-v28.png',
    'figures/cards/protein-card-overlay.png',
    'figures/cards/sphere-packing-card-v29.webp',
    'figures/curved-manifolds/spheres-on-sphere-original.png',
  ];
  for (let i = 0; i < assets.length; i++) {
    assert.ok(research[i].includes(assets[i]));
    assert.ok(asset(assets[i]));
  }
  const card = source('src/components/ResearchCard.astro');
  const css = source('src/styles/global.css');
  for (const klass of ['media-protein-contained','media-surrogate-contained']) {
    assert.ok(card.includes(klass));
  }
  assert.match(css, /\.research-card-media\.media-protein-contained img[^{]*\{[^}]*object-fit:contain;/);
  assert.ok(asset('figures/pentagon-smectic-v28.png'));
  assert.ok(source('src/content/research/symbops.mdx').includes('pentagon-smectic-v28.png'));
});
