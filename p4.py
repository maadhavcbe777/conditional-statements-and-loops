lst=[]
n=int(input("enter the no of values"))
for i in range(0,n):
    a=int(input())
    lst.append(a)
print("list is",lst)
print("positive numbers is")
for i in lst:
    if(i>0):
        print(i)