#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
##############################################
#
# Name: U7.2_Threading_Beispiel.py
#
# Purpose: Prüfen der Verfügbarkeit einiger URLs
#
##############################################

import threading
import urllib.request
import time

response = []
threads = []
urls = [
    "http://chp.ch",
    "http://cssgmbh.ch",
    "http://irgendeinedomain.ch",
    "http://zouberhuet.ch"]


def get_url(url):  # Funktion
    threads.append(url)
    try:
        response.append(urllib.request.urlopen(url).read())
    except BaseException:
        response.append("Probleme mit " + url)
    threads.remove(url)


for url in urls:  # Starten der Threads
    t = threading.Thread(target=get_url, args=(url,))
    t.start()

while threads:
    pass  # Auf Ende der Threads warten
for r in response:
    if "Probleme" in str(r):
        print(r)
