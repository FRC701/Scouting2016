#------------------------------------------------------------------------------
# team Module
#   -- Keeps track of valuable team information and scorings
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# TeamInfo Class
#   -- Stores performance information
#------------------------------------------------------------------------------
class _TeamInfo(object):
    """Used to handle information for different teams."""

    def __init__(self):
        self.matches = []                   # list holding the matches the team was in
        self.noShow = 0                     # number of matches for which the team didn't show up
        
        self.autoHadAuto = 0                # number of matches for which the team had autonomous
        self.autoReachesDefences = 0
        self.autoCrossesDefences = 0
        self.autoDefences1 = []
        self.autoDefences2 = []
        self.autoBouldersInLowGoal = []
        self.autoBouldersInHigh = []
        self.autoOther = 0                  # number of matches for which the team did something else in auto

        self.teleLowBar = []
        self.teleDamageCounter1 = []
        self.teleDefences1 = []
        self.teleDamagecounter2 = []
        self.teleDefences2 = []
        self.teleDamageCounter3 = []
        self.teleDefences3 = []
        self.teleDamageCounter4 = []
        self.teleDefences4 = []
        self.teleDamageCounter5 = []
        self.teleBouldersInLowGoal = []
        self.teleBouldersInHighGoal = []
        self.teleBouldersInLowGoal = []
        self.teleBouldersInHighGoal = []

        self.postFouls = []                 # list containing the number of fouls each match
        self.postTechFouls = []
        self.postRedCard = 0                # number of matches for which robot received red card
        self.postYellowCard = 0             # number of matches for which robot received yellow card
        self.postDisabled = 0               # number of matches for which robot was disabled
        self.postplayedDefensively = 0
        self.postCaptured = 0
        self.postBreached = 0
        self.postChallengeState = []
        self.postScaleState = []

        self.scoredInTele = 0               # number of matches for which the robot scored in tele-op
        self.scoredInAuto = 0               # number of matches for which the robot scored in auto
        self.hasFoul = 0                    # number of matches for which the robot received a foul

    def get_info(self):
        self.avgAutoBoulderInLowGoal = float(sum(self.autoBouldersInLowGoal))/float(len(self.autoBouldersInLowGoal)) if len(self.autoBouldersInLowGoal) else 0
        self.avgAutoBouldersInHighGoal = float(sum(self.autoBoulderInHighGoal))/float(len(self.autoBouldersInHighGoal)) if len(self.autoBouldersInHIghGoal) else 0

        self.avgTeleBouldersInLowGoal = float(sum(self.teleBouldersInLowGoal))/float(len(self.teleBouldersInLowGoal)) if len(self.teleBouldersInLowGoal) else 0
        self.avgTeleBouldersInHighGoal = float(sum(self.teleBOuldersInHighGoal))/float)(len(self.teleBouldersInHighGoal)) if len(self.teleBouldersInHighGoal) else 0
        
        self.avgPostFoul = sum(self.postFouls)/len(self.postFouls) if len(self.postFouls) else 0
        self.avgPostTechFoul = sum(self.postTechFoul)/len(self.postTechFouls) if len(self.postTechFouls) else 0 
                
    def getAttr(self, source):
        return getattr(self, source)

#------------------------------------------------------------------------------
# TeamScores Class
#   -- stores data about a team's scores
#------------------------------------------------------------------------------
class _TeamScores(object):
    """Used to handle scoring data for different teams."""

    def __init__(self):
        self.oScores = []               # list holding offensive scores
        self.tScores = []               # list holding total scores
        self.autoScores = []            # list holding auto scores
        self.autoLowGoal = []
        self.autoHighGoal = []
        self.teleScores = []            # list holding tele scores
        self.teleDefencesDamageScore = []
        self.teleLowGoal = []
        self.teleHighGoal = []
        self.foulScores = []            # list holding foul scores
        
    def get_maxmin_scores(self):
        self.maxOffScore = max(self.oScores)
        self.minOffScore = min(self.oScores)
        self.maxTotalScore = max(self.tScores)
        self.minTotalScore = min(self.tScores)
        self.maxAutoScore = max(self.autoScores)
        self.minAutoScore = min(self.autoScores)
        self.maxAutoLowGoal = max(self.autoLowGoal)
        self.minAutoLowGoal = min(self.autoLowGoal)
        self.maxAutoHighGoal = max(self.autoHighGoal)
        self.minAutoHighGoal = min(self.autoHighGoal)
        self.maxTeleScore = max(self.teleScores)
        self.minTeleScore = min(self.teleScores)
        self.maxTeleDefencesDamageScore = max(self.teleDefencesDamageScore)
        self.minTeleDefencesDamageScore = min(self.teleDefencesDamageScore)
        self.maxTeleLowGoal = max(self.teleLowGoal)
        self.minTeleLowGoal = min(self.teleLowGoal)
        self.maxTeleHighGoal = max(self.teleHighGoal)
        self.minTeleHighGoal = min(self.teleHighGoal)
        self.maxFoulScore = max(self.foulScores)
        self.minFoulScore = min(self.foulScores)

    def get_avg_scores(self, matches=1, auto=0):
        self.avgOffScore = sum(self.oScores)/matches if matches else 0
        self.avgAutoScore = sum(self.autoScores)/auto if auto else 0
        self.avgAutoLowGoal = sum(self.autoLowGoal)/auto if auto else 0
        self.avgAutoHighGoal = sum(self.autoHighGoal)/auto if auto else 0
        self.avgTeleScore = sum(self.teleScores)/matches if matches else 0
        self.avgTeleDefencesDamageScore = sum(self.teleDefencesDamageScore)/matches if matches else 0
        self.avgTeleLowGoal = sum(self.teleLowGoal)/matches if matches else 0
        self.avgTeleHighGoal = sum(self.teleHighGoal)/matches if matches else 0
        self.avgFoulScore = sum(self.foulScores)/matches if matches else 0
        self.avgTotalScore = sum(self.tScores)/matches if matches else 0

    def getAttr(self, source):
        return getattr(self, source)

