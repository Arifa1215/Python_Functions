def sum_of_squares(m,n):
    sum_of_squares =0
    for i in range(m,n+1):
        sum_of_squares+=i**2 
    return sum_of_squares
    


m=int(input())
n=int(input())
print(sum_of_squares(m,n))