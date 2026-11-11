#!/usr/bin/env node
/** Copy this site's public D3 figures from the original GitHub repository and
 * replace source links with local media paths. Run before retiring the old site.
 */
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { resolve, join } from 'node:path';

const root = resolve(import.meta.dirname, '..');
const article = join(root, 'src/content/research/emergent-d3-symmetry.mdx');
const destination = join(root, 'public/figures/d3');
const prefix = 'https://raw.githubusercontent.com/jalogan/jalogan.github.io/master/assets/img/learned_group_symmetry_D3/';
const referencePattern = /https:\/\/raw\.githubusercontent\.com\/jalogan\/jalogan\.github\.io\/master\/assets\/img\/learned_group_symmetry_D3\/([A-Za-z0-9_.-]+\.(?:png|jpe?g|webp|gif|svg))/g;
const source = readFileSync(article, 'utf8');
const files = [...new Set([...source.matchAll(referencePattern)].map(m => m[1]))];
if (!files.length) {
  console.log('No remote D3 figure references remain; migration is already complete.');
  process.exit(0);
}
const downloaded = new Map();
for (const file of files) {
  const url = prefix + file;
  let response;
  try { response = await fetch(url, { signal: AbortSignal.timeout(18000) }); }
  catch (err) { console.error(`Unable to download ${file}: ${err.message}`); process.exit(1); }
  if (!response.ok || !((response.headers.get('content-type') || '').startsWith('image/'))) {
    console.error(`Original image unavailable (${response.status}) or invalid content type: ${url}`);
    process.exit(1);
  }
  const data = Buffer.from(await response.arrayBuffer());
  if (data.length < 100) { console.error(`Image was unexpectedly small: ${file}`); process.exit(1); }
  downloaded.set(file, data);
  console.log(`Verified ${file}: ${Math.ceil(data.length/1024)} KB`);
}
mkdirSync(destination, {recursive:true});
for (const [file, data] of downloaded) writeFileSync(join(destination,file),data);
const local = source.replace(referencePattern, (_, file) => `/figures/d3/${file}`);
writeFileSync(article, local);
console.log(`Migrated ${downloaded.size} original D3 figures to public/figures/d3/. Run npm run launch:check to verify.`);
