a="abcabcaai"
i=0
count=0
while(i<len(a)):
    if(a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u"):
        count=count+1
    i=i+1
print(count)