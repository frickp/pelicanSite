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
    ('Blog','http://frickp.github.io'),  
    ('Greenleaf lab','http://greenleaf.stanford.edu'),
    ('Insight Data Science','http://insightdatascience.com'),
    ('Quaranta lab', 'http://ccsb.vanderbilt.edu/qlab/frontpage'),
    ('Vanderbilt quantitative bioscience','https://medschool.vanderbilt.edu/cpb/')
    )

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/peterlfrick/'),
        ('GitHub','https://github.com/frickp'), 
	 )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#MARKUP = ('md', 'ipynb','html','rmd')
MARKUP = ('md','html')

PLUGIN_PATHS = ['addIns/plugins/','addIns/plugins/pelican-plugins/']
PLUGINS = ['ipynb','sitemap','liquid_tags','liquid_tags.notebook','tag_cloud']
#PLUGINS = ['sitemap','liquid_tags']
REVERSE_CATEGORY_ORDER = True
STATIC_PATHS = ['images']
THEME ='addIns/themes/Flex'
#THEME = 'addIns/themes/pelican-bootstrap3/'
ABOUT_ME = 'Thanks for visiting! I am a quantitative scientist, trained in both physics and systems biology. I am passionate about interrogating data intelligently to understand complex systems. This blog is for exploring stats, machine learning, and data science.'
#AVATAR = 'https://raw.githubusercontent.com/frickp/pelicanSite/master/images/headShot.jpg'
AVATAR = 'https://raw.githubusercontent.com/frickp/insight/master/FrickHeadshot.jpg'
DISPLAY_TAGS_ON_SIDEBAR = True
#HIDE_SIDEBAR = True
SITELOGO = 'https://raw.githubusercontent.com/frickp/insight/master/FrickHeadshot.jpg'
#PYGMENTS_STYLE=['friendly']
#NOTEBOOK_DIR = 'notebooks'
#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')
#IPYNB_USE_META_SUMMARY = ['False']
TAG_CLOUD_MAX_ITEMS=5
IGNORE_FILES = ['*ipynb_checkpoints']
#ARTICLE_PATHS = [
#	'151015_pca_5yo*',
#	'151017_miningDataScience*',
#	'151019_scrapeDataSciencePt2*',
#	'151204_SF_scrapeSalary*',
#	'151209_MyFirst_MySQL*'
#]
