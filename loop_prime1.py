user=int(input("enter any num"))
result=0
i=1
while(i<=user):
    if(user%i==0):
        result=result+1
    i=i+1
if(result==user):
    print(i,"prime")
else:
    print(i,"not prime")