SITE = "https://backtosource.vip"
BRAND = "Gratitude Attitude"
AUTHOR = "Esther Michele Kazir"
QUOTE = "The sky has woven stars for you, all that remains is to agree."
IG = "https://www.instagram.com/gratitude.mindset.on/"
FB = "https://www.facebook.com/gratitudemindon"
APP_IOS = "https://apps.apple.com/app/id6805992249"

def amz(asin):
    return f"https://www.amazon.com/dp/{asin}"

BOOK = {
    "slug": "gratitude-attitude-book",
    "name": "Gratitude Attitude",
    "subtitle": "A Practical Guide to Consciousness Transformation",
    "img": "gratitude-attitude",
    "hardcover": "B0H1QCT253",
    "kindle": "B0GS6WBFQK",
    "pages": 78,
}

JOURNAL = {
    "slug": "agreement-journal",
    "name": "The Agreement Journal",
    "subtitle": "Signed & Arrived: 42 Evenings of Gratitude and Evidence",
    "img": "journal",
    "asin": "B0HNKLZX38",
    "isbn": "9798162441816",
    "pages": 124,
    "size": "6 x 9 in",
}

WORKBOOK_PAGES = 97

GROUPS = {
    "night": "Night Sky",
    "horizon": "Golden Horizon",
    "bloom": "In Bloom",
    "wonder": "Wonder",
    "classic": "Classic",
}

# One interior, eleven covers. Each cover gets its own page and its own words.
COVERS = [
    {"slug": "cosmic-roses", "name": "Cosmic Roses", "asin": "B0H5Q1D6T3", "group": "night",
     "line": "Crimson roses under a violet galaxy.",
     "for": "the romantic who keeps one foot on the ground and one in the stars",
     "body": "Deep red roses bloom against a field of violet nebula, framed by the gold ring and crown. It is the most dramatic cover in the collection, made for the person who wants their practice to feel like a ritual, not a chore. Leave it on the nightstand. It earns the space."},
    {"slug": "cosmic-wink", "name": "Cosmic Wink", "asin": "B0HDYKGBCJ", "group": "night",
     "line": "Sunrise breaking over the edge of the planet.",
     "for": "the one who suspects the universe is in on the joke",
     "body": "A flare of first light crosses the curve of the earth, purple sky above, gold type centered in the ring. The view from orbit is a reminder that the scale of a bad day is small. For the person who already knows that, and wants a daily place to remember it."},
    {"slug": "cheshire-cosmic", "name": "Cheshire Cosmic", "asin": "B0H5J268MT", "group": "night",
     "line": "A constellation grin across a black sky.",
     "for": "the night thinker with a mischievous streak",
     "body": "Stars connected into one wide golden smile, floating over pure black. Quiet at first glance, playful the second time you look. Made for the person who does their best thinking after dark and does not take themselves too seriously."},
    {"slug": "the-calling", "name": "The Calling", "asin": "B0H5PYXLHZ", "group": "horizon",
     "line": "A lone figure walking toward a golden horizon.",
     "for": "the one standing at the edge of a next chapter",
     "body": "A figure in white walks a lit path toward a horizon on fire with sunset. This is the cover for thresholds: a new role, a move, a decision already made in the heart and not yet on paper. The workbook gives that decision a daily structure."},
    {"slug": "thrive", "name": "Thrive", "asin": "B0H5PPBHN2", "group": "horizon",
     "line": "A silhouette above the clouds at golden hour.",
     "for": "the climber, the founder, the one mid-ascent",
     "body": "A figure stands on the summit with the sun breaking through below the cloud line. Built for people in motion who need a place to stop for five minutes, name what is already working, and choose the next step on purpose."},
    {"slug": "time-to-bloom", "name": "Time to Bloom", "asin": "B0H5HTZQT9", "group": "bloom",
     "line": "Soft wildflowers on warm cream.",
     "for": "a season of beginnings",
     "body": "Pastel cosmos, daisies and lavender drift across the left edge of a cream cover with gold lettering. Gentle without being sleepy. A natural gift for a birthday, a fresh start, a new home, or anyone you want to tell: this is your season."},
    {"slug": "tulip", "name": "Tulip", "asin": "B0H5B3Y4JM", "group": "bloom",
     "line": "Red tulips against an open blue sky.",
     "for": "the direct one who likes things bright and clear",
     "body": "Saturated red tulips rise into a clean blue sky. The boldest daylight cover in the collection. For the person who wants their practice simple, visible and impossible to ignore on the desk."},
    {"slug": "childhood", "name": "Childhood", "asin": "B0H59Y9QCZ", "group": "wonder",
     "line": "A small explorer with a telescope among floating castles.",
     "for": "the inner child, and the one raising one",
     "body": "A watercolor child looks through a telescope at castles, kites and hot-air balloons drifting overhead. It speaks to curiosity before cynicism. A thoughtful gift for a new parent, a teacher, or anyone reconnecting with the version of themselves that still wondered."},
    {"slug": "princess", "name": "Princess", "asin": "B0H4ZMRQK4", "group": "wonder",
     "line": "A blush gown before a pink castle.",
     "for": "the dreamer of any age who still believes in castles",
     "body": "A storybook figure in a pink gown faces a castle glittering in the distance, gold sparkles trailing behind. Sweet, unapologetic and unmistakable. For the person who has never stopped believing the good ending is real."},
    {"slug": "optimistic", "name": "Optimistic", "asin": "B0HG4NB4L2", "group": "wonder",
     "line": "A hand-drawn smile and a sign that says YOU CAN DO IT.",
     "for": "the minimalist with a sense of humor",
     "body": "Black line art on white: the title inside a circle that turns into a grin, and a stick figure holding a handwritten sign. The most minimal cover in the collection, and the most honest. For someone who needs encouragement without decoration."},
    {"slug": "your-grass-is-green", "name": "Your Grass Is Green", "asin": "B0H5Q1LD7L", "group": "classic",
     "line": "Forest green with gold pinstripes.",
     "for": "the classicist who wants a book that looks like it belongs in a library",
     "body": "Deep green cloth tones, vertical gold stripes and a gold ring at the center. Quiet, grounded and timeless. The name is the message: the grass you are standing on is already green. This is the cover to give when you want the gift to feel serious."},
]
