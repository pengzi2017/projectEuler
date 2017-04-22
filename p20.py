#p20 Factorial digit sum

def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)

def sum_of_digit(num):
    numStr=str(num)
    s=0
    for i in numStr:
        s+=int(i)
    return s

def main():
    num=fact(100)
    result=sum_of_digit(num)
    print('The sum_of_digit in the number 100! is %s'%result)

main()
