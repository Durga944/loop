n=int(input("enter any num"))
i=0
while(n>0):
    i=n//2
    if(i*2==n):
        print("even")
else:
    print("odd")
    i=i+1