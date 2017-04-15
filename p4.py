#-*- coding:utf-8 -*-
#求两个三位数乘积的最大的回文数

def palindrome(n):
    temp=str(n)
    l=len(temp)
    for i in range(0,l/2):
        if temp[i] != temp[l-1-i]:  # 不能写成if true else false的形式，
            return False            #因为return一出现就意味着整个函数的
        else:                       #结束，当然循环也只会执行一次
            pass
    return True

def largestPalindrome():
    for i in range(999,0,-1):
        for j in range(i,0,-1):
            if palindrome(i*j):
                print i,'*',j,'=',i*j
            else:
                pass

if '__name__'=='__main__':
    largestPalindrome()