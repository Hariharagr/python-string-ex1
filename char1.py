s = input('enter any string with digit')
output = ''
for x in s:
    if x.isalpha():
        ch = x
        output = output + ch
    else:
      newch = chr(ord(ch)+int(x))
      output = output + newch
print(output)


s = 'ad12aswq55'
output = ''
num = ''
i = 0
while i<len(s):
         if s[i].isalpha():
             ch = s[i]
         else:
            num = num + s[i]
            if i == len(s)-1:
                output = output + ch*int(num)
            if i+1 < len(s) and s[i+1].isalpha():
                output = output + ch*int(num)
                num = ''
         i=i+1
print(output)






