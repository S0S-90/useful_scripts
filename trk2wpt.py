### script to make waypoints marked in outdooractive visible in locus map
### see also tourenplanung.md

# USER INPUT

INP_FILE = "t183809435_wanderung gramschatzer.gpx" # name of the input file
OUT_FILE = "wanderung_gramschatzer_wald.gpx"       # name of the output file


# PROGRAM

import xml.etree.ElementTree as ElementTree
import re

# class for waypoints
class Waypoint:
    def __init__(self, name, sym, coords):
        self.name = name
        self.coords = coords
        self.symbol = sym
    def __str__(self):
        return "{}: {}".format(self.name, self.coords)

# read xml tree and get namespace 
tree = ElementTree.parse(INP_FILE)
root = tree.getroot()
namespace = root.tag[:-3] # root.tag ends with "gpx"

# get all trackpoints
track = root.find("{}trk".format(namespace))
trkseg = track.find("{}trkseg".format(namespace))
trackpoints = trkseg.findall("{}trkpt".format(namespace))

# find and create waypoints out of trackpoints
waypoints = []
for trkpt in trackpoints: # go through all trackpoints
    name = trkpt.find("{}name".format(namespace))
    # if trackpoint has a name and this name does not only consist of coordinates
    if name != None and re.match("-?\d*\.\d*,-?\d\.\d*" , name.text) == None: 
        sym = trkpt.find("{}sym".format(namespace))
        waypoints.append(Waypoint(name.text, sym.text, trkpt.attrib)) # create waypoint

# for every waypoint create a wpt element in the xml tree
for wpt in waypoints:
    element = ElementTree.Element('wpt', attrib=wpt.coords)
    root.append(element)
    name = ElementTree.SubElement(element, "name")
    name.text = wpt.name
    sym = ElementTree.SubElement(element, "sym")
    sym.text = wpt.symbol

# write modified xml in new gpx file
ElementTree.register_namespace("", namespace[1:-1]) # do not add a namespace (namespace here without {})
tree = ElementTree.ElementTree(root)
with open(OUT_FILE, "wb") as new_gpx:
    tree.write(new_gpx, encoding = 'utf-8', xml_declaration=True)
