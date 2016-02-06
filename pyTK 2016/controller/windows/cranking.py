#------------------------------------------------------------------------------
# cranking module
#   -- contains the functions and classes for controlling the ranking window
#------------------------------------------------------------------------------
from Tkinter import *

from model.calculate import *

#------------------------------------------------------------------------------
# get_none function
#   -- passes through so that a None list can delete all of its contents
#------------------------------------------------------------------------------
def get_none(sort=None,rev=None):
    pass

#------------------------------------------------------------------------------
# RankingController Class
#   -- used to get and set data for Ranking objects and their Listings
#------------------------------------------------------------------------------
class RankingController():

    # use these to index values to display, use the system: ("key",term)
    # where key corredsponds to a value in self.rankingTypes and term is
    # the function to call when that option is selected
    rankingTypes = ["None",
                    "Offensive Score",
                    "Defensive Score",
                    "Total Score",
                    "Auto Score",
                    "Auto Crosses Defences Score","Auto Boulders in Low Goal Score","Auto Boulders in High Goal Score",
                    "Tele Score",
                    "Tele Defences Damage Score","Tele Boulders in Low Goal Score","Tele Boulders in High Goal Score","Tele Times Challenge was Successful", "Tele Times Scaling was Successful",
                    "Weighted Score", "Offensive Weighted Score", "Defensive Weighted Score", "Foul Score"]

    rankingIndex = [("None",get_none),
                    ("Offensive Score",get_off_rank),
                    ("Defensive Score",get_def_rank),
                    ("Total Score",get_tot_rank),
                    ("Auto Score",get_auto_rank),
                    ("Auto Crosses Defences Score",get_auto_Crosses_Defences_rank),
                    ("Auto Boulders in Low Goal Score",get_auto_Low_Goal_rank),
                    ("Auto Boulders in High Goal Score",get_auto_High_Goal_rank),
                    ("Tele Score",get_tele_rank),
                    ("Tele Defences Damage Score",get_tele_Defences_Damage_rank),
                    ("Tele Boulders in Low Goal Score",get_tele_Low_Goal_rank),
                    ("Tele Boulders in High Goal Score",get_tele_High_Goal_rank),
                    ("Tele Times Challenge was Successful",get_post_Challenge_State_Successful_rank),
                    ("Tele Times Scaling was Successful",get_post_Scale_State_Successful_rank),
                    ("Weighted Score",get_w_rank),
                    ("Offensive Weighted Score",get_wo_rank),
                    ("Defensive Weighted Score",get_wd_rank),
                    ("Foul Score",get_foul_rank)]

    sortOptions = [("Maximum","max"),("Average","avg"),("Minimum","min")]

    def __init__(self):
        self.sort = StringVar()
        self.sort.set("avg")
        self.rev = BooleanVar()
        self.rev.set(1)
        self.data = None

    def load_rankings(self,kind="None"):
        for value, func in self.rankingIndex:
            if value==kind:
                self.data = func(sort=self.sort.get(),rev=self.rev.get())
                break
