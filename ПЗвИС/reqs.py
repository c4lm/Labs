#!/usr/bin/python3
import re 
import codecs 
import glob 
import os
import multiprocessing

import urllib.request as ur
from bs4 import BeautifulSoup

"""
def create_succesful_attempts_log(filename):
	pattern=".*[\t]htt.{1,2}[:][/][/].*[\t].*html.*200.*Allowed.*"
	url_pattern="[\t]htt.{1,2}[:][/][/].*?[\t]"
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
	regex=re.compile(pattern,re.IGNORECASE)
	with codecs.open("/home/styd/Desktop/ISA correct logs/words"+filename[-20:]+".txt", "w",encoding = 'utf-8', errors = 'ignore') as saved:
		with codecs.open(filename, "r",encoding = 'utf-8', errors = 'ignore') as f:
			content=f.readlines()
			for line in content:
				try:
					if(regex.match(line)):
						url = re.search(url_pattern, line).group(0)[1:-1]
				
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
						saved.write(url+'\n')
						saved.write(text+'\n')

				except:
					print()
					continue


		print("Done with ",filename)


if __name__ == '__main__':
	file_list = glob.glob("/home/styd/Desktop/ISA correct logs/*.w3c")
	file_list.sort()
	pool = multiprocessing.Pool()
	pool.map_async(create_succesful_attempts_log, file_list)
	pool.close()
	pool.join()
"""
url = "http://youtube.com"
                                                
req = ur.Request(url)

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
print(url)
print(text)
