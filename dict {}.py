d = {}                                    # creating a empty dictionary
d["compiled"] = "java"
d["interpreter"] = "python"
d["scripting"] = "javascript"
print(d)                                    #{'compiled': 'java', 'interpreter': 'python', 'scripting': 'javascript'}
if "interpreter" in d:
    print(d["interpreter"])                  #python
if "compiled" in d:
   del d["compiled"]
   print(d)                                #{'interpreter': 'python', 'scripting': 'javascript'}
del d
d = dict([(100,"jan"),(200,"feb"),(300,"mar"),(400,"apr")])
print(type(d))
print(d)                                      #{100: 'jan', 200: 'feb', 300: 'mar', 400: 'apr'}

d1 = dict(((100,"jan"),(200,"feb"),(300,"mar"),(400,"apr")))
print(type(d))
print(d)                                         #{100: 'jan', 200: 'feb', 300: 'mar', 400: 'apr'}


d2 = dict([[100,"jan"],[200,"feb"],[300,"mar"],[400,"apr"]])
print(type(d))
print(d)                                               #{100: 'jan', 200: 'feb', 300: 'mar', 400: 'apr'}

d3 = dict({(100,"jan"),(200,"feb"),(300,"mar"),(400,"apr")})
print(type(d))
print(d)                                          #{100: 'jan', 200: 'feb', 300: 'mar', 400: 'apr'}

#e = dict({[100,"jan"],[200,"feb"],[300,"mar"],[400,"apr"]})   = unhashable object inside set{} not allowed
#e1 = dict({{100,"jan"},{200,"feb"},{300,"mar"},{400,"apr"}})   = set{} itself a unhashable object

del d                                             # deleting the d varialble
d= {100: 'jan', 200: 'feb', 300: 'mar', 400: 'apr'}
print(d[100])     #jan
print(d.get(100))    #jan
print(d.get(100,'december'))   #jan
del d[100]
print(d.get(100,'december'))  #december
print(d.get(100))    #none
d[100] ="january"
if len(d) !=0:
    print(d.pop(200))     #feb
while True:
    print("popitem method removing:",d.popitem())   #popitem method removing: (100, 'january')
    if len(d) ==0:                                  #popitem method removing: (400, 'apr')
        break                                        #popitem method removing: (300, 'mar')



