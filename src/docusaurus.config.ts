import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'My Site',
  tagline: 'Dinosaurs are cool',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },
themes: ['@docusaurus/theme-live-codeblock'],
plugins: ['docusaurus-lunr-search'],
  // Set the production url of your site here
  url: 'https://your-docusaurus-site.example.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'facebook', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

    themeConfig: {
    prism: {
      additionalLanguages: ['markup'],
    },
    
    navbar: {
      title: 'Format.JS',
      logo: {
        alt: 'FormatJS',
        src: 'img/logo.svg',
        srcDark: 'img/logo-dark.svg',
      },
      items: [
        {
          to: 'docs/getting-started/installation',
          label: 'Docs',
          position: 'left',
          activeBaseRegex: 'docs/(getting-started|guides|core-concepts)',
        },
        {
          to: 'docs/react-intl',
          label: 'API References',
          position: 'left',
          activeBaseRegex:
            'docs/(vue-intl|intl|react-intl|intl-messageformat|icu-messageformat-parser)',
        },
        {
          to: 'docs/polyfills',
          label: 'Polyfills',
          position: 'left',
        },
        {
          to: 'docs/tooling/cli',
          label: 'Tooling',
          position: 'left',
          activeBaseRegex:
            'docs/tooling/(cli|linter|babel-plugin|ts-transformer|swc-plugin)',
        },
        {
          href: 'https://github.com/formatjs/formatjs',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Getting Started',
              to: 'docs/getting-started/installation',
            },
            {
              to: 'docs/polyfills',
              label: 'Polyfills',
            },
            {
              to: 'docs/intl-messageformat',
              label: 'Libraries',
            },
            {
              to: 'docs/tooling/cli',
              label: 'Tooling',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Stack Overflow',
              href: 'https://stackoverflow.com/questions/tagged/formatjs',
            },
            {
              label: 'Slack',
              href: 'https://formatjs.slack.com/',
            },
          ],
        },
        {
          title: 'Social',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/formatjs/formatjs',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} FormatJS. Built with Docusaurus.`,
    },
    liveCodeBlock: {
      /**
       * The position of the live playground, above or under the editor
       * Possible values: "top" | "bottom"
       */
      playgroundPosition: 'bottom',
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
