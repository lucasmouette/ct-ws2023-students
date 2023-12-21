'''
13. Python Module und Pakete
Seite 2.4

Aufgabe:

Erstellen Sie mit VS Code ein Python Skript mit dem Namen mein_erstes_skript.py.

Das Skript soll eine Funktion welcome() enthalten, welche den Nutzer nach seinem Namen fragt und diesen begrüßt. Die Funktion soll den Namen zurückliefern.
Rufen Sie die Funktion im Skript aus.
Testen Sie das Skript.
'''

# numpy wird oft so importiert: import numpy as np

import mein_erstes_modul as mm
# man könnte auch: from mein_erstes_modul import *
# hat aber folgenden Nachteil: Kann hier zu Namenskoallitionen zwischen Funktionen kommen 

mm.welcome()
