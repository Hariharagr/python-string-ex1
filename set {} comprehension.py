s = {x*x for x in range(1, 19)}     # comprehension of set
print(s)
s1 ={x*x for x in range(1, 100) if x%5==0}
print(sorted(s1))
s2 = {x**x for x in range(1, 200) if x%2 == 0} # squareroot  of even numbers
print(sorted(s2))
s3 = {x**x for x in range(1, 300) if x%3 == 0} # cube of odd numbers
print(sorted(s3))

w = ("python is both procedure and object oriented language") # findinfg vowels from the given string
s=set(w)
v={"a","e","i","o","u"}
result = s.intersection(v)
result1 = s&v
print(sorted(result))
print(sorted(result1))
