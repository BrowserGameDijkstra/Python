from math import *
print("Logik um auf wahr/falsch zu prüfen")
print("-----------------------------------------------------")
print()
# verschiedene Ansätze zB per Logik.Zeichen
# ((8 < 5) or (4 != 7)) or not (not (4 == 5))

# per Variable endet mit true (besser)
ergebnis = ((8 < 5) or (4 != 7)) or not (not (4 == 5))
print(ergebnis)