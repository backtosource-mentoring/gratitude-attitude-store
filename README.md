# Gratitude Attitude - Store Site

Static site for the Gratitude Attitude book collection by Esther Michele Kazir.
Books link to Amazon. Hosted on Netlify (publish directory: `site/`).

## Structure
- `site/` - the deployed site (HTML, CSS, JS, images, sitemap, redirects)
- `build/` - Python generator. `data.py` holds books, ASINs and cover copy.

## Rebuild
```
cd build && python3 build2.py
```
Edit `build/data.py` (ASINs, cover text, app link) and rebuild. Then redeploy `site/`.

## Live products (checked 2026-10-21)
- Gratitude Attitude: hardcover B0H1QCT253, Kindle B0GS6WBFQK
- Workbook, 11 covers: see `build/data.py`
- The Agreement Journal: B0HNKLZX38
- App (iOS): https://apps.apple.com/app/id6805992249
