#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jindřich Smitka'
SITENAME = u'Jindřich Smitka'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ('Daniel Bultas', 'http://bultas.info/'),
    # ('', ''),
)

# Social widget
SOCIAL = (
    ('Twitter', 'http://twitter.com/jindrichsmitka'),
    ('Google+', 'https://plus.google.com/105092425314734561226'),
    ('Github', 'https://github.com/s-m-i-t-a'),
    ('Bitbucket', 'https://bitbucket.org/jsmitka'),
)

DEFAULT_PAGINATION = 10

DATE_FORMATS = {
    "en": "%Y-%m-%d",
    "cs": "%d.%B %Y",
}

# GITHUB_URL = 'https://github.com/s-m-i-t-a'

GOOGLE_ANALYTICS = 'UA-22752857-1'

TWITTER_USERNAME = 'jindrichsmitka'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
