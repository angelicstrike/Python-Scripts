from pylab import *

historyList = []
timeList = []

readHistory = open("/home/james/ProgrammingProjects/power/history.txt", "r")

for line in readHistory.readlines():
    splitter = line.strip("\n").split(" ")
    historyList.append(splitter[0])
    timeList.append(splitter[1])

a = array(historyList)
b = array(timeList)

plot(b, a)
show()
