#------------------------------------------------------------------------------
# csearch module
#   -- contains data and information for controlling the search window
#------------------------------------------------------------------------------
from Tkinter import *

from model import team

#------------------------------------------------------------------------------
# SearchController class
#   -- contains functions, lists, data, etc, for handling the search window
#------------------------------------------------------------------------------
class SearchController():
    """Class that handles commands from the search window."""

    entryItemGenAuto = [("avgOff","Offensive Score >= "),
                        ("avgDef","Defensive Score >= "),
                        ("avgTotal","Total Score >= "),
                        ("avgAutoScore","Auto Score >= "),
                        ("pReachesDefences","Matches Reached Defences >= "),
                        ("pCrossesDefences","Matches Crossesed Defences >= "),
                        ("avgAutoReachesDefencesScore","Auto Reaches Defences Score >= "),
                        ("avgAutoCrossesDefencesScore","Auto Crosses Defences Score >= "),
                        ("avgAutoLowGoalScore","Auto Boulders in Low Goal Score >= "),
                        ("avgAutoHighGoalScore","Auto Boulders in High Goal Score >= ")]
                        

    entryItemTelePost = [("avgTeleScore","Tele Score >= "),
                         ("pTelePortcullis","Portcullis Crossed Percent >= "),
                         ("pTelePortcullisM","Percent Crossed Portcullis per Match >= "),
                         ("pTeleChevaldeFrise","Percent Crossed Cheval de Frise >= "),
                         ("pTeleChevaldeFriseM","Percent Crossed Cheval de Frise per Match >= "),
                         ("pTeleMoat","Percent Crossed Moat >= "),
                         ("pTeleMoatM","Percent Crossed Moat per Match >= "),
                         ("pTeleRamparts","Percent Crossed Ramparts: "),
                         ("pTeleRampartsM","Percent Crossed Ramparts per Match >= "),
                         ("pTeleDrawbridge","Percent Crossed Drawbridge >= "),
                         ("pTeleDrawbridgeM","Percent Crossed Drawbridge per Match >= "),
                         ("pTeleSallyPort","Percent Crossed Sally Port >= "),
                         ("pTeleSallyPortM","Percent Crossed Sally Port per Match >= "),
                         ("pTeleRoughTerrain","Percent Crossed Rough Terrain >= "),
                         ("pTeleRoughTerrainM","Percent Crossed Rough Terrain per Match >= "),
                         ("pTeleRockWall","Percent Crossed Rock Wall >= "),
                         ("pTeleRockWallM","Percent Crossed Rock Wall per Match >= "),
                         ("avgTeleDefencesDamageScore","Average Damage on Defences Score >= "),
                         ("avgTeleLowGoal","Average Boulders Scored In Low Goal >= "),
                         ("avgTeleHighGoal","Average Boulders Scored In High Goal >= "),
                         ("avgFoulScore","Foul Score <= ")]
    
    checkItemTypes = [("autoHadAuto","Had Autonomous"),
                      ("autoOther","Had Other Autonomous"),
                      ("scoredInTele","Scored in Tele"),
                      ("postNoShow","Always Showed Up"),
                      ("postDisabled","Never Disabled"),
                      ("hasFoul","No Fouls"),
                      ("postYellowCard","No Yellow Cards"),
                      ("postRedCard","No Red Cards")]
                    
    def searchGreater(self, value=None, index=None):
        try:
            self.matchedList = filter(lambda team:team.getAttr(index)>=int(value.get()), self.matchedList)
        except:
             print "Invalid Search Parameter " + str(value.get()) + " for " + str(index)
             value.set(0)

    def searchLess(self, value=None, index=None):
        try:
            self.matchedList = filter(lambda team:team.getAttr(index)<=int(value.get()), self.matchedList)
        except:
             print "Invalid Search Parameter " + str(value.get()) + " for " + str(index)
             value.set(999)

    def searchHas(self, value=None, index=None):
        try:
            if value.get() == 1:
                self.matchedList = filter(lambda team:team.Info.getAttr(index) >= 1, self.matchedList)
        except:
            value.set(0)

    def searchNever(self, value=None, index=None):
        try:
            if value.get() == 1:
                self.matchedList = filter(lambda team:team.Info.getAttr(index) == 0, self.matchedList)
        except:
            value.set(0)

    
    Searches = {"avgOff":searchGreater,
                "avgDef":searchGreater,
                "avgTotal":searchGreater,
                "avgAutoScore":searchGreater,
                "pReachesDefences":searchGreater,
                "pCrossesDefences":searchGreater,
                "avgAutoReachesDefencesScore":searchGreater,
                "avgAutoCrossesDefencesScore":searchGreater,
                "avgAutoLowGoalScore":searchGreater,
                "avgAutoHighGoalScore":searchGreater,
                "autoHadAuto":searchHas,
                "scoredInAuto":searchHas,
                "autoOther":searchHas,
                "avgTeleScore":searchGreater,
                "pTelePortcullis":searchGreater,
                "pTeleContainerScore":searchGreater,
                "pTelePortcullisM":searchGreater,
                "pTeleChevaldeFrise":searchGreater,
                "pTeleChevaldeFriseM":searchGreater,
                "pTeleMoat":searchGreater,
                "pTeleMoatM":searchGreater,
                "pTeleRamparts":searchGreater,
                "pTeleRampartsM":searchGreater,
                "pTeleDrawbridge":searchGreater,
                "pTeleDrawbridgeM":searchGreater,
                "pTeleSallyPort":searchGreater,
                "pTeleSallyPortM":searchGreater,
                "pTeleRoughTerrain":searchGreater,
                "pTeleRoughTerrainM":searchGreater,
                "pTeleRockWall":searchGreater,
                "pTeleRockWallM":searchGreater,
                "avgTeleDefencesDamageScore":searchGreater,
                "avgTeleLowGoal":searchGreater,
                "avgTeleHighGoal":searchGreater,
                "avgTeleLitterToLandfill":searchGreater,
                "scoredInTele":searchHas,
                "avgFoulScore":searchLess,
                "postDisabled":searchNever,
                "noShow":searchNever,
                "hasFoul":searchNever,
                "postHadYellow":searchNever,
                "postHadRed":searchNever}

    def search(self):
        self.matchedList = team.Team.team_list

        for index, value in self.searchVariables:
            if index in self.Searches:
                self.Searches[index](self,value,index)

    def addWanted(self,number=None):
        for t in team.Team.team_list:
            if t.number == int(number) and t not in team.Team.wanted:
                team.Team.wanted.append(t)
                break

        self.wantedList = team.Team.wanted

    def subWanted(self,number=None):
        for t in team.Team.wanted:
            if t.number == int(number):
                team.Team.wanted.remove(t)
                break

        self.wantedList = team.Team.wanted

    def sortWanted(self,rList=None):
        newList = []
        for item in rList:
            for t in team.Team.team_list:
                if t.number == int(item):
                    newList.append(t)
                    break
                    
        team.Team.wanted = newList
        self.wantedList = team.Team.wanted
        
    def __init__(self):
        self.matchedList = team.Team.team_list
        self.searchVariables = []
        self.wantedList = team.Team.wanted
        
