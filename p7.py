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
    i,a=0,1
    while i <10001:
        if isPrime(a):
            i+=1
        a+=1

    print a

main()