#encoding=utf-8
#最大质因数

from math import sqrt

def isPrime(x):
    if x==1:
        return 0
    if x==2:
        return 1
    if x>2:
        for i in range(2,int(sqrt(x))+2):
            if x%i==0:
                return 0
            elif i ==int(sqrt(x)+1):
                return 1

def LargestPrimeFactor(n):
    for i in xrange(n,0,-1):
        if n%i ==0 and isPrime(i):
            print i
            break

LargestPrimeFactor(13195)