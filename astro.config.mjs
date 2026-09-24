import { defineConfig } from 'astro/config';

import partytown from '@astrojs/partytown';

import cloudflare from "@astrojs/cloudflare";

import critters from 'astro-critters';

export default defineConfig({
  output: "hybrid",

  build: {
    format: 'directory'
  },

  integrations: [partytown({
      config: {
        forward: ['dataLayer.push'],
      },
    }),
    // Inlines the above-the-fold ("critical") CSS directly into each
    // prerendered page's <head> and switches the rest of the shared
    // stylesheet to load asynchronously (preload + swap), so the CSS
    // bundle no longer blocks first render (~990ms per PageSpeed Insights).
    critters(),
  ],
  adapter: cloudflare()
});