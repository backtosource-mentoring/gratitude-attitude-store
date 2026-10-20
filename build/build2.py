from build import *

PRACTICE_FAQ = [
    ("How long should a daily gratitude practice take?", "Five minutes is enough. Consistency matters more than length. A short practice you keep beats a long one you skip."),
    ("Is it better to practice gratitude in the morning or at night?", "Both work. Morning sets direction for the day. Evening lets you review what actually happened. Many people do three lines in the morning and a short evidence log at night."),
    ("What if I cannot think of anything to be grateful for?", "Go smaller and more specific. A warm cup, a message that arrived, a door someone held. Specific beats grand. On hard days, one honest line counts."),
    ("Do I need a special journal?", "No. Any notebook works. A guided workbook or journal helps because the structure removes the question of what to write, which is where most people quit."),
    ("What does writing gratitude in the past tense mean?", "You describe something you want as if it already happened and you are thankful for it, then sign it. It turns a vague wish into a clear decision you can act on and track."),
]

def build_practice():
    p = "/gratitude-practice/"
    title = "How to Practice Gratitude Daily: A Practical 5-Minute Guide"
    desc = "How to practice gratitude so it sticks: three daily moves, a 5-minute routine, gratitude in the past tense, hard days, and the mistakes that make lists fade."
    toc = [("why", "Why most gratitude lists fade"), ("moves", "The three moves"), ("routine", "A 5-minute daily routine"),
           ("past", "Gratitude in the past tense"), ("hard", "Gratitude on hard days"), ("week", "The weekly reset"),
           ("mistakes", "Five common mistakes"), ("tools", "Tools that make it easier"), ("faq", "Questions")]
    body = f'''
<article class="article">
 <div class="narrow">
  {crumbs_html([("Home", "/"), ("Gratitude Practice", p)])}
  <p class="eyebrow">Guide</p>
  <h1>How to practice gratitude <em class="gold">so it actually sticks</em></h1>
  <div class="byline"><img src="/img/esther-michele-kazir.webp" alt="" width="44" height="44">By {AUTHOR}</div>
  <p class="lead">Gratitude is not a mood you wait for. It is a skill, and like any skill it grows with short, specific, repeated practice. Here is a five-minute daily method you can start tonight.</p>
  <nav class="toc" aria-label="Contents"><ol>{"".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in toc)}</ol></nav>

  <h2 id="why">Why most gratitude lists fade</h2>
  <p>Most people start a gratitude list with good intentions and stop within two weeks. The reason is rarely laziness. It is repetition without attention. Writing "my family, my health, my home" every night turns into a ritual the hand performs while the mind is somewhere else.</p>
  <p>Gratitude works when it changes what you notice. That only happens when the practice forces you to look again, every day, at something specific. The method below is built around that one idea.</p>

  <h2 id="moves">The three moves</h2>
  <h3>1. Notice</h3>
  <p>Before the mind lists what is missing, catch three things that are already working. Make each one specific and from the last 24 hours. Not "my partner", but "the way he left the coffee ready before I woke up". Specific details pull your attention back into your actual day.</p>
  <h3>2. Agree</h3>
  <p>Choose one thing you want and write it as if it already arrived, in the past tense, with thanks. "I am grateful the project was approved and the team felt proud." Then sign it. The signature matters. It turns a wish into a decision you have agreed to.</p>
  <h3>3. Act</h3>
  <p>Write one small action, taken today, that moves toward what you just agreed to. One email. One call. Ten minutes of the work. Gratitude without action becomes daydreaming. Action without gratitude becomes pressure. Together they become direction.</p>

  <div class="inline-cta"><a href="/gratitude-workbook/">{pic("time-to-bloom", "Gratitude Attitude Workbook", sizes="130px")}</a><div><h3>Want the structure done for you?</h3><p>The Gratitude Attitude Workbook guides each move with prompts and daily frameworks.</p><a class="btn btn-ghost on-light" href="/gratitude-workbook/">See the workbook {ARROW}</a></div></div>

  <h2 id="routine">A 5-minute daily routine</h2>
  <ol>
   <li><b>Minute 1.</b> Sit somewhere quiet. Put the phone face down. Take three slow breaths.</li>
   <li><b>Minutes 2 to 3.</b> Notice: write three specific things from the last day that you are thankful for.</li>
   <li><b>Minute 4.</b> Agree: write one thing you want, in the past tense, with thanks. Sign it.</li>
   <li><b>Minute 5.</b> Act: write the one action you will take today. Then close the book.</li>
  </ol>
  <p>Do it at the same time and place every day. Pair it with something you already do: the first coffee, or the last ten minutes before sleep. A fixed trigger removes the daily decision of whether to practice.</p>

  <h2 id="past">Gratitude in the past tense</h2>
  <p>Writing gratitude for something that has not arrived yet feels strange at first. That is the point. It moves you from hoping to deciding. You stop asking "will it happen?" and start acting like someone it already happened to.</p>
  <p>The second half of the practice is evidence. Keep a page open next to each agreement. When anything related shows up, even something small, write what arrived and the date. Over weeks, you build a record you can actually read back. Doubt argues with feelings. It has a harder time arguing with dates.</p>
  <div class="callout"><p>This is the exact structure of <a href="/agreement-journal/">The Agreement Journal</a>: agreement on the left page, evidence on the right, for 42 evenings.</p></div>

  <h2 id="hard">Gratitude on hard days</h2>
  <p>On a hard day, a list of three can feel dishonest. Do not force it. Write one true line instead. "I am grateful I got through this afternoon." "I am grateful someone answered when I called." Gratitude does not deny the hard thing. It refuses to let the hard thing be the only thing you see.</p>
  <p>If even one line is too much, write what you would want to be grateful for a week from now, in the past tense. Then rest. The practice is still alive.</p>

  <h2 id="week">The weekly reset</h2>
  <p>Once a week, read back the last seven days. Circle what repeated. Note what arrived. Cross out any agreement that no longer feels like yours and write a clearer one. The weekly reset keeps the practice honest and stops it from becoming wallpaper.</p>

  <h2 id="mistakes">Five common mistakes</h2>
  <ul>
   <li><b>Being vague.</b> "Health, family, home" every day trains the hand, not the eye. Get specific.</li>
   <li><b>Waiting to feel grateful first.</b> Write first. The feeling often follows the writing, not the other way around.</li>
   <li><b>Making it long.</b> A 30-minute practice survives one good week. A 5-minute one survives a hard month.</li>
   <li><b>Skipping the action.</b> Gratitude and agreement without one step today slowly turns into wishing.</li>
   <li><b>Never reading it back.</b> The record is the reward. Read it on Sundays.</li>
  </ul>

  <h2 id="tools">Tools that make it easier</h2>
  <p>Any notebook works. Structure makes it easier to keep going, because the hardest part of a blank page is deciding what to write. The Gratitude Attitude collection was built around exactly this method:</p>
  <ul>
   <li><a href="/gratitude-attitude-book/">Gratitude Attitude</a>, the book: the ideas and the story behind the practice.</li>
   <li><a href="/gratitude-workbook/">The Gratitude Attitude Workbook</a>: guided exercises and daily frameworks, in eleven hardcover covers.</li>
   <li><a href="/agreement-journal/">The Agreement Journal</a>: a 42-evening cycle of past-tense gratitude and dated evidence.</li>
  </ul>

  <h2 id="faq">Questions</h2>
  {faq_html(PRACTICE_FAQ)}
  <div class="callout" style="margin-top:50px"><p><em class="gold">"{QUOTE}"</em></p></div>
 </div>
</article>'''
    art = {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc,
           "author": PERSON, "publisher": ORG, "datePublished": TODAY, "dateModified": TODAY,
           "image": SITE + "/img/time-to-bloom-800.jpg", "mainEntityOfPage": SITE + p, "inLanguage": "en"}
    howto = {"@context": "https://schema.org", "@type": "HowTo", "name": "5-minute daily gratitude practice", "totalTime": "PT5M",
             "step": [{"@type": "HowToStep", "name": n, "text": t} for n, t in [
                 ("Settle", "Sit somewhere quiet, put the phone face down and take three slow breaths."),
                 ("Notice", "Write three specific things from the last day that you are thankful for."),
                 ("Agree", "Write one thing you want in the past tense, with thanks, and sign it."),
                 ("Act", "Write the one action you will take today toward it.")]]}
    page(p, title, desc, body, [art, howto, crumbs_ld([("Home", "/"), ("Gratitude Practice", p)]), faq_ld(PRACTICE_FAQ)],
         og_img="/img/time-to-bloom-800.jpg", priority="0.9", og_type="article")

