#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
##############################################
#
# Name: U7.2_PrimRechner_Single.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.07.2017
#
# Purpose: Errechnet die Primzahlen innerhalb eines definierten Zahlenbereiches
#
##############################################

# Variabeln
pc = []  # Liste für Primzahlenzähler

# Funkdtionen


def primrechner(ps, pe):
    print("Suche Primzahlen von", ps, "bis", pe)
    for z in range(ps, pe + 1):
        pc.append(z)
        for z2 in range(2, z):
            if not z % z2:
                pc.remove(z)
                break


# Prozess starten
primrechner(1, 30000)

# Abschluss
print("Es wurden", len(pc), "Primzahlen gefunden")
