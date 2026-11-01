# SEO and crawlable learning pages

Updated 1 November 2026. This release adds 47 real HTML pages: the home map, 42 lesson pages, the lesson index, the resource library and the weekly plan. The lesson text, practice tasks, exit checks and internal links are present in the HTML response, not only inside a JavaScript modal.

## What the build produces

- A unique title, description and canonical URL for every generated page.
- A single H1 and meaningful heading hierarchy for each page.
- Crawlable links between the home outline, lesson index, prerequisites, next lesson and resource library.
- JSON-LD using WebSite, LearningResource/WebPage and BreadcrumbList, with the actual author and revision date.
- A sitemap covering every generated canonical page, plus a permissive robots.txt pointing to that sitemap.
- Open Graph and Twitter metadata with a shared 1200 × 630 image.
- Relative asset URLs that work under the GitHub Pages project subpath.
- Lazy thumbnails and click-to-load YouTube players; videos do not autoplay on page load.

This site does not invent ratings, course accreditation, video upload dates or rich-result eligibility. It does not publish a fake VideoObject record for a video whose required metadata was not verified. Search engines decide indexing and ranking; publication and a sitemap alone do not guarantee placement.

## Verification

`npm run check` validates the curriculum and parses every generated HTML page. It checks unique canonicals/titles, descriptions, valid JSON-LD, one H1, local links/assets, visible lesson content, complete sitemap coverage and the absence of eager resource-library iframes. `npm test` additionally checks URL normalization, playlist identity, unsafe URL rejection, deduplication of the eleven supplied links and old progress compatibility.

## Primary references

- [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Google JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- [YouTube embedded player parameters](https://developers.google.com/youtube/player_parameters)

These official references informed the implementation. The editorial lesson structure and user-interface choices are original.

The coding lab adds the 47th canonical page. All 42 lesson pages link to context-specific practice. Its editor loads the Python runtime on demand; the brief, runtime description and navigation are present in the generated HTML.
