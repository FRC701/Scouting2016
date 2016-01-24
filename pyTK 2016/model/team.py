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
        self.numOff = 0                     # the number of matches for which the team played offensively
        self.numDef = 0                     # the number of matches for which the team played defensively
        self.noShow = 0                     # number of matches for which the team didn't show up
        
        self.autoHadAuto = 0                # number of matches for which the team had autonomous
        self.autoReachesDefences = 0
        self.autoCrossesDefences = 0
        self.autoDefences1 = []
        self.autoDefences2 = []
        self.autoLowGoal = []
        self.autoHigh = []
        self.autoOther = 0                  # number of matches for which the team did something else in auto

        self.teleHadTele = 0
        self.teleLowBar = []
        self.telePortcullis = []
        self.teleChevaldeFrise = []
        self.teleRamparts = []
        self.teleMoat = []
        self.teleDrawbridge = []
        self.teleSallyPort = []
        self.teleRoughTerrain = []
        self.teleRockWall = []
        self.teleLowGoal = []
        self.teleHighGoal = []
        self.teleFromLowGoal = []
        self.teleFromHighGoal = []

        self.postFouls = []                 # list containing the number of fouls each match
        self.postTechFouls = []
        self.postRedCard = 0                # number of matches for which robot received red card
        self.postYellowCard = 0             # number of matches for which robot received yellow card
        self.postDisabled = 0               # number of matches for which robot was disabled
        self.postplayedDefensively = 0
        self.postCaptured = 0
        self.postBreached = 0
        self.postChallengeState = []
        self.NotAttempedC = 0
        self.AttemptedC = 0
        self.SuccessfulC = 0
        self.postScaleState = []
        self.NotAttemptedS = 0
        self.AttemptedS = 0
        self.SuccessfulS = 0

        self.scoredInTele = 0               # number of matches for which the robot scored in tele-op
        self.scoredInAuto = 0               # number of matches for which the robot scored in auto
        self.hasFoul = 0                    # number of matches for which the robot received a foul

    def get_info(self):
        self.avgAutoLowGoal = float(sum(self.autoLowGoal))/float(len(self.autoLowGoal)) if len(self.autoLowGoal) else 0
        self.avgAutoHighGoal = float(sum(self.autoHighGoal))/float(len(self.autoHighGoal)) if len(self.autoHighGoal) else 0

        self.avgTeleLowGoal = float(sum(self.teleLowGoal))/float(len(self.teleLowGoal)) if len(self.teleLowGoal) else 0
        self.avgTeleHighGoal = float(sum(self.teleHighGoal))/float(len(self.teleHighGoal)) if len(self.teleHighGoal) else 0
        
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
        self.dScores = []           # list holding defensive scores
        self.tScores = []               # list holding total scores
        self.wScores = []           # list holding weighted  scores
        self.woScores = []          # list holding weighted offensive scores
        self.wdScores = []          # list holding weighted defensive scores
        self.autoScores = []            # list holding auto scores
        self.autoCrossesDefencesScores = []
        self.autoLowGoal = []
        self.autoHighGoal = []
        self.teleScores = []            # list holding tele scores
        self.teleDefencesDamageScore = []
        self.teleLowGoal = []
        self.teleHighGoal = []
        self.postChallengeStateScore = []
        self.postScaleStateScore = []
        self.foulScores = []            # list holding foul scores
        
    def get_maxmin_scores(self):
        self.maxOffScore = max(self.oScores)
        self.minOffScore = min(self.oScores)
        self.maxDefScore = max(self.dScores)
        self.minDefScore = min(self.dScores)
        self.maxTotalScore = max(self.tScores)
        self.minTotalScore = min(self.tScores)
        self.maxWScore = max(self.wScores)
        self.minWScore = min(self.wScores)
        self.maxWOScore = max(self.woScores)
        self.minWOScore = min(self.woScores)
        self.maxWDScore = max(self.wdScores)
        self.minWDScore = min(self.wdScores)
        self.maxAutoScore = max(self.autoScores)
        self.minAutoScore = min(self.autoScores)
        self.maxAutoCrossesDefencesScore = max(self.autoCrossesDefencesScores)
        self.minAutoCrossesDefencesScore = min(self.autoCrossesDefencesScores)
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
        self.maxPostChallengeStateScore = max(self.postChallengeStateScores)
        self.minPostScaleStateScore = min(self.postScaleStateScores)
        self.maxFoulScore = max(self.foulScores)
        self.minFoulScore = min(self.foulScores)

    def get_avgOff_scores(self, matches=1, auto=0):
        self.avgOffScore = sum(self.oScores)/matches if matches else 0
        self.avgAutoScore = sum(self.autoScores)/auto if auto else 0
        self.avgAutoCrossessDefencesScore = sum(self.autoCrossesDefencesScore)/auto if auto else 0
        self.avgAutoLowGoal = sum(self.autoLowGoal)/auto if auto else 0
        self.avgAutoHighGoal = sum(self.autoHighGoal)/auto if auto else 0
        self.avgTeleScore = sum(self.teleScores)/matches if matches else 0
        self.avgTeleDefencesDamageScore = sum(self.teleDefencesDamageScore)/matches if matches else 0
        self.avgTeleLowGoal = sum(self.teleLowGoal)/matches if matches else 0
        self.avgTeleHighGoal = sum(self.teleHighGoal)/matches if matches else 0
        self.avgPostChallengeStateScore = sum(self.postChallengStateScore)/matches if matches else 0
        self.avgPostScaleStateScore = sum(self.postScaleStateScore)/matches if matches else 0
        self.avgFoulScore = sum(self.foulScores)/matches if matches else 0
        self.avgTotalScore = sum(self.tScores)/matches if matches else 0
        
     def get_avgDef_scores(self, matches=1, defensive=0, assistive=0):
        self.avgDefScore = sum(self.dScores)/matches if defensive else 0

    def get_avgWeight_scores(self):
        self.avgTotalScore = sum(self.tScores)/len(self.tScores) if len(self.tScores) else 0
        self.avgWScore = sum(self.wScores)/len(self.wScores) if len(self.wScores) else 0
        self.avgWOScore = sum(self.woScores)/len(self.woScores) if len(self.woScores) else 0
        self.avgWDScore = sum(self.wdScores)/len(self.wdScores) if len(self.wdScores) else 0

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
    def_rank = []
    auto_Crosses_Defences_rank = []
    auto_Low_Goal_rank = []
    auto_High_Goal_rank = []
    tele_rank = []
    tele_Defences_Damage_rank = []
    tele_Low_Goal_rank = []
    tele_High_Goal_rank = []
    post_Challenge_State_Successful = []
    post_Scale_State_Successful = []
    w_rank = []
    wo_rank = []
    wd_rank = []
    wa_rank = []
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
        self.avgDef = 0
        self.pOff = 0
        self.pDef = 0     

