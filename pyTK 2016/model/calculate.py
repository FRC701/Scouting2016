#------------------------------------------------------------------------------
# calculate module
#   -- functions for handling data input, output, and caclulations
#------------------------------------------------------------------------------
import math
from statlib import stats

from team import *
from entry import *

#------------------------------------------------------------------------------
# calculate_data function
#   -- handles data and stores it to the teams
#------------------------------------------------------------------------------
def calculate_data():
    
    for entry in Entry.entries:
        entry.sort()

    # get basic team data from the entries
    for entry in Entry.entries:
        done = False
        for team in Team.team_list:
            if team.number == entry.team:
                assign_team_values(team, entry)

                done = True
        if done == False:
            newTeam = Team(entry.team)
            print "Added Team #: " + str(entry.team)

            assign_team_values(newTeam,entry)

    # get the rest of the information about each team
    for team in Team.team_list:
        team.get_details()

#------------------------------------------------------------------------------
# assign_basic_team_values function
#   -- assigns some basic values from an entry to a team
#   -- still needs error handling
#------------------------------------------------------------------------------
def assign_team_values(team, entry):
    team.Info.matches.append(entry.match)
    team.Info.noShow += int(entry.noShow)

    team.Info.autoHadAuto += int(entry.autoHadAuto)
    team.Info.autoReachesDefences += int (entry.autoReacheesDefences)
    team.Info.autoReachesDefences.append(float(entry.autoReachesDefencesScore))
    team.Info.autoCrossesDefences += int (entry.autoReachesDefences)
    team.Info.autoCrossesdefencesScore.append(float(entry.autoCrosssesDefencesScore))
    team.Info.autoLowGoal.append(float(entry.autoLowGoal))
    team.Info.autoHighGoal.append(float(entry.autoHighGoal))
    team.Info.autoOther += int(entry.autoOther)

    team.Info.teleLowBar.append(float(entry.teleLowBarDamage))
    team.Info.telePortcullis.append(float(entry.telePortcullisDamage))
    team.Info.teleChevaldeFrise.append(float(entry.teleChevaldeFriseDamage))
    team.Info.teleMoat.append(float(entry.teleMoatDamage))
    team.Info.teleRamparts.append(float(entry.teleRampartsDamage))
    team.Info.teleDrawbridge.append(float(entry.teleDrawbridgeDamage))
    team.Info.teleSallyPort.append(float(entry.teleSallyPortDamage))
    team.Info.teleRockWall.append(float(entry.teleRockWallDamage))
    team.Info.teleRoughTerrain.append(float(entry.teleRoughTerrainDamage))
    team.Info.teleDefencesDamageScore.append(float(entry.teleDefencesDamageScore))

    team.Info.teleLowGoal.append(float(entry.teleLowGoal))
    team.Info.teleHighGoal.append(float(entry.teleHighGoal))

    team.Info.postFouls.append(float(entry.postFouls))
    team.Info.postTechFouls.sppend(float(entry.postTechFoals))
    team.Info.postRedCard += int(entry.postRedCard)
    team.Info.postYellowCard += int(entry.postYellowCard)
    team.Info.postDisabled += int(entry.postDisabled)
    team.Info.postPlayedDefensively += int(entry.postPlayedDefensively)
    team.Info.postCapture += int(entry.postCapture)
    team.Info.postBreached += int (entry.postBreached)
    team.Info.postChallengeStateScore.append(float(entry.postChallengeStateScore))
    team.Info.NotAttemptedC += int (entry.NotAttempedC)
    team.Info.AttemptedC += int (entry.AttemptedC)
    team.Info.SuccessfulC += int (entry.SuccessfulC)
    team.Info.postScaleStateScore.append(float(entry.postScaleStateScore))
    team.Info.NotAttemptedS += int (entry.NotAttempedS)
    team.Info.AttemptedS += int (entry.AttemptedS)
    team.Info.SuccessfulS += int (entry.SuccessfulS)

    team.Info.scoredInTele += int(entry.scoredInTele)
    team.Info.scoredInAuto += int(entry.scoredInAuto)
    team.Info.hasFoul += int(entry.hasFoul)

    team.Scores.oScores.append(entry.offensiveScore)
    team.Scores.autoScores.append(entry.autoScore)
    team.Scores.autoCrossesDefencesScore.append(entry.autoCrossesDefencesScore)
    team.Scores.autoLowGoal.append(entry.autoLowGoal)
    team.Scores.autoHighGoal.append(entry.autoHighGoal)
    team.Scores.teleScores.append(entry.teleScore)
    team.Scores.teleDefencesDamageScore.append(entry.teleDefencesDamageScore)
    team.Scores.teleLowGoal.append(entry.teleLowGoal)
    team.Scores.teleHighGoal.append(entry.teleHighGoal)
    #team.Scores.postChallengeStateScore.append(entry.postChallengeStateScore)
    team.Scores.postChallengeStateSuccessful.append(entry.SuccessfulC)
    #team.Scores.postScaleStateScore.append(entry.postScaleStateScore)
    team.Scores.postScaleStateSuccessful.append(entry.SuccessfulS)
    team.Scores.foulScores.append(entry.foulScore)
    team.Scores.tScores.append(entry.totalScore)

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

