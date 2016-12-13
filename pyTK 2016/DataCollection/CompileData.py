
try:
    dataAll = open("C:\Workspace2016\Scouting2016\pyTK 2016\DataCollection\dataAll.txt","w")
    dataAll.close()
    print "DataAll Cleared"
    data1 = open("C:\Workspace2016\Scouting2016\pyTK 2016\DataCollection\data1.txt","r")
    lines1 = data1.readlines()
    print "Data1 read"
    data2 = open("C:\Workspace2016\Scouting2016\pyTK 2016\DataCollection\data2.txt","r")
    lines2 = data2.readlines()
    print "Data2 read"
    data3 = open("C:\Workspace2016\Scouting2016\pyTK 2016\DataCollection\data3.txt","r")
    lines3 = data3.readlines()
    print "Data3 read"
    data4 = open("C:\Workspace2016\Scouting2016\pyTK 2016\DataCollection\data4.txt","r")
    lines4 = data4.readlines()
    print "Data4 read"
    data5 = open("C:\Workspace2016\Scouting2016\pyTK 2016\DataCollection\data5.txt","r")
    lines5 = data5.readlines()
    print "Data5 read"
    data6 = open("C:\Workspace2016\Scouting2016\pyTK 2016\DataCollection\data6.txt","r")
    lines6 = data6.readlines()
    print "Data6 read"
    dataAll = open("C:\Workspace2016\Scouting2016\pyTK 2016\DataCollection\dataAll.txt","w")
    linesAll = lines1 + lines2 + lines3 + lines4 + lines5 + lines6
    print "Compiling Data"
    dataAll.writelines(linesAll)
    dataAll.close()
    print "Data Compiled"
except:
    pass
    print "Failed to Compile"
