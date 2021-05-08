from funcs import *

menu()

#    f"Tag: {t[0]} \n"
#    f"Monat: {t[1]} {t[2]} \n"
#    f"Uhrzeit: {t[3]} \n"
#    f"Jahr: {t[4]} \n"

#        print(f"Tag: {t[0]} \n")
#        print(f"Monat: {t[1]} {t[2]} \n")
#        print(f"Uhrzeit: {t[3]} \n")
#        print(f"Jahr: {t[4]} \n")

while True:
    wahl = str(input(">>>>"))
    if wahl == "1":
        datum()
    elif wahl == "2":
        pip()