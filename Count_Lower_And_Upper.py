def Count_Lower_And_Upper(S):
    Count_Lower = 0
    Count_Upper = 0 
    for i in S:
        if i.isupper():
            Count_Upper+=1 
        elif i.islower():
            Count_Lower+=1 
    print(Count_Upper)
    print(Count_Lower)







S=input()
Count_Lower_And_Upper(S)