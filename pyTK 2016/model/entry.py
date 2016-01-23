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
        self.autoDefences1 = int(data[index]))
        index += 1
        self.autoDefences2 = int(data[index]))
        index += 1
        self.autoBouldersInLowGoal = float(data[index])
        index += 1
        self.autoBouldersInHighGoal = float(data[index])
        index += 1
        self.autoOther = bool(int(data[index]))
        

        # tele-op data
        self.teleLowBar = str(data[index]))
        index +=1
        self.teleDamageCounter1 = float(data[inde]))
        index +=1
        self.teleDefences1 = str(data[index]))
        index +=1
        self.teleDamageCounter2 = float(data[index]))
        index +=1
        self.teleDefences2 = str(data[index]))
        index +=1
        self.teleDamageCounter3 = float(data[index]))
        index +=1
        self.teleDefences3 = str(data[index]))
        index +=1
        self.teleDamageCounter4 = float(data[index]))
        index +=1
        self.teleDefences4 = str(data[index]))
        index +=1
        self.teleDamageCounter5 = float(data[index]))
        index +=1
        self.teleBouldersInLowGoal = float(data[index]))
        index +=1
        self.teleBouldersInHighGoal = float(data[index]))
        index +=1
        self.teleBouldersFromLowGoal = float(data[index]))
        index +=1
        self.teleBouldersFromHighGoal = float(data[index]))
         
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
        self.postChallengeState = int(data[index]))
        index += 1
        self.postScaleState = int(data[index]))
        index += 1

        self.entries.append(self)
    def sort(self):
        """Calculates basic scoring and information."""
            
        self.avgTeleBouldersInLowGoal = float(sum(self.teleBouldersInLowGoal))/float(len(self.teleBouldersInLowGoal)) if len(self.BouldersInLowGoal) else 0
        self.avgTeleBouldersInHighGoal = float(sum(self.teleBouldersInHighGoal))/float(len(self.teleBouldersInHighGoal)) if len(self.teleBouldersInHighGoal) else 0
        self.avgTeleBouldersFromLowGoal = float(sum(self.teleBouldersFromLowGoal))/float(len(self.teleBouldersFromLowGoal)) if len(self.teleBouldersFromLowGoal) else 0
        self.avgTeleBouldersFromHighGoal = float(sum(self.teleBouldersFromHighGoal))/float(len(self.teleBouldersFromHighGoal)) if len(self.teleBouldersFromHighGoal) else 0

        self.autoReachesDefences = 2 if self.autoReachesDefences = 1 else self.autoReachesDefences = 0

        self.autoCrossesDefences = 10 if self.autoDefences1 >=1 and self.autoDefences2 = 0 elif self.autoDefences2 >= 1 and self.autoDefences = 0 else self.autoCrossesDefences = 0
        self.autoCrossesDefences = 20 if self.autoDefences1 >=1 and self.autoDefences2 >= 1 else self.autoCrossesDefences = 0

        self.autoLowGoal = (self.autoBouldersInLowGoal*5)
        self.autoHighGoal = (self.autoBouldersInHighGoal*10)

        self.autoScore = (self.autoReachesDefences + self.autoCrossesDefences + self.autoLowGoal + self.autoHighGoal)
        
        self.teleDC1 = (self.teleDamageCounter1*5) 
        self.teleDC2 = (self.teleDamageCounter2*5) 
        self.teleDC3 = (self.teleDamageCounter3*5) 
        self.teleDC4 = (self.teleDamageCounter4*5) 
        self.teleDC5 = (self.teleDamageCounter5*5)
        
        self.teleDefencesDamageScore = (self.teleDC1 + self.teleDC2 + self.teleDC3 + self.teleDC4 + self.teleDC5)

        self.teleLowGoal = (self.teleBouldersInlowGoal*2)
        self.teleHighGoal = (self.teleBouldersInHighGoal*5)
        
        self.teleScore = (self.teleDefencesScore + self.teleLowGoal + self.teleHighGoal)

        self.scoredInAuto = True if self.autoScore > 0 else False
        self.scoredInTele = True if self.teleScore > 0 else False
        self.hasFoul      = True if self.postFouls > 0 elif self.postTechFouls > 0 elif self.postFouls > 0 and self.postTechFouls > 0 else False

        self.offensiveScore = (self.autoScore + self.teleScore)
        self.foulScore = (5*self.postFouls + 5*self.postTechFoul)

        self.totalScore = (self.offensiveScore - self.foulScore)
