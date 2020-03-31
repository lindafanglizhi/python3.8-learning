list_1=[-8,5,0,4,9,-20,-2,8,2,-4]
list_1.sort(key=lambda x: (x < 0, abs(x)))
print(list_1)
a=list(filter(lambda x:x>=0,list_1))
b=list(filter(lambda x:x<0,list_1))
a1=sorted(a)
b1=sorted(b,reverse=True)
print(a1+b1)