import json, os, html, datetime
from data import *

OUT = __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "docs")
TODAY = datetime.date.today().isoformat()
PAGES = []  # (path, priority)
E = html.escape

ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'

def pic(name, alt, w=400, cls="", eager=False, sizes="(max-width:600px) 70vw, 340px"):
    lazy = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    h = round(w * (1329 / 1000)) if name == "gratitude-attitude" else (round(w * 1.5) if name == "journal" else round(w * 4 / 3))
    return (f'<picture><source type="image/webp" srcset="/img/{name}-400.webp 400w, /img/{name}-800.webp 800w" sizes="{sizes}">'
            f'<img src="/img/{name}-800.jpg" alt="{E(alt)}" width="{w}" height="{h}" class="{cls}" {lazy}></picture>')

def buy(asin, label="Get it on Amazon", cls="btn-gold", item=""):
    return f'<a class="btn {cls}" href="{amz(asin)}" target="_blank" rel="noopener" data-buy="{E(item or asin)}">{label} {ARROW}</a>'

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "</script>"

PERSON = {"@type": "Person", "@id": SITE + "/#author", "name": AUTHOR, "url": SITE + "/about/",
          "image": SITE + "/img/esther-michele-kazir.jpg", "jobTitle": "Author", "sameAs": [IG, FB]}
ORG = {"@type": "Organization", "@id": SITE + "/#brand", "name": BRAND, "url": SITE + "/",
       "logo": SITE + "/img/icon-512.png", "founder": {"@id": SITE + "/#author"}, "sameAs": [IG, FB]}

def crumbs_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)]}

def crumbs_html(items):
    parts = [f'<a href="{u}">{E(n)}</a>' for n, u in items[:-1]] + [E(items[-1][0])]
    return '<nav class="crumbs" aria-label="Breadcrumb">' + "<span>/</span>".join(parts) + "</nav>"

NAV = [("The Book", "/gratitude-attitude-book/"), ("The Workbook", "/gratitude-workbook/"),
       ("The Journal", "/agreement-journal/"), ("Gratitude Practice", "/gratitude-practice/"), ("About", "/about/")]

def page(path, title, desc, body, jsonld=(), og_img="/img/gratitude-attitude-800.jpg", priority="0.7", og_type="website", sticky=""):
    url = SITE + path
    nav = "".join(f'<a href="{u}"{" aria-current=page" if u == path else ""}>{n}</a>' for n, u in NAV)
    lds = "".join(ld(x) for x in jsonld)
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="{AUTHOR}">
<meta name="theme-color" content="#0e2a20">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/img/icon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/img/icon-180.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Josefin+Sans:wght@300;400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
<script>document.documentElement.className='js'</script>
{lds}
</head>
<body>
<a class="sr" href="#main">Skip to content</a>
<header class="site-header">
 <div class="wrap">
  <a class="brand" href="/" aria-label="{BRAND} home"><img src="/img/logo.webp" alt="" width="42" height="42"><span>{BRAND}</span></a>
  <button class="menu-btn" aria-label="Menu" aria-expanded="false" aria-controls="nav"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M3 7h18M3 12h18M3 17h18"/></svg></button>
  <nav class="nav" id="nav" aria-label="Main">{nav}<a class="btn btn-gold" href="/gratitude-workbook/">Choose your vibe</a></nav>
 </div>
