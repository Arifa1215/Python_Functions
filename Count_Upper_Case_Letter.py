def Count_Upper_Case_Letter(S):
    count=0
    for i in S:
        if i.isupper():
            count+=1 
    print(count)







S=input()
Count_Upper_Case_Letter(S)