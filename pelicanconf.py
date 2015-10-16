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
LINKS = (
	 ('Quaranta lab', 'http://ccsb.vanderbilt.edu/qlab/frontpage'),
         ('Greenleaf lab','http://greenleaf.stanford.edu'),
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
PLUGINS = ['ipynb','sitemap','liquid_tags','liquid_tags.notebook']
#PLUGINS = ['sitemap','liquid_tags']
REVERSE_CATEGORY_ORDER = True
THEME = 'addIns/themes/pelican-bootstrap3/'
STATIC_PATHS = ['images']
ABOUT_ME = 'Thanks for visiting! I am a quantitative scientist, trained in both physics and systems biology. I am passionate about interrogating data intelligently to understand complex systems. This blog is a journal about transitioning from academia to a career in data science.'
AVATAR = 'https://raw.githubusercontent.com/frickp/pelicanSite/master/images/headShot.jpg'

#PYGMENTS_STYLE=['friendly']
#NOTEBOOK_DIR = 'notebooks'
#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')
#IPYNB_USE_META_SUMMARY = ['False']
TAG_CLOUD_MAX_ITEMS=5
