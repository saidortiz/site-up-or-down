#!/usr/bin/env python
import os, time, httplib, socket
from termcolor import colored

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#urls
SITES = [
	"www.github.com.com",
	"www.redteamsec.com",
	"www.security.divdesign.com",
	"www.aguirremasaguirre.com",
	"www.i3sec.com.mx",
	"www.google.com.mx",
]

#for search if url is up or down
for site in SITES:
			try: #intenta hacer la peticion
				conn = httplib.HTTPConnection(site, timeout=10)
				conn.request("HEAD", "/")
				response = conn.getresponse()
				if response.status == 200:
					print "\a"
					print colored ("{0:30} {1:10}".format(site, response.status),"white") + '\x1b[6;30;42m' + 'Success!' + '\x1b[0m'


               #close conection
				conn.close()
			except (httplib.HTTPException, socket.error) as ex: #envia el error

			   print colored( site) + '\x1b[6;30;43m' + 'site is down!' + '\x1b[0m'






#time.sleep(5)
#os.system("clear")