#------------------------------------------------------------------------------
# TeamRankings class
#   -- place to store ranking lists, for viewing team ranks
#------------------------------------------------------------------------------
class TeamRankings(object):
    """Used to keep track of rankings for each team."""

    off_rank = []
    auto_rank = []
    auto_Low_Goal_rank = []
    auto_High_Goal_rank = []
    tele_rank = []
    tele_Defences_Damage_rank = []
    tele_Low_Goal_rank = []
    tele_High_Goal_rank = []
    foul_rank = []
    tot_rank = []
    
    def __init__(self):
        print
        # no non-static class variables
        # team cannot track its own ranking:
            # rankings are defined by the user
            # rankings are dynamic, constantly changing to user request

    def getAttr(self, source):
        return getattr(self, source)

#------------------------------------------------------------------------------
# Team Class
#   -- stores and recalls team specific data
#------------------------------------------------------------------------------
class Team(object):
    """Store and recall data on a team from here."""

    team_list = []  # list holding all the teams currently loaded in the database
    available = []  # list holding all the teams not currently selected
    wanted = []     # list holding all the teams in our wanted list
    
    def __init__(self, num):
        self.number = num
        self.Info = _TeamInfo()
        self.Scores = _TeamScores()
        self.team_list.append(self)
        self.available.append(self)

        # a few of the final details predefined so as to satisfy predictions with null teams
        self.avgOff = 0
        self.pOff = 0
        
    def get_details(self): # gets all of the information for the team
        self.Info.get_info()
        self.Scores.get_avg_scores(len(self.Info.matches),self.Info.autoHadAuto)
        self.Scores.get_maxmin_scores()

        matches = self.Info.matches
        self.numMatch = len(matches)
        self.pNoShow  = str(int(100*self.Info.noShow)/len(matches)) + "%"
        self.pDisabled = str(int(100*self.Info.postDisabled)/len(matches)) + "%"
        self.avgOff = round(self.Scores.avgOffScore,2)
        self.avgTotal = round(self.Scores.avgTotalScore,2)

        self.pHadAuto = str(int(100*self.Info.autoHadAuto)/len(matches)) + "%"
        self.pReachesDefences = str(int(100*self.Info.autoReachesDefences)/len(matches)) + "%"
        self.pCrossesDefences = str(int(100*self.Info.autoCrossesDefences)/len(matches)) + "%"
        self.avgAutoScore = round(self.Scores.avgAutoScore,2)
        self.avgAutoLowGoal = round(self.Scores.avgAutoLowGoal,2)
        self.avgAutoHighGoal = round(self.Scores.avgAutoHighGoal,2)
        self.pAutoOther = str(int(100*self.Info.autoOther)/len(matches)) + "%"
        
        self.avgTeleScore = round(self.Scores.avgTeleScore,2)
        self.avgTeleDefencesDamageScore = round(self.Scores.avgTeleDefencesDamageScore, 2)
        self.avgTeleLowGoal = round(self.Scores.avgTeleLowGoal,2)
        self.avgTeleHighGoal = round(self.Scores.avgTeleHighGoal,2)
       
        self.avgFoulScore = round(self.Scores.avgFoulScore,2)
        self.avgPostFoul = round(self.Info.avgPostFoul,2)
        self.pFoul = str(int(100*self.Info.hasFoul)/len(matches)) + "%"
        self.pYellow = str(int(100*self.Info.postYellowCard)/len(matches)) + "%"
        self.pRed = str(int(100*self.Info.postRedCard)/len(matches)) + "%"
        self.pPlayedDefensively = str(int(100*self.Info.postPlayedDefensively)/len(matches)) + "%"
        self.pCaptured = str(int(100*self.Info.postCaptured)/len(matches)) + "%"
        self.pBreached = str(int(100*self.Info.postBreached)/len(matches)) + "%"

    def getAttr(self, source):
        return getattr(self, source)