</header>
<main id="main">
{body}
</main>
{sticky}
<footer class="site-footer">
 <div class="wrap">
  <div class="cols">
   <div><a class="brand" href="/"><img src="/img/logo.webp" alt="" width="42" height="42" loading="lazy"><span>{BRAND}</span></a>
    <p>Books, workbooks and journals by {AUTHOR}. Gratitude, practiced like a skill.</p>
    <p><em class="gold">"{QUOTE}"</em></p></div>
   <div><h4>Books</h4><ul>
    <li><a href="/gratitude-attitude-book/">Gratitude Attitude</a></li>
    <li><a href="/gratitude-workbook/">The Workbook</a></li>
    <li><a href="/agreement-journal/">The Agreement Journal</a></li></ul></div>
   <div><h4>Read</h4><ul>
    <li><a href="/gratitude-practice/">How to Practice Gratitude</a></li>
    <li><a href="/gratitude-gifts/">Gratitude Gifts</a></li>
    <li><a href="/about/">About the Author</a></li></ul></div>
   <div><h4>Follow</h4><ul>
    <li><a href="{APP_IOS}" target="_blank" rel="noopener">The App (iPhone)</a></li>
    <li><a href="{IG}" target="_blank" rel="noopener">Instagram</a></li>
    <li><a href="{FB}" target="_blank" rel="noopener">Facebook</a></li></ul></div>
  </div>
  <div class="legal"><span>&copy; {datetime.date.today().year} {AUTHOR}. All rights reserved.</span><span>All books are sold and shipped by Amazon.</span></div>
 </div>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>'''
    d = OUT + path
    os.makedirs(d, exist_ok=True)
    open(d + "index.html", "w").write(doc)
    PAGES.append((path, priority))

def book_ld(name, sub, img, url, editions, desc, isbn=None, pages=None):
    o = {"@context": "https://schema.org", "@type": "Book", "@id": SITE + url + "#book", "name": name,
         "alternateName": f"{name}: {sub}", "author": PERSON, "publisher": ORG, "inLanguage": "en",
         "image": SITE + f"/img/{img}-800.jpg", "url": SITE + url, "description": desc,
         "genre": ["Self-Help", "Personal Growth", "Gratitude"],
         "workExample": [{"@type": "Book", "bookFormat": f"https://schema.org/{fmt}", "url": amz(a),
                          **({"isbn": isbn} if isbn and fmt == "Hardcover" else {}),
                          **({"numberOfPages": pages} if pages and fmt == "Hardcover" else {}),
                          "potentialAction": {"@type": "ReadAction", "target": amz(a)}} for fmt, a in editions]}
    return o

def faq_ld(qa):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]}

def faq_html(qa):
    return '<div class="faq">' + "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in qa) + "</div>"

def tile(c, sizes="(max-width:600px) 45vw, 240px"):
    return (f'<a class="tile reveal" data-g="{c["group"]}" href="/gratitude-workbook/{c["slug"]}/">'
            f'<div class="img">{pic(c["slug"], c["name"] + " cover of the Gratitude Attitude Workbook", sizes=sizes)}</div>'
            f'<div class="grp">{GROUPS[c["group"]]}</div><h3>{E(c["name"])}</h3><p>{E(c["line"])}</p></a>')

def gallery(with_filters=True):
    f = ""
    if with_filters:
        f = ('<div class="filters" role="group" aria-label="Filter covers by mood">'
             '<button class="chip" data-g="all" aria-pressed="true">All 11</button>' +
             "".join(f'<button class="chip" data-g="{k}" aria-pressed="false">{v}</button>' for k, v in GROUPS.items()) + "</div>")
    return f + '<div class="grid">' + "".join(tile(c) for c in COVERS) + "</div>"

HOME_FAQ = [
    ("What is Gratitude Attitude?", f"Gratitude Attitude is a collection of books by {AUTHOR}: the original book, a hands-on workbook and a 42-day journal. Together they turn gratitude from a feeling you wait for into a short daily practice you run on purpose."),
    ("Is every workbook cover different inside?", f"No. All eleven covers share the same {WORKBOOK_PAGES}-page interior. The cover is the only difference, so you can pick the one that fits you, or the person you are gifting."),
    ("Where can I buy the books?", "Every edition is sold and shipped by Amazon. Each button on this site opens the exact Amazon page for that edition."),
    ("Which one should I start with?", "Start with the book if you want the ideas and the story of Lily. Start with the workbook if you want to practice from day one. Choose The Agreement Journal if you already practice and want a 42-day record of what arrived."),
    ("Who are these books for?", "For every soul ready to move from autopilot to intention. Entrepreneurs, parents, students, people starting over. No experience needed."),
    ("Are the books hardcover?", "Yes. The workbook and The Agreement Journal are premium hardcovers. The original book is available in hardcover and as a Kindle eBook."),
]

def build_home():
    trio = [
        (BOOK["img"], "Read", "Gratitude Attitude", "The original book. The ideas, the story of Lily, and a clear map out of survival mode.", "/gratitude-attitude-book/", BOOK["hardcover"]),
        ("cosmic-roses", "Practice", "The Workbook", f"{WORKBOOK_PAGES} pages of exercises and daily frameworks. One interior, eleven covers to choose from.", "/gratitude-workbook/", None),
        ("journal", "Prove", "The Agreement Journal", "42 evenings. Write it in the past tense, sign it, and log the evidence when it arrives.", "/agreement-journal/", JOURNAL["asin"]),
    ]
    cards = ""
    for img, tag, name, txt, url, asin in trio:
        b = buy(asin, "Amazon", item=name) if asin else f'<a class="btn btn-gold" href="/gratitude-workbook/">Choose your vibe {ARROW}</a>'
        cards += (f'<article class="card reveal"><a href="{url}">{pic(img, name + " book cover", cls="cover")}</a>'
                  f'<div class="tag">{tag}</div><h3><a href="{url}" style="text-decoration:none">{E(name)}</a></h3><p>{E(txt)}</p>'
                  f'<div class="btn-row">{b}<a class="btn btn-ghost on-light" href="{url}">Details</a></div></article>')
    fan = "".join(pic(s, "") .replace('alt=""', f'alt="{n} workbook cover"') for s, n in
                  [("tulip", "Tulip"), ("thrive", "Thrive"), ("cosmic-roses", "Cosmic Roses"), ("time-to-bloom", "Time to Bloom"), ("cheshire-cosmic", "Cheshire Cosmic")])
    body = f'''
