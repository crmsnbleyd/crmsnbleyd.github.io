AUTHOR = 'Arnav Andrew Jose'
SITENAME = 'Language Modelling Course'
SITEURL = ''

PATH = 'electra'
OUTPUT_PATH = 'electra/'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

THEME = "electra-theme/Flex"
THEME_COLOR = "dark" #or "light"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ( ('Introduction', '/electra/category/introduction.html'),
          ('Terminology', '/electra/category/terminology.html'),
          ('Neural Networks', '/electra/category/neural_networks.html'),
          ('Models', '/electra/category/models.html'),
          ('Huggingface', 'https://huggingface.co'),
          ('Pytorch Documentation', 'https://pytorch.org/docs/stable/index.html'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/crmsnbleyd'),
          ('Linkedin', 'https://www.linkedin.com/in/arnav-andrew-jose'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ARTICLE_ORDER_BY = 'date'
