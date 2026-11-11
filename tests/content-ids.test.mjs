import test from 'node:test';
import assert from 'node:assert/strict';
import { readdirSync, readFileSync } from 'node:fs';
import { join, resolve } from 'node:path';

const base = resolve('src/content');
const components = /<(FigureGroup|Figure|VideoFigure|VideoGroup|Equation)\b[^>]*?\bid="([^"]+)"/g;
const refs = /<(FigRef|EqRef)\b[^>]*?\bid="([^"]+)"/g;

function files(dir) {
  return readdirSync(dir, { withFileTypes: true }).flatMap(entry => {
    const path = join(dir, entry.name);
    return entry.isDirectory() ? files(path) : entry.isFile() && entry.name.endsWith('.mdx') ? [path] : [];
  });
}

for (const path of files(base)) {
  test(`scientific IDs and references are valid in ${path.slice(base.length+1)}`, () => {
    const source = readFileSync(path, 'utf8');
    const ids = new Set();
    for (const [, component, id] of source.matchAll(components)) {
      assert.match(id, /^(fig|eq)-[a-z0-9-]+$/, `Invalid ID: ${id}`);
      assert.equal(id.startsWith(component === 'Equation' ? 'eq-' : 'fig-'), true, `${component} ID has wrong prefix: ${id}`);
      assert.equal(ids.has(id), false, `Duplicate ID: ${id}`);
      ids.add(id);
    }
    for (const [, component, id] of source.matchAll(refs)) {
      assert.equal(ids.has(id), true, `Unresolved ${component}: ${id}`);
    }
  });
}
