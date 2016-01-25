#------------------------------------------------------------------------------
# entry module
#   -- makes sense of the data collected
#------------------------------------------------------------------------------
from stack import *

#------------------------------------------------------------------------------
# Entry class
#   -- Equivalent to a single ms-access entry
#   -- each match has 6 of these entries
#------------------------------------------------------------------------------
class Entry(object):
    """Pull in loaded data and sort it to be later assigned to team values."""

    entries = [] # list holding all the entries, 6 per match
    
    def __init__(self, data):
        # general info
        index = 0
        self.match = int(data[index])
        index += 1
        self.team = int(data[index])
        index += 1
        self.allianceColor = int(data[index])
        index += 1
        self.noShow = bool(int(data[index]))
        
        
        # autonomous data
        self.autoHadAuto = bool(int(data[index]))
        index += 1
        self.autoReachesDefences = bool(int(data[index]))
        index += 1
        self.autoCrossesDefences = bool(int(data[index]))
        index += 1
        self.autoDefences1 = int(data[index])
        index += 1
        self.autoDefences2 = int(data[index])
        index += 1
        self.autoBouldersInLowGoal = float(data[index])
        index += 1
        self.autoBouldersInHighGoal = float(data[index])
        index += 1
        self.autoOther = bool(int(data[index]))
        

        # tele-op data
        self.teleLowBar = str(data[index])
        index +=1
        self.teleDamageCounter1 = float(data[index])
        index +=1
        self.teleDefences1 = str(data[index])
        index +=1
        self.teleDamageCounter2 = float(data[index])
        index +=1
        self.teleDefences2 = str(data[index])
        index +=1
        self.teleDamageCounter3 = float(data[index])
        index +=1
        self.teleDefences3 = str(data[index])
        index +=1
        self.teleDamageCounter4 = float(data[index])
        index +=1
        self.teleDefences4 = str(data[index])
        index +=1
        self.teleDamageCounter5 = float(data[index])
        index +=1
        self.teleBouldersInLowGoal = float(data[index])
        index +=1
        self.teleBouldersInHighGoal = float(data[index])
        index +=1
        self.teleBouldersFromLowGoal = float(data[index])
        index +=1
        self.teleBouldersFromHighGoal = float(data[index])
         
        # post data
        self.postFouls = float(data[index])
        index += 1
        self.postTechFouls = float(data[index])
        index += 1
        self.postRedCard = bool(int(data[index]))
        index += 1
        self.postYellowCard = bool(int(data[index]))
        index += 1
        self.postDisabled = bool(int(data[index]))
        index += 1
        self.postPlayedDefensively = bool(int(data[index]))
        index += 1
        self.postCaptured = bool(int(data[index]))
        index += 1
        self.postBreached = bool(int(data[index]))
        index += 1
        self.postChallengeState = int(data[index])
        index += 1
        self.postScaleState = int(data[index])
        index += 1

        self.entries.append(self)
    def primary_sort(self):
        """Calculates basic scoring and information."""
        self.avgAutoBouldersInLowGoal = float(sum(self.autoBouldersInLowGoal))/float(len(self.autoBouldersInLowGoal)) if len(self.autoBouldersInLowGoal) else 0
        self.avgAutoBouldersInHighGoal = float(sum(self.autoBouldersInHighGoal))/float(len(self.autoBouldersInHighGoal)) if len(self.autoBouldersInHighGoal) else 0
        self.avgTeleBouldersInLowGoal = float(sum(self.teleBouldersInLowGoal))/float(len(self.teleBouldersInLowGoal)) if len(self.teleBouldersInLowGoal) else 0
        self.avgTeleBouldersInHighGoal = float(sum(self.teleBouldersInHighGoal))/float(len(self.teleBouldersInHighGoal)) if len(self.teleBouldersInHighGoal) else 0
        self.avgTeleBouldersFromLowGoal = float(sum(self.teleBouldersFromLowGoal))/float(len(self.teleBouldersFromLowGoal)) if len(self.teleBouldersFromLowGoal) else 0
        self.avgTeleBouldersFromHighGoal = float(sum(self.teleBouldersFromHighGoal))/float(len(self.teleBouldersFromHighGoal)) if len(self.teleBouldersFromHighGoal) else 0

        self.autoReachesDefencesScore = 0

        self.autoReachesDefencesScore = 2 if self.autoReachesDefences == 1 else self.autoReachesDefencesScore = 0

        self.autoCrossesDefencesScore = 0

        if self.autoDefences1 >= 1 and self.autoDefences2 == 0:
             self.autoCrossesDefencesScore = 10
        elif self.autoDefences2 >= 1 and self.autoDefences == 0:
             self.autoCrossesDefencesScore = 10
        self.autoCrossesDefencesScore = 20 if self.autoDefences1 >= 1 and self.autoDefences2 >= 1 else 0

        self.avgAutoCrossesDefencesScore = float(sum(self.autoCrossesDefencesScore))/float(len(self.autoDefencesScore)) if len(self.autoDefencesScore) else 0

        self.autoLowGoal = (self.autoBouldersInLowGoal*5)
        self.autoHighGoal = (self.autoBouldersInHighGoal*10)

        self.autoScore = (self.autoReachesDefences + self.autoCrossesDefences + self.autoLowGoal + self.autoHighGoal)

        self.teleLowBarDamage = self.teleDamageCounter1

        self.telePortcullisDamage = 0
        self.teleChevaldeFriseDamage = 0
        if self.teleDefences1 == "Portcullis":
            self.telePortcullisDamage = self.teleDamageCounter2
        elif self.teleDefences1 == "Cheval de Frise":
            self.teleChevaldeFriseDamage = self.teleDamageCounter2

        self.teleMoatDamage = 0
        self.teleRampartsDamage = 0
        if self.teleDefences2 == "Moat":
            self.teleMoatDamage = self.teleDamageCounter3
        elif self.teleDefences2 == "Rmaparts":
            self.teleRampartsDamage = self.teleDamageCounter3
            
        self.teleDrawbridgeDamage = 0
        self.teleSallyPortDamage = 0
        if self.teleDefences3 == "Drawbridge":
            self.teleDrawbridgeDamage = self.teleDamageCounter4
        elif self.teleDefences4 == "Sally Port":
            self.teleSallyPortDamage = self.teleDamageCounter4

        self.teleRockWallDamage = 0
        self.teleRoughTerrain = 0
        if self.Defences4 == "Rock Wall":
            self.teleRockWallDamage = self.teleDamageCounter5
        elif self.Defences4 == "Rough Terrain":
            self.teleRoughTerrainDamage = self.teleDamageCounter5
        
        self.teleDC1 = (self.teleDamageCounter1*5) 
        self.teleDC2 = (self.teleDamageCounter2*5) 
        self.teleDC3 = (self.teleDamageCounter3*5) 
        self.teleDC4 = (self.teleDamageCounter4*5) 
        self.teleDC5 = (self.teleDamageCounter5*5)
        
        self.teleDefencesDamageScore = (self.teleDC1 + self.teleDC2 + self.teleDC3 + self.teleDC4 + self.teleDC5)

        self.avgTeleDefencesDamageScore = float(sum(self.teleDefencesDamageScore))/float(len(self.teleDamageDamageScore)) if len(self.teleDefencesDamageScore)  else 0

        self.teleLowGoal = (self.teleBouldersInLowGoal*2)
        self.teleHighGoal = (self.teleBouldersInHighGoal*5)

        self.teleFromLowGoal = (self.teleBouldersFromLowGoal*2)
        self.teleFromHighGoal = (self.teleBouldersFromHighGoal*5)

        self.DefensiveScore = (self.teleFromLowGoal + self.teleFromHighGoal)

        self.postChallengeStateScore = 5 if self.postChallengeState = 2 else self.postChallengeStateScore = 0
        self.postScaleStateScore = 15 if self.postScaleState = 2 else self.postScaleStateScore = 0
        
        self.teleScore = (self.teleDefencesDamageScore + self.teleLowGoal + self.teleHighGoal + self.postChallengeStateScore + self.postScaleStateScore)

        self.postChallengeStateScore = 0
        self.postScaleStateScore = 0

        self.postChallengeStateScore = 5 if self.postChallengeState == 2 else 0
        self.postScaleStateScore = 5 if self.postScaleState == 1 else 0
        self.postScaleStateScore = 15 if self.postScaleState == 2 else 0

        self.NotAttemptedC = True if self.postChallengeState == 0 else False
        self.AttemptedC = True if self.postChallenState == 1 else False
        self.SuccessfulC = True if self.postChallenState == 2 else False

        self.NotAttemptedS = True if self.postScaleState == 0 else False
        self.AttemptedS = True if self.postScaleState == 1 else False 
        self.SuccessfulS = True if self.postScaleState == 2 else False

        self.avgTeleChallengeStateSuccessful = float(sum(self.SuccessfulC))/float(len(self.postChallengeState)) if len(self.postChallengeState) else 0
        self.avgTeleScaleStateSuccessful = float(sum(self.SuccesfulS))/float(len(self.postScaleState)) if len(self.postScaleState) else 0 

        self.scoredInAuto = True if self.autoScore > 0 else False
        self.scoredInTele = True if self.teleScore > 0 else False
        self.hasFoul      = True if self.postFouls > 0 elif self.postTechFouls > 0 elif self.postFouls > 0 and self.postTechFouls > 0 else False

        self.offensiveScore = (self.autoScore + self.teleScore)
        self.foulScore = (5*self.postFouls + 5*self.postTechFoul)

        self.offensive = True if self.offensiveScore > 0 else False
        self.defensive = self.postPlayedDefensively

    def secondary_sort(self, oppOff, allOff, allDef):
        # result = difference between offensive scores /
        #          the number of defensive players
        self.defensiveScore = (allOff-oppOff) / allDef / 2.0 if self.defensive else 0
    def tertiary_sort(self):
        """Calculates total scores."""
        self.totalScore = (self.offensiveScore + self.defensiveScore 
                           - self.foulScore)
        self.totalTAScore = (self.offensiveScore + self.defensiveScore)
