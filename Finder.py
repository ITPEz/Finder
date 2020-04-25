import requests, os
import time
os.system('clear')
os.system('cls')	
banner = '''
  __ _           _ _       
 / _(_)_ __   __| (_)_ __  
| |_| | '_ \ / _` | | '_ \ 
|  _| | | | | (_| | | | | |
|_| |_|_| |_|\__,_|_|_| |_|
'''

print(banner)

exist = []
def get(url):
	request = requests.get(url)
	if request.status_code < 404:
		print ('Success : '+url)
		exist.append(url)
	else:
		print ('Error : '+url)
default = ['admin', 'admin.php', 'administrator', 'login', 'wp-admin', 'wp-login.php', 'user', 'login.html', 'admin/login0','admin/login.php','admin/login']

site = input('Website Scan : ')
wdl = input('Page Scan : ')

if site.startswith('http') == False:
	site = 'http://'+site
if wdl == '':
	wdl = default
else:
	wdl = open(wdl)
	wdl = wdl.readlines()


for word in wdl:
	page = site+'/'+word
	get(page)

print ('Success ALL')
print (', '.join(exist))
time.sleep(60)
