data = [ 1,2,3,4,5,6,2,7]
seen = set()
dupes = [x for x in data if x in seen or seen.add(x)]   

print("dupes", dupes) 
print("seen", seen) 
