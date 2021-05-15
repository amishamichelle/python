def order (x):
    n=0
    while(x!=0):
        n=n+1
        x=x//10
    return n
def power (x,y):
    if y==0:
        return 1
    if y%2==0:
        return power(x,y//2)*power(x,y//2)
    return x*power(x,y//2)*power(x,y//2)    

def armstrong(x):
    n = order(x)
    temp = x
    sum1 = 0
      
    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + power(r, n)
        temp = temp // 10
    # If condition satisfies
    return (sum1 == x)

x=int(input("enter the number"))
print(armstrong(x))

if armstrong(x)==True:
    print("It is an armstrong number")
elif armstrong(x)==False:
    print("It is not an armstrong number")
else:
    print("unexpected input")
