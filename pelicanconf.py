#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Loïc Séguin-C."
SITENAME = u"Loïc Séguin-C."
SITEURL = 'http://loicseguin.github.com'
FEED_DOMAIN = SITEURL

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = 'fr'
DEFAULT_CATEGORY = 'blogue'

DATE_FORMATS = {'fr': '%d %B %Y'}
OUTPUT_PATH = "."
PATH = "content/"

DISPLAY_CATEGORIES_ON_MENU = True
DIRECT_TEMPLATES = ('index', 'archives')
AUTHOR_SAVE_AS = False
TAG_SAVE_AS = False
#MENUITEMS = [("Blogue", SITEURL)]
THEME = "klaatu"

# global metadata to all the contents
DEFAULT_METADATA = (('summary', ''),)
#PLUGINS = ['pelican.plugins.github_activity',]
#GITHUB_URL = "http://github.com/loicseguin/"
#GITHUB_ACTIVITY_FEED = 'https://github.com/loicseguin.atom'

# Blogroll
#LINKS =  (
    #('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
    #('Python.org', 'http://python.org'),
    #('Jinja2', 'http://jinja.pocoo.org')
         #)

# Social widget
SOCIAL = (
          ('twitter', 'http://twitter.com/lseguinc'),
          ('github', 'http://github.com/loicseguin')
         )

DEFAULT_PAGINATION = 12

