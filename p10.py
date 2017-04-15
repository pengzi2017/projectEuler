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

def main():
    s=0
    for i in range(1,1000001):
        if isPrime(i):
            s=s+i
            #print s
    print s

main()