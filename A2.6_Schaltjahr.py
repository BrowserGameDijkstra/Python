# A2.6 Programm, welches entscheidet,
# ob ein Jahr ein Schaltjahr ist
jahr = int(input("Bitte geben Sie ein Jahr an: "))
if jahr%4 == 0: # Modulo4
       if jahr%100 == 0:
          if jahr%400 == 0:
             if jahr == 4000:
                  print ("Kein Schaltjahr")
             else:
                  print("Schaltjahr")
          else:
               print("Kein Schaltjahr")
       else:
           print("Schaltjahr")
else:
     print("Kein Schaltjahr")
# auf richtiges einrücken achten passendes if zugeöriges  else!
