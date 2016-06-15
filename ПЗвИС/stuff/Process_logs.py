from multiprocessing import Pool  
import re 
import codecs 
import glob 
import itertools
import os
#multiprocessing files, sequentially processing lines
'''
def grouper(n, iterable, fillvalue=None):
	"grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
	args = [iter(iterable)] * n
	return itertools.zip_longest(fillvalue=fillvalue, *args)
'''
def create_succesful_attempts_log(filename):
	pattern=".*\tvideo.*\t.*\t.*\t.*\t.*\t.*\tinternal\texternal.*allowed.*|.*\taudio.*\t.*\t.*\t.*\t.*\t.*\tinternal\texternal.*allowed.*|.*[.]vk[.]me.*internal\texternal.*allowed.*|.*[/]+vk[.]com.*internal\texternal.*allowed.*|.*[=]vk[.]com.*internal\texternal.*allowed.*|.*torrent.*internal\texternal.*allowed.*|.*[/]dk[?]cmd[=].*internal\texternal.*allowed.*|.*[/]dk[?]st[.]cmd[=].*internal\texternal.*allowed.*|.*[/]+ok[.]ru.*internal\texternal.*allowed.*|.*[=]ok[.]ru.*internal\texternal.*allowed.*|.*vkontakte[.]ru.*internal\texternal.*allowed.*|.*odnoklassniki[.]ru.*internal\texternal.*allowed.*|.*fullstuff.*internal\texternal.*allowed.*|.*radio.*internal\texternal.*allowed.*|.*android.*internal\texternal.*allowed.*|.*mobile.*internal\texternal.*allowed.*|.*ntv.*internal\texternal.*allowed.*|.*skype.*internal\texternal.*allowed.*|.*player.*internal\texternal.*allowed.*|.*vkapp.*internal\texternal.*allowed.*|.*instagram.*internal\texternal.*allowed.*|.*phone.*internal\texternal.*allowed.*|.*nokia.*internal\texternal.*allowed.*|.*thl.*internal\texternal.*allowed.*|.*game.*internal\texternal.*allowed.*|.*vungle.*internal\texternal.*allowed.*|.*appstore.*internal\texternal.*allowed.*|.*google-play.*internal\texternal.*allowed.*|.*itunes.*internal\texternal.*allowed.*|.*viber.*internal\texternal.*allowed.*|.*kot49h.*internal\texternal.*allowed.*|.*btwebclient.*internal\texternal.*allowed.*|.*mediaget.*internal\texternal.*allowed.*|.*game.*internal\texternal.*allowed.*|.*darwin.*internal\texternal.*allowed.*|.*ut_core.*internal\texternal.*allowed.*|.*speedcam.*internal\texternal.*allowed.*|.*eminem50cent[.]ru.*internal\texternal.*allowed.*|.*yaplakal[.]com.*internal\texternal.*allowed.*"
	regex=re.compile(pattern,re.IGNORECASE)
	with codecs.open(filename, "r",encoding = 'utf-8', errors = 'ignore') as f:
		content=f.readlines()
		content=[line for line in content if regex.match(line)]
	with codecs.open("/home/styd/Desktop/ISA processed logs/"+"n"+os.path.basename(filename), "w",encoding = 'utf-8', errors = 'ignore') as f:
		f.writelines(content)
	print("Done with "+filename)


if __name__ == '__main__':
	file_list = glob.glob("/home/styd/Desktop/ISA new logs/*.w3c")
	file_list.sort()
	pool = Pool()
	pool.map_async(create_succesful_attempts_log, file_list)
	pool.close()
	pool.join()
	'''
	file_list_groups = list(grouper(4,file_list,None))

	test=[]
	for x in range(0, len(file_list_groups[0]) ):
		if(file_list_groups[0][x] is not None):
			with codecs.open(file_list_groups[0][x], "r",encoding = 'utf-8', errors = 'ignore') as f:
				tmplist=f.readlines()
				test.extend(tmplist)
				print("done with {0}", file_list_groups[0][x])
	test=[line for line in test if 'Debian' in line]
	with codecs.open("/home/styd/Desktop/Kek.w3c", "w",encoding = 'utf-8', errors = 'ignore') as f:
		f.writelines(test)
	print("done")
	'''


