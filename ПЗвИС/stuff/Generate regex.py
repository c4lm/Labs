import codecs
with codecs.open("/home/styd/Desktop/regexes2", "r",encoding = 'utf-8', errors = 'ignore') as f:
		patterns=f.readlines()
		pattern=""
		for line in patterns:
			pattern+=line.strip()+"|"
		print(pattern)			
