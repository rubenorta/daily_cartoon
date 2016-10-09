#!/usr/bin/python
# -*- coding: utf-8 -*-
import feedparser, requests, re, time
from datetime import datetime
from bs4 import BeautifulSoup

import cartoon

my_cartoons = []

# Download from eldiario.es
feed = feedparser.parse('http://www.eldiario.es/rss/section/20038/')
c = feed.entries[0]
bergara = cartoon.Cartoon(c.title, c.links[1].href, c.links[0].href, 'http://www.eldiario.es', 'Bernardo Vergara', c.published)
my_cartoons.append(bergara)

feed = feedparser.parse('http://www.eldiario.es/rss/section/20039/')
c = feed.entries[0]
manel = cartoon.Cartoon(c.title, c.links[1].href, c.links[0].href, 'http://www.eldiario.es','Manel Fontedevila', c.published)
my_cartoons.append(manel)

# Download from ctxt.es 
r = requests.get('http://ctxt.es/es/?tpl=22&tpid=299')
page_text = r.text.encode('utf-8')
soup = BeautifulSoup(page_text,'html.parser')

results = soup.findAll("a", {"title" : re.compile('Leer el.*')})
results = list(set(results))

for link in results:
    r = requests.get(link.get('href'))
    print link.get('href')
    #r = requests.get('http://ctxt.es/es/20160928/Multimedia/8741/')
    page_text = r.text.encode('utf-8')
    soup = BeautifulSoup(page_text,'html.parser')
    titles = soup.find_all('h1')
    regex = ur'^El (.*) de hoy: (.*) \((.*)\)$'
    result = re.match(regex, titles[-1].getText())

    published_at = datetime.strptime(result.group(3), '%d/%m/%Y')
    today = time.strftime('%d/%m/%Y')
    print published_at
    print today

    if (today == published_at):
    	ctxt = cartoon.Cartoon(result.group(2), c.links[1].href, link.get('href'), 'http://ctxt.es',result.group(1), result.group(3))
    	print ctxt
    	my_cartoons.append(ctxt)

    print "\n----------------------"

n_cartoons = len(my_cartoons)
print 'Cartoons downloaded {0}'.format(n_cartoons) 

# Links
#http://www.republica.com/vinetas/