def factor_of_number(n):
    factor =0 
    for i in range(1,n+1):
        if n%i==0:
            factor = i
            print(factor)


n=int(input())
factor_of_number(n)