def get_primary_details(self): # gets the offensive values of Team
        self.Info.get_info()
        self.Scores.get_avgOff_scores(len(self.Info.matches),
                                   self.Info.numOff,
                                   self.Info.autoHadAuto, self.Info.teleHadTele)

    def get_secondary_details(self): # gets the defensive values of the team
        self.Info.get_info()
        self.Scores.get_avgDef_scores(len(self.Info.matches),
                                         self.Info.numDef)

    def get_tertiary_details(self): # gets the max and min scores, etc. of the team
        self.Scores.get_avgWeight_scores()
        self.Scores.get_maxmin_scores()


    def get_final_details(self): # gets all of the information for the team
        matches = self.Info.matches
        self.numMatch = len(matches)
        self.pNoShow  = str(int(100*self.Info.noShow)/len(matches)) + "%"
        self.pDisabled = str(int(100*self.Info.postDisabled)/len(matches)) + "%"
        self.avgOff = round(self.Scores.avgOffScore,2)
        self.avgTotal = round(self.Scores.avgTotalScore,2)

        self.pHadAuto = str(int(100*self.Info.autoHadAuto)/len(matches)) + "%"
        self.pReachesDefences = str(int(100*self.Info.autoReachesDefences)/len(matches)) + "%"
        self.pCrossesDefences = str(int(100*self.Info.autoCrossesDefences)/len(matches)) + "%"
        self.avgCrossesDefencesScore = round(self.Info.autoCrossesDefencesScore, 2)
        self.avgAutoScore = round(self.Scores.avgAutoScore,2)
        self.avgAutoLowGoal = round(self.Scores.avgAutoLowGoal,2)
        self.avgAutoHighGoal = round(self.Scores.avgAutoHighGoal,2)
        self.pAutoOther = str(int(100*self.Info.autoOther)/len(matches)) + "%"
        
        self.avgTeleScore = round(self.Scores.avgTeleScore,2)
        self.pTelePortcullis = str(int(100*self.Info.telePortcullis)/int(self.Scores.teleDefencesDamageScore/5)) + "%"
        self.pTeleChevaldeFrise = str(int(100*self.Info.teleChevaldeFrise)/int(self.Scores.teleDefencesDamageScore/5)) + "%"
        self.pTeleMoat = str(int(100*self.Info.tele)/int(self.Scores.teleDefencesDamageScore/5)) + "%"
        self.pTeleRamparts = str(int(100*self.Info.teleRamparts)/int(self.Scores.teleDefencesDamageScore/5)) + "%"
        self.pTeleDrawbridge = str(int(100*self.Info.teleDrawbridge)/int(self.Scores.teleDefencesDamageScore/5)) + "%"
        self.pTeleSallyPort = str(int(100*self.Info.teleSallyPort)/int(self.Scores.teleDefencesDamageScore/5)) + "%"
        self.pTeleRoughTerrain = str(int(100*self.Info.teleRoughTerrain)/int(self.Scores.teleDefencesDamageScore/5)) + "%"
        self.pTeleRockWall = str(int(100*self.Info.teleRockWall)/int(self.Scores.teleDefencesDamageScore/5)) + "%"
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
        self.avgChallengStateScore = round(self.Scores.avgChallengeStateScore, 2)
        self.pChallengeStateNotAttempted = str(int(100*self.Info.NotAttemptedC)/len(self.Info.postChallengeState)) + "%"
        self.pChallengeStateAttempted = str(int(100*self.Info.AttemptedC)/len(self.Info.postChallengeState)) + "%"
        self.pChallengeStateSuccessful = str(int(100*self.Info.SuccessfulC)/len(self.Info.postChallengeState)) + "%"
        self.avgScaleStateScore = round(self.Score.avgScaleStateScore, 2)
        self.pScaleStateNotAttempted = str(int(100*self.Info.NotAttemptedS)/len(self.Info.postScaleState)) + "%"
        self.pScaleStateAttempted = str(int(100*self.Info.AttemptedS)/len(self.Info.postScaleState)) + "%"
        self.pScaleStateSuccessful = str(int(100*self.Info.SuccessfulS)/len(self.Info.postScaleState)) + "%"

    def getAttr(self, source):
        return getattr(self, source)
