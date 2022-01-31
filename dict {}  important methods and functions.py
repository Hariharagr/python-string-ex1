i = 1
d = {}
while i<=26:
    d[i] = chr(64+i)   # creating alphabets as values
    i = i+1
print(d)
d1 = d.copy()  #cloning
alpha=[]
while len(d) != 0:
    a = ("processing item to remove",d.popitem())       # removing and returning those items
    b=list(a[1]) # type casting tuple into list
    alpha = alpha + b # adding elements one by one into list 
print(alpha) 
print(d)

k = d1.keys()
print("key",k)   # getting only keys

v = d1.values()
print("value",v)  # getting only values

i = d1.items()
print("items",i)   # gettting pairs of items

for key1,values1 in d1.items():
    print("{} : {} " .format(key1,values1) ,end=",  ")   # getting each items and seperating their key and value
print()
sum = ""
for values2 in d1.values():
       sum = sum+values2   # getting only values and adding them
print(sum)










