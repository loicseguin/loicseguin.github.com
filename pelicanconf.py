#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u"Loïc Séguin-C."
SITENAME = u"Loïc Séguin-C."
SITEURL = ''

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = u'fr'
LOCALE = 'fr_CA.utf-8'
DATE_FORMATS = {u'fr': u'%d %B %Y'}

DEFAULT_CATEGORY = 'blogue'

OUTPUT_PATH = "."

# Use nice URLs
ARTICLE_URL = '{category}/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
THEME = "cadabra"
FOOTER_QUOTE = "Klaatu verata nicto"
MD_EXTENSIONS = ['fenced_code', 'codehilite', 'toc', 'tables', 'footnotes']

# Social widget
SOCIAL = (
          ('email', 'mailto:loic@loicseguin.com'),
          ('twitter', 'http://twitter.com/lseguinc'),
          ('github', 'http://github.com/loicseguin'),
          #('bitbucket', 'http://bitbucket.org/loicseguin'),
          ('linkedin','http://ca.linkedin.com/pub/loïc-séguin-charbonneau/42/a92/397/'),
          ('flickr', 'http://www.flickr.com/photos/loicseguin')
         )

DEFAULT_PAGINATION = 8
GOOGLE_ANALYTICS = 'UA-41506771-1'

