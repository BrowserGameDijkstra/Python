# A3.1.3 Maximum und das Minimum einer Zahlenliste
# Funktionen die Extremwerte einer beliebigen Zahlenliste ermittelt
"""werte = [-1, 2, 4, 5, 9,12]
# LSG ohne fkt
Max = werte[0]
Min = werte[0]
for k in werte:
    if k>Max:
        Max = k
        if k<Min:
            Min = k
print("Maximum: ",Max)
print("Minimum: ",Min)"""

# LSG mit fkt
def maxmin(Liste): # initialisiert fkt mit Objekt Liste
    Max = Liste[0] # array mit 1 Feld
    Min = Liste[0]
    for k in Liste:
        if k>Max:
           Max = k
        if k<Min:
           Min = k
    return Min,Max
# main
werte = [-1, 2, 4, 5, 9,12]
Max, Min = maxmin(werte) # ruft fkt auf und gibt Min, Max aus
print("Maxwert: ",Max)
print("Minwert: ",Min)



