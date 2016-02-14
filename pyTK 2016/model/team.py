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
        self.autoLowGoal = []
        self.autoHighGoal = []
        self.autoOther = 0                  # number of matches for which the team did something else in auto

        self.teleHadTele = 0
        self.teleLowBarDamage = []
        self.telePortcullisDamage = []
        self.teleChevaldeFriseDamage = []
        self.teleRampartsDamage = []
        self.teleMoatDamage = []
        self.teleDrawbridgeDamage = []
        self.teleSallyPortDamage = []
        self.teleRoughTerrainDamage = []
        self.teleRockWallDamage = []
        self.teleDefencesDamageScore = []
        self.teleDC1 = []
        self.teleDC2 = []
        self.teleDC3 = []
        self.teleDC4 = []
        self.teleDC5 = []
        self.teleDC6 = []
        self.teleDC7 = []
        self.teleDC8 = []
        self.teleDC9 = []
        self.teleLowGoal = []
        self.teleHighGoal = []

        self.postFouls = []                 # list containing the number of fouls each match
        self.postTechFouls = []
        self.postRedCard = 0                # number of matches for which robot received red card
        self.postYellowCard = 0             # number of matches for which robot received yellow card
        self.postDisabled = 0               # number of matches for which robot was disabled
        self.postPlayedDefensively = 0
        self.postPlayedAssistively = 0
        self.postCaptured = 0
        self.postBreached = 0
        self.postChallengeState = []
        self.postChallengeStateScore = []
        self.NotAttemptedC = 0
        self.AttemptedC = 0
        self.SuccessfulC = 0
        self.postScaleState = []
        self.postScaleStateScore = []
        self.NotAttemptedS = 0
        self.AttemptedS = 0
        self.SuccessfulS = 0

        self.scoredInTele = 0               # number of matches for which the robot scored in tele-op
        self.scoredInAuto = 0               # number of matches for which the robot scored in auto
        self.hasFoul = 0                    # number of matches for which the robot received a foul

    def get_info(self):
        self.avgAutoLowGoal = float(sum(self.autoLowGoal))/float(len(self.autoLowGoal)) if len(self.autoLowGoal) else 0
        self.avgAutoHighGoal = float(sum(self.autoHighGoal))/float(len(self.autoHighGoal)) if len(self.autoHighGoal) else 0

        self.pTeleLowBarDamage = float(sum(100*self.teleDC1))/float(sum(self.teleDefencesDamageScore)) if sum(self.teleDefencesDamageScore) else 0
        self.pTeleLowBarDamageM = float(sum(self.teleLowBarDamage))/float(len(self.matches)) if len(self.matches) else 0
        self.pTelePortcullisDamage = float(sum(100*self.teleDC2))/float(sum(self.teleDefencesDamageScore)) if sum(self.teleDefencesDamageScore) else 0
        self.pTelePortcullisDamageM = float(sum(self.telePortcullisDamage))/float(len(self.matches)) if len(self.matches) else 0
        self.pTeleChevaldeFriseDamage = float(sum(100*self.teleDC3))/float(sum(self.teleDefencesDamageScore)) if sum(self.teleDefencesDamageScore) else 0
        self.pTeleChevaldeFriseDamageM = float(sum(self.teleChevaldeFriseDamage))/float(len(self.matches)) if len(self.matches) else 0
        self.pTeleMoatDamage = float(sum(100*self.teleDC4))/float(sum(self.teleDefencesDamageScore)) if sum(self.teleDefencesDamageScore) else 0
        self.pTeleMoatDamageM = float(sum(self.teleMoatDamage))/float(len(self.matches)) if len(self.matches) else 0
        self.pTeleRampartsDamage = float(sum(100*self.teleDC5))/float(sum(self.teleDefencesDamageScore)) if sum(self.teleDefencesDamageScore) else 0
        self.pTeleRampartsDamageM = float(sum(self.teleRampartsDamage))/float(len(self.matches)) if len(self.matches) else 0
        self.pTeleDrawbridgeDamage = float(sum(100*self.teleDC6))/float(sum(self.teleDefencesDamageScore)) if sum(self.teleDefencesDamageScore) else 0
        self.pTeleDrawbridgeDamageM = float(sum(self.teleDrawbridgeDamage))/float(len(self.matches)) if len(self.matches) else 0
        self.pTeleSallyPortDamage = float(sum(100*self.teleDC7))/float(sum(self.teleDefencesDamageScore)) if sum(self.teleDefencesDamageScore) else 0
        self.pTeleSallyPortDamageM = float(sum(self.teleSallyPortDamage))/float(len(self.matches)) if len(self.matches) else 0
        self.pTeleRockWallDamage = float(sum(100*self.teleDC8))/float(sum(self.teleDefencesDamageScore)) if sum(self.teleDefencesDamageScore) else 0
        self.pTeleRockWallDamageM = float(sum(self.teleRockWallDamage))/float(len(self.matches)) if len(self.matches) else 0
        self.pTeleRoughTerrainDamage = float(sum(100*self.teleDC9))/float(sum(self.teleDefencesDamageScore)) if sum(self.teleDefencesDamageScore) else 0
        self.pTeleRoughTerrainDamageM = float(sum(self.teleRoughTerrainDamage))/float(len(self.matches)) if len(self.matches) else 0

        self.avgTeleLowGoal = float(sum(self.teleLowGoal))/float(len(self.teleLowGoal)) if len(self.teleLowGoal) else 0
        self.avgTeleHighGoal = float(sum(self.teleHighGoal))/float(len(self.teleHighGoal)) if len(self.teleHighGoal) else 0
        
        self.avgPostFoul = sum(self.postFouls)/len(self.postFouls) if len(self.postFouls) else 0
        self.avgPostTechFoul = sum(self.postTechFouls)/len(self.postTechFouls) if len(self.postTechFouls) else 0 
                
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
        self.autoReachesDefencesScores = []
        self.autoCrossesDefencesScores = []
        self.autoLowGoal = []
        self.autoHighGoal = []
        self.teleScores = []            # list holding tele scores
        self.teleDefencesDamageScore = []
        self.teleLowGoal = []
        self.teleHighGoal = []
        self.postChallengeStateScore = []
        self.postChallengeStateSuccessful = []
        self.postScaleStateScore = []
        self.postScaleStateSuccessful = []
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
        self.maxAutoReachesDefencesScores = max(self.autoReachesDefencesScores)
        self.minAutoReachesDefencesScores = min(self.autoReachesDefencesScores)
        self.maxAutoCrossesDefencesScores = max(self.autoCrossesDefencesScores)
        self.minAutoCrossesDefencesScores = min(self.autoCrossesDefencesScores)
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
        self.maxPostChallengeStateScore = max(self.postChallengeStateScore)
        self.minPostChallengeStateScore = min(self.postChallengeStateScore)
        self.maxPostChallengeStateSuccessful = max(self.postChallengeStateSuccessful)
        self.minPostChallengeStateSuccessful = min(self.postChallengeStateSuccessful)
        self.maxPostScaleStateScore = max(self.postScaleStateScore)
        self.minPostScaleStateScore = min(self.postScaleStateScore)
        self.maxPostScaleStateSuccessful = max(self.postScaleStateSuccessful)
        self.minPostScaleStateSuccessful = min(self.postScaleStateSuccessful)
        self.maxFoulScore = max(self.foulScores)
        self.minFoulScore = min(self.foulScores)

    def get_avgOff_scores(self, matches=1,offensive=0, auto=0, tele=0):
        self.avgOffScore = sum(self.oScores)/matches if matches else 0
        self.avgAutoScore = sum(self.autoScores)/auto if auto else 0
        self.avgAutoReachesDefencesScores = sum(self.autoReachesDefencesScores)/auto if auto else 0
        self.avgAutoCrossesDefencesScores = sum(self.autoCrossesDefencesScores)/auto if auto else 0
        self.avgAutoLowGoal = sum(self.autoLowGoal)/auto if auto else 0
        self.avgAutoHighGoal = sum(self.autoHighGoal)/auto if auto else 0
        self.avgTeleScore = sum(self.teleScores)/matches if matches else 0
        self.avgTeleDefencesDamageScore = sum(self.teleDefencesDamageScore)/matches if matches else 0
        self.avgTeleLowGoal = sum(self.teleLowGoal)/matches if matches else 0
        self.avgTeleHighGoal = sum(self.teleHighGoal)/matches if matches else 0
        self.avgPostChallengeStateScore = sum(self.postChallengeStateScore)/matches if matches else 0
        self.avgPostChallengeStateSuccessful = sum(self.postChallengeStateSuccessful)/matches if matches else 0
        self.avgPostScaleStateScore = sum(self.postScaleStateScore)/matches if matches else 0
        self.avgPostScaleStateSuccessful = sum(self.postScaleStateSuccessful)/matches if matches else 0
        self.avgFoulScore = sum(self.foulScores)/matches if matches else 0
        self.avgTotalScore = sum(self.tScores)/matches if matches else 0
        
    def get_avgDef_scores(self, matches=1, defensive=0):
        self.avgDefScore = sum(self.dScores)/matches if defensive else 0

    def get_avgWeight_scores(self):
        self.avgTotalScore = sum(self.tScores)/len(self.tScores) if len(self.tScores) else 0
        self.avgWScore = sum(self.wScores)/len(self.wScores) if len(self.wScores) else 0
        self.avgWOScore = sum(self.woScores)/len(self.woScores) if len(self.woScores) else 0
        self.avgWDScore = sum(self.wdScores)/len(self.wdScores) if len(self.wdScores) else 0

    def getAttr(self, source):
        return getattr(self, source)
