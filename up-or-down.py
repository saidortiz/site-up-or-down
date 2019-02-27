from urllib2 import Request, urlopen, HTTPError, URLError, os

from colorama import init

from termcolor import cprint, colored
from pyfiglet import figlet_format
cprint(figlet_format('url check!', font='small'),
       'red', 'on_white', attrs=['bold'])

user_input = raw_input("Inserta ruta de tu archivo txt: ")


if os.path.exists(user_input):
    f = open(user_input,'r+')

    list_of_lists = []

    with open(user_input) as f:
        for line in f:
            if line.strip():
                list_of_lists = line           
                user_agent = 'Mozilla/20.0.1 (compatible; MSIE 5.5; Windows NT)'
                headers = { 'User-Agent':user_agent }

                req = Request('http://' + list_of_lists, headers = headers)            
                try:                
                        page_open = urlopen(req, timeout = 1)
                        text = '\x1b[6;30;42m' + '\tsite found' + '\x1b[0m'
                        print "\a"
                        errorcode = page_open.getcode()
                        print colored (" {0:10} {1:10} {2:20}".format( line, text, errorcode  ),"white")
                        print "\a"
                        #create a txt with up sites
                        if os.path.exists("up.txt"):
                            with open('up.txt', 'a') as the_file:

                                the_file.write( list_of_lists)

                        else:
                            with open('up', 'a') as the_file:
                                the_file.write( list_of_lists)

                except HTTPError, e:
                        print colored ("{0:0} {1:10}".format(e.code, line)) + '\x1b[31m' + '\tnot found!' + '\x1b[31m'
                        #create a txt with down sites
                        if os.path.exists("down.txt"):
                            with open('down.txt', 'a') as the_file:
                                the_file.write( list_of_lists)

                        else:
                            with open('down', 'a') as the_file:
                                the_file.write( list_of_lists)

else:
    print('no encontro tu archivo en '+str(user_input))



