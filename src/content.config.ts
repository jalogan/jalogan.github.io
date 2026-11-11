import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const research = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/research' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    category: z.string(),
    year: z.number().optional(),
    status: z.enum(['Published research', 'Research preprint', 'Independent research', 'Draft']).optional(),
    image: z.string().optional(),
    imageAlt: z.string().optional(),
    video: z.string().optional(),
    featured: z.boolean().default(false),
    order: z.number().default(99),
    problem: z.string(),
    contribution: z.string(),
    result: z.string(),
    methods: z.array(z.string()),
    publicationUrl: z.string().url().optional(),
    originalUrl: z.string().url().optional()
  })
});
const notes = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/notes' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    category: z.string(),
    status: z.enum(['Exploration', 'Technical note', 'Completed']).default('Exploration'),
    order: z.number().default(99)
  })
});
export const collections = { research, notes };
