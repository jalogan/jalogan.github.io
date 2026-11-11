import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { join, resolve } from 'node:path';
const root=process.cwd();
const get=p=>readFileSync(resolve(root,p),'utf8');

test('protein paper is identified by its final peer-reviewed journal DOI',()=>{
  const publication=get('src/pages/publications.astro');
  const article=get('src/content/research/protein-modeling.mdx');
  assert.match(publication,/Effect of stereochemical constraints on the structural properties of folded proteins/);
  assert.match(publication,/Physical Review E 112, 054405 \(2025\)/);
  assert.match(publication,/https:\/\/doi.org\/10.1103\/9wf9-ywhw/);
  assert.match(article,/status: 'Published research'/);
  assert.doesNotMatch(article, /2025 preprint|2025 research preprint/);
  assert.match(article, /N-n\+1/);
});

test('the surrogate-force equation and caption specify the chosen vector sign convention',()=>{
  const article=get('src/content/research/md-surrogate.mdx');
  assert.ok(article.includes('from particle $i$ toward particle $j$'));
  assert.ok(article.includes('f(r) = dU/dr'));
  assert.ok(article.includes('−dU/dr'));
});

test('absent photo and CV files never generate public filler or dead CV navigation',()=>{
  const about=get('src/pages/about.astro');
  const header=get('src/components/SiteHeader.astro');
  const footer=get('src/components/SiteFooter.astro');
  assert.match(about,/availablePhotos\.length > 0 &&/);
  assert.match(about,/showCv &&/);
  assert.match(header,/showCv && <a class="nav-cta"/);
  assert.match(footer,/showCv && <a href="\/about\/#cv"/);
  assert.doesNotMatch(about,/Photo will appear here|PDF to be added/);
});

test('public SEO metadata and correctly scoped sitemap are available',()=>{
  const layout=get('src/layouts/BaseLayout.astro');
  assert.match(layout,/og:url/);
  assert.match(layout,/rel="canonical"/);
  const sitemap=get('public/sitemap.xml');
  assert.match(sitemap,/https:\/\/jalogan.github.io\/research\/protein-modeling\//);
  assert.match(sitemap,/https:\/\/jalogan.github.io\/notes\/rg-loop-geometry\//);
  assert.match(get('public/robots.txt'),/Sitemap: https:\/\/jalogan.github.io\/sitemap.xml/);
});

test('reader-facing pages and article copy contain no editorial placeholders or chat residue',()=>{
  const dirs=['src/content/research','src/content/notes','src/pages'];
  const bad=/(?:as (?:an AI|ChatGPT)|as requested in (?:the|our) chat|photo will appear here|pdf to be added|this section is intentionally a forward-looking test plan|I updated the website|TODO:|TBD:)/i;
  const scan=dir=>{
    for(const item of readdirSync(resolve(root,dir),{withFileTypes:true})){
      const path=join(dir,item.name);
      if(item.isDirectory()) scan(path);
      else if(/\.(?:astro|mdx)$/.test(item.name))assert.doesNotMatch(get(path),bad,path);
    }
  };
  dirs.forEach(scan);
});
