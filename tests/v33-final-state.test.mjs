import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,existsSync} from 'node:fs';
const read = path => readFileSync(path,'utf8');

test('final selected protein overlay is used by homepage and research listing metadata',()=>{
  const article=read('src/content/research/protein-modeling.mdx');
  assert.match(article,/image: '\/figures\/cards\/protein-card-overlay\.png'/);
  assert.ok(existsSync('public/figures/cards/protein-card-overlay.png'));
  assert.match(read('src/components/ResearchCard.astro'),/cards\/protein-/);
  assert.doesNotMatch(article,/image: '\/figures\/cards\/protein-5tkw-comparison-v32-white\.webp'/);
});

test('curved manifold Figure 3 is a numbered video pair with the two original MP4s',()=>{
  const article=read('src/content/research/packing-on-curved-manifolds.mdx');
  assert.match(article,/<VideoGroup id="fig-manifold-mono-jamming"/);
  assert.match(article,/mono-small-plane-jamming\.mp4/);
  assert.match(article,/mono-small-sphere-jamming\.mp4/);
  for(const media of ['mono-small-plane-jamming.mp4','mono-small-sphere-jamming.mp4']){
    assert.ok(existsSync(`public/video/curved-manifolds/${media}`));
  }
});

test('Safari back navigation and page visibility resume the curved-manifolds card video',()=>{
  const card=read('src/components/ResearchCard.astro');
  assert.match(card,/pageshow/);
  assert.match(card,/visibilitychange/);
  assert.match(card,/media-manifolds-contained/);
  assert.match(card,/video\.play\(\)/);
});

test('the final figure polish and polymer note are retained',()=>{
  const symbops=read('src/content/research/symbops.mdx');
  assert.match(symbops,/experimental-diamond-axes-panel-a\.png/);
  assert.match(symbops,/experimental-diamond-sublattices-panel-b\.png/);
  assert.match(read('src/content/research/protein-modeling.mdx'),/protein-fig1-combined-uncropped\.png/);
  assert.match(read('src/content/notes/rg-loop-geometry.mdx'),/three-dimensional, non-overlapping chains/);
});
