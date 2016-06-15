from multiprocessing import Pool  
import re 
import codecs 
import glob 
import itertools
import os
#multiprocessing files, sequentially processing lines

def grouper(n, iterable, fillvalue=None):
	"grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
	args = [iter(iterable)] * n
	return itertools.zip_longest(fillvalue=fillvalue, *args)

def create_succesful_attempts_log(line):

	pattern=".*Internal\tExternal.*Allowed.*"
	regex=re.compile(pattern)
	if regex.match(line):
		tmp.append(line.lower())


if __name__ == '__main__':
	file_list = glob.glob("/home/styd/Desktop/ISA new logs/*.w3c")
	file_list.sort()
	file_list_groups = list(grouper(4,file_list,None))
	for i in range(0, len(file_list_groups) ):
		tmp=[]
		concat=[]
		for x in range(0, len(file_list_groups[i]) ):
			if(file_list_groups[i][x] is not None):
				with codecs.open(file_list_groups[i][x], "r",encoding = 'utf-8', errors = 'ignore') as f:
					tmplist=f.readlines()
					concat.extend(tmplist)
			print("Saved in memory "+str(i)+str(len(tmp)))
		pool = Pool()
		pool.map(create_succesful_attempts_log, concat)
		pool.close()
		pool.join()
		with codecs.open("/home/styd/Desktop/ISA processed logs/Processed_log", "a+",encoding = 'utf-8', errors = 'ignore') as f:
			f.writelines(tmp)
	print("Done with this shit")

	
