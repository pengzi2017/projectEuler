#encoding=utf8
#有必要在Ubuntu 上做测试

def LCM():
    divisors = [x for x in range(1,21)]
    x = 1
    while True:
        smallest = True
        for i in divisors:
            if x % i != 0:
                smallest = False
                break
        if smallest:
            print(x)
            break
        x += 1

LCM()