<section class="hero dark stars">
 <div class="wrap">
  <div>
   <p class="eyebrow">Books by {AUTHOR}</p>
   <h1>Gratitude, practiced <em class="gold">like a skill.</em></h1>
   <p class="lead">Not a mood to wait for. A short daily practice that moves you from survival mode into intention, with a book to understand it, a workbook to train it, and a journal to prove it.</p>
   <div class="btn-row">
    <a class="btn btn-gold" href="#collection">Start here {ARROW}</a>
    <a class="btn btn-ghost" href="/gratitude-workbook/">See all 11 vibes</a>
   </div>
   <p class="hero-note">Premium hardcovers &middot; Shipped by Amazon worldwide</p>
  </div>
  <div class="hero-art"><span class="halo"></span><span class="halo h2"></span>
   <a class="book3d" href="/gratitude-attitude-book/" aria-label="Gratitude Attitude book">{pic("gratitude-attitude", "Gratitude Attitude: A Practical Guide to Consciousness Transformation, hardcover by Esther Michele Kazir", eager=True)}</a>
  </div>
 </div>
</section>

<div class="dark quote-band"><div class="wrap"><blockquote>"{QUOTE}"<cite>{AUTHOR}</cite></blockquote></div></div>

<section id="collection">
 <div class="wrap center">
  <p class="eyebrow">The collection</p>
  <h2>Read it. Practice it. <em class="gold">Prove it.</em></h2>
  <p class="lead narrow">Three books, one method. Pick the door that fits where you are today.</p>
  <div class="trio">{cards}</div>
 </div>
</section>

<section class="dark stars">
 <div class="wrap center">
  <p class="eyebrow">The method</p>
  <h2>Five minutes. Three moves.</h2>
  <p class="lead narrow">Every book in the collection runs on the same daily loop. Simple enough to keep, specific enough to work.</p>
  <div class="steps" style="text-align:left">
   <div class="step reveal"><span class="n">01</span><h3>Notice</h3><p>Catch what is already working before the mind lists what is missing. Three things, written down, specific.</p></div>
   <div class="step reveal"><span class="n">02</span><h3>Agree</h3><p>Write what you want in the past tense, as if it already arrived. Sign it. Wishing becomes a decision.</p></div>
   <div class="step reveal"><span class="n">03</span><h3>Act</h3><p>One aligned action today. Small is fine. Then log the evidence when it shows up, with the date.</p></div>
  </div>
  <p style="margin-top:50px"><a class="btn btn-ghost" href="/gratitude-practice/">Read the full practice guide {ARROW}</a></p>
 </div>
</section>

