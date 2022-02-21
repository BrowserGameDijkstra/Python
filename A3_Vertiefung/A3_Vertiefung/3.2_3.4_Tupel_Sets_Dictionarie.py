# Tupels
"""
- ähnlich Liste jedoch unveränderlich
 und somit vor Änderung geschützt
"""
werte = (10,20,30)
type(werte)

# Sets-Mengen
"""
- Schnittmenge,Differenzmenge,Vereinigungsmenge Operationen (&,-,|) 
"""
Menge1 = set([12,34,60,12,72,34,90])
print(Menge1)
Menge2 = set([17,90,34,34,112,9,12])
print(Menge2)
a=Menge1&Menge2
print(a)
b=Menge1-Menge2
print(b)
c=Menge2-Menge1
print(c)
d=Menge1|Menge2
print(d)
for i in Menge1:
    print(i)

# 3.4  Dictionaries
# ungeordnete Sammlung von Schlüssel-Wert-Paaren
#  Tabelle  die aus zwei Spalten besteht -> Schlüssel - Wert
# Bsp
woerterbuch = {"rot":"red","gelb":"yellow","gruen":"green"}

