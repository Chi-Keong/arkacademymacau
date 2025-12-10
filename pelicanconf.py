AUTHOR = 'Chi'
SITENAME = 'Ark Academy Macau'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Australia/NSW'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# Social widget
# SOCIAL = (
#     ("You can add links in your config file", "#"),
#     ("Another social link", "#"),
# )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

#Meun Setting
RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = [
    ('Home',  '/'),
    ('About',  '/pages/about.html'),
    ('Classes',  '/pages/classes.html'),
    # ('Blog', '/archives.html'),
    ('Contact', '/pages/contact.html'),
]

# Theme
THEME = 'themes/new-bootstrap2/new-bootstrap2'

SITENAME = 'Ark Academy Macau'
SITESUBTITLE = 'Small-group statistics learning in Macau'
SITEURL = 'https://arkacademymacau.com'

# Optional social / meta
AUTHOR = 'Your Name'
TIMEZONE = 'Asia/Macau'
DEFAULT_LANG = 'en'

# If you don’t want “category” in URLs later:
# ARTICLE_URL = 'blog/{slug}/'
# ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'
