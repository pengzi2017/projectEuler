def count_divisors(n):
    count=0
    for i in range(1,n+1):
        if n%i ==0:
            count+=1
    return count

i=1
while True:
    if count_divisors(i)>100:
       print i
       break
    i+=1