<section class="cream">
 <div class="wrap">
  <div class="split">
   <div class="fan reveal" aria-hidden="false">{fan}</div>
   <div>
    <p class="eyebrow">The workbook</p>
    <h2>One workbook. <em class="gold">Eleven vibes.</em></h2>
    <p class="lead">The same {WORKBOOK_PAGES}-page interior in eleven hardcover editions, from night-sky cosmic to soft florals to library green. Choose your vibe. Or your best friend's vibe, for the perfect gift.</p>
    <ul class="ticks"><li>Practical exercises and creative prompts</li><li>Daily reflection frameworks</li><li>Consciousness anchors for stressful days</li><li>Premium hardcover, made to sit on a desk</li></ul>
    <a class="btn btn-gold" href="#covers">Find your vibe {ARROW}</a>
   </div>
  </div>
 </div>
</section>

<section id="covers">
 <div class="wrap center">
  <p class="eyebrow">Choose your vibe</p>
  <h2>Yours, or a friend's?</h2>
  {gallery()}
 </div>
</section>

<section class="dark stars">
 <div class="wrap">
  <div class="split rev">
   <div class="center"><a href="/agreement-journal/" class="book3d" style="display:inline-block;transform:rotateY(14deg)">{pic("journal", "The Agreement Journal hardcover, 42 evenings of gratitude and evidence", sizes="(max-width:600px) 60vw, 300px")}</a></div>
   <div>
    <p class="eyebrow">New &middot; The Agreement Journal</p>
    <h2>Stop hoping. <em class="gold">Start keeping receipts.</em></h2>
    <p class="lead">You have written down what you want before. What you never had is proof. Each evening: a quote, three lines of gratitude in the past tense, one action, your signature. The facing page stays empty until reality catches up.</p>
    <ul class="ticks"><li>42 daily spreads: agreement left, evidence right</li><li>Undated, so you start tonight</li><li>{JOURNAL["pages"]} pages, {JOURNAL["size"]} hardcover</li></ul>
    <div class="btn-row">{buy(JOURNAL["asin"], item="The Agreement Journal")}<a class="btn btn-ghost" href="/agreement-journal/">Look inside</a></div>
   </div>
  </div>
 </div>
</section>

<section class="cream" id="app">
 <div class="wrap split">
  <div>
   <p class="eyebrow">The app &middot; Gratitude Attitude: Daily</p>
   <h2>The journal lives at night. <em class="gold">The app is for the day.</em></h2>
   <p class="lead">One screen, one line at a time from the same collection. Tap the card for a new one, or press Align Now when doubt shows up mid-day. Works offline, no account, no ads.</p>
   <div class="btn-row"><a class="btn btn-gold" href="{APP_IOS}" target="_blank" rel="noopener" data-buy="app-ios">Download on the App Store {ARROW}</a></div>
   <p class="fine">iPhone and iPad. Android coming soon.</p>
  </div>
  <div class="center"><img src="/img/logo.webp" alt="Gratitude Attitude emblem" width="260" height="257" loading="lazy" style="margin:0 auto;filter:drop-shadow(0 20px 40px rgba(168,131,42,.35))"></div>
 </div>
</section>

<section>
 <div class="wrap">
  <div class="author">
   <img src="/img/esther-michele-kazir.webp" alt="{AUTHOR}, author of Gratitude Attitude" width="320" height="320" loading="lazy">
   <div>
    <p class="eyebrow">The author</p>
    <h2>{AUTHOR}</h2>
    <p class="lead">Esther writes for people who are done collecting inspiration and ready to practice. Her work draws on the teachings of Abraham Hicks, Bruce Lipton and Viktor Frankl, and turns them into tools you can open every morning.</p>
    <a class="btn btn-ghost on-light" href="/about/">Read her story {ARROW}</a>
   </div>
  </div>
 </div>
</section>

<section>
 <div class="wrap center">
  <p class="eyebrow">Questions</p>
  <h2>Before you choose</h2>
  {faq_html(HOME_FAQ)}
 </div>
</section>

<section class="dark stars center">
 <div class="narrow">
  <h2>Your practice starts <em class="gold">tonight.</em></h2>
  <p class="lead">Pick a book. Open it before bed. Write three lines. That is the whole beginning.</p>
  <div class="btn-row">{buy(BOOK["hardcover"], "Get the book", item="Gratitude Attitude hardcover")}<a class="btn btn-ghost" href="/gratitude-workbook/">Choose a workbook</a></div>
 </div>
