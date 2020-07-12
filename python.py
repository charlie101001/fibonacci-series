a = int(input("enter lenght of series"))
f=0
s=1
if a<0:
    print("wrong input")
else :
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next
