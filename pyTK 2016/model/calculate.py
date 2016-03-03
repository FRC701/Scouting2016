#------------------------------------------------------------------------------
# calculate module
#   -- functions for handling data input, output, and caclulations
#------------------------------------------------------------------------------
import math
from statlib import stats

from team import *
from entry import *
from match import *

#------------------------------------------------------------------------------
# calculate_data function
#   -- handles data and stores it to the teams
#------------------------------------------------------------------------------
def calculate_data():
    
    for entry in Entry.entries:
        entry.primary_sort()

    # get basic team data from the entries
    for entry in Entry.entries:
        done = False
        for team in Team.team_list:
            if team.number == entry.team:
                assign_basic_team_values(team, entry)

                done = True
        if done == False:
            newTeam = Team(entry.team)
            print "Added Team #: " + str(entry.team)

            assign_basic_team_values(newTeam, entry)

   # get primary offensive information about the team
    for team in Team.team_list:
        team.get_primary_details()
    
    # get basic match data from the entries
    for entry in Entry.entries:
        done = False
        for match in Match.matches:
            if match.number == entry.match:
                assign_basic_match_values(match, entry)

                done = True
        if done==False:
            newMatch = Match(entry.match)
            print "Added Match #: " + str(entry.match)
            assign_basic_match_values(newMatch, entry)

    # get defensive scores for each entry
    for entry in Entry.entries:
        if entry.defensive:
            for match in Match.matches:
                if match.number == entry.match:
                    if entry.allianceColor == 0:
                        oppOff = match.offScore1
                        allOff = match.offScore0
                        allDef = match.def0
                    elif entry.allianceColor == 1:
                        oppOff = match.offScore0
                        allOff = match.offScore1
                        allDef = match.def1
        else:
            oppOff = 0
            allOff = 0
            allDef = 0

        entry.secondary_sort(oppOff,allOff,allDef)

        # get total score for the entry
        entry.tertiary_sort()

    # get team defensive scores
    for entry in Entry.entries:
        for team in Team.team_list:
            if team.number == entry.team:
                team.Scores.dScores.append(entry.defensiveScore)
    for team in Team.team_list:
        team.get_secondary_details()

    # get match defensive scores
    for entry in Entry.entries:
        for match in Match.matches:
            if match.number == entry.match:
                if entry.allianceColor == 0:
                    match.defScore0 += entry.defensiveScore
                elif entry.allianceColor == 1:
                    match.defScore1 += entry.defensiveScore
    # get match total scores
    for match in Match.matches:
        match.get_total()

    # weight = (s[m]/(s[w]-s[1]))
    for entry in Entry.entries:
        for match in Match.matches:
            if match.number == entry.match:
                entry.wScore = abs(entry.totalScore/(match.total0 - match.total1)) if match.total0 != match.total1 else entry.totalScore
                entry.woScore = abs(entry.offensiveScore/(match.offScore0 - match.offScore1)) if match.offScore0 != match.offScore1 else entry.offensiveScore
                entry.wdScore = abs(entry.defensiveScore/(match.defScore0 - match.defScore1)) if match.defScore0 != match.defScore1 else entry.defensiveScore
                    
    # get team average, weighted, total, and max/min scores
    for team in Team.team_list:
        for entry in Entry.entries:
            if entry.team == team.number:
                team.Scores.wScores.append(entry.wScore)
                team.Scores.woScores.append(entry.woScore)
                team.Scores.wdScores.append(entry.wdScore)
                team.Scores.tScores.append(entry.totalScore)

        team.get_tertiary_details()
        team.get_final_details()
#------------------------------------------------------------------------------
# calculate_pit_data function
#   - handles pit data and stores it to the teams
#------------------------------------------------------------------------------
def calculate_pit_data():
    for entry in PitEntry.entries:
        done = False
        for team in Team.team_list:
            if team.number == entry.team:
                assign_pit_entry_values(team, entry)
                done = True
        if done == False:
            newTeam = Team(entry.team)
            print "Added Team #: " + str(entry.team)
            assign_pit_entry_values(Team.team_list[len(Team.team_list)-1],entry)
        