</section>'''
    website = {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#site", "name": BRAND, "url": SITE + "/",
               "publisher": {"@id": SITE + "/#brand"}, "inLanguage": "en"}
    org = {"@context": "https://schema.org", **ORG}
    items = {"@context": "https://schema.org", "@type": "ItemList", "name": "Gratitude Attitude collection", "itemListElement": [
        {"@type": "ListItem", "position": 1, "url": SITE + "/gratitude-attitude-book/", "name": "Gratitude Attitude"},
        {"@type": "ListItem", "position": 2, "url": SITE + "/gratitude-workbook/", "name": "Gratitude Attitude Workbook"},
        {"@type": "ListItem", "position": 3, "url": SITE + "/agreement-journal/", "name": "The Agreement Journal"}]}
    page("/", "Gratitude Attitude | Gratitude Workbook, Journal & Book",
         "Gratitude, practiced like a skill. A hardcover gratitude workbook in 11 covers, a 42-day gratitude journal, and the Gratitude Attitude book.",
         body, [website, org, items, faq_ld(HOME_FAQ), {"@context": "https://schema.org", "@type": "MobileApplication", "name": "Gratitude Attitude: Daily", "operatingSystem": "iOS, iPadOS", "applicationCategory": "LifestyleApplication", "url": APP_IOS, "author": {"@id": SITE + "/#author"}}], priority="1.0")

def build_book():
    p = "/gratitude-attitude-book/"
    desc = "Gratitude Attitude by Esther Michele Kazir: a practical guide from survival mode to purpose, abundance and joy, told through the story of Lily. Hardcover and Kindle."
    qa = [("What is the book about?", "It is a practical guide to shifting from survival mode into intention. Through the story of Lily, a determined character who refuses to accept her limits, the book walks through the principles of how attention and gratitude shape the life you build."),
          ("Is there a Kindle edition?", "Yes. Gratitude Attitude is available on Amazon as a Kindle eBook and as a hardcover."),
          ("Is there a workbook to go with it?", "Yes. The Gratitude Attitude Workbook turns the ideas into daily exercises. It comes in eleven hardcover cover editions with the same interior.")]
    body = f'''
<section class="product">
 <div class="wrap">
  {crumbs_html([("Home", "/"), ("Gratitude Attitude", p)])}
  <div class="split">
   <div class="cover-wrap">{pic(BOOK["img"], "Gratitude Attitude book cover by Esther Michele Kazir", eager=True, sizes="(max-width:900px) 80vw, 460px")}</div>
   <div>
    <p class="eyebrow">The original book</p>
    <h1>Gratitude Attitude</h1>
    <p class="lead">A Practical Guide to Consciousness Transformation</p>
    <p>Are you living at your full potential, or are your plans still sitting next to your doubts? Your mind is your most powerful tool. It can carry you toward what matters, or it can quietly hold you in place.</p>
    <p>In <em>Gratitude Attitude</em>, {AUTHOR} lays out a clear, practical route from survival mode to a life of purpose, abundance and joy. You follow Lily, a determined character who refuses to settle for her limits, and see each principle at work in a real life before you try it in yours.</p>
    <div class="facts"><div><b>Formats</b><span>Hardcover &middot; Kindle</span></div><div><b>Hardcover</b><span>{BOOK["pages"]} pages</span></div><div><b>Language</b><span>English</span></div></div>
    <div class="btn-row">{buy(BOOK["hardcover"], "Hardcover on Amazon", item="Gratitude Attitude hardcover")}{buy(BOOK["kindle"], "Kindle", "btn-ghost on-light", item="Gratitude Attitude Kindle")}</div>
    <p class="fine">Sold and shipped by Amazon. Price and delivery shown at checkout.</p>
    <h2 style="margin-top:60px;font-size:36px">Inside the book</h2>
    <ul class="ticks"><li>Why the mind defaults to survival mode, and how to step out of it</li><li>The story of Lily, told chapter by chapter alongside the method</li><li>Gratitude as a daily practice, not a passing feeling</li><li>Ideas drawn from Abraham Hicks, Bruce Lipton and Viktor Frankl, made practical</li><li>A closing space to write your own quotes</li></ul>
    <div class="inline-cta"><a href="/gratitude-workbook/">{pic("thrive", "Gratitude Attitude Workbook", sizes="130px")}</a><div><h3>Practice what you read</h3><p>The workbook turns each idea into exercises you can do in minutes.</p><a class="btn btn-ghost on-light" href="/gratitude-workbook/">Choose your vibe {ARROW}</a></div></div>
    {faq_html(qa)}
   </div>
  </div>
 </div>
