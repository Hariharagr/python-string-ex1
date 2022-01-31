s = set()     # creating a empty set
s.add(range(1,12))      # adding iteratable ojects
s.update(range(12,25),range(25,30))  # updating iteratable objects two arguments
s.add(('a','b','c'))   # adding string
print(s)
s.remove(24)       # removing exact object
while len(s) != 0:
    print(s.pop())      #removing all objects and returning those object
print(s)
s.clear()    # clearing all objects
ch = 0
while ch<26:
     s.add(chr(65+ch))  #addding alphabets one by one
     ch = ch+1
print(sorted(s))   # sortind in ascending order
s1=s            # creating a duplicate reference variable
s2 =s.copy()     # clonning whole content to s2
print('#####################################################################################################################################################')
print("s:",s)
print("s1:",s1)
print("s2:",s2)
print('the address of set{} s',id(s))
print('the address of set{} s1',id(s1))
print('the address of set{} s2',id(s2))
print('is the reference of  s and s1 are same?:',s1 is s)
print('is the content of s and s1 are same?:',s1 == s)
print('is the reference of s1 and s2 are same?:',s1 is s2)
print('is the content of  s1 and s2 are same?:',s1 == s2)
s.clear()
print(s)


x= {10,20,30,40}
y= {50,60,70,80}
print("union:",x.union(y))
print(x|y)

x1= {10,20,30,40,50,60,}
y1= {50,60,70,80}
print("intersectionx:",x1.intersection(y1))
print(x1&y1)

x2= {10,20,30,40,50,60}
y2= {50,60,70,80}
print("difference:",x2.difference(y))
print(x-y)

x= {10,20,30,40,50,60}
y= {50,60,70,80}
print("symmetric_difference:",x.symmetric_difference(y))
print(x^y)






