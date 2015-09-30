#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mlle Carnot'
SITENAME = u'Mlle Carnot'
SITEURL = 'http://localhost:8000'
TWITTER_USERNAME = 'mllecarnot'

PATH = 'content'
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('À l\'attaque du découd-vite' , 'http://decoudvite.com'),
         ('The Wearability Project', 'http://pachi-pachi.fr/'),
         ('L\'oiseau botté','http://www.oiseaubotte.com/'),
         ('E-penser','https://www.youtube.com/user/epenser1'),)

MENUITEMS = (
         ('la couture', '/couture'),
         ('la thermo' , '/thermo'),
)

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math']

# Social widget
SOCIAL = ()

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_PAGINATION = 3
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
CATEGORYS_URL = 'categories/'
CATEGORYS_SAVE_AS = 'categories/index.html'

THEME = 'theme/mllecarnot'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

