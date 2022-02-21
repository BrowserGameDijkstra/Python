 #A3.4.3 Programm,  beliebig viele deutsch-englische Wortpaare anfordert.  deutschen Worten als Schlüssel  Woerterbuch
# angelegt  mit Werten gefüllt   Eingabe  beendet wenn der Benutzer ohne weitere Eingabe die Return-Taste
"""Pseudo
1. leeres dict Woerterbuch anlegen
2. input deutsches Wort
3. while Schleife mit Abbruchbed. ENTER (= " ") while wortDE!="":
4. wortEN input
5. zuordnung wordDE zu wordEN
6. input wordDE um Schleife zu vervollständigen
7. Ausgabe
"""
"""
Woerterbuch = {}
wortDE = input("Bitte ein deutsches Wort eingeben")
while wortDE!="": # kein Leerzeichen zwischen ""!
    wortEN = input("Bitte ein englisches Wort eingeben")
    Woerterbuch[wortDE] = wortEN
    wortDE = input("Bitte ein deutsches Wort eingeben")
print(Woerterbuch)
"""
# A 3.4.4 nach der Abfrage der Worte zunächst geprüft wird, ob zu einem deutschen Wort (Schlüssel) schon ein Eintrag vorhanden ist.
 # Meldung und den vorhandenen Eintrag ausgeben Benutzer entscheiden ob er diesen Eintrag überschreiben will oder nicht

Woerterbuch = {}
wortDE = input("Bitte ein deutsches Wort eingeben")
while wortDE!="": # kein Leerzeichen zwischen ""!
    wortEN = input("Bitte ein englisches Wort eingeben")
    # Schlüssel schon vorhanden?
    if wortDE in Woerterbuch.keys():
    # Schlüssel schon vorhanden
       print("Warnung! Ein Eintrag ist schon vorhanden!")
    # Ausgabe des vorh. Schlüssels
       print("Schluessel: ", wortDE, " Wert: ", Woerterbuch[wortDE])
    # Ausgabe zur Löschung
       antwort = input("Sollen diese Werte ueberschrieben werden? (j/n)")
       if antwort.upper() == "J": # upper stellt sicher daß Eingabe immer Grossgeschr. ist
          Woerterbuch[wortDE] = wortEN
    else:
        Woerterbuch[wortDE] = wortEN
    wortDE = input("Bitte ein deutsches Wort eingeben")
print(Woerterbuch)