def get_discount(k):
    if k<500:
        print("5%")
    elif k>=500 and k<2500:
        print("10%")
    else:
        print("20%")

k=int(input())
get_discount(k)

        