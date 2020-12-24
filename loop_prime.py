i=1
while(i<=10):
    j=2
    while(j<i):
        if(i%2==0):
            print(i,"not prime")
            break
        j=j+1
    else:
            print(i,"prime")
    i=i+1




#     s=int(input("enter any num"))
# n=int(input("enter any num"))
# if(n==500):
#     print(s//n)
# if(n==200):
#     print(s//n)
# elif(n==100):
#     print(s//n)
# else:
#     print(" it is not vilid")