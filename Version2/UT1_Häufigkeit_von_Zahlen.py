#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
####################################################
#
# Uebung UT1_Häufigkeit_von_Zahlen
# Schreiben Sie ein Programm, welches die Häufigkeit
# des Auftretens der grössten Zahlen in einem Tupel aus gibt.
#
####################################################

# Variabeln
tup1 = (2, 17, 10, 9, 16, 3, 9, 16, 5, 1, 17, 14)
maxZahl = 0
Anzahl = 0

# Auswertung
for i in tup1:
    if i > maxZahl:
        maxZahl = i
        Anzahl = tup1.count(i)

# Ausgabe
print("Häufigstes Element ist die", maxZahl, "mit", Anzahl, "Treffern")
