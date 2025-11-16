s = {1,8,2,3}
print(s)

# len to lenth of the set
print(len(s))

# remove method to remove the element
s1 = {1,8,2,3}
s1.remove(8)
print(s1)

# Pop method use to remove any element
s2 = {12,26,38,45,53,68,75,82,90}
s2.pop()
print(s2)

# cleae method to clear the all set
s3 = {12,26,38,45,53,68,75,82,90}
s3.clear()
print(s3)

# Union method to return a new set with all item from both set
s4 = {12,26,38,45,53,68,75,82,90}
s5 = {23,43,13,54,90}
a=s4.union(s5)
print(a)

# Inertsection method to return set which contain only repeted element from both set
s4 = {12,26,38,45,53,68,75,82,90}
s5 = {23,43,13,54,90}
a=s4.intersection(s5)
print(a)