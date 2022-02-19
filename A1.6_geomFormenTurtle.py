from turtle import * # ZeichnenBibo

# gleichseitiges Dreieck zeichnen
color("green")    # Zeichenfarbe gruen
pensize(1)        # Liniendicke 1 Pixel
forward(100)      # erste Linie zeichnen – 100 Pixel lang
left(120)         # um 120 Grad drehen (Gegenuhrzeigersinn)
forward(100)      # zweite Linie zeichnen
left(120)         # um 120 Grad drehen
forward(100)      # Dreieck ist fertig gezeichnet
# Viereck zeichnen
color("black") # Zeichenfarbe schwarz
pensize(2) # Liniendicke 2 Pixel
penup() # Stift anheben
goto(200,0) # Schildkroete waagerecht nach rechts
setheading(0) # Schildkroete waagerecht nach rechts
pendown() # Stift absenken
forward(100) # erste Linie zeichnen – 100 Pixel lang
left(90) # um 90 Grad drehen (Gegenuhrzeigersinn)
forward(100) # zweite Linie zeichnen
left(90)# um 90 Grad drehen
forward(100) # dritteLinie zeichnen
left(90) # um 90 Grad drehen
forward(100) # vierte (letzte) Linie zeichnen – 100 Pixel lang
# Fuenfeck zeichnen – mit mehreren Kurzbefehlen
# in einer Zeile
color("red"); pensize(3); penup(); goto(0,-200)
setheading(0); pendown();
fd(100); lt(72); fd(100); lt(72); fd(100); lt(72)
fd(100); lt(72); fd(100); lt(72) # Sechseck zeichnen – mit mehreren Kurzbefehlen # in einer Zeile
color("blue"); pensize(4); penup(); goto(200,-200)
setheading(0); pendown();
fd(100); lt(60); fd(100); lt(60); fd(100); lt(60)
fd(100); lt(60); fd(100); lt(60); fd(100); lt(60)
print("Zum Beenden ins Grafikfenster klicken!")
exitonclick()
# Sechseck zeichnen – mit mehreren Kurzbefehlen
# in einer Zeile
color("blue"); pensize(4); penup(); goto(200,-200)
setheading(0); pendown();
fd(100); lt(60); fd(100); lt(60); fd(100); lt(60); fd(100); lt(60); fd(100); lt(60); fd(100); lt(60)
print("Zum Beenden ins Grafikfenster klicken!")
exitonclick()