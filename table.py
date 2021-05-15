n=int(input("Enter the number you want table of: "))
t=int(input("Enter til which number you want it: "))
r=list(map(lambda x:n * x, range(0,t)))
for i in range(t):
    print(f'{n} x {i} = {r[i]}')
