import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

const source = (filename) => readFileSync(resolve(process.cwd(), filename), 'utf8');

test('contact page posts to existing Formspree endpoint and includes all required controls', () => {
  const page = source('src/pages/contact.astro');
  assert.match(page, /action="https:\/\/formspree\.io\/f\/xrbavorj" method="POST"/);
  for (const name of ['name','email','subject','message','_gotcha']) {
    assert.ok(page.includes(`name="${name}"`), `${name} field missing`);
  }
  assert.match(page, /name="message" rows="12" required/);
  assert.match(page, /role="status" aria-live="polite"/);
  assert.match(page, /headers: \{ 'Accept': 'application\/json' \}/);
  assert.doesNotMatch(page, /mailto:/);
});

test('contact link appears on homepage, about page, footer, and navigation', () => {
  for (const filename of ['src/pages/index.astro','src/pages/about.astro','src/components/SiteHeader.astro','src/components/SiteFooter.astro']) {
    const content = source(filename);
    assert.ok(content.includes('/contact/'), `${filename} missing contact link`);
  }
  assert.equal((source('src/pages/about.astro').match(/class="about-contact-panel"/g) || []).length, 1);
});

test('science card images retain matching backgrounds and a non-cropping fit', () => {
  const card = source('src/components/ResearchCard.astro');
  const css = source('src/styles/global.css');
  assert.match(card, /media-symbops-contained/);
  assert.match(card, /media-packing-contained/);
  assert.match(css, /\.research-card-media\.media-symbops-contained \{background:#fff;\}/);
  assert.match(css, /\.research-card-media\.media-packing-contained \{background:#fff;\}/);
  assert.match(css, /\.research-card-media\.media-packing-contained img \{[^}]*object-fit:contain;/);
});

test('original contact URL forwards to the new contact page', () => {
  const redirect = source('src/pages/contact_me/index.astro');
  assert.match(redirect, /http-equiv="refresh" content="0;url=\/contact\/"/);
  assert.match(redirect, /href="\/contact\/"/);
});

test('reframed card images are used and the CV/photo slots are ready for user files', () => {
  const sym = source('src/content/research/symbops.mdx');
  const packing = source('src/content/research/sphere-packing.mdx');
  const about = source('src/pages/about.astro');
  const header = source('src/components/SiteHeader.astro');
  assert.match(sym, /symbops-sphere-card-v27.webp/);
  assert.match(packing, /sphere-packing-card-v29.webp/);
  assert.match(about, /about-photo-1.jpg/);
  assert.match(about, /about-photo-2.jpg/);
  assert.match(about, /hasResearchCv/);
  assert.match(about, /hasIndustryResume/);
  assert.match(about, /target=\"_blank\"/);
  assert.match(about, /download>Download/);
  assert.match(header, /about\/#cv/);
});
