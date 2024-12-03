
list = ['a','b','c']

print( ','.join(list)) # a,b,c
print( ','.join(f"'{item}'" for item in list))) # 'a','b','c'