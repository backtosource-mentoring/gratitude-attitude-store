# Gratitude Attitude - Store Site

Static site for the Gratitude Attitude book collection by Esther Michele Kazir.
Books link to Amazon. Hosted on GitHub Pages from the `docs/` folder, custom domain backtosource.vip.

## Structure
- `docs/` - the published site (HTML, CSS, JS, images, sitemap, CNAME)
- `build/` - Python generator. `data.py` holds books, ASINs and cover copy.

## Rebuild
```
cd build && python3 build2.py
```
Edit `build/data.py` (ASINs, cover text, app link) and rebuild. Note: the generator does not touch `docs/CNAME`, `docs/.nojekyll` or the redirect script in `docs/404.html`; re-add them if you wipe `docs/`. Commit and push - Pages republishes automatically.

## Live products (checked 2026-10-21)
- Gratitude Attitude: hardcover B0H1QCT253, Kindle B0GS6WBFQK
- Workbook, 11 covers: see `build/data.py`
- The Agreement Journal: B0HNKLZX38
- App (iOS): https://apps.apple.com/app/id6805992249
