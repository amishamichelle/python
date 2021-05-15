lst=[]
n=int(input("Enter n elements: "))
print("Enter elements")
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print(lst)
def swaplist(nlst):
    temp=nlst[0]
    nlst[0]=nlst[n-1]
    nlst[n-1]=temp
    return nlst
print(swaplist(lst))
