/** Copies original public media from a LOCAL checkout of jalogan.github.io.
 * Usage: node scripts/import_legacy_media.mjs /path/to/old/jalogan.github.io
 * No network access, image generation, or destructive operations.
 */
import { existsSync, cpSync, mkdirSync, readdirSync, statSync, writeFileSync } from 'node:fs';
import { join, resolve, relative } from 'node:path';
const source = resolve(process.argv[2] || '');
if (!process.argv[2] || !existsSync(join(source, '_projects'))) {
  console.error('Usage: npm run import:legacy -- /path/to/old/jalogan.github.io');
  console.error('The source must be the old Jekyll repository root containing _projects/.');
  process.exit(2);
}
const publicRoot = resolve('public');
const dest = join(publicRoot, 'legacy');
const roots = ['assets/img','assets/videos','assets/video','assets/gif','assets/media'];
let n = 0;
const names = [];
function walk(dir) {
  for (const entry of readdirSync(dir, { withFileTypes:true })) {
    const full=join(dir,entry.name);
    if (entry.isDirectory()) walk(full);
    else if (/\.(png|jpe?g|gif|webp|svg|mp4|webm)$/i.test(entry.name)) {
      const rel=relative(source,full);
      const target=join(dest,rel);
      mkdirSync(join(target,'..'),{recursive:true});
      cpSync(full,target,{force:true});
      names.push(`/legacy/${rel.split('\\').join('/')}`); n++;
    }
  }
}
for(const base of roots) {const p=join(source,base); if(existsSync(p)&&statSync(p).isDirectory()) walk(p);}
// Root-level videos in the original repository are also retained.
for (const name of readdirSync(source)) if(/\.(mp4|webm)$/i.test(name)) {
  cpSync(join(source,name),join(dest,name),{force:true}); names.push(`/legacy/${name}`); n++;
}
writeFileSync(join(dest,'asset-index.json'),JSON.stringify({source:source,paths:names},null,2));
console.log(`Imported ${n} original media files into public/legacy. Existing site artwork and articles were not modified.`);
console.log('Use public/legacy/asset-index.json to choose additional original research card images.');
