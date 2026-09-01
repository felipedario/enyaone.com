import { defineCollection, z } from 'astro:content';

const songsCollection = defineCollection({
  type: 'data',
  schema: z.array(z.object({
    title: z.string(),
    songLink: z.string().optional(),
    albumText: z.string(),
    albumLinks: z.array(z.object({
      title: z.string(),
      href: z.string()
    })),
    streamLink: z.string().optional()
  }))
});

const albumsCollection = defineCollection({
  type: 'data',
  schema: z.array(z.object({
    title: z.string(),
    year: z.string().optional(),
    type: z.string().optional(),
    cover: z.string(),
    link: z.string().optional(),
    description: z.string(),
    buyLink: z.string().optional()
  }))
});

export const collections = {
  'songs': songsCollection,
  'albums': albumsCollection
};
