#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
##############################################
#
# Uebung:
# Erstellen Sie ein Programm, welches fünf Prozesse startet
# Die Prozesse sollen nur aus einem sleep-Kommando bestehen
# Die sleep-Time soll per Zufallszahl zwischen 10 und 20 Sekunden liegen
#
##############################################

#### Lösung: ####

from multiprocessing import Process, Pipe
import random
import time

# Variabeln
pia, pib = Pipe()  # Pipe erstellen

# Funktionen


def start_sleep(pc):
    n = random.randint(10, 20)
    print("Starte sleep mit", n, "Sekunden")
    time.sleep(n)
    pia.send(pc)


# Prozesse starten
for pc in range(5):
    px = Process(target=start_sleep, args=(pc,))
    px.start()

# Abschluss
for pc in range(5):
    resp = pib.recv()
