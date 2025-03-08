import threading
import random

def getinput(val):
    global x
    x = input(str(val) + '\n')
    return

x = -1

usrtime = int(input("How many seconds do you get to type a scrambled version of 'hello, world'? "))

eval = ""
usedindex = []
helloworld = "hello, world"
sortin = True

while True:
    placeholder = random.randint(0, len(helloworld)-1)
    if placeholder not in usedindex:
        eval += helloworld[placeholder]
        usedindex.append(placeholder)
    elif len(usedindex) == len(helloworld):
        break

t1 = threading.Thread(target=getinput, args=(eval,))

t1.start()
t1.join(timeout=usrtime)

typeofeval = type(eval)
if typeofeval(x) == eval:
    print("hello, world")
else:
    print('\ngoodbye, world')
