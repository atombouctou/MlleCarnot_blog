#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mlle Carnot'
SITENAME = u'MlleCarnot'
SITEURL = 'http://localhost:8000'
TWITTER_USERNAME = 'mllecarnot'

PATH = 'content'
STATIC_PATH = 'images'

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

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math']
         

# Social widget
SOCIAL = ()

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = 10

THEME = 'theme/tuxlite_zf'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

