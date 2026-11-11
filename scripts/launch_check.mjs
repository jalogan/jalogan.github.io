#!/usr/bin/env node
/** Checks release-dependent items not covered by the repository unit tests. */
import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { resolve, join } from 'node:path';
const root=resolve(import.meta.dirname, '..');
const p = s => join(root,s);
let failures=0;
const info = s => console.log(`• ${s}`);
const article = readFileSync(p('src/content/research/emergent-d3-symmetry.mdx'),'utf8');
const remote = [...article.matchAll(/https:\/\/raw\.githubusercontent\.com\/jalogan\/jalogan\.github\.io\/master\/assets\/img\/learned_group_symmetry_D3\/[A-Za-z0-9_.-]+\.(?:png|jpe?g|webp|gif|svg)/g)];
if(remote.length){
  console.error(`BLOCKER: ${remote.length} D3 image references still depend on the legacy GitHub repository.`);
  console.error('Before replacing the old GitHub Pages repository, run: npm run migrate:d3:remote');
  console.error('Or use a local checkout: npm run migrate:d3 -- /path/to/old-jalogan-site');
  failures++;
}else info('D3 images are locally referenced.');
const optional=[
  'public/docs/jack-logan-research-cv.pdf','public/docs/jack-logan-industry-resume.pdf',
  'public/images/about/about-photo-1.jpg','public/images/about/about-photo-2.jpg'
];
for (const item of optional) if(existsSync(p(item))) info(`Included: ${item}`); else info(`Optional asset absent (automatically hidden from visitors): ${item}`);
if(!existsSync(p('public/sitemap.xml'))||!existsSync(p('public/robots.txt'))){ console.error('BLOCKER: sitemap.xml or robots.txt is missing.'); failures++; }
const pages = ['about','contact','publications','index'];
for(const name of pages) {
 const t=readFileSync(p(`src/pages/${name}.astro`),'utf8');
 if(/(?:Photo will appear here|PDF to be added|as an AI language model|as requested in the chat)/i.test(t)){
  console.error(`BLOCKER: ${name}.astro contains a visitor-facing placeholder or prompt residue.`); failures++;
 }
}
if(failures){console.error(`Release audit failed with ${failures} blocker(s).`);process.exit(1);}
console.log('Source-level launch audit passed. A local Astro build, browser visual check, and deployed contact-form test are still required.');