#------------------------------------------------------------------------------
# assign_basic_team_values function
#   -- assigns some basic values from an entry to a team
#   -- still needs error handling
#------------------------------------------------------------------------------
def assign_basic_team_values(team, entry):
    team.Info.matches.append(entry.match)
    team.Info.numOff += int(entry.offensive)
    team.Info.numDef += int(entry.defensive)
    team.Info.noShow += int(entry.noShow)

    team.Info.autoHadAuto += int(entry.autoHadAuto)
    team.Info.autoReachesDefences += int (entry.autoReachesDefences)
    team.Info.autoCrossesDefences += int (entry.autoCrossesDefences)
    team.Info.autoStartsAsSpybot += int (entry.autoStartsAsSpybot)
    team.Info.autoLowGoal.append(float(entry.autoBouldersInLowGoal))
    team.Info.autoHighGoal.append(float(entry.autoBouldersInHighGoal))
    team.Info.autoOther += int(entry.autoOther)

    team.Info.teleLowBarDamage.append(float(entry.teleLowBarDamage))
    team.Info.teleDC1.append(float(entry.teleDC1))
    team.Info.telePortcullisDamage.append(float(entry.telePortcullisDamage))
    team.Info.teleDC2.append(float(entry.teleDC2))
    team.Info.teleChevaldeFriseDamage.append(float(entry.teleChevaldeFriseDamage))
    team.Info.teleDC3.append(float(entry.teleDC3))
    team.Info.teleMoatDamage.append(float(entry.teleMoatDamage))
    team.Info.teleDC4.append(float(entry.teleDC4))
    team.Info.teleRampartsDamage.append(float(entry.teleRampartsDamage))
    team.Info.teleDC5.append(float(entry.teleDC5))
    team.Info.teleDrawbridgeDamage.append(float(entry.teleDrawbridgeDamage))
    team.Info.teleDC6.append(float(entry.teleDC6))
    team.Info.teleSallyPortDamage.append(float(entry.teleSallyPortDamage))
    team.Info.teleDC7.append(float(entry.teleDC7))
    team.Info.teleRockWallDamage.append(float(entry.teleRockWallDamage))
    team.Info.teleDC8.append(float(entry.teleDC8))
    team.Info.teleRoughTerrainDamage.append(float(entry.teleRoughTerrainDamage))
    team.Info.teleDC9.append(float(entry.teleDC9))
    team.Info.teleDefencesDamageScore.append(float(entry.teleDefencesDamageScore))

    team.Info.teleLowGoal.append(float(entry.teleBouldersInLowGoal))
    team.Info.teleHighGoal.append(float(entry.teleBouldersInHighGoal))
    team.Info.teleTotalBouldersShotLG.append(float(entry.teleTotalBouldersShotLG))
    team.Info.teleTotalBouldersShotHG.append(float(entry.teleTotalBouldersShotHG))

    team.Info.postFouls.append(float(entry.postFouls))
    team.Info.postTechFouls.append(float(entry.postTechFouls))
    team.Info.postRedCard += int(entry.postRedCard)
    team.Info.postYellowCard += int(entry.postYellowCard)
    team.Info.postDisabled += int(entry.postDisabled)
    team.Info.postPlayedDefensively += int(entry.postPlayedDefensively)
    team.Info.postPlayedAssistively += int(entry.postPlayedAssistively)
    team.Info.postCaptured += int(entry.postCaptured)
    team.Info.postBreached += int (entry.postBreached)
    team.Info.postChallengeStateScore.append(float(entry.postChallengeStateScore))
    team.Info.NotAttemptedC += int (entry.NotAttemptedC)
    team.Info.AttemptedC += int (entry.AttemptedC)
    team.Info.SuccessfulC += int (entry.SuccessfulC)
    team.Info.postScaleStateScore.append(float(entry.postScaleStateScore))
    team.Info.NotAttemptedS += int (entry.NotAttemptedS)
    team.Info.AttemptedS += int (entry.AttemptedS)
    team.Info.SuccessfulS += int (entry.SuccessfulS)

    team.Info.scoredInTele += int(entry.scoredInTele)
    team.Info.scoredInAuto += int(entry.scoredInAuto)
    team.Info.hasFoul += int(entry.hasFoul)

    team.Scores.oScores.append(entry.offensiveScore)
    team.Scores.autoScores.append(entry.autoScore)
    team.Scores.autoReachesDefencesScores.append(entry.autoReachesDefencesScore)
    team.Scores.autoCrossesDefencesScores.append(entry.autoCrossesDefencesScore)
    team.Scores.autoLowGoal.append(entry.autoLowGoal)
    team.Scores.autoHighGoal.append(entry.autoHighGoal)
    team.Scores.teleScores.append(entry.teleScore)
    team.Scores.teleDefencesDamageScore.append(entry.teleDefencesDamageScore)
    team.Scores.teleLowGoal.append(entry.teleLowGoal)
    team.Scores.teleHighGoal.append(entry.teleHighGoal)
    team.Scores.postChallengeStateScore.append(entry.postChallengeStateScore)
    team.Scores.postChallengeStateSuccessful.append(entry.SuccessfulC)
    team.Scores.postScaleStateScore.append(entry.postScaleStateScore)
    team.Scores.postScaleStateSuccessful.append(entry.SuccessfulS)
    team.Scores.foulScores.append(entry.foulScore)
   
    
