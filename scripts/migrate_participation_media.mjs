#!/usr/bin/env node
/** Import the original Participation Ensembles cover from a local checkout
 * of the previous Jekyll website, without modifying that checkout.
 * Usage: npm run migrate:participation -- ../old-jalogan-site
 */
import {existsSync, mkdirSync, copyFileSync, readFileSync, writeFileSync} from 'node:fs';
import {resolve, join} from 'node:path';

const root = resolve(import.meta.dirname,'..');
const roots = process.argv[2] ? [resolve(process.argv[2])] : [
  resolve(root,'../old-jalogan-site'),
  resolve(root,'../jalogan.github.io'),
  resolve(root,'../old-site')
];
const relative = 'assets/img/superposition_entropy/cover_image2_cropped.png';
const src = roots.map(dir=>join(dir,relative)).find(existsSync);
if (!src) {
  console.error(`Could not find ${relative} in your local old-site checkout.\nUsage: npm run migrate:participation -- /absolute/path/to/old-jalogan-site`);
  process.exit(1);
}
const destDir=join(root,'public/figures/participation');
mkdirSync(destDir,{recursive:true});
copyFileSync(src,join(destDir,'original-participation-cover.png'));
console.log('Archived original Participation Ensembles cover for comparison. The V25 four-piece puzzle card and the mathematical article illustration remain unchanged.');
