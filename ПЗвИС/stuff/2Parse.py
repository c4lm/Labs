#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re 
import codecs 
import glob 
import os
#import multiprocessing

import urllib.request as ur
from bs4 import BeautifulSoup

if __name__ == '__main__':

	filename="/home/styd/Desktop/ISA correct logs/hh.ru.txt"	
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
	url = "https://spb.hh.ru/"

	req = ur.Request(url, headers = headers)

	html = ur.urlopen(req).read()
	soup = BeautifulSoup(html, "lxml")

	# kill all script and style elements
	for script in soup(["script", "style"]):
	    script.extract()    # rip it out

	text = soup.get_text()
	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = '\n'.join(chunk for chunk in chunks if chunk)
	print(url+'\n')
	#print(text)
	lst=text.split('\n')
	print(lst)
	print()
	lst=[re.sub("[\—\:\;\,\.\-\=\?\!\(\)\[\]\d+\/]",'',words).lower() for words in lst]
	for words in lst:
		if re.match(u"[\u0400-\u0500]+",words):
			print(words)

	with codecs.open(filename, "w",encoding = 'utf-8', errors = 'ignore') as f:
		for words in lst:
			words_t=words.split(' ')
			for x in words_t:
				if x=="" or x=="\n":
					continue
				else:
					f.write(x+'\n')



