import sys
input = sys.stdin.readline


def inp():return(int(input()))
def inlt():return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():return(map(int,input().split()))


def solution(n):
    i = 1
    s = 1
    while n > s:
        s += i + 1
        i += 1
    return n - (s - i)

if __name__ == '__main__':
    n = inp()
    print(solution(n))