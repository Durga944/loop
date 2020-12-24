a=1
while(a<=100):
    if(a%3==0):
        print("nav")
    if(a%7==0):
        print("gurukul")
    if(a%3==0 and a%7==0):
        print("navgurukul")
    else:
        print(a)
    a=a+1