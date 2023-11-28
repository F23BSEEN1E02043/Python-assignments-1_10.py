a=[1,2,3,4,5,6]
b=[7,8,9,10,11,12]
list_res=[]
for n in a:
    if n % 2 != 0:
        list_res.append(n)
for n in b:
    if n % 2 == 0:
        list_res.append(n)
        print('new list is:',list_res)        