#------------------------------------------------------------------------------
# assign_basic_match_values function
#   -- assigns some basic values from the entry to a match
#   -- still needs error handling
#------------------------------------------------------------------------------
def assign_basic_match_values(match, entry):
    match.teams.append(entry.team)
    if entry.allianceColor == 0:
        match.all0.append(entry.team)
        match.offScore0 += entry.offensiveScore
        match.off0 += int(entry.offensive)
        match.def0 += int(entry.defensive)
                    
    elif entry.allianceColor == 1:
        match.all1.append(entry.team)
        match.offScore1 += entry.offensiveScore
        match.off1 += int(entry.offensive)
        match.def1 += int(entry.defensive)

#------------------------------------------------------------------------------
# assign_pit_entry_values function
#   -- takes PitEntry values and puts them into a team
#   -- still needs error handling
#------------------------------------------------------------------------------
def assign_pit_entry_values(team, entry):
    
    team.PitInfo.answer1 = entry.answer1
    team.PitInfo.answer2 = entry.answer2
    team.PitInfo.answer3 = entry.answer3
    team.PitInfo.answer4 = entry.answer4
    team.PitInfo.answer5 = entry.answer5
    team.PitInfo.answer6 = entry.answer6
    
    
#------------------------------------------------------------------------------
# get_rank functions
#   -- calculates rankings for avg, min, and max scores for each team
#------------------------------------------------------------------------------
def get_off_rank(sort="avg",rev=True):

    TeamRankings.off_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            TeamRankings.off_rank.append([team.Scores.avgOffScore,team.number])
        elif sort == "max":
            TeamRankings.off_rank.append([team.Scores.maxOffScore,team.number])
        elif sort == "min":
            TeamRankings.off_rank.append([team.Scores.minOffScore,team.number])

    TeamRankings.off_rank.sort(reverse=rev)

    return TeamRankings.off_rank

def get_def_rank(sort="avg",rev=True):

    TeamRankings.def_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.numDef > 0:
                TeamRankings.def_rank.append([team.Scores.avgDefScore,team.number])
        elif sort == "max":
            if team.Info.numDef > 0:
                TeamRankings.def_rank.append([team.Scores.maxDefScore,team.number])
        elif sort == "min":
            if team.Info.numDef > 0:
                TeamRankings.def_rank.append([team.Scores.minDefScore,team.number])

    TeamRankings.def_rank.sort(reverse=rev)

    return TeamRankings.def_rank

