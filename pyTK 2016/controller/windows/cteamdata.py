#------------------------------------------------------------------------------
# cteamdata module
#   -- contains the functions and classes for controlling the teamdata window
#------------------------------------------------------------------------------
from Tkinter import *

from model.team import *

#------------------------------------------------------------------------------
# TeamDataController Class
#   -- contains information for setting and getting data and display values
#------------------------------------------------------------------------------
class TeamDataController():
    """Class that handles commands from the teamdata window."""

    # use these to index values to display, use the system: ("key", "term")
    # where key corresponds to a value in team and term labels that value
    dataLabelVals = [("numMatch","Number of Matches: "),
                     ("pNoShow","No Show: "),
                     ("pDisabled","Disabled: "),
                     ("avgOff","Average Offensive Score: "),
                     ("avgDef","Average Defensive Score: "),
                     ("avgTotal","Average Total Score: "),
                     ("avgAutoScore","Average Auto Score: "),
                     ("pHadAuto","Had Auto Mode: "),
                     ("pReachesDefences","Matches Reached Defences: "),
                     ("pCrossesDefences","Matches Crossesed Defences: "),
                     ("pStartsAsSpybot","Matches Started as Spybot: "),
                     ("avgAutoReachesDefencesScores","Average Auto Reaches Defences Score: "),
                     ("avgAutoCrossesDefencesScores","Average Auto Crosses Defences Score: "),
                     ("avgAutoLowGoal","Average Auto Boulders Scored In Low Goal: "),
                     ("avgAutoHighGoal","Average Auto Boulders Scored In High Goal: "),
                     ("pAutoOther","Matches Had Other: "),
                     ("avgTeleScore","Average Tele Score: "),
                     ("pTeleLowBar","Percent Team Crossed Low Bar out of Total Defences Crossed: "),
                     ("pTeleLowBarM","Number of Times Team Crossed Low Bar per Match: "),
                     ("pTelePortcullis","Percent Team Crossed Portcullis out of Total Defences Crossed: "),
                     ("pTelePortcullisM","Number of Times Team Crossed Portcullis per Match: "),
                     ("pTeleChevaldeFrise","Percent Team Crossed Cheval de Frise out of Total Defences Crossed: "),
                     ("pTeleChevaldeFriseM","Number of Times Team Crossed Cheval de Frise per Match: "),
                     ("pTeleMoat","Percent Team Crossed Moat out of Total Defences Crossed: "),
                     ("pTeleMoatM","Number of Times Team Crossed Moat per Match: "),
                     ("pTeleRamparts","Percent Team Crossed Ramparts out of Total Defences Crossed: "),
                     ("pTeleRampartsM","Number of Times Team Crossed Ramparts per Match: "),
                     ("pTeleDrawbridge","Percent Team Crossed Drawbridge out of Total Defences Crossed: "),
                     ("pTeleDrawbridgeM","Number of Times Team Crossed Drawbridge per Match: "),
                     ("pTeleSallyPort","Percent Team Crossed Sally Port out of Total Defences Crossed: "),
                     ("pTeleSallyPortM","Number of Times Team Crossed Sally Port per Match: "),
                     ("pTeleRoughTerrain","Percent Team Crossed Rough Terrain out of Total Defences Crossed: "),
                     ("pTeleRoughTerrainM","Number of Times Team Crossed Rough Terrain per Match: "),
                     ("pTeleRockWall","Percent Team Crossed Rock Wall out of Total Defences Crossed: "),
                     ("pTeleRockWallM","Number of Times Team Crossed Rock Wall per Match: "),
                     ("avgTeleDefencesDamageScore","Average Damage on Defences Score: "),
                     ("avgTeleLowGoal","Average Boulders Scored In Low Goal: "),
                     ("avgTeleHighGoal","Average Boulders Scored In High Goal: "),
                     ("pTeleShootingPercentage","Percent of Boulders made in High Goal: "),
                     ("avgFoulScore","Average Number of Points taken off by Fouls per Match: "),
                     ("avgPostFoul","Average Number of Fouls per Match: "),
                     ("pFoul","Matches Had Foul: "),
                     ("pYellow","Matches Had Yellow Card: "),
                     ("pRed","Matches Had Red Card: "),
                     ("pPlayedDefensively","Matches Played Defensive: "),
                     ("pPlayedAssistively","Matches Played Assistive: "),
                     ("pCaptured","Matches Had Captured: "),
                     ("pBreached","Matches Had Breached: "),
                     ("avgPostChallengeStateScores","Average Challenge State Score: "),
                     ("pChallengeStateNotAttempted","Matches Challenge State Was Not Attempted: "),
                     ("pChallengeStateAttempted","Matches Challenge State Attempted: "),
                     ("pChallengeStateSuccessful","Matches Challenge State Succesful: "),
                     ("avgPostScaleStateScores","Average Scale State Score: "),
                     ("pScaleStateNotAttempted","Matches Scale State Not Attempted: "),
                     ("pScaleStateAttempted","Matches Scale State Attempted: "),
                     ("pScaleStateSuccessful","Matches Scale State Succesful: ")]

    maxminLabelVals = [("maxOffScore","Maximum Offensive Score: "),("minOffScore","Minimum Offensive Score: "),
                       ("maxDefScore","Maximum Defensive Score: "),("minOffScore","Minimum Defensive Score: "),
                       ("maxTotalScore","Maximum Total Score: "),("minTotalScore","Minimum Total Score: "),
                       ("maxAutoScore","Maximum Auto Score: "),("minAutoScore","Minimum Auto Score: "),
                       ("maxAutoCrossesDefencesScores","Maximum Auto Crosses Defences Score: "),("minAutoCrossesDefencesScores","Minimum Auto Crosses Defences Score: "),
                       ("maxAutoLowGoal","Maximum Auto Boulders in Low Goal Score: "),("minAutoLowGoal","Minimum Auto Boulders in Low Goal Score: "),
                       ("maxAutoHighGoal","Maximum Auto Boulders in High Goal Score: "),("minAutoHighGoal","Minimum Auto Boulders in High Goal Score: "),
                       ("maxTeleScore","Maximum Tele Score: "),("minTeleScore","Minimum Tele Score: "),
                       ("maxTeleDefencesDamageScore","Maximum Tele Defences Damage Score: "),("minTeleDefencesDamageScore","Minimum Tele Defences Damage Score: "),
                       ("maxTeleLowGoal","Maximum Tele Boulders in Low Goal Score: "),("minTeleLowGoal","Minimum Tele Boulders in Low Goal Score: "),
                       ("maxTeleHighGoal","Maximum Tele Boulders in High Goal Score: "),("minTeleHighGoal","Minimum Tele Boulders in High Goal Score: "),     
                       ("maxFoulScore","Maximum Foul Score: "),("minFoulScore","Minimum Foul Score: ")]
    
    pitDataStrings = [("answer1","How experienced are your drivers?: "),
                      ("answer2","How many cycles can you do?: "),
                      ("answer3","Can you play defensively?: "),
                      ("answer4","Does the robot shoot in the low goal or high goal?: "),
                      ("answer5","Where do you prefer to shoot?: "),
                      ("answer6","Do you have an autonomous, if so which defence do you start in front of?: ")]
                       

    graphVals = [("avgOff","Scores","oScores"),
                 ("avgTotal","Scores","tScores"),
                 ("avgAutoScore","Scores","autoScores"),
                 ("avgAutoReachesDefencesScores","Scores","autoReachesDefencesScores"),
                 ("avgAutoCrossesDefencesScores","Scores","autoCrossesDefencesScores"),
                 ("avgAutoLowGoal","Info","autoLowGoal"),
                 ("avgAutoHighGoal","Info","autoHighGoal"),
                 ("avgTeleScore","Scores","teleScores"),
                 ("pTeleLowBarM","Info","teleLowBarDamage"),
                 ("pTelePortcullisM","Info","telePortcullisDamage"),
                 ("pTeleChevaldeFriseM","Info","teleChevaldeFriseDamage"),
                 ("pTeleMoatM","Info","teleMoatDamage"),
                 ("pTeleRampartsM","Info","teleRampartsDamage"),
                 ("pTeleDrawbridgeM","Info","teleDrawbridgeDamage"),
                 ("pTeleSallyPortM","Info","teleSallyPortDamage"),
                 ("pTeleRockWallM","Info","teleRockWallDamage"),
                 ("pTeleRoughTerrainM","Info","teleRoughTerrainDamage"),
                 ("avgTeleDefencesDamageScore","Scores","teleDefencesDamageScore"),
                 ("avgTeleLowGoal","Info","teleLowGoal"),
                 ("avgTeleHighGoal","Info","teleHighGoal"),
                 ("avgPostChallengeStateScores","Scores","teleChallengStateScore"),
                 ("avgPostScaleStateScores","Scores","teleScaleStateScore"),
                 ("avgFoulScore","Scores","foulScores"),
                 ("avgPostFoul","Info","postFouls")]
    
    def __init__(self):
        self.teamNum = 0
        self.entry = None
        self.data = None
        self.image = None

    # gets the team # from self.entry and finds the corresponding team
    # returns true if the team was found and false if not
    def loadData(self):
        try:
            self.teamNum = int(self.entry.get())
        except:
            print "Team value not valid."
            self.teamNum = 0
            
        for team in Team.team_list:
            if team.number == self.teamNum:
                self.data = team
                print "Loading team..."
                return True
            
        print "Team not found."
        return False

    # gets the image file corresponding to self.teamNum and returns it
    # if team is not found: returns nopic.gif
    def get_PhotoImage(self):
        image_name = "Images/" + str(self.teamNum) + ".gif"
        try:
            open(image_name)
        except:
            self.image = PhotoImage(file="Images/nopic.gif")
            return self.image
        
        self.image = PhotoImage(file=image_name)
        return self.image

    def get_GraphData(self, graphType=None):
        index = None
        data = None
        try:
            graphName = self.dataLabelVals[int(graphType[0])][0]  
        except:
            graphName = None

        #find the index and attr name
        for x, y, z in self.graphVals:
            if x == graphName:
                index = y
                data = z
                break # do not continue to iterate through the list
        try:
            currentIndex = self.data.getAttr(index)
            return currentIndex.getAttr(data)
        except:
            print "Cannot find data for that graph."
            return None
