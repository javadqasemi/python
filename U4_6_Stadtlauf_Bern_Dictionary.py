#! env python3
####################################################
#
# Uebung:
# Im untenstehnden Code läuft die Figur zum Zytgloggen Turm
# Hierbei wird mit if-Kommandos geprüft, ob die Figure an einer Sehenswürdigkeit vorbei läuft
#
# Ändern Sie die Funktion "check_text()" so ab, dass sie für die Prüfung, 
# ob eine Sehenswürdigkeit angezeigt werden soll, das Dictionary "pos" verwendet
# In diesem Dictionary sind pro Position die x,y-Werte in einem Tupel enthalten
#
# Vorhandene Funktionen
#
# go_right()   : Geht einen Schritt nach rechts
# go_left()    : Geht einen Schritt nach links
# go_up()      : Geht einen Schritt hoch
# go_down()    : Geht einen Schritt runter
# go_walk_right(x,y): Läuft zur Position x,y nach rechts
# go_walk_left(x,y) : Läuft zur Position x,y nach links
# Taste q      : Abbruch des Spiels
#
# Hinweis: Neuer Code nur im markierten Bereich eintragen
#
####################################################

#Module
import pygame
import time
from stadtlauf_bern_modul import *

d=1           ##Anzahl Durchgänge
slower=0.01   #Je höher die Zahl, umso langsamer läuft die Figur
#Wegdaten zum Zytglogge
zytglogge=((21,155), (22,155), (23,155), (24,155), (25,155), (26,155), (27,155), (28,155), (29,155), (30,154), (31,154), (32,154), (33,154), (34,154), (35,154), (36,154), (37,154), (38,154), (39,154), (40,153), (41,153), (42,153), (43,153), (44,153), (45,153), (46,153), (47,153), (48,153), (49,153), (50,152), (51,152), (52,152), (53,152), (54,152), (55,152), (56,152), (57,152), (58,152), (59,152), (60,151), (61,151), (62,151), (63,151), (64,151), (65,151), (66,151), (67,151), (68,151), (69,151), (70,150), (71,150), (72,150), (73,150), (74,150), (75,150), (76,150), (77,150), (78,150), (79,150), (80,149), (81,149), (82,149), (83,149), (84,149), (85,149), (86,149), (87,149), (88,149), (89,149), (90,148), (91,148), (92,148), (93,148), (94,148), (95,148), (96,148), (97,148), (98,148), (99,148), (100,147), (101,147), (102,147), (103,147), (104,147), (105,147), (106,147), (107,147), (108,147), (109,147), (110,146), (111,146), (112,146), (113,146), (114,146), (115,146), (116,146), (117,146), (118,146), (119,146), (120,145), (121,145), (122,145), (123,145), (124,145), (125,145), (126,145), (127,145), (128,145), (129,145), (130,144), (131,144), (132,144), (133,144), (134,144), (135,144), (136,144), (137,144), (138,144), (139,144), (140,143), (141,143), (142,143), (143,143), (144,143), (145,143), (146,143), (147,143), (148,143), (149,143), (150,142), (151,142), (152,142), (153,142), (154,142), (155,142), (156,142), (157,142), (158,142), (159,142), (160,141), (161,141), (162,141), (163,141), (164,141), (165,141), (166,141), (167,141), (168,141), (169,141), (170,140), (171,140), (172,140), (173,140), (174,140), (175,140), (176,140), (177,140), (178,140), (179,140), (180,139), (181,139), (182,139), (183,139), (184,139), (185,139), (186,139), (187,139), (188,139), (189,139), (190,138), (191,138), (192,138), (193,138), (194,138), (195,138), (196,138), (197,138), (198,138), (199,138), (200,137), (201,137), (202,137), (203,137), (204,137), (205,137), (206,137), (207,137), (208,137), (209,137), (210,136), (211,136), (212,136), (213,136), (214,136), (215,136), (216,136), (217,136), (218,136), (219,136), (220,137), (221,137), (222,137), (223,137), (224,137), (225,137), (226,137), (227,137), (228,137), (229,137), (230,138), (231,138), (232,138), (233,138), (234,138), (235,138), (236,138), (237,138), (238,138), (239,138), (240,139), (241,139), (242,139), (243,139), (244,139), (245,139), (246,139), (247,139), (248,139), (249,139), (250,140), (251,140), (252,140), (253,140), (254,140), (255,140), (256,140), (257,140), (258,140), (259,140), (260,141), (261,141), (262,141), (263,141), (264,141), (265,141), (266,141), (267,141), (268,141), (269,141), (270,142), (271,142), (272,142), (273,142), (274,142), (275,142), (276,142), (277,142), (278,142), (279,142), (280,143), (281,143), (282,143), (283,143), (284,143), (285,143), (286,143), (287,143), (288,143), (289,143), (290,144), (291,144), (292,144), (293,144), (294,144), (295,144), (296,144), (297,144), (298,144), (299,144), (300,145), (301,145), (302,145), (303,145), (304,145), (305,145), (306,145), (307,145), (308,145), (309,145), (310,146), (311,146), (312,146), (313,146), (314,146), (315,146), (316,146), (317,146), (318,146), (319,146), (320,147), (321,147), (322,147), (323,147), (324,147), (325,147), (326,147), (327,147), (328,147), (329,147), (330,148), (331,148), (332,148), (333,148), (334,148), (335,148), (336,148), (337,148), (338,148), (339,148), (340,149), (341,149), (342,149), (343,149), (344,149), (345,149), (346,149), (347,149), (348,149), (349,149), (350,150), (351,150), (352,150), (353,150), (354,150), (355,150), (356,150), (357,150), (358,150), (359,150), (360,151), (361,151), (362,151), (363,151), (364,151), (365,151), (366,151), (367,151), (368,151), (369,151), (370,152), (371,152), (372,152), (373,152), (374,152), (375,152), (376,152), (377,152), (378,152), (379,152), (380,153), (381,153), (382,153), (383,153), (384,153), (385,153), (386,153), (387,153), (388,153), (389,153), (390,154), (391,154), (392,154), (393,154), (394,154), (395,154), (396,154), (397,154), (398,154), (399,154), (400,155), (401,155), (402,155), (403,155), (404,155), (405,155), (406,155), (407,155), (408,155), (409,155), (410,156), (411,156), (412,156), (413,156), (414,156), (415,156), (416,156), (417,156), (418,156), (419,156), (420,157), (421,157), (422,157), (423,157), (424,157), (425,157), (426,157), (427,157), (428,157), (429,157), (430,158), (431,158), (432,158), (433,158), (434,158), (435,158), (436,158), (437,158), (438,158), (439,158), (440,159), (441,159), (442,159), (443,159), (444,159), (445,159), (446,159), (447,159), (448,159), (449,159), (450,159), (451,159), (452,159), (453,159), (454,159), (455,159), (456,159), (457,159), (458,159), (459,159), (460,159), (461,159), (462,159), (463,159), (464,159), (465,159), (466,159), (467,159), (468,159), (469,159), (470,159))

