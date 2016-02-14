#------------------------------------------------------------------------------
# dataio module
#   -- handles data input and output
#------------------------------------------------------------------------------
from entry import *
from team import *
from match import *
import model

#------------------------------------------------------------------------------
# import_data functions
#   -- takes data from the user and loads it into the database
#------------------------------------------------------------------------------
def import_data(Filename=""):

    model.imported = False

    # clear any and all old data so as to avoid two sets of conflicting data
    # until I find a way to simply make changes rather than rewrite everything
    Entry.entries = []
    Match.matches = []

    try:
        newData = open(Filename, "r")
        print "Data Opened"
    except:
        pass
        print "Error, could not open selected file."
    try:
        print
        for line in newData:
            if line == "end":
                print "END OF FILE"
                break
            try:
                newEntry = Entry(parse_data(line))
                print "New Entry Parsed"
            except:
                print "Match Data does not match format: skipping line..."
        print 
        print "Data Parsed"

        model.imported = True
    except:
        pass
        print "Error, could not parse data."

def import_pitData(Filename=""):

    model.pitImported = False
    
    PitEntry.entries = []

    try:
        newData = open(Filename, "r")
        print "File Opened"
    except:
        pass
        print "Error, could not open selected file."
    try:
        print "Parsing PitData"
        for line in newData:
            newPitEntry = PitEntry(parse_pitData(line))
        print "--PitData Parsed"

        model.pitImported = True
    except:
        print "Error, could not parse data."

def clear_importData():
    model.imported = False
    model.pitImported = False
    Entry.entries = []
    PitEntry.entries = []
    Match.matches = []
    Team.available = []
    Team.team_list = []

#------------------------------------------------------------------------------
# parse_data functions
#   -- takes each line of a file and transfers it into data ready for an entry
#------------------------------------------------------------------------------
def parse_data(info):
    data = []
    new = ""
    for character in info:
        if character != "\n" and character !="," and character != "$" and character != "\r":
            new += str(character)
        else:  
            try:
                data.append(new)
                new=""
            except:
                break
            if "\n" in character: break
            if "\r" in character: break
        
    return data

def parse_pitData(info):
    data = []
    new = ""
    for character in info:
        if character != "\n" and character !="$"and character != "\r":
            new += str(character)
        else:  
            try:
                data.append(new)
                new=""
            except:
                break
            if "\n" in character: break
            if "\r" in character: break
    return data

