# Tour planen und auf dem Smartphone offline anzeigen

### Planung auf Outdooractive

* Plane die Tour auf Outdooractive (https://www.outdooractive.com/de/routeplanner/). **Achtung!** Erstelle noch während der Planung alle Wegpunkte, da nachträgliches Hinzufügen nicht zu funktionieren scheint.
* Speichere die Planung und erstelle eine Tour.
* Da die Outdooractive App in der kostenlosen Version nicht offline funktioniert, lade die Tour als gpx herunter.

### Track bearbeiten

Würde man den gpx-Track auf das Smartphone laden und ihn mit Locus Map öffnen, würden die erstellten Wegpunkte jedoch nicht angezeigt werden. Dies liegt daran, dass sie im gpx-File nicht als Wegpunkte, sondern als Trackpunkte gespeichert sind.

**Achtung!** Die im Folgenden beschriebene Bearbeitung kann statt von Hand auch mit Hilfe des Skripts ``trk2wpt.py`` durchgeführt werden.

* Um das zu ändern, öffne die Datei mit einem Text-Editor und kopiere alle Trackpunkte, die Wegpunkten entsprechen, hinter den Track, dessen Ende durch ``</trk>`` gekennzeichnet ist. Die entsprechenden Trackpunkte sehen folgendermaßen aus, d.h. sie haben einen Namen und noch ein paar andere Attribute, die die restlichen Trackpunkte nicht haben:

  ```xml
        <trkpt lat="49.883462" lon="9.955692">
          <ele>286.7</ele>
          <name>Parkplatz</name>
          <sym>waypointFlagComb</sym>
          <extensions>
            <oa:mapZoom>15</oa:mapZoom>
          </extensions>
        </trkpt>
  ```

* Wandle die kopierten Trackpunkte in Wegpunkte um. Ersetze dazu ``trkpt`` durch ``wpt``. Außerdem brauchen die Wegpunkte nur die Koordinaten, einen Namen und das Symbol, alles andere kann gelöscht werden. Der Wegpunkt sieht dann also folgendermaßen aus:

  ```xml
    <wpt lat="49.883462" lon="9.955692">
          <name>Parkplatz</name>
          <sym>waypointFlagComb</sym>
    </wpt>
  ```

### Anzeigen mit Locus Map

Kopiere den so modfizierten gpx-Track auf das Smartphone und öffne ihn mit Locus Map (https://play.google.com/store/apps/details?id=menion.android.locus&hl=de). Er wird nun mitsamt der Wegpunkte angezeigt.