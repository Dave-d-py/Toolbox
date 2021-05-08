from colored import fg, bg, attr
import pyfiglet
import time
import ctypes
import os, sys

def pip():
    pack = input("Packet Namen eingeben >>> ")
    os.system(f"pip install {pack}")


def datum():
    t = time.ctime()
    t = t.split()

    ctypes.windll.user32.MessageBoxW(0, f"Tag: {t[0]} \n"
                                        f"Monat: {t[1]} {t[2]} \n"
                                        f"Uhrzeit: {t[3]} \n"
                                        f"Jahr: {t[4]} \n", "Datum", 0)


def menu():
    color = fg('#C0C0C0') + bg('#00005f')
    res = attr('reset')

    out = pyfiglet.figlet_format("Tool - Box", font="big")
    print(color + out + res)
    print("[1] - Zeit")
    print("[2] - pip installation")
    print("[3] - Dos Angriff")