import { defineConfig } from 'astro/config';

import partytown from '@astrojs/partytown';

import cloudflare from "@astrojs/cloudflare";

export default defineConfig({
  output: "hybrid",

  build: {
    format: 'directory'
  },

  integrations: [partytown({
      config: {
        forward: ['dataLayer.push'],
      },
    }),],
  adapter: cloudflare()
});