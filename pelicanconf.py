#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Peter Frick'
SITENAME = u'Peter Frick'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
        )

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/pub/peter-frick/39/455/ab7'),
        ('GitHub','https://github.com/frickp'), 
	 )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb','html','rmd')

PLUGIN_PATHS = ['addIns/plugins/','addIns/pelican-plugins/']
PLUGINS = ['ipynb','sitemap','rmd_reader']
REVERSE_CATEGORY_ORDER = True
THEME = 'addIns/themes/pelican-bootstrap3/'
