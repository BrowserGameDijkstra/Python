print("Umrechnung der Temperaturen von Celsius in Fahrenheit")
print("-----------------------------------------------------")
print()
Celsius = input("Bitte geben Sie eine Temperatur in Celsius ein: ")
Celsius = float(Celsius)

Fahrenheit = 9/5 * Celsius + 32
print()
print("Sie haben %f Grad Celsius eingegeben." % Celsius)
print()
print("Diese Temperatur entspricht %f Grad Fahrenheit." % Fahrenheit)