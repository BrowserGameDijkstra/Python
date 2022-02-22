# 3.8.1 Schlüsselwort-Parameter
# Funktion beinhaltet einen Programmcode, der mehrfach verwendet werden soll
# Funktionen haben Übergabeparameter (auch formale Parameter  einfache Parameter)
# können auch Werte zurückgeben (Rückgabewerte, Return Values)
# Bei den Parametern der Funktion kann es aber auch optionale Parameter geben
"""
Funktion Quadrat() hat fünf Parameter,Alle Parameter müssen übergeben werden, wenn Funktion aufgerufen
bestimmte Para meter nicht bedeutsam  deshalb bereits voreingestellte Werte (sogenannte Default-Werte)
"""
"""
from turtle import *
def Quadrat(x,y,Laenge,Farbe,Dicke): # Farben ändern sich nach Zuordnung
    pensize(Dicke)
    pencolor(Farbe)
    penup()
    goto(x,y)
    pendown()
    for i in range(4):
        forward(Laenge)
        left(90)
# Aufrufe der Funktion Quadrat(0,0,100,"red",4)
Quadrat(0,0,100,"red",4)
Quadrat(100,-100,100,"blue",2)

# Beispiel zeigt, wie die Linienfarbe und Liniendicke als optionale Parameter erklärt werden können
from turtle import *
def Quadrat(x,y,Laenge,Farbe="black",Dicke=3):
    pensize(Dicke)
    pencolor(Farbe)
    penup()
    goto(x,y)
    pendown()
    for i in range(4):
        forward(Laenge)
        left(90)
# Aufrufe der Funktion Quadrat(0,0,100)
Quadrat(100,-100,100)
Quadrat(200,0,100,Farbe="red")
"""
# Schlüsselwort-Parameter  müssen  nach den Pflicht-Parametern (Positions-Parametern) stehen

# 3.8.2 Module
# Funktion in einem Modul speichern und die bei Bedarf zu importieren.
# Funktion Quadrat() unter einem anderen Namen als normale Python-Datei abgespeichert.
# import des Moduls geometry. py und ausführen in externer Funktion
from geometry import Quadrat
for x in range(0, 200, 40):
    for y in range(0, 200, 40):
        Quadrat(x, y, 40)
