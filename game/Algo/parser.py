#!/usr/bin/env python
# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser
import urllib2

import sys
#print sys.getdefaultencoding()

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.utile=[]
        self.check=False
        self.n=0
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag=='ol' and self.n==0:
            self.check=True
            self.n=1
            #print 'OL******'
        if tag=='ul':
            self.check=False

    #def handle_endtag(self, tag):
        #print "Encountered an end tag :", tag
        
    def handle_data(self, data):
        if self.check:
            self.utile.append(data)
            #print "Encountered some data  :", data

def aligne(liste):
    p=''
    b=0
    par=0
    for mot in liste:
        for i in mot:
            if i==' ' and b==0:
                p=p+i
                b=1
            elif not i==' ' and not i=='.':
                if i=='(':
                    par=1
                elif i==')':
                    par=0
                p=p+i
                b=0
            elif i=='.' and par==0:
                p=p+i
                return p[1:len(p)]
            elif i=='.' and par==1:
                p=p+i
            elif i=='\n':
                return p[1:len(p)]
    return p[1:len(p)]
    
def requete_mot(mot):
    url='http://fr.wiktionary.org/wiki/'+mot
    mystring = urllib2.urlopen(url).read()
    utf8_str = mystring.decode('utf-8')
    parser = MyHTMLParser()
    parser.feed(utf8_str)
    return aligne(parser.utile)
    

        