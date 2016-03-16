#------------------------------------------------------------------------------
# entry module
#   -- makes sense of the data collected
#------------------------------------------------------------------------------

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
        index += 1
        
        # autonomous data
        self.autoHadAuto = (str(data[index]) == 'true')
        index += 1
        self.autoReachesDefences = (str(data[index]) == 'true')
        index += 1
        self.autoCrossesDefences = (str(data[index]) == 'true')
        index += 1
        self.autoStartsAsSpybot = (str(data[index]) == 'true')
        index += 1
        self.autoDefences1 = int(data[index])
        index += 1
        self.autoBouldersInLowGoal = float(data[index])
        index += 1
        self.autoBouldersInHighGoal = float(data[index])
        index += 1
        self.autoOther = (str(data[index]) == 'true')
        index += 1

        
        # tele-op data
        self.teleLowBar = (data[index])
        index +=1
        self.teleDamageCounter1 = float(data[index])
        index +=1
        self.teleDefences1 = (data[index])
        index +=1
        self.teleDamageCounter2 = float(data[index])
        index +=1
        self.teleDefences2 = (data[index])
        index +=1
        self.teleDamageCounter3 = float(data[index])
        index +=1
        self.teleDefences3 = (data[index])
        index +=1
        self.teleDamageCounter4 = float(data[index])
        index +=1
        self.teleDefences4 = (data[index])
        index +=1
        self.teleDamageCounter5 = float(data[index])
        index +=1
        self.teleBouldersInLowGoal = float(data[index])
        index +=1
        self.teleBouldersLowGoalMissed = float(data[index])
        index +=1
        self.teleBouldersInHighGoal = float(data[index])
        index +=1
        self.teleBouldersHighGoalMissed = float(data[index])
        index +=1
         
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
        self.postPlayedAssistively = bool(int(data[index]))
        index += 1
        self.postCaptured = bool(int(data[index]))
        index += 1
        self.postBreached = bool(int(data[index]))
        index += 1
        self.postChallengeState = int(data[index])
        index += 1
        self.postScaleState = int(data[index])
        

        self.entries.append(self)
        
    def primary_sort(self):
        """Calculates basic scoring and information."""
       
        self.autoReachesDefencesScore = 0

        if self.autoReachesDefences == True:
             self.autoReachesDefencesScore = 2

        self.autoCrossesDefencesScore = 0 

        if self.autoDefences1 > 0:
             self.autoCrossesDefencesScore = 10

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
        self.teleRoughTerrainDamage = 0
        if self.teleDefences4 == "Rock Wall":
            self.teleRockWallDamage = self.teleDamageCounter5
        elif self.teleDefences4 == "Rough Terrain":
            self.teleRoughTerrainDamage = self.teleDamageCounter5
            
        if self.teleLowBarDamage <= 2 and not self.autoDefences1 == 9:
            self.teleDC1 = (self.teleLowBarDamage*5)
        elif self.teleLowBarDamage <= 2 and self.teleLowBarDamage != 0 and self.autoDefences1 == 9:
            self.teleDC1 = (self.teleLowBarDamage*5) - 5
        elif self.teleLowBarDamage == 0 and self.autoDefences1 == 9:
            self.teleDC1 = 0
        elif self.teleLowBarDamage > 2 and self.autoDefences1 == 9:
            self.teleDC1 = 5
        else:
            self.teleDC1 = 10
            
        if self.telePortcullisDamage <= 2 and not self.autoDefences1 == 1:
            self.teleDC2 = (self.telePortcullisDamage*5)
        elif self.telePortcullisDamage <= 2 and self.telePortcullisDamage != 0 and self.autoDefences1 == 1:
            self.teleDC2 = (self.telePortcullisDamage*5) - 5
        elif self.telePortcullisDamage == 0 and self.autoDefences1 == 1:
            self.teleDC2 = 0
        elif self.telePortcullisDamage > 2 and self.autoDefences1 == 1:
            self.teleDC2 = 5
        else:
            self.teleDC2 = 10

        if self.teleChevaldeFriseDamage <= 2 and not self.autoDefences1 == 2:
            self.teleDC3 = (self.teleChevaldeFriseDamage*5)
        elif self.teleChevaldeFriseDamage <= 2 and self.teleChevaldeFriseDamage != 0 and self.autoDefences1 == 2:
            self.teleDC3 = (self.teleChevaldeFrise*5) - 5
        elif self.teleChevaldeFriseDamage == 0 and self.autoDefences1 == 2:
            self.teleDC3 = 0
        elif self.teleChevaldeFriseDamage > 2 and self.autoDefences1 == 2:
            self.teleDC3 = 5
        else:
            self.teleDC3 = 10

        if self.teleMoatDamage <= 2 and not self.autoDefences1 == 3:    
            self.teleDC4 = (self.teleMoatDamage*5)
        elif self.teleMoatDamage <= 2 and self.teleMoatDamage != 0 and self.autoDefences1 == 3:
            self.teleDC4 = (self.teleMoatDamage*5) - 5
        elif self.teleMoatDamage == 0 and self.autoDefences1 == 3:
            self.teleDC4 = 0
        elif self.teleMoatDamage > 2 and self.autoDefences1 == 3:
            self.teleDC4 = 5
        else:
            self.teleDC4 = 10

        if self.teleRampartsDamage <= 2 and not self.autoDefences1 == 4:
            self.teleDC5 = (self.teleRampartsDamage*5)
        elif self.teleRampartsDamage <= 2 and self.teleRampartsDamage != 0 and self.autoDefences1 == 4:
            self.teleDC5 = (self.teleRampartsDamag*5) - 5
        elif self.teleRampartsDamage == 0 and self.autoDefences1 == 4:
            self.teleDC5 = 0
        elif self.teleRampartsDamage > 2 and self.autoDefences1 == 4:
            self.teleDC5 = 5
        else:
            self.teleDC5 = 10

        if self.teleDrawbridgeDamage <= 2 and not self.autoDefences1 == 5:
            self.teleDC6 = (self.teleDrawbridgeDamage*5)
        elif self.teleDrawbridgeDamage <= 2 and self.teleDrawbridgeDamage != 0 and self.autoDefences1 ==5:
            self.teleDC6 = (self.teleDrawbridgeDamage*5) - 5
        elif self.teleDrawbridgeDamage == 0 and self.autoDefences1 == 5:
            self.teleDC6 = 0
        elif self.teleDrawbridgeDamage > 2 and self.autoDefences1 == 5:
            self.teleDC6 = 5
        else:
            self.teleDC6 = 10

        if self.teleSallyPortDamage <= 2 and not self.autoDefences1 == 6:
            self.teleDC7 = (self.teleSallyPortDamage*5)
        elif self.teleSallyPortDamage <= 2 and self.teleSallyPortDamage != 0 and self.autoDefences1 == 6:
            self.teleDC7 = (self.teleSallyPOrtDamage*5) - 5
        elif self.teleSallyPortDamage == 0 and self.autoDefences1 == 6:
            self.teleDC7 = 0
        elif self.teleSallyPortDamage > 2 and self.autoDefences == 6:
            self.teelDC7 = 5
        else:
            self.teleDC7 = 10

        if self.teleRockWallDamage <= 2 and not self.autoDefences1 == 7:
            self.teleDC8 = (self.teleRockWallDamage*5)
        elif self.teleRockWallDamage <= 2 and self.teleRockWallDamage != 0 and self.autoDefences1 == 7:
            self.teleDC8 = (self.teleRockWallDamage*5) - 5
        elif self.teleRockWallDamage == 0 and self.autoDefences1 == 7:
            self.teleDC8 = 0
        elif self.teleRockWallDamage > 2 and self.autoDefences1 == 7:
            self.teleDC8 = 5
        else:
            self.teleDC8 = 10

        if self.teleRoughTerrainDamage <= 2 and not self.autoDefences1 == 8:
            self.teleDC9 = (self.teleRoughTerrainDamage*5)
        elif self.teleRoughTerrainDamage <= 2 and self.teleRoughTerrainDamage != 0 and self.autoDefences1 == 8:
            self.teleDC9 = (self.teleRoughTerrainDamage*5) - 5
        elif self.teleRoughTerrainDamage == 0 and self.autoDefences1 == 8:
            self.teleDC9 = 0
        elif self.teleRoughTerrainDamage > 2 and self.autoDefences1 == 8:
            self.teleDC9 = 5
        else:
            self.teleDC9 = 10
        
        self.teleDefencesDamageScore = (self.teleDC1 + self.teleDC2 + self.teleDC3 + self.teleDC4 + self.teleDC5 + self.teleDC6 + self.teleDC7 + self.teleDC8 + self.teleDC9)

        self.teleLowGoal = (self.teleBouldersInLowGoal*2)
        self.teleHighGoal = (self.teleBouldersInHighGoal*5)
        
        self.teleTotalBouldersShotLG = (self.teleBouldersInLowGoal + self.teleBouldersLowGoalMissed)
        self.teleTotalBouldersShotHG = (self.teleBouldersInHighGoal + self.teleBouldersHighGoalMissed)

        self.postChallengeStateScore = 0

        if self.postChallengeState == 2:
            self.postChallengeStateScore = 5


        self.postScaleStateScore = 0
        
        if self.postScaleState == 2 :
            self.postScaleStateScore = 15
        
        self.teleScore = (self.teleDefencesDamageScore + self.teleLowGoal + self.teleHighGoal + self.postChallengeStateScore + self.postScaleStateScore)

        self.postChallengeStateScore = 0
        self.postScaleStateScore = 0

        self.postChallengeStateScore = 5 if self.postChallengeState == 2 and not self.postScaleState == 2 else 0
        self.postScaleStateScore = 15 if self.postScaleState == 2 else 0

        self.NotAttemptedC = True if self.postChallengeState == 0 else False
        self.AttemptedC = True if self.postChallengeState == 1 else False
        self.SuccessfulC = True if self.postChallengeState == 2 else False

        self.NotAttemptedS = True if self.postScaleState == 0 else False
        self.AttemptedS = True if self.postScaleState == 1 else False 
        self.SuccessfulS = True if self.postScaleState == 2 else False

        self.scoredInAuto = True if self.autoScore > 0 else False
        self.scoredInTele = True if self.teleScore > 0 else False
        self.hasFoul      = True if self.postFouls >0 or self.postTechFouls > 0 else False

        self.offensiveScore = (self.autoScore + self.teleScore)
        self.foulScore = (5*self.postFouls) + (5*self.postTechFouls)

        #self.offensiveScore = 0 if self.foulScore >= self.offensiveScore else  self.offensiveScore = (self.autoScore + self.teleScore)

        self.offensive = True if self.offensiveScore > 0 else False
        self.defensive = self.postPlayedDefensively
        self.assistive = self.postPlayedAssistively
        

    def secondary_sort(self, oppOff, allOff, allDef):
        # result = difference between offensive scores /
        #          the number of defensive players
        self.defensiveScore = (allOff-oppOff) / allDef / 2.0 if self.defensive else 0
    def tertiary_sort(self):
        """Calculates total scores."""
        self.totalScore = (self.offensiveScore + self.defensiveScore) 
                           #- self.foulScore)
        self.totalTAScore = (self.offensiveScore + self.defensiveScore)


class PitEntry(object):

    entries = []

    def __init__(self, data):
        self.team =int(data[0])

        self.answer1 = str(data[1])
        self.answer2 = str(data[2])
        self.answer3 = str(data[3])
        self.answer4 = str(data[4])
        self.answer5 = str(data[5])
        self.answer6 = str(data[6])

        self.entries.append(self)






        
