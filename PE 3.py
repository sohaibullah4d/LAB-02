print("MUHAMMAD SOHAIB - 18B-054-CS - SEC-A")
print("LAB NO: 02")

import math
print("\n(a)\n")
lst = [1,3,5,7,9,11,13,15,17]
mid_index = math.floor(len(lst)/2)
print("The index of the middle number in lst is:",mid_index)

print("\n(b)\n")
print("The middle element of the lst is:",lst[mid_index])

print("\n(c)\n")
lst.sort()
lst.reverse()
print("The list in decending order is:",lst)

print("\n(d)\n")
lst = [1,3,5,7,9,11,13,15,17]
lst.pop()
lst.remove(1)
lst.append(1)
print(lst)
