#!/usr/bin/env python
import sys, os, time, httplib, socket
from colorama import init

from termcolor import cprint, colored
from pyfiglet import figlet_format



cprint(figlet_format('UP OR DOWN!', font='small'),
       'red', 'on_white', attrs=['bold'])


#urls
SITES = [

	"www.redteamsec.com",
	"www.security.divdesign.com",
	"www.aguirremasaguirre.com",
	"www.i3sec.com.mx",
	"www.google.com.mx",
    "www.pietschsoft.com",
    "www.Extratorrent.cc",
    "www.Vube.com",
    "www.Sukebei.nyaa.se",

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
