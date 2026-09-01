import { defineConfig } from 'astro/config';

import partytown from '@astrojs/partytown';

export default defineConfig({
  output: 'static',

  build: {
    format: 'directory'
  },

  integrations: [partytown()]
});