def get_auto_rank(sort="avg",rev=True):

    TeamRankings.auto_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.autoHadAuto > 0:
                TeamRankings.auto_rank.append([team.Scores.avgAutoScore,team.number])
        elif sort == "max":
            if team.Info.autoHadAuto > 0:
                TeamRankings.auto_rank.append([team.Scores.maxAutoScore,team.number])
        elif sort == "min":
            if team.Info.autoHadAuto > 0:
                TeamRankings.auto_rank.append([team.Scores.minAutoScore,team.number])

    TeamRankings.auto_rank.sort(reverse=rev)

    return TeamRankings.auto_rank

def get_auto_Crosses_Defences_rank(sort="avg",rev=True):

    TeamRankings.auto_Crosses_Defences_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.autoHadAuto > 0:
                TeamRankings.auto_Crosses_Defences_rank.append([team.Scores.avgAutoCrossesDefencesScores,team.number])
        elif sort == "max":
            if team.Info.autoHadAuto > 0:
                TeamRankings.auto_Crosses_Defences_rank.append([team.Scores.maxAutoCrossesDefencesScores,team.number])
        elif sort == "min":
            if team.Info.autoHadAuto > 0:
                TeamRankings.auto_Crosses_Defences_rank.append([team.Scores.minAutoCrossesDefencesScores,team.number])

    TeamRankings.auto_Crosses_Defences_rank.sort(reverse=rev)

    return TeamRankings.auto_Crosses_Defences_rank

def get_auto_Low_Goal_rank(sort="avg",rev=True):

    TeamRankings.auto_Low_Goal_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.autoHadAuto > 0:
                TeamRankings.auto_Low_Goal_rank.append([team.Scores.avgAutoLowGoal,team.number])
        elif sort == "max":
            if team.Info.autoHadAuto > 0:
                TeamRankings.auto_Low_Goal_rank.append([team.Scores.maxAutoLowGoal,team.number])
        elif sort == "min":
            if team.Info.autoHadAuto > 0:
                TeamRankings.auto_Low_Goal_rank.append([team.Scores.minAutoLowGoal,team.number])

    TeamRankings.auto_Low_Goal_rank.sort(reverse=rev)

    return TeamRankings.auto_Low_Goal_rank

def get_auto_High_Goal_rank(sort="avg",rev=True):

    TeamRankings.auto_High_Goal_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.autoHadAuto > 0:
                TeamRankings.auto_High_Goal_rank.append([team.Scores.avgAutoHighGoal,team.number])
        elif sort == "max":
            if team.Info.autoHadAuto > 0:
                TeamRankings.auto_High_Goal_rank.append([team.Scores.maxAutoHighGoal,team.number])
        elif sort == "min":
            if team.Info.autoHadAuto > 0:
                TeamRankings.auto_High_Goal_rank.append([team.Scores.minAutoHighGoal,team.number])

    TeamRankings.auto_High_Goal_rank.sort(reverse=rev)

    return TeamRankings.auto_High_Goal_rank

def get_tele_rank(sort="avg",rev=True):

    TeamRankings.tele_rank = []

    for team in Team.team_list:
        if sort == "avg":
            TeamRankings.tele_rank.append([team.Scores.avgTeleScore,team.number])
        elif sort == "max":
            TeamRankings.tele_rank.append([team.Scores.maxTeleScore,team.number])
        elif sort == "min":
            TeamRankings.tele_rank.append([team.Scores.minTeleScore,team.number])

    TeamRankings.tele_rank.sort(reverse=rev)

    return TeamRankings.tele_rank

def get_tele_Defences_Damage_rank(sort="avg",rev=True):

    TeamRankings.tele_Defences_Damage_rank = []

    for team in Team.team_list:
        if sort == "avg":
            TeamRankings.tele_Defences_Damage_rank.append([team.Scores.avgTeleDefencesDamageScore,team.number])
        elif sort == "max":
            TeamRankings.tele_Defences_Damage_rank.append([team.Scores.maxTeleDefencesDamageScore,team.number])
        elif sort == "min":
            TeamRankings.tele_Defences_Damage_rank.append([team.Scores.minTeleDefencesDamageScore,team.number])

    TeamRankings.tele_Defences_Damage_rank.sort(reverse=rev)

    return TeamRankings.tele_Defences_Damage_rank

