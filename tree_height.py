import sys
import threading
#import numpy
from collections import namedtuple

elem = namedtuple("elem", ["value", "depth"])

#def compute_height(n, parents):
    # Write this function
    #max_height = 0
    # Your code here
    #return max_height

def compute_height(val, h, index):
    global max_height
    if(val.depth>0):
        if(h+val.depth>max_height):
            max_height = h+val.depth
        return
    elif(val.value != -1):
        compute_height(l[val.value], h+1, val.value)
    else:
        if(h>max_height):
            max_height = h
        return
    l[index] = elem(val.value, h+1)

def main():
    # implement input form keyboard and from files
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    inp = input()
    if("i" in inp):
        print("Now input data from keyboard")
        count = int(input())
        text = input()
    elif("F" in inp):
        FName = input("Enter the name of the file: ")
        if("a" in FName):
            print("Sorry, the name can't contain letter 'a'")
        else:
            with open(FName, mode="r") as file:
                count = int(file.readline())
                text = file.readline()
                
    text = text.split()
    text = map(int, text)
    global l
    global max_height
    l = list(text)
    for i in range(len(l)):
        l[i] = elem(l[i], 0)
    max_height = 0
    val = 0
    for i in range(len(l)):
        val = l[i]
        compute_height(val, 0, i)
    print(max_height+1)
            
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))