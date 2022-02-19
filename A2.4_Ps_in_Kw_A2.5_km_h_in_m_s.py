"""# A2.4 PS in kW mittels einer Programmschleife mit 3 Nachkomma
faktor = 0.7354
print("PS | kW")
print()
for ps in range(50, 210, 5):
    kW = ps * faktor
    print("%9.2f %9.2f" % (ps, kW))
"""
# A2.5 Programmschleife eine Umrechnungstabelle von km/h in m/s.
faktor = 0.2777
print(" km/h | m/s ")
print()
for kmh in range(0, 275, 25):
    ms = kmh * faktor
    print("%9.2f %9.2f" % (kmh, ms))