def get_tele_Low_Goal_rank(sort="avg",rev=True):

    TeamRankings.tele_Low_Goal_rank = []

    for team in Team.team_list:
        if sort == "avg":
            TeamRankings.tele_Low_Goal_rank.append([team.Scores.avgTeleLowGoal,team.number])
        elif sort == "max":
            TeamRankings.tele_Low_Goal_rank.append([team.Scores.maxTeleLowGoal,team.number])
        elif sort == "min":
            TeamRankings.tele_Low_Goal_rank.append([team.Scores.minTeleLowGoal,team.number])

    TeamRankings.tele_Low_Goal_rank.sort(reverse=rev)

    return TeamRankings.tele_Low_Goal_rank

def get_tele_High_Goal_rank(sort="avg",rev=True):

    TeamRankings.tele_High_Goal_rank = []

    for team in Team.team_list:
        if sort == "avg":
            TeamRankings.tele_High_Goal_rank.append([team.Scores.avgTeleHighGoal,team.number])
        elif sort == "max":
            TeamRankings.tele_High_Goal_rank.append([team.Scores.maxTeleHighGoal,team.number])
        elif sort == "min":
            TeamRankings.tele_High_Goal_rank.append([team.Scores.minTeleHighGoal,team.number])

    TeamRankings.tele_High_Goal_rank.sort(reverse=rev)

    return TeamRankings.tele_High_Goal_rank



def get_w_rank(sort="avg",rev=True):

    TeamRankings.w_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
                TeamRankings.w_rank.append([team.Scores.avgWScore,team.number])
        elif sort == "max":
                TeamRankings.w_rank.append([team.Scores.maxWScore,team.number])
        elif sort == "min":
                TeamRankings.w_rank.append([team.Scores.minWScore,team.number])

    TeamRankings.w_rank.sort(reverse=rev)

    return TeamRankings.w_rank

def get_wo_rank(sort="avg",rev=True):

    TeamRankings.wo_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.numOff > 0:
                TeamRankings.wo_rank.append([team.Scores.avgWOScore,team.number])
        elif sort == "max":
            if team.Info.numOff > 0:
                TeamRankings.wo_rank.append([team.Scores.maxWOScore,team.number])
        elif sort == "min":
            if team.Info.numOff > 0:
                TeamRankings.wo_rank.append([team.Scores.minWOScore,team.number])

    TeamRankings.wo_rank.sort(reverse=rev)

    return TeamRankings.wo_rank

def get_wd_rank(sort="avg",rev=True):

    TeamRankings.wd_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.numDef > 0:
                TeamRankings.wd_rank.append([team.Scores.avgWDScore,team.number])
        elif sort == "max":
            if team.Info.numDef > 0:
                TeamRankings.wd_rank.append([team.Scores.maxWDScore,team.number])
        elif sort == "min":
            if team.Info.numDef > 0:
                TeamRankings.wd_rank.append([team.Scores.minWDScore,team.number])

    TeamRankings.wd_rank.sort(reverse=rev)

    return TeamRankings.wd_rank


def get_foul_rank(sort="avg",rev=False): # foul rank default from least points to most

    TeamRankings.foul_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.hasFoul:
                TeamRankings.foul_rank.append([team.Scores.avgFoulScore,team.number])
        elif sort == "max":
            if team.Info.hasFoul:
                TeamRankings.foul_rank.append([team.Scores.maxFoulScore,team.number])
        elif sort == "min":
            if team.Info.hasFoul:
                TeamRankings.foul_rank.append([team.Scores.minFoulScore,team.number])

    TeamRankings.foul_rank.sort(reverse=rev)

    return TeamRankings.foul_rank

