helloworld = "hello, world"
input = input("Write something: ")

def check(array):
    for i in range (len(array)):
        if array[i] in helloworld:
            print(helloworld)
            return
        elif i == len(array)-1:
            print("no 'hello, world' characters in input")


if len(helloworld) > len(input):
    whichone = input
else:
    whichone = helloworld

check(whichone)
