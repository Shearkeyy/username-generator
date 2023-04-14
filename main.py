import requests
import random
from concurrent.futures import ThreadPoolExecutor
import threading
from colorama import Fore, init

init()
def get_username():
    try:
     names = requests.post(
        "https://www.spinxo.com/services/NameService.asmx/GetNames",
        json={"snr":{"category":0,"UserName":"","Hobbies":"","ThingsILike":"","Numbers": "1,2,3,4,5,6.7,8,9,,,,!,$,|","WhatAreYouLike":"human,ghost,ghoul","Words":",,,,,,,,,,,,,,,,    , , , , , , , , , , , ,,  ,  , , , ,  ,  , , , , ,, ,  , ,, ,,,,    ,  , , , , ,   ,, ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,ᕦ,,😎,,ᕤ,,♫,,紫,の,,デ,ク,ス,タ,ー,<3,ツ,,~,,竹,,ᵒᴥᵒ,,Σ,,*-*,,™,,♡,,,♡,,,♡,,カ,,タ,,🌷,,☁,,✇,,,ϟ,,水,,望,,み,♣,♥,♦,♔,♕,♚,♛,♟,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,","Stub":"username","LanguageCode":"en","NamesLanguageID":"45","Rhyming":False,"OneWord":True,"UseExactWords":False,"ScreenNameStyleString":"Any","GenderAny":True,"GenderMale":False,"GenderFemale":False}}
     )
     oldname = (random.choice(names.json()["d"]["Names"]))
     if "|" in oldname:
       newname = oldname.replace("|", "")
       print(Fore.GREEN,"[+]",Fore.RESET,newname)
     else:
       newname = oldname
       print(Fore.GREEN,"[+]",Fore.RESET,newname)

    except Exception as i:
       print()
    return newname

def main():
 print_lock = threading.Lock()
 print_lock.acquire()
 try:
  with open('username.txt', "a+", encoding="utf-8") as f:
    f.write(get_username()+"\n")
    f.close()
 except Exception as i:
       print()
 print_lock.release()
 main()

threads = []
for i in range(500):
    thread = threading.Thread(target=main)
    threads.append(thread)

# Start all threads
for thread in threads:
    thread.start()


