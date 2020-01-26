n = [ int(i) for i in input("Enter a list: ").split()]
j = 0
p = len(n)
q = len(n)
lst = []
while(p>0):
    cal =1
    for i in range(0,q):
          if(i!=j):
             cal = cal * n[i]
    lst.append(cal)
    j+=1
    p-=1
print(lst)
        
