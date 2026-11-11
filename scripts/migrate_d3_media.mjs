#!/usr/bin/env node
/** Copy original D3 project figures from the locally cloned legacy Jekyll website.
 * Usage: npm run migrate:d3 -- /path/to/old-jalogan-site
 * If a figure is missing, leave its GitHub original URL intact rather than inventing media.
 */
import { existsSync, mkdirSync, readdirSync, copyFileSync, readFileSync, writeFileSync } from 'node:fs';
import { resolve, join, dirname } from 'node:path';

const root = resolve(import.meta.dirname, '..');
const candidateRoots = process.argv[2] ? [resolve(process.argv[2])] : [
  resolve(root, '../old-jalogan-site'),
  resolve(root, '../jalogan.github.io'),
  resolve(root, '../old-site'),
];
const originalRelative = 'assets/img/learned_group_symmetry_D3';
const sourceRoot = candidateRoots.flatMap(p=>[join(p, originalRelative), join(p, 'public/figures/d3')]).find(p=>existsSync(p));
if (!sourceRoot) {
  console.error(`Could not find ${originalRelative} or public/figures/d3 under the supplied directory.\nRun: npm run migrate:d3 -- /absolute/path/to/old-jalogan-site (or your V24 folder that already has the migrated figures)`);
  process.exit(1);
}
const output = join(root, 'public/figures/d3');
mkdirSync(output,{recursive:true});
let copied = 0;
for (const file of readdirSync(sourceRoot)) {
  if (!/\.(?:png|jpe?g|webp|svg|gif)$/i.test(file)) continue;
  copyFileSync(join(sourceRoot,file),join(output,file));
  copied++;
}
const oldPrefix = 'https://raw.githubusercontent.com/jalogan/jalogan.github.io/master/assets/img/learned_group_symmetry_D3/';
const page = join(root,'src/content/research/emergent-d3-symmetry.mdx');
let mdx = readFileSync(page,'utf8');
let migrated = 0;
mdx = mdx.replaceAll(/https:\/\/raw\.githubusercontent\.com\/jalogan\/jalogan\.github\.io\/master\/assets\/img\/learned_group_symmetry_D3\/([\w.-]+\.(?:png|jpe?g|webp|svg|gif))/g, (url,file)=>{
  if (!existsSync(join(output,file))) return url;
  migrated++;
  return `/figures/d3/${file}`;
});
writeFileSync(page,mdx,'utf8');
console.log(`Copied ${copied} original images. Switched ${migrated} references to local assets.`);
if(migrated===0) console.log('No figure names matched. Remote references remain unchanged.');
