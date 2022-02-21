# ganze Zahlen stapeln mit fkt
Stapel = []  # array erzeugen
def AufDenStapel(eintrag): # fkt um Stapel zu erzeugen
    Stapel.append(eintrag)
    print("Der Eintrag ", eintrag, " wurde auf den Stapel gelegt")    
                                      
                              
def StapelLaenge():    # Abschnitt gibt Anzahl Elemnte Stapel an
    return len(Stapel)
def StapelAusgeben():  # Anzahl Stapel
     print()
     for i in Stapel:
         print(i )
     print()

def VonDemStapel():
    if len(Stapel) != 0:
        oben = Stapel[-1]  # fängt vom letzten Element an die werte auszugeben 0 wäre vom ersten 1 vom zweiten
        Stapel.remove(oben)
        print("Das Element ", oben, " wurde vom Stapel entfernt")
    else:
        print("Der Stapel ist leer!")
        print("Es kann nichts entfernt werden!")
        AufDenStapel(29)
        AufDenStapel(155)
        AufDenStapel(134)
        AufDenStapel(12)
        AufDenStapel(14)
        print(StapelLaenge())
        StapelAusgeben()   # zeigt Stapel nach ablegen
# ruft fkt 4 mal auf
VonDemStapel()
VonDemStapel()
VonDemStapel()
VonDemStapel()
VonDemStapel()
VonDemStapel()   


