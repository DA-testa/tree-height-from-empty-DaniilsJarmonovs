#Izstrādāja: Daniils Jarmonovs (221RDC003) - 18. grupa

import sys
import threading
#import numpy
from collections import namedtuple

elem = namedtuple("elem", ["value", "depth", "visited"])

def main():
    inp = input()
    text = ""
    count = 0
    if("I" in inp):
        count = int(input())
        text = input()
    elif("F" in inp):
        FName = input()
        if("a" in FName):
            print("Sorry, the name can't contain letter 'a'")
        else:
            with open("./test/"+FName, mode="r") as file:
                count = int(file.readline())
                text = file.readline()
                
    text = text.split()
    text = map(int, text)
    l = list(text)
    max_height = 0
    for i in range(count):
        l[i] = elem(l[i], 0, False)
    for i in range(count):
        val = l[i]
        if(not val.visited):
            tail = [i]
            height = 1
            while(val.value != -1):
                tail.append(val.value)
                val = l[val.value]
                height = height + 1
                if(val.visited):
                    height = height + val.depth
                    break
            if height>max_height:
                max_height = height
            n = val.depth
            for j in range(len(tail)-1, -1, -1):
                node = tail[j]
                if l[node].depth<n:
                    l[node] = elem(l[node].value, n, True)
                n += 1
    print(max_height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()