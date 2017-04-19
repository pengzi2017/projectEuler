#-*- coding:utf-8 -*-

s=0
i=1
j=2

while j<4000000:
    i=i+j
    j=j+i
    if i%2 ==0:
        s=s+i
    elif j%2== 0:
        s=s+j

print s

#别人解法
def fib_generator(n):
    a, b = 1, 1
    while b <= n:
        a, b = b, a + b
        yield a


def solution(n):
    return sum(i for i in fib_generator(n) if not i % 2)

if __name__ == '__main__':
    print(solution(4000000))
