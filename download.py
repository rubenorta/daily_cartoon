#!/usr/bin/python
# -*- coding: utf-8 -*-
import feedparser, requests, re, time, pytz
from datetime import datetime, timedelta
from dateutil import parser
from bs4 import BeautifulSoup

import logging

logging.basicConfig(filename='download.log',level=logging.INFO)
import cartoon

my_cartoons = []
my_links = []

logging.info('======= Starting sesion....')

#
# Download from eldiario.es
#

feed = feedparser.parse('http://www.eldiario.es/rss/section/20038/')
c = feed.entries[0]
published_at = parser.parse(c.published)
logging.info(published_at.strftime('%m/%d/%Y') + " " + c.title + " " + c.links[1].href + " " + c.links[0].href + " http://www.eldiario.es Bernardo Vergara ")

if (published_at.date() == datetime.today().date()):
    bergara = cartoon.Cartoon(c.title, c.links[1].href, c.links[0].href, 'http://www.eldiario.es', 'Bernardo Vergara', published_at)
    my_cartoons.append(bergara)
    logging.info('ADDED ' + c.title)

feed = feedparser.parse('http://www.eldiario.es/rss/section/20039/')
c = feed.entries[0]
published_at = parser.parse(c.published)
logging.info(published_at.strftime('%m/%d/%Y') + " " + c.title + " " + c.links[1].href + " " + c.links[0].href + " http://www.eldiario.es Bernardo Vergara ")

if (published_at.date() == datetime.today().date()):
    manel = cartoon.Cartoon(c.title, c.links[1].href, c.links[0].href, 'http://www.eldiario.es','Manel Fontedevila', published_at)
    my_cartoons.append(manel)
    logging.info('ADDED ' + c.title)
#
# Download from ctxt.es 
#

r = requests.get('http://ctxt.es/es/?tpl=22&tpid=299')
page_text = r.text.encode('utf-8')
soup = BeautifulSoup(page_text,'html.parser')
results = soup.findAll("a", {"title" : re.compile('Leer el.*')})

for link in results:
    my_links.append(link.get('href'))

my_links = list(set(my_links))

for link in my_links:
    r = requests.get(link)
    #r = requests.get('http://ctxt.es/es/20161005/Multimedia/8851/JR-Mora-prensa.htm')
    page_text = r.text.encode('utf-8')
    soup = BeautifulSoup(page_text,'html.parser')
    titles = soup.find_all('h1')
    regex = ur'^(El|La) (.*) de hoy: (.*) \((.*)\)$'
    result = re.match(regex, titles[-1].getText())

    published_at = pytz.timezone('Europe/Madrid').localize(datetime.strptime(result.group(4), '%d/%m/%Y'))
    logging.info(published_at.strftime('%m/%d/%Y') + " " + result.group(3) + " " + c.links[1].href + " " + link + " http://www.eldiario.es " + result.group(2))

    if (published_at.date() == datetime.today().date()):
    	ctxt = cartoon.Cartoon(result.group(3), c.links[1].href, link, 'http://ctxt.es',result.group(2), published_at)
    	my_cartoons.append(ctxt)
        logging.info('ADDED ' + result.group(3))

print 'Cartoons downloaded {0}'.format(len(my_cartoons)) 

#
# Download from republica.com
#

r = requests.get('http://www.republica.com/vinetas/')
page_text = r.text.encode('utf-8')
soup = BeautifulSoup(page_text,'html.parser')
results = soup.findAll("a", {"title" : re.compile('La vi.eta: .*')})

title = results[0].get('title')
regex = ur'La vi.eta: (.*)'
result = re.search(regex, title)
title = result.group(1)
url = results[0].get('href')
regex = ur'url\((.*)\)'
result = re.search(regex, str(results[0]))
image = result.group(1)
regex = ur'(\d\d\d\d/\d\d/\d\d)/'
result = re.search(regex, url)
published_at = pytz.timezone('Europe/Madrid').localize(datetime.strptime(result.group(1), '%Y/%m/%d'))
publisher = 'http://www.republica.com/vinetas'
author = 'Ferran Martín'

logging.info(published_at.strftime('%m/%d/%Y') + " " + title.encode('utf-8') + " " + image + " " + url.encode('utf-8') + "  " + publisher + " " + author)

if (published_at.date() == datetime.today().date()):
    republica = cartoon.Cartoon(title, image, url, 'http://www.republica.com/vinetas','Ferran Martín', published_at)
    my_cartoons.append(republica)
    logging.info('ADDED ' + title)
