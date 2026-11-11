import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { dirname, join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';
const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const source = join(root, 'src');
function files(folder) {
  return readdirSync(folder, {withFileTypes:true}).flatMap(entry => {
    const p = join(folder, entry.name);
    return entry.isDirectory() ? files(p) : /\.(mdx|astro)$/.test(entry.name) ? [p] : [];
  });
}
const sources = files(source);
test('public source does not contain handoff or migration notes', () => {
  const banned = [
    /this write-up preserves the figures/i,
    /the original write-up offered/i,
    /for the site write-up/i,
    /previous website/i,
    /this figure has not yet been copied/i,
    /view my existing public profile/i,
    /now labeled directly on the curves/i,
    /the website homepage is separate exploratory/i,
  ];
  for (const file of sources) {
    const content = readFileSync(file, 'utf8');
    for (const pattern of banned) assert.doesNotMatch(content, pattern, relative(source,file));
  }
});
test('all explicitly referenced local scientific media files exist', () => {
  for (const file of sources) {
    const content = readFileSync(file, 'utf8');
    const paths = [...content.matchAll(/(?:\bsrc\s*=\s*['"]|\bposter\s*=\s*['"]|\bsrc\s*:\s*['"]|\bimage\s*:\s*['"])(\/[^'"]+)/g)].map(match=>match[1]);
    for (const p of paths) {
      if (!/^\/(?:figures|video|art|images)\//.test(p)) continue;
      assert.ok(existsSync(join(root,'public',p.slice(1))), `Missing media ${p} referenced in ${relative(root,file)}`);
    }
  }
});