</section>'''
    sticky = f'<div class="sticky-buy"><span>Gratitude Attitude<br><small style="color:var(--on-dark-muted)">Hardcover &middot; Kindle</small></span>{buy(BOOK["hardcover"], "Amazon", item="Gratitude Attitude hardcover sticky")}</div>'
    page(p, "Gratitude Attitude Book by Esther Michele Kazir | Hardcover & Kindle", desc, body,
         [book_ld("Gratitude Attitude", BOOK["subtitle"], BOOK["img"], p, [("Hardcover", BOOK["hardcover"]), ("EBook", BOOK["kindle"])], desc, pages=BOOK["pages"]),
          crumbs_ld([("Home", "/"), ("Gratitude Attitude", p)]), faq_ld(qa)], priority="0.9", sticky=sticky)

WB_INSIDE = '<ul class="ticks"><li>Practical tools: exercises and creative prompts that shift your daily mindset</li><li>Daily reflection frameworks for clarity and self-discovery</li><li>Consciousness anchors for stressful moments</li><li>Space to write, every day, in a hardcover that lasts</li></ul>'

def build_workbook_hub():
    p = "/gratitude-workbook/"
    desc = f"A {WORKBOOK_PAGES}-page hardcover gratitude workbook with daily exercises and reflection frameworks. One interior, 11 cover designs. Pick yours or gift one."
    qa = [("Do the covers have different content?", f"No. All eleven editions share the same {WORKBOOK_PAGES}-page interior. Only the cover changes."),
          ("Is this a gratitude journal?", "It is a workbook: guided exercises, prompts and daily frameworks, with space to write. For a pure 42-day journaling cycle, see The Agreement Journal."),
          ("Is it a good gift?", "Yes. Choosing the cover that matches someone's personality is what makes it personal. Order it on Amazon and send it straight to them."),
          ("Do I need to read the book first?", "No. The workbook stands on its own. The book adds the ideas and the story behind each exercise.")]
    body = f'''
<section class="product" style="padding-bottom:40px">
 <div class="wrap center">
  {crumbs_html([("Home", "/"), ("The Workbook", p)])}
  <p class="eyebrow">Gratitude Attitude Workbook</p>
  <h1>The gratitude workbook, <em class="gold">in your vibe.</em></h1>
  <p class="lead narrow">A hands-on, {WORKBOOK_PAGES}-page hardcover that takes you from automatic, limiting habits of mind into a steady daily practice. One interior. Eleven vibes. Choose yours, or your friend's for the perfect gift.</p>
 </div>
</section>
<section style="padding-top:0">
 <div class="wrap center" id="covers">{gallery()}</div>
</section>
<section class="cream">
 <div class="wrap split">
  <div>
   <p class="eyebrow">What is inside</p>
   <h2>Not another journal. <em class="gold">A tool.</em></h2>
   <p class="lead">Each section is built to be used, not admired. Open it for five minutes in the morning or the evening and move one step from reaction to intention.</p>
   {WB_INSIDE}
  </div>
  <div>
   <div class="facts" style="grid-template-columns:1fr 1fr"><div><b>Interior</b><span>{WORKBOOK_PAGES} pages</span></div><div><b>Format</b><span>Hardcover</span></div><div><b>Editions</b><span>11 covers</span></div><div><b>Ships</b><span>via Amazon</span></div></div>
   {faq_html(qa)}
  </div>
 </div>
</section>'''
    il = {"@context": "https://schema.org", "@type": "ItemList", "name": "Gratitude Attitude Workbook cover editions",
          "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": SITE + f"/gratitude-workbook/{c['slug']}/", "name": c["name"]} for i, c in enumerate(COVERS)]}
    page(p, "Gratitude Workbook in 11 Hardcover Covers | Gratitude Attitude", desc, body,
         [il, crumbs_ld([("Home", "/"), ("The Workbook", p)]), faq_ld(qa)], og_img="/img/cosmic-roses-800.jpg", priority="0.9")

def build_cover(c, i):
    p = f"/gratitude-workbook/{c['slug']}/"
    name = f"Gratitude Attitude Workbook: {c['name']} Edition"
    desc = f"{c['name']} edition of the Gratitude Attitude Workbook. {c['line']} A {WORKBOOK_PAGES}-page hardcover gratitude workbook."
    others = [x for x in COVERS if x is not c]
    others = (others[i:] + others[:i])[:4]
    body = f'''
