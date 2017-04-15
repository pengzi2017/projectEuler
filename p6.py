def main():
    n=100
    s1=s2=0
    for i in range(1,n+1):
        s1=s1+i**2
        s2=s2+i

    print s2**2-s1

main()