def get_tot_rank(sort="avg",rev=True):

    TeamRankings.tot_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            TeamRankings.tot_rank.append([team.Scores.avgTotalScore,team.number])
        elif sort == "max":
            TeamRankings.tot_rank.append([team.Scores.maxTotalScore,team.number])
        elif sort == "min":
            TeamRankings.tot_rank.append([team.Scores.minTotalScore,team.number])

    TeamRankings.tot_rank.sort(reverse=rev)

    return TeamRankings.tot_rank

#------------------------------------------------------------------------------
# predict functions
#   -- calculates predicted alliance scores predicts match outcomes
#------------------------------------------------------------------------------
def predict_scores(team1=None,team2=None,team3=None):
    #pOff1 = float(team1.pOff.rstrip("%"))/100
    #pOff2 = float(team2.pOff.rstrip("%"))/100
    #pOff3 = float(team3.pOff.rstrip("%"))/100
    #pDef1 = float(team1.pDef.rstrip("%"))/100
    #pDef2 = float(team2.pDef.rstrip("%"))/100
    #pDef3 = float(team3.pDef.rstrip("%"))/100
   
    try:
        offScore = ((team1.avgOff)+(team2.avgOff)+(team3.avgOff))
        defScore = ((team1.avgDef)+(team2.avgDef)+(team3.avgDef))
       
    except:
        offScore = 0
        defScore = 0

    expectedScores = [offScore, defScore]

    return expectedScores

def predict_outcome(teams=[]):

    team1 = teams[0]
    team2 = teams[1]
    team3 = teams[2]
    team4 = teams[3]
    team5 = teams[4]
    team6 = teams[5]

    # standard deviations
    Sigmas = [[],[],[],[],[],[]]

    for score in team1.Scores.tScores:
        Sigmas[0].append(((score-team1.avgTotal)**2)/len(team1.Scores.tScores))
    for score in team2.Scores.tScores:
        Sigmas[1].append(((score-team2.avgTotal)**2)/len(team2.Scores.tScores))
    for score in team3.Scores.tScores:
        Sigmas[2].append(((score-team3.avgTotal)**2)/len(team3.Scores.tScores))
    for score in team4.Scores.tScores:
        Sigmas[3].append(((score-team4.avgTotal)**2)/len(team4.Scores.tScores))
    for score in team5.Scores.tScores:
        Sigmas[4].append(((score-team5.avgTotal)**2)/len(team5.Scores.tScores))
    for score in team6.Scores.tScores:
        Sigmas[5].append(((score-team6.avgTotal)**2)/len(team6.Scores.tScores))

    r1 = math.sqrt(sum(Sigmas[0]))
    r2 = math.sqrt(sum(Sigmas[1]))
    r3 = math.sqrt(sum(Sigmas[2]))
    b1 = math.sqrt(sum(Sigmas[3]))
    b2 = math.sqrt(sum(Sigmas[4]))
    b3 = math.sqrt(sum(Sigmas[5]))
    
    mur = (float(1)/3)*(team1.avgTotal+team2.avgTotal+team3.avgTotal)
    mub = (float(1)/3)*(team4.avgTotal+team5.avgTotal+team6.avgTotal)
    
    rst = math.sqrt((float(1)/float(9))*(r1**2+r2**2+r3**2))
    bst = math.sqrt((float(1)/float(9))*(b1**2+b2**2+b3**2))
    
    if mur > mub:
        zval = (mur-mub)/math.sqrt((rst**2)+(bst**2)) if math.sqrt((rst**2)+(bst**2)) > 0 else 0
        perr = stats.lzprob(zval)
        perr = round(perr,4)
        return "Red Alliance: " + str(100*perr)
    
    else:
        zval = (mub-mur)/math.sqrt((rst**2)+(bst**2)) if math.sqrt((rst**2)+(bst**2)) > 0 else 0
        perr = stats.lzprob(zval)
        perr = round(perr, 4)
        return "Blue Alliance: " + str(100*perr)