def build_gifts():
    p = "/gratitude-gifts/"
    desc = "Meaningful gratitude gifts: hardcover gratitude workbooks in 11 covers matched to personality, plus a 42-day gratitude journal. Find the right one."
    picks = [("For the dreamer", "cosmic-roses"), ("For the founder", "thrive"), ("For a new beginning", "time-to-bloom"),
             ("For a new parent", "childhood"), ("For the minimalist", "optimistic"), ("For the classicist", "your-grass-is-green")]
    by = {c["slug"]: c for c in COVERS}
    cards = "".join(f'<article class="card reveal"><a href="/gratitude-workbook/{s}/">{pic(s, by[s]["name"] + " gratitude workbook gift", cls="cover")}</a><div class="tag">{t}</div><h3>{by[s]["name"]}</h3><p>{E(by[s]["line"])}</p><div class="btn-row">{buy(by[s]["asin"], "Amazon", item=by[s]["name"] + " gift")}<a class="btn btn-ghost on-light" href="/gratitude-workbook/{s}/">Details</a></div></article>' for t, s in picks)
    body = f'''
<section class="product" style="padding-bottom:20px">
 <div class="wrap center">
  {crumbs_html([("Home", "/"), ("Gratitude Gifts", p)])}
  <p class="eyebrow">Gift guide</p>
  <h1>A gift that says <em class="gold">I see you.</em></h1>
  <p class="lead narrow">Flowers fade. A hardcover gratitude workbook sits on a desk for months and gets opened every day. Choose their vibe, and the gift becomes personal before they open it.</p>
 </div>
</section>
<section style="padding-top:30px">
 <div class="wrap center">
  <div class="trio">{cards}</div>
  <p style="margin-top:50px"><a class="btn btn-gold" href="/gratitude-workbook/">See all 11 vibes {ARROW}</a></p>
 </div>
</section>
<section class="dark stars">
 <div class="wrap split">
  <div class="center">{pic("journal", "The Agreement Journal gift", sizes="300px")}</div>
  <div>
   <p class="eyebrow">For the one who already practices</p>
   <h2>The Agreement Journal</h2>
   <p class="lead">A 42-evening hardcover for someone who journals, sets intentions, and wants proof. Undated, so they can start the night they unwrap it.</p>
   <div class="btn-row">{buy(JOURNAL["asin"], item="Agreement Journal gift")}<a class="btn btn-ghost" href="/agreement-journal/">Details</a></div>
  </div>
 </div>
</section>
<section>
 <div class="narrow">
  <h2>How to send it as a gift</h2>
  <ol style="font-size:20px"><li>Open the edition on Amazon.</li><li>At checkout, enter the recipient's address.</li><li>Add a gift message. Amazon prints it on the packing slip.</li></ol>
  <div class="callout"><p>Gift message idea: <em class="gold">"{QUOTE}"</em></p></div>
 </div>
</section>'''
    page(p, "Gratitude Gifts: Hardcover Workbooks & Journal | Gratitude Attitude", desc, body,
         [crumbs_ld([("Home", "/"), ("Gratitude Gifts", p)])], og_img="/img/cosmic-roses-800.jpg", priority="0.8")

