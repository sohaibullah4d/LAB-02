print("MUHAMMAD SOHAIB - 18B-054-CS - SEC-A")
print("LAB NO: 02")

print("\n(a)\n")

monthsL = ['Jan','Feb','Mar','May']
monthsT = ('Jan','Feb','Mar','May')
monthsL.insert(3,'Apr')
monthsE = list(monthsT)
monthsE.insert(3,'Apr')
monthsT = tuple(monthsE)


print(monthsL)
print(monthsT)

print("\n(b)\n")
monthsL = ['Jan','Feb','Mar','May']
monthsT = ('Jan','Feb','Mar','May')
monthsL.append('Jun')
monthsT = monthsT + ('Jun',)

print(monthsL)
print(monthsT)

print("\n(c)\n")
monthsL = ['Jan','Feb','Mar','May']
monthsT = ('Jan','Feb','Mar','May')
monthsL.append('Jun')
monthsT = monthsT + ('Jun',)

print(monthsL)
print(monthsT)

print("\n(d)\n")
monthsL = ['Jan','Feb','Mar','May']
monthsT = ('Jan','Feb','Mar','May')
monthsL.remove('Feb')
monthsE = list(monthsT)
monthsE.remove('Feb')
monthsT = tuple(monthsE)

print(monthsL)
print(monthsT)

print("\n(e)\n")
monthsL = ['Jan','Feb','Mar','May']
monthsT = ('Jan','Feb','Mar','May')
monthsL.reverse()
monthsE = list(monthsT)
monthsE.reverse()
monthsT = tuple(monthsE)

print(monthsL)
print(monthsT)

print("\n(f)\n")
monthsL = ['Jan','Feb','Mar','May']
monthsT = ('Jan','Feb','Mar','May')
monthsL.sort()
monthsE = list(monthsT)
monthsE.sort()
monthsT = tuple(monthsE)

print(monthsL)
print(monthsT)





































      
