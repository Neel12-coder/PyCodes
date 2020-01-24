n=int(input("Enter how many no.s: "))
k = int(input("Enter number2"))
lst=[]
flag = 0
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele)
for x in lst:
    for y in lst:
        if(x+y == k):
          flag =1
if(flag == 1): 
  print(True)
else:
  print(False)
         
