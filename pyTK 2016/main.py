from Tkinter import *
import tkFileDialog
import tkMessageBox
from view.windows import *
from controller.windows import *

from model import model, imports, calculate


class App(Frame):

    def import_data(self):
        imports.import_data(tkFileDialog.askopenfilename())
        self.imported = model.imported
        if self.imported:
            calculate.calculate_data()
        else:
            tkMessageBox.showinfo("Warning","Import Data Failed.")


    def import_pitData(self):
        imports.import_pitData(tkFileDialog.askopenfilename())
        self.pitImported = model.pitImported
        if self.pitImported:
            calculate.calculate_pit_data()
        else:
            tkMessageBox.showinfo("Warning","Import PitData Failed.")

    def clear_importData(self):
        imports.clear_importData()
        self.pitImported = False
        self.imported = False
        tkMessageBox.showinfo("INFO", "Data Cleared.")
        
    def teamdata(self):
        if self.imported:
            newWindow = Toplevel(self)
            controller = cteamdata.TeamDataController()
            teamdata = vteamdata.TeamData(newWindow,self,controller)
        else:
            tkMessageBox.showinfo("Warning","No data has been imported.")

    def ranking(self):
        if self.imported:
            newWindow = Toplevel(self)
            controller = cranking.RankingController()
            ranking = vranking.Ranking(newWindow,self,controller)
        else:
            tkMessageBox.showinfo("Warning","No data has been imported.")

    def search(self):
        if self.imported:
            newWindow = Toplevel(self)
            controller = csearch.SearchController()
            search = vsearch.Search(newWindow,self,controller)
        else:
            tkMessageBox.showinfo("Warning","No data has been imported.")
        
    def predict(self):
        if self.imported:
            newWindow = Toplevel(self)
            controller = cpredict.PredictController()
            predict = vpredict.Predict(newWindow,self,controller)
        else:
            tkMessageBox.showinfo("Warning","No data has been imported.")

    def choose(self):
        if self.imported:
            newWindow = Toplevel(self)
            controller = cchoose.ChooseController()
            choose = vchoose.Choose(newWindow,self,controller)
        else:
            tkMessageBox.showinfo("Warning","No data has been imported.")

    def startup(self):
        # create a frame to put the window buttons in
        self.wbf = Frame(self)
        self.wbf.pack(side=RIGHT,padx=5)

        self.teamdataB = Button(self.wbf, text="Team Data",
                               command=self.teamdata)
        self.teamdataB.pack(side=TOP,pady=5)

        self.rankingB = Button(self.wbf, text="Ranking",
                              command=self.ranking)
        self.rankingB.pack(side=TOP,pady=5)
        self.searchB = Button(self.wbf, text="Search",
                              command=self.search)
        self.searchB.pack(side=TOP,pady=5)
        self.predictB = Button(self.wbf,text="Predict",
                               command=self.predict)
        self.predictB.pack(side=TOP,pady=5)
        self.chooseB = Button(self.wbf,text="Choose",
                              command=self.choose)
        self.chooseB.pack(side=TOP,pady=5)

        # create a frame to put the import buttons in
        self.importFrame = Frame(self)
        self.importFrame.pack(side=LEFT,padx=5)

        self.importB = Button(self.importFrame, text="Import Data",
                              command=self.import_data)
        self.importB.pack(side=TOP,pady=5)

        self.importA = Button(self.importFrame, text="Import pitData",
                              command=self.import_pitData)
        self.importA.pack(side=TOP,pady=5)

        self.clearImportsB = Button(self.importFrame, text="Clear Imports",
                                    command=self.clear_importData)
        self.clearImportsB.pack(side=TOP,pady=5)

        

    def __init__(self,parent=None):
        self.parent = parent
        self.imported = False

        self.parent.title("SAD 1.0")
        self.parent.geometry("+0+0")
        Frame.__init__(self,parent)
        self.pack()

        self.startup()

root = Tk()

app = App(root)

app.mainloop()
