# Wahrheitstabelle der logischen Funktionen and und or
# durch Einsatz von for Schleifen

# True True True
# False True False
b = True
for a in True, False:
    c = a and b
    print(a, b, c)

# True (True, False) (True, False) True
# False (True, False) False (True, False)
b = True,False
for a in True, False:
    c = a and b
    d = a or b
    print(a, b, c, d)
    
 # A2.2  Wahrheitstabelle der logischen Funktionen 
 # c = (a and not b) or (not a and b). 
for a in True, False: 
     for b in True, False:
        c = (a and not b) or (not a and b)
     print(a, b, c)  