<section class="product">
 <div class="wrap">
  {crumbs_html([("Home", "/"), ("The Workbook", "/gratitude-workbook/"), (c["name"], p)])}
  <div class="split">
   <div class="cover-wrap">{pic(c["slug"], f"{c['name']} cover, Gratitude Attitude Workbook hardcover by {AUTHOR}", eager=True, sizes="(max-width:900px) 80vw, 460px")}</div>
   <div>
    <p class="eyebrow">{GROUPS[c["group"]]} &middot; Workbook edition</p>
    <h1>{E(c["name"])}</h1>
    <p class="lead">{E(c["line"])} For {E(c["for"])}.</p>
    <p>{E(c["body"])}</p>
    <div class="facts"><div><b>Format</b><span>Hardcover</span></div><div><b>Interior</b><span>{WORKBOOK_PAGES} pages</span></div><div><b>Author</b><span>E. M. Kazir</span></div></div>
    <div class="btn-row">{buy(c["asin"], item=c["name"])}<a class="btn btn-ghost on-light" href="/gratitude-workbook/">See all vibes</a></div>
    <p class="fine">Same interior in all 11 editions. Sold and shipped by Amazon.</p>
    <h2 style="margin-top:60px;font-size:36px">Inside every edition</h2>
    {WB_INSIDE}
    <div class="callout"><p><em class="gold">Giving it as a gift?</em> Order on Amazon and enter the recipient's address at checkout. Amazon lets you add a gift message.</p></div>
   </div>
  </div>
  <div class="more">
   <h2>Other vibes you might love</h2>
   <div class="grid" style="margin-top:30px">{"".join(tile(x) for x in others)}</div>
  </div>
 </div>
</section>'''
    sticky = f'<div class="sticky-buy"><span>{E(c["name"])}<br><small style="color:var(--on-dark-muted)">Workbook &middot; Hardcover</small></span>{buy(c["asin"], "Amazon", item=c["name"] + " sticky")}</div>'
    bl = book_ld(name, "A Practical Guide to Consciousness Transformation", c["slug"], p, [("Hardcover", c["asin"])],
                 f"{c['line']} {c['body']}", pages=WORKBOOK_PAGES)
    bl["isPartOf"] = {"@type": "CreativeWork", "name": "Gratitude Attitude Workbook", "url": SITE + "/gratitude-workbook/"}
    page(p, f"{c['name']} Gratitude Workbook | Hardcover | Gratitude Attitude", desc, body,
         [bl, crumbs_ld([("Home", "/"), ("The Workbook", "/gratitude-workbook/"), (c["name"], p)])],
         og_img=f"/img/{c['slug']}-800.jpg", priority="0.8", sticky=sticky)

def build_journal():
    p = "/agreement-journal/"
    desc = "A 42-day undated gratitude and manifestation journal. Write it in the past tense, sign it, log the evidence. 124-page 6x9 hardcover by Esther Michele Kazir."
    qa = [("Is The Agreement Journal dated?", "No. It is undated. Start any evening and repeat the 42-day cycle as many times as you like."),
          ("How long does each evening take?", "About five to ten minutes: one quote, three lines of gratitude written in the past tense, one aligned action, and your signature."),
          ("What goes on the evidence page?", "It stays blank until something arrives. Then you write what came and the date it came. Over 42 days you build a dated record."),
          ("How is it different from the workbook?", "The workbook teaches the practice with exercises and frameworks. The journal is a focused 42-day cycle for logging agreements and evidence.")]
    body = f'''