def build_misc():
    nf = f'''<section class="dark stars center" style="min-height:80svh;display:flex;align-items:center"><div class="narrow">
<p class="eyebrow">Page not found</p><h1>This page has <em class="gold">moved on.</em></h1>
<p class="lead">The store has a new home. Everything you are looking for is one click away.</p>
<div class="btn-row"><a class="btn btn-gold" href="/">Home {ARROW}</a><a class="btn btn-ghost" href="/gratitude-workbook/">All workbook covers</a></div></div></section>'''
    page("/404/", "Page not found | Gratitude Attitude", "This page has moved.", nf)
    PAGES.pop()
    os.replace(OUT + "/404/index.html", OUT + "/404.html"); os.rmdir(OUT + "/404")
    s = open(OUT + "/404.html").read().replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
    open(OUT + "/404.html", "w").write(s)
    urls = "".join(f"<url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>" for u, pr in PAGES)
    open(OUT + "/sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    open(OUT + "/robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    open(OUT + "/site.webmanifest", "w").write(json.dumps({"name": BRAND, "short_name": BRAND, "start_url": "/", "display": "browser",
        "background_color": "#0e2a20", "theme_color": "#0e2a20", "icons": [{"src": "/img/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}))
    # Netlify: caching, security headers, and 301s from the old Shopify URLs so existing links keep their value
    open(OUT + "/netlify.toml", "w").write('''[build]
  publish = "."

[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
    X-Frame-Options = "SAMEORIGIN"

[[headers]]
  for = "/img/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=604800"
''')
    old = ["/products/*  /gratitude-workbook/  301", "/collections/*  /gratitude-workbook/  301", "/collections  /gratitude-workbook/  301",
           "/pages/about*  /about/  301", "/pages/*  /  301", "/blogs/*  /gratitude-practice/  301", "/cart  /gratitude-workbook/  301",
           "/search  /gratitude-workbook/  301", "/index.html  /  301", "http://backtosource.vip/*  https://backtosource.vip/:splat  301!",
           "https://www.backtosource.vip/*  https://backtosource.vip/:splat  301!"]
    open(OUT + "/_redirects", "w").write("\n".join(old) + "\n")

if __name__ == "__main__":
    build_home(); build_book(); build_workbook_hub()
    for i, c in enumerate(COVERS): build_cover(c, i)
    build_journal(); build_practice(); build_gifts(); build_about(); build_misc()
    print(len(PAGES), "pages")
