#BATSMAN

def runsBatsman(score, run):
    if(run >= 0 and run <=10):
        score += run*1
    elif(run > 10 and run <= 30):
        score += 10 + 0.5*(run - 10)
    elif(run > 30 and run <= 50):
        score += 20 + 0.5*(run - 30)
    else:
        score += 40
    return score

def strikeRateBatsman(score, str, ball):
    if(str <= 50 and ball > 5):
        score -= 5
    elif(str > 50 and str <= 100):
        score += 0.1*(str)
    elif(str > 100 and str <= 150):
        score += 5 + 0.1*(str - 100)
    elif(str > 150 and str <= 200):
        score += 10 + 0.1*(str - 150)
    else:
        score += 20
    return score

def boundariesBatsman(score, boundr):
    if(boundr >= 0 and boundr <=3):
        score += 0
    elif(boundr > 3 and boundr <= 7):
        score += 1.25*(boundr - 3)
    elif(boundr > 7 and boundr <= 10):
        score += 5 + (5/3)*(boundr - 7)
    elif(boundr > 10 and boundr <= 15):
        score += boundr
    else:
        score += 20
    return score

def teamContributionBatsman(score, contri):
    if(contri >= 0 and contri <=20):
        score += 0.25*(contri)
    elif(contri > 20 and contri <= 40):
        score += 5 + 0.25*(contri - 20)
    elif(contri > 40 and contri <= 60):
        score += 10 + 0.25*(contri - 40)
    elif(contri > 60):
        score += 20
    else:
        score += 20
    return score


def totalPointsBatsman(run, ball, str, boundr, contri):
    score = 0
    score = runsBatsman(score, run)
    score = strikeRateBatsman(score, str, ball)
    score = boundariesBatsman(score, boundr)
    score = teamContributionBatsman(score, contri)
    return score


#BOWLER

def wicketsBowler(score, wkt):
    if(wkt == 0):
        score += 0
    elif(wkt == 1):
        score += 10
    elif(wkt == 2):
        score += 20
    elif(wkt == 3):
        score += 30
    else:
        score += 40
    return score

def economyBowler(score, econ, over):
    if(econ <= 5 and over > 2):
        score += 20
    elif(econ <= 6):
        score += 17.5
    elif(econ > 6 and econ <= 7):
        score += 12.5
    elif(econ > 7 and econ <= 8):
        score += 5
    elif(econ > 8 and econ < 10):
        score += 0
    else:
        score += -5
    return score

def averageBowler(score, avg):
    if(avg < 10):
        score += 20
    elif(avg >= 10 and avg <= 20):
        score += 20 - 0.5*(avg - 10)
    elif(avg > 20 and avg <= 30):
        score += 15 - (avg - 20)
    elif(avg > 30):
        score += 2
    else:
        score += 0
    return score

def teamContributionBowler(score, contri):
    if(contri >= 0 and contri <=20):
        score += 0.25*(contri)
    elif(contri > 20 and contri <= 40):
        score += 5 + 0.25*(contri - 20)
    elif(contri > 40 and contri <= 60):
        score += 10 + 0.25*(contri - 40)
    else:
        score += 20
    return score


def totalPointsBowler(wkt, over, econ, avg, contri):
    score = 0
    score = wicketsBowler(score, wkt)
    score = economyBowler(score, econ, over)
    score = averageBowler(score, avg)
    score = teamContributionBowler(score, contri)
    return score



#ALL ROUNDER

def runsAllRounder(score, run):
    if(run >= 0 and run <= 5):
        score += 0
    elif(run > 5 and run <= 15):
        score += run - 5
    elif(run > 15 and run <= 30):
        score += 10 + (2/3)*(run - 15)
    else:
        score += 20
    return score

def wicketsAllRounder(score, wkt):
    if(wkt == 0):
        score += 0
    elif(wkt == 1):
        score += 5
    elif(wkt == 2):
        score += 10
    elif(wkt == 3):
        score += 15
    else:
        score += 20
    return score


def strikeRateAllRounder(score, str, ball):
    if(str <= 100 and ball > 5):
        score = 0
    elif(str > 100 and str <= 125):
        score += 0.2*(str - 100)
    elif(str > 125 and str <= 175):
        score += 5 + 0.1*(str - 125)
    elif(str > 175 and str <= 250):
        score += 10 + (1/15)*(str - 175)
    else:
        score += 20
    return score


def economyAllRounder(score, econ, over):
    if(econ <= 5 and over > 2):
        score += 20
    elif(econ > 5 and econ <= 7):
        score += 15
    elif(econ > 7 and econ <= 9):
        score += 10
    elif(econ > 9 and econ <= 10):
        score += 5
    else:
        score += -5
    return score


def teamContributionAllRounder(score, contri):
    if(contri >= 0 and contri <=20):
        score += 0.25*(contri)
    elif(contri > 20 and contri <= 40):
        score += 5 + 0.25*(contri - 20)
    elif(contri > 40 and contri <= 60):
        score += 10 + 0.25*(contri - 40)
    elif(contri > 60):
        score += 20
    else:
        score += 20
    return score


def totalPointsAllRounder(run, ball, str, wkt, over, econ, contri):
    score = 0
    score = runsAllRounder(score, run)
    score = wicketsAllRounder(score, wkt)
    score = strikeRateAllRounder(score, str, ball)
    score = economyAllRounder(score, econ, over)
    score = teamContributionBowler(score, contri)
    return score
