import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

w = inp()
if w % 2 == 0 and w != 2:
    print("YES")
else:
    print("NO")
def add():
    print(1+2)
def sub():
    print(3-1)
def div():
    print(4//2)
