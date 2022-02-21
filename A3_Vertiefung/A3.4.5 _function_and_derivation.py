# Aufgabe 3.4.5 Programm, Eingabe des Namens einer mathematischen Funktion die Ableitung  Funktion als Zeichenkette ausgibt.
# Verwenden Sie ein Dictionary, Wenn ein Funktionsname geben wird, der nicht in dem Dictionary enthalten ist,
# soll eine Fehlermeldung ausgegeben werden. Der Programmabbruch soll wie bei Aufgabe 3
"""Funktionsname Ableitung
sin(x) cos(x)
cos(x) -sin(x)
exp(x) exp(x)
ln(x) 1/x
x 1
"""
""" Pseudo
1. Tabelle als Diff erzeugen
2. input mit Abfrage nach funktion
2. while Schleife mit Abbrbed. !=""
3. Abfrage ob funktion vorhanden
4. Ausgabe wenn ja
5. ansonsten Ausgabe nicht vorh
6. wieder zur Eingabe funktion
"""
Diff = {"sin(x)":"cos(x)","cos(x)":"-sin(x)", \
        "exp(x)": "exp(x)", "ln(x)": "1/x", "x": "1" }
funktion = input("Bitte Funktion eingeben")
while funktion!= "":
        if funktion in Diff.keys():
                print("Die Funktion hat die Ableitung")
                print(Diff[funktion])
        else:
                print("Diese Funktion ist nicht in der Tabelle enthalten!")
        funktion = input("Bitte Funktion eingeben")
