def is_prime(number):
    if number>1:
        for i in range(2, number):
            if (number % i)==0:
                return "Not a Prime Number"
            else:
                return "Prime Number"
    elif number==1:
        return "Not a Prime Number"

number = int(input())
result = is_prime(number)
print(result)