#------------------------------------------------------------------------------
# TeamPitInfo Class
#   -- stores data unrelated to performance on the field
#------------------------------------------------------------------------------
class _TeamPitInfo(object):
    """Used to handle information about a teams chassis and other
       non-performance related information."""

    def __init__(self):
      self.answer1 = ""
      self.answer2 = ""
      self.answer3 = ""
      self.answer4 = ""
      self.answer5 = ""
      self.answer6 = ""

    def getAttr(self, source):
        return getattr(self, source)    

#------------------------------------------------------------------------------
# TeamRankings class
#   -- place to store ranking lists, for viewing team ranks
#------------------------------------------------------------------------------
class TeamRankings(object):
    """Used to keep track of rankings for each team."""

    off_rank = []
    def_rank = []
    auto_rank = []    
    auto_Crosses_Defences_rank = []
    auto_Low_Goal_rank = []
    auto_High_Goal_rank = []
    tele_rank = []
    tele_Defences_Damage_rank = []
    tele_Low_Goal_rank = []
    tele_High_Goal_rank = []
    post_Challenge_State_Successful_rank = []
    post_Scale_State_Successful_rank = []
    w_rank = []
    wo_rank = []
    wd_rank = []
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
        self.PitInfo = _TeamPitInfo()
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
        self.Info.get_info()
        matches = self.Info.matches
        self.numMatch = len(matches)
        self.pNoShow  = str(int(100*self.Info.noShow)/len(matches)) + "%"
        self.pDisabled = str(int(100*self.Info.postDisabled)/len(matches)) + "%"
        self.avgOff = round(self.Scores.avgOffScore,2)
        self.avgDef = round(self.Scores.avgDefScore,2)
        self.avgTotal = round(self.Scores.avgTotalScore,2)

        self.pHadAuto = str(int(100*self.Info.autoHadAuto)/len(matches)) + "%"
        self.pReachesDefences = str(int(100*self.Info.autoReachesDefences)/len(matches)) + "%"
        self.pCrossesDefences = str(int(100*self.Info.autoCrossesDefences)/len(matches)) + "%"
        self.avgAutoReachesDefencesScores = str(self.Scores.avgAutoReachesDefencesScores)
        self.avgAutoCrossesDefencesScores = str(self.Scores.avgAutoCrossesDefencesScores)
        self.avgAutoScore = round(self.Scores.avgAutoScore,2)
        self.avgAutoLowGoal = round(self.Scores.avgAutoLowGoal,2)
        self.avgAutoHighGoal = round(self.Scores.avgAutoHighGoal,2)
        self.pAutoOther = str(int(100*self.Info.autoOther)/len(matches)) + "%"
        
        self.avgTeleScore = round(self.Scores.avgTeleScore,2)
        self.pTeleLowBar = str(round(self.Info.pTeleLowBarDamage,2)) + "%"
        self.pTeleLowBarM = round(self.Info.pTeleLowBarDamageM,2)
        self.pTelePortcullis = str(round(self.Info.pTelePortcullisDamage,2)) + "%"
        self.pTelePortcullisM = round(self.Info.pTelePortcullisDamageM,2)
        self.pTeleChevaldeFrise = str(round(self.Info.pTeleChevaldeFriseDamage,2)) + "%"
        self.pTeleChevaldeFriseM = round(self.Info.pTeleChevaldeFriseDamageM,2)
        self.pTeleMoat = str(round(self.Info.pTeleMoatDamage,2)) + "%"
        self.pTeleMoatM = round(self.Info.pTeleMoatDamageM,2)
        self.pTeleRamparts = str(round(self.Info.pTeleRampartsDamage,2)) + "%"
        self.pTeleRampartsM = round(self.Info.pTeleRampartsDamageM,2)
        self.pTeleDrawbridge = str(round(self.Info.pTeleDrawbridgeDamage,2)) + "%"
        self.pTeleDrawbridgeM = round(self.Info.pTeleDrawbridgeDamageM,2)
        self.pTeleSallyPort = str(round(self.Info.pTeleSallyPortDamage,2)) + "%"
        self.pTeleSallyPortM = round(self.Info.pTeleSallyPortDamageM,2)
        self.pTeleRoughTerrain = str(round(self.Info.pTeleRoughTerrainDamage,2)) + "%"
        self.pTeleRoughTerrainM =round(self.Info.pTeleRoughTerrainDamageM,2)
        self.pTeleRockWall = str(round(self.Info.pTeleRockWallDamage,2)) + "%"
        self.pTeleRockWallM = round(self.Info.pTeleRockWallDamageM,2)
        self.avgTeleDefencesDamageScore = round(self.Scores.avgTeleDefencesDamageScore, 2)
        self.avgTeleLowGoal = round(self.Scores.avgTeleLowGoal,2)
        self.avgTeleHighGoal = round(self.Scores.avgTeleHighGoal,2)
       
        self.avgFoulScore = round(self.Scores.avgFoulScore,2)
        self.avgPostFoul = round(self.Info.avgPostFoul,2)
        self.pFoul = str(int(100*self.Info.hasFoul)/len(matches)) + "%"
        self.pYellow = str(int(100*self.Info.postYellowCard)/len(matches)) + "%"
        self.pRed = str(int(100*self.Info.postRedCard)/len(matches)) + "%"
        self.pPlayedDefensively = str(int(100*self.Info.postPlayedDefensively)/len(matches)) + "%"
        self.pPlayedAssistively = str(int(100*self.Info.postPlayedAssistively)/len(matches)) + "%"
        self.pCaptured = str(int(100*self.Info.postCaptured)/len(matches)) + "%"
        self.pBreached = str(int(100*self.Info.postBreached)/len(matches)) + "%"
        self.avgPostChallengeStateScores = round(self.Scores.avgPostChallengeStateScore, 2)
        self.pChallengeStateNotAttempted = str(int(100*self.Info.NotAttemptedC)/len(matches)) + "%"
        self.pChallengeStateAttempted = str(int(100*self.Info.AttemptedC)/len(matches)) + "%"
        self.pChallengeStateSuccessful = str(int(100*self.Info.SuccessfulC)/len(matches)) + "%"
        self.avgPostScaleStateScores = round(self.Scores.avgPostScaleStateScore, 2)
        self.pScaleStateNotAttempted = str(int(100*self.Info.NotAttemptedS)/len(matches)) + "%"
        self.pScaleStateAttempted = str(int(100*self.Info.AttemptedS)/len(matches)) + "%"
        self.pScaleStateSuccessful = str(int(100*self.Info.SuccessfulS)/len(matches)) + "%"

    def getAttr(self, source):
        return getattr(self, source)