<section class="product">
 <div class="wrap">
  {crumbs_html([("Home", "/"), ("The Agreement Journal", p)])}
  <div class="split">
   <div class="cover-wrap">{pic("journal", "The Agreement Journal hardcover cover by Esther Michele Kazir", eager=True, sizes="(max-width:900px) 80vw, 460px")}</div>
   <div>
    <p class="eyebrow">New &middot; 42-day gratitude journal</p>
    <h1>The Agreement Journal</h1>
    <p class="lead">Signed &amp; Arrived: 42 Evenings of Gratitude and Evidence</p>
    <p>You have written down what you want before. You have said the affirmations. What you have never had is proof.</p>
    <p>This journal runs one 42-day cycle on a single idea: write it in the past tense, sign your name to it, and leave the facing page empty until reality catches up. At the end you are not holding a book of hopes. You are holding a dated record of what your own writing came before.</p>
    <div class="facts"><div><b>Format</b><span>Hardcover</span></div><div><b>Pages</b><span>{JOURNAL["pages"]}</span></div><div><b>Size</b><span>{JOURNAL["size"]}</span></div></div>
    <div class="btn-row">{buy(JOURNAL["asin"], item="The Agreement Journal")}</div>
    <p class="fine">ISBN 979-8162441816 &middot; Sold and shipped by Amazon.</p>
    <h2 style="margin-top:60px;font-size:36px">How each evening works</h2>
    <ul class="ticks"><li><b>Left page, the agreement:</b> one quote, three lines of gratitude for something not yet here, one aligned action, your signature</li><li><b>Right page, the evidence:</b> blank until something arrives, then what came and the date</li><li>A weekly opener and a weekly reset</li><li>Undated. Start tonight, repeat the cycle as often as you need</li></ul>
    <div class="callout"><p>Sign it. Log it. <em class="gold">Prove it.</em></p></div>
    {faq_html(qa)}
   </div>
  </div>
 </div>
</section>'''
    sticky = f'<div class="sticky-buy"><span>The Agreement Journal<br><small style="color:var(--on-dark-muted)">Hardcover &middot; 42 evenings</small></span>{buy(JOURNAL["asin"], "Amazon", item="Agreement Journal sticky")}</div>'
    page(p, "The Agreement Journal: 42-Day Gratitude Journal | Hardcover", desc, body,
         [book_ld(JOURNAL["name"], JOURNAL["subtitle"], "journal", p, [("Hardcover", JOURNAL["asin"])], desc, isbn=JOURNAL["isbn"], pages=JOURNAL["pages"]),
          crumbs_ld([("Home", "/"), ("The Agreement Journal", p)]), faq_ld(qa)], og_img="/img/journal-800.jpg", priority="0.9", sticky=sticky)

def build_about():
    p = "/about/"
    desc = f"About {AUTHOR}, author of Gratitude Attitude, the Gratitude Attitude Workbook and The Agreement Journal."
    body = f'''
<section class="article">
 <div class="narrow">
  {crumbs_html([("Home", "/"), ("About", p)])}
  <img src="/img/esther-michele-kazir.webp" alt="{AUTHOR}" width="220" height="220" style="border-radius:50%;margin-bottom:30px" fetchpriority="high">
  <p class="eyebrow">The author</p>
  <h1>{AUTHOR}</h1>
  <p class="lead">Author of the Gratitude Attitude collection.</p>
  <p>Esther writes for people who have read enough about gratitude and are ready to practice it. Her books take ideas she has lived with for years, from the teachings of Abraham Hicks, Bruce Lipton and Viktor Frankl, and turn them into simple tools: a few lines in the morning, a signature at night, a page that waits for evidence.</p>
  <p>The original book, <a href="/gratitude-attitude-book/">Gratitude Attitude</a>, follows Lily from survival mode to intention. <a href="/gratitude-workbook/">The workbook</a> turns each idea into exercises. <a href="/agreement-journal/">The Agreement Journal</a> runs a 42-day cycle of gratitude written in the past tense.</p>
  <div class="callout"><p><em class="gold">"{QUOTE}"</em></p></div>
  <p>Follow along on <a href="{IG}" target="_blank" rel="noopener">Instagram</a> and <a href="{FB}" target="_blank" rel="noopener">Facebook</a>.</p>
 </div>
</section>'''
    pl = {"@context": "https://schema.org", "@type": "ProfilePage", "mainEntity": PERSON}
    page(p, f"About {AUTHOR} | Author of Gratitude Attitude", desc, body, [pl, crumbs_ld([("Home", "/"), ("About", p)])],
         og_img="/img/esther-michele-kazir.jpg", priority="0.6", og_type="profile")
