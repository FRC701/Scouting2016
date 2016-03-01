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
                        ("avgAutoReachesDefencesScores","Auto Reaches Defences Score >= "),
                        ("avgAutoCrossesDefencesScores","Auto Crosses Defences Score >= "),
                        ("avgAutoLowGoal","Auto Boulders in Low Goal >= "),
                        ("avgAutoHighGoal","Auto Boulders in High Goal >= ")]
                        

    entryItemTelePost = [("avgTeleScore","Tele Score >= "),
                         ("pTelePortcullisM","Percent Crossed Portcullis per Match >= "),
                         ("pTeleChevaldeFriseM","Percent Crossed Cheval de Frise per Match >= "),
                         ("pTeleMoatM","Percent Crossed Moat per Match >= "),
                         ("pTeleRampartsM","Percent Crossed Ramparts per Match >= "),
                         ("pTeleDrawbridgeM","Percent Crossed Drawbridge per Match >= "),
                         ("pTeleSallyPortM","Percent Crossed Sally Port per Match >= "),
                         ("pTeleRoughTerrainM","Percent Crossed Rough Terrain per Match >= "),
                         ("pTeleRockWallM","Percent Crossed Rock Wall per Match >= "),
                         ("avgTeleDefencesDamageScore","Average Damage on Defences Score >= "),
                         ("avgTeleLowGoal","Average Boulders Scored In Low Goal >= "),
                         ("avgTeleHighGoal","Average Boulders Scored In High Goal >= "),
                         ("avgFoulScore","Foul Score <= ")]
    
    checkItemTypes = [("autoHadAuto","Had Autonomous"),
                      ("autoStartsAsSpybot","Starts as Spybot"),
                      ("autoOther","Had Other Autonomous"),
                      ("scoredInTele","Scored in Tele"),
                      ("postPlayedDefensively","Played Defensively"),
                      ("postPlayedAssistively","Played Assistively"),
                      ("NotAttemptedC","Challenge Not Attempted"),
                      ("AttemptedC","Challenge Attempted"),
                      ("SuccessfulC","Challenge Successful"),
                      ("NotAttemptedS","Scale Not Attempted"),
                      ("AttemptedS","Scale Attempted"),
                      ("SuccessfulS","Scale Successful"),
                      ("postNoShow","Always Showed Up"),
                      ("postDisabled","Never Disabled"),
                      ("hasFoul","No Fouls"),
                      ("postYellowCard","No Yellow Cards"),
                      ("postRedCard","No Red Cards")]
                    
    def searchGreater(self, value=None, index=None):
        try:
            self.matchedList = filter(lambda team:team.getAttr(index)>=float(value.get()), self.matchedList)
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
                "avgAutoReachesDefencesScores":searchGreater,
                "avgAutoCrossesDefencesScores":searchGreater,
                "avgAutoLowGoal":searchGreater,
                "avgAutoHighGoal":searchGreater,
                "autoHadAuto":searchHas,
                "autoStartsAsSpybot":searchHas,
                "scoredInAuto":searchHas,
                "autoOther":searchHas,
                "avgTeleScore":searchGreater,
                "pTelePortcullis":searchGreater,
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
                "postHadRed":searchNever,
                "NotAttemptedC":searchHas,
                "AttemptedC":searchHas,
                "SuccessfulC":searchHas,
                "NotAttemptedS":searchHas,
                "AttemptedS":searchHas,
                "SuccessfulS":searchHas}

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
        
