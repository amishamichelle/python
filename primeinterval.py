s=int(input("enter the start interval"))
e=int(input("enter the end interval"))
for i in range(s,e+1):
        for j in range(2,i):
            if(i%j==0):
                break;
        else:
            print(i)
