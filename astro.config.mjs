import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import { unified } from '@astrojs/markdown-remark';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import remarkScientificRefs from './plugins/remarkScientificRefs.mjs';

export default defineConfig({
  site: 'https://jalogan.github.io',
  output: 'static',
  integrations: [mdx()],
  markdown: {
    processor: unified({
      remarkPlugins: [remarkMath, remarkScientificRefs],
      rehypePlugins: [rehypeKatex]
    })
  }
});
