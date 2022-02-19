# A2.3 Funktion namens XOR, die die logische Funktion Entweder-Oder realisiert

# Funktionsdefinition 
def XOR(a, b):
    # XOR realisiert die Entweder-Oder-Funktion
    # dürfen nicht gleichen Wert haben
    c = (a and not b) or (not a and b)
    return c
    # Hauptprogramm 
for a in True, False:
    for b in True, False:
        print(a, b, XOR(a, b))
