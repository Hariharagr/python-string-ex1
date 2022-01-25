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