def get_auto_Crosses_Defence_rank(sort="avg",rev=True):

    TeamRankings.auto_Crosses_Defence_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.autoHadAuto > 0:
                TeamRankings.auto_Crosses_Defences_rank.append([team.Scores.avgAutoCrossesDefencesScore,team.number])
        elif sort == "max":
            if team.Info.autoHadAuto > 0:
                TeamRankings.auto_Crosses_Defences_rank.append([team.Scores.maxAutoCrossesDefencesScore,team.number])
        elif sort == "min":
            if team.Info.autoHadAuto > 0:
                TeamRankings.auto_Crosses_Defences_rank.append([team.Scores.minAutoCrossesDefencesScore,team.number])

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
        if sort == "avg":s
            TeamRankings.tele_rank.append([team.Scores.avgTeleScore,team.number])
        elif sort == "max":
            TeamRankings.tele_rank.append([team.Scores.maxTeleScore,team.number])
        elif sort == "min":
            TeamRankings.tele_rank.append([team.Scores.minTeleScore,team.number])

    TeamRankings.tele_rank.sort(reverse=rev)

    return TeamRankings.tele_rank

def get_tele_Defences_Damage_Score_rank(sort="avg",rev=True):

    TeamRankings.tele_Defences_Damage_Score_rank = []

    for team in Team.team_list:
        if sort == "avg":
            TeamRankings.tele_Defences_Damage_Score_rank.append([team.Scores.avgTeleDefencesDamageScore,team.number])
        elif sort == "max":
            TeamRankings.tele_Defences_Damage_Score_rank.append([team.Scores.maxTeleDefencesDamageScore,team.number])
        elif sort == "min":
            TeamRankings.tele_Defences_Damage_Score_rank.append([team.Scores.minTeleDefencesDamageScore,team.number])

    TeamRankings.tele_Defences_Damage_Score_rank.sort(reverse=rev)

    return TeamRankings.tele_Defences_Damage_Score_rank

def get_tele_Low_Goal_rank(sort="avg",rev=True):

    TeamRankings.tele_Low_Goal_rank = []

    for team in Team.team_list:
        if sort == "avg":
            TeamRankings.tele_Low_Goal_rank.append([team.Scores.avgTeleBouldersInLowGoal,team.number])
        elif sort == "max":
            TeamRankings.tele_Low_Goal_rank.append([team.Scores.maxTeleBouldersInLowGoal,team.number])
        elif sort == "min":
            TeamRankings.tele_Low_Goal_rank.append([team.Scores.minTeleBouldersInLowGoal,team.number])

    TeamRankings.tele_Low_Goal_rank.sort(reverse=rev)

    return TeamRankings.tele_Low_Goal_rank

def get_tele_High_Goal_rank(sort="avg",rev=True):

    TeamRankings.tele_High_Goal_rank = []

    for team in Team.team_list:
        if sort == "avg":
            TeamRankings.tele_High_Goal_rank.append([team.Scores.avgTeleBouldersInHighGoal,team.number])
        elif sort == "max":
            TeamRankings.tele_High_Goal_rank.append([team.Scores.maxTeleBouldersInHighGoal,team.number])
        elif sort == "min":
            TeamRankings.tele_High_Goal_rank.append([team.Scores.minTeleBouldersInHighGoal,team.number])

    TeamRankings.tele_High_Goal_rank.sort(reverse=rev)

    return TeamRankings.tele_High_Goal_rank

def get_post_Challenge_State_Successful_rank(sort="avg",rev=False):

    TeamRankings.post_Challenge_State_Successful_rank = []

    for team in Team.team_list:
        if sort == "avg":
            TeamRankings.post_Challenge_State_Successful_rank.append([team.Scores.avgPostChallengeStateSuccessful,team.number])
        elif sort == "max":
            TeamRankings.post_Challenge_State_Successsful_rank.append([team.Scores.maxPostChallengeStateSuccessful, team.number])
        elif sort == "min":
            TeamRankings.post_Challenge_State_Successsful_rank.append([team.Scores.minPostChallengeStateSuccessful, team.number])

    TeamRankings.post_Challenge_State_Successsful_rank.sort(reverse=rev)

    return TeamRankings.post_Challenge_State_Successsful_rank

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
    try:
        # make each team a confidence internal over proportion means and use
        # that confidence interval to calculate a total range of scores (from lowest
        # theoretical to highest theoretical, then take the center of that
        # total range and place it as the expected offensive score
        offScore = (team1.avgOff+team2.avgOff+team3.avgOff)
    except:
        offScore = 0

    expectedScores = [offScore]

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
