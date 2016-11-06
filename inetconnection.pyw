from __future__ import division

import Tkinter
import datetime
import urllib

def connected():     # prueft, ob Internetverbindung vorhanden (google.de erreichbar)
    try:
        urllib.urlopen("http://www.google.de")
    except IOError:
        return False
    else:
        return True
        
    
class Programmdurchlauf(object):

    def __init__(self, logdatei):

        self._stop = False
        self._logdatei = logdatei
        
        with open(self._logdatei, "a") as datei:    # schreibt Datum und Uhrzeit des Programmstarts in Datei, ausserdem, ob Internetverbindung vorhanden
            jetzt = datetime.datetime.now()
            datei.write(jetzt.strftime("%d.%m.%Y\n"))
            self._inet = connected()
            if self._inet:
                datei.write(jetzt.strftime("%H:%M:%S - Internet da\n"))
                self._online = 1
                self._offline = 0
            else:
                datei.write(jetzt.strftime("%H:%M:%S - Internet weg\n"))
                self._online = 0
                self._offline = 1

    def gui_erstellen(self):            # erstellt die GUI
        self._root = Tkinter.Tk()                             
        self._root.title("inetconnection")
        self._stop_button = Tkinter.Button(self._root, text="Quit", command = self.ende)
        self._start_button = Tkinter.Button(self._root, text="Start", command = self.check_inet_connection)
        self._start_button.pack()
        self._stop_button.pack()
        self._label = Tkinter.Label(self._root, text="bitte auf Start klicken")
        self._label.pack()
        self._root.mainloop()
        
    def check_inet_connection(self):    # prueft jede Minute die Internetverbindung, schreibt bei Aenderung Ergebnis in Datei und zaehlt Online- und Offline-Minuten
        if not self._stop:
            self._label.config(text = "Programm lauft...")
            with open(self._logdatei, "a") as datei:
                jetzt = datetime.datetime.now()
                inet_neu = connected()
                if inet_neu:
                    if inet_neu != self._inet:
                        datei.write(jetzt.strftime("%H:%M:%S - Internet da\n"))
                    self._online = self._online + 1
                else:
                    if inet_neu != self._inet:
                        datei.write(jetzt.strftime("%H:%M:%S - Internet weg\n"))
                    self._offline = self._offline + 1
                self._inet = inet_neu
            self._root.after(60000, self.check_inet_connection)

    def ende(self):          # beendet die Schleife zur Pruefung der Interntverbindung, schreibt gesamte Online- und Offline-Zeit in Datei
        self._stop = True
        jetzt = datetime.datetime.now()
        with open(self._logdatei, "a") as datei:
            datei.write(jetzt.strftime("%H:%M:%S - Ende\n"))
            self._onlineprozent = round(self._online / (self._online + self._offline) * 100, 1)
            self._offlineprozent = round(self._offline / (self._online + self._offline) * 100, 1)
            datei.write("online: {} Minuten ({}%), offline: {} Minuten ({}%)\n".format(self._online, self._onlineprozent, self._offline, self._offlineprozent))
        self._label.config(text = "Programm kann geschlossen werden")


def main():
    a = Programmdurchlauf("inetconnection.txt")
    a.gui_erstellen()


if __name__ == "__main__":
    main()