#Dictionary mit Positionsdaten für Sehenswürdigkeiten
pos={}
pos['Käfigturm']=(200,280,120,150)
pos['Zytglogge']=(410,490,140,160)

##############################################
#######################################
# Hier kommt Ihre Code Anpassung

#Funktion
def check_text(x,y):
   ''' Prüfen ob eine Sehenswürdigkeit angezeigt werden soll'''

   if x>200 and x<280 and y>120 and y<150:
      text2show='Käfigturm'
      xt,yt=x,y
   elif x>410 and x<490 and y>140 and y<160:
      text2show='Zytglogge'
      xt,yt=x,y
   else:
      text2show,xt,yt='',x,y

   return text2show,xt,yt

#bis hier
#######################################
##############################################

#Start Game
while run:
    clock.tick(27)
    if d>0:

       for wg in zytglogge:
         gx,gy=wg
         time.sleep(slower)  #Laufgeschwindigkeit reduzieren
         x,y=go_walk_right(gx,gy)

         text2show,xt,yt=check_text(x,y)       #Prüfen ob eine Sehenswürdigkeit angezeigt werden soll
         redrawGameWindow(text2show,xt,yt-15)  #Grafik neu darstellen

    d-=1
    go_stop()
    run=check_key()  #Prüfen ob und welche Taste gedrückt wurde
    redrawGameWindow(text2show,xt,yt-15)  #Grafik neu darstellen 
    
#Ende Darstellung
pygame.quit()

