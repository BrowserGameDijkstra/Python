# 3.5 Slicing
# sequenziellen Objekttypen
Satz = "Stadt Wuppertal"
print(Satz[0],Satz[14])
print(Satz[-1])
Liste = [ 1, 4, 9, 16, 25, 36, 49, 64 ]
print(Liste[0],Liste[7],Liste[-1])
Satz = "Stadt Wuppertal"
Name = Satz[6:14]
print(Name)
Kfz = ( "W", "E", "DO", "BO" , "K", "D")
Ruhrgebiet = Kfz[1:4]
print(Ruhrgebiet)
Kennzeichen = Kfz[:]
print(Kennzeichen)

# 3.6 List Comprehensions
# List Comprehensions erzeugen aus einer Eingabeliste eine Ausgabeliste.
# einfache Form Ausgabeliste = [ Ausdruck for Element in Eingabeliste ]
Ein = [ 1,5,10,16 ]
Aus = [i+3 for i in Ein]
print(Aus)
Aus2 = [k**2 for k in Ein]
print(Aus2)
Rein = ["Kugel","Zylinder","Quader"]
Raus = [len(x) for x in Rein]
print(Raus)
Ein = range(10)
Aus = [ x**3 for x in Ein if x%2==0 ]
print(Aus)
Liste1 = [ 1,5,6,12,17]
Liste2 = [ 2,5,6,19,12,23]
Liste3 = [u for u in Liste1 if u in Liste2]
print(Liste3)