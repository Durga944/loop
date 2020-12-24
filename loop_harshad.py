num=int(input("enter any num"))
a=num
sum=0
while(num>0):
    rem=num%10
    sum=sum+rem
    num=num//10
if(a%sum==0):
    print(a,"harshad")
else:
    print(a,"not harshad")
    
    