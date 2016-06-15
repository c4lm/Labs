import re 
import codecs 
import glob 
import os
#multiprocessing files, sequentially processing lines

def create_succesful_attempts_log(file_list):
	pattern=".*htt.{1,2}[:][/][/][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}.*"
	regex=re.compile(pattern,re.IGNORECASE)
	count_resolved=0
	count_unresolved=0	
	for filename in file_list:
		with codecs.open(filename, "r",encoding = 'utf-8', errors = 'ignore') as f:
			content=f.readlines()
			for line in content:
				if(regex.match(line)):
					count_unresolved+=1
				else:
					count_resolved+=1

		print("Done with ",filename, str(count_resolved), str(count_unresolved))
	print("Resolved urls,  Unresolved urls,  Resolved percentage", str(count_resolved), str(count_unresolved), count_unresolved/float(count_resolved+count_unresolved)*100)


if __name__ == '__main__':
	file_list = glob.glob("/home/styd/Desktop/ISA correct logs/*.w3c")
	file_list.sort()
	create_succesful_attempts_log(file_list)
	print("Done.")
	

