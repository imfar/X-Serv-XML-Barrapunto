#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Simple XML parser for the RSS channel from BarraPunto
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# September 2009
#
# Just prints the news (and urls) in BarraPunto.com,
#  after reading the corresponding RSS channel.

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys

def normalize_whitespace(text):
    "Remove redundant whitespace from a string"
    return ' '.join(text.split())


class myContentHandler(ContentHandler):

	def __init__ (self):
		self.inItem = False
		self.inContent = False
		self.theContent = ""

	def startElement (self, name, attrs):
		if name == 'item':
			self.inItem = True
		elif self.inItem:
			if name == 'title':
				self.inContent = True
			elif name == 'link':
				self.inContent = True
            
	def endElement (self, name):
		global title
		if name == 'item':
			self.inItem = False
		elif self.inItem:
			if name == 'title':
				title = self.theContent
				self.inContent = False
				self.theContent = ""
			elif name == 'link':
				link = "<a href='" + self.theContent + "'>" + title + "</a><br>"
				fd.write(link)
				self.inContent = False
				self.theContent = ""
	def characters (self, chars):
		if self.inContent:
			self.theContent = self.theContent + chars
    

# Abrir archivo html y escribir en el codigo html
fd = open('index.html', 'w')
html_code = "<html><body><h1>PRACTICA SARO - 10.3. Titulares de BarraPunto</h1><p>"
fd.write(html_code)

title = ""

# Load parser and driver
theParser = make_parser()
theHandler = myContentHandler()
theParser.setContentHandler(theHandler)

# Ready, set, go!
theParser.parse("http://barrapunto.com/index.rss")
fd.write("</p></body></html>")
print("Parse complete")
fd.close()
