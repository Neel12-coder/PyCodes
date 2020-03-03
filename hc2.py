n = int(input())
score= [int(i) for i in input().split()]
m = int(input())
alice = [ int(i) for i in input().split()]
sc = set(score)
sc1 = []
for x in sc:
    sc1.append(x)
sc1.sort(reverse=True)
#print(sc1)
for y in alice:
    if y in sc1:
        a=sc1.index(y)
        print(a+1)
    else:
        sc1.append(y)
        sc1.sort(reverse= True)
        b = sc1.index(y)
        print(b+1)
        sc1.remove(y)
        
