import time

if(__name__ == '__main__'):
    chargeReader = open("/sys/class/power_supply/CMB1/charge_now")
    chargeNow = chargeReader.readline()
    
    designReader = open("/sys/class/power_supply/CMB1/charge_full_design")
    chargeFullDesign = designReader.readline()
    
    chargeRemaining = float(chargeNow)/float(chargeFullDesign)
    chargeRemaining = chargeRemaining*100

    writeHistory = open("/home/james/ProgrammingProjects/power/history.txt", "a")
    writeHistory.write(str(chargeRemaining) + " " + str(time.time()) + '\n')
    writeHistory.close()

    print str(chargeRemaining) + '%'
