# -*- coding: utf-8 -*-

import sys

def autoChord(hamList):
    solutionSpace = 3
    oyasumi = "z"

    resultAr = []
    currentAr = []

    predictionN = []
    predictionC = []

    penaltyCurrentAr = []
    penaltySumAr = []
    for index in range(0, solutionSpace):
        resultAr.append([]) #解
        currentAr.append([]) #現在の解候補たち
        predictionN.append(0)
        predictionC.append(0)
        penaltyCurrentAr.append(0) #ぺなるてぃなう
        penaltySumAr.append(0) #ぺなるてぃ積算

    #fw = open('chord3.txt', 'w')
    nowtick = 0

    for ham in hamList: #predictionN[iN]を頼りに連結すべきresult[]を選びますー
        predictionN = ham.getChordSolutionArray() #候補列挙
        nowtick += ham.length

        if(ham.note[0].degree == -1): #おやすみの場合，，，
            for iN in range(0, solutionSpace):
                #おやすみの場合は固定0なので安心ですー
                currentAr[iN] = resultAr[iN] + [predictionN[iN]]
        else:
            for iN in range(0, solutionSpace):
                minimumpenalty = sys.maxint #最小値ですー
                selected = 0
                for iC in range(0, solutionSpace):
                    penalty = calculatePenaltyChord(predictionC[iC], predictionN[iN], nowtick)
                    penalty = penalty + penaltySumAr[iC]

                    if penalty<minimumpenalty : #ペナルティを最小化するよーに，，，，
                        minimumpenalty = penalty
                        selected = iC
                # ＼選ばれたのはresult[selected]でした，，，／
                currentAr[iN] = resultAr[selected] + [predictionN[iN]]
                penaltyCurrentAr[iN] = minimumpenalty
            predictionC = predictionN #現在に持ってきます

        for index in range(0, solutionSpace):
            resultAr[index] = currentAr[index]
            penaltySumAr[index] = penaltyCurrentAr[index]


            # でばっぐしゅつりょく
            #print ""
            #fw.write('\n')
            #for time in range(0, len(resultAr[index])):
            #    if (resultAr[index][time] == 0):
            #        print oyasumi,
            #        #fw.write(oyasumi)
            #    else:
            #        print "("+str(resultAr[index][time])+")",
            #        #fw.write("("+str(resultAr[index][time])+")")
        #print u"pena: ", penaltySumAr[index]
        #fw.write("pena: "+str(penaltySumAr[index])+"\n")

        #print ""
        #fw.write('\n')

    #fw.close()

    # 結果～
    minimumpenalty = sys.maxint #最小値ですー
    selected = 0 #選ばれたのｈ（ｒｙ

    for iC in range(0, solutionSpace):
        penalty = penaltySumAr[iC]
        if penalty<minimumpenalty: #ペナルティを最小化するよーに，，，，
            minimumpenalty = penalty
            selected = iC

    for time in range(0, len(hamList)):
        hamList[time].chord = resultAr[selected][time]
        # hamList[time].show()

    return


#こっちもルールは分離しました
def calculatePenaltyChord(current, next, nowbeat):
    statedic = {"MURI":0, "HOLD":1, "PROG":2, "UNST":3, "SUBS":4}
    harmonymatrix = [
        ["HOLD","PROG","UNST","UNST","UNST","UNST","UNST","UNST"],
        ["MURI","HOLD","UNST","UNST","UNST","UNST","UNST","UNST"],
        ["MURI","MURI","HOLD","MURI","MURI","PROG","MURI","MURI"],
        ["MURI","MURI","MURI","HOLD","MURI","MURI","PROG","MURI"],
        ["MURI","PROG","PROG","MURI","HOLD","PROG","UNST","PROG"],
        ["MURI","PROG","MURI","MURI","MURI","HOLD","SUBS","MURI"],
        ["MURI","MURI","PROG","SUBS","SUBS","SUBS","HOLD","SUBS"],
        ["MURI","MURI","MURI","SUBS","MURI","MURI","MURI","HOLD"]]

    state = harmonymatrix[current][next]
    penalty = 0
    if state=="MURI":
        penalty = 100
        return penalty
    elif state=="HOLD":
        penalty = 0
        if nowbeat%4 == 0: penalty+=2
        return penalty
    elif state=="PROG":
        penalty = 2
        if nowbeat%4 == 0: penalty-=1
        if nowbeat%2 == 0: penalty-=1
        return penalty
    elif state=="UNST":
        penalty = 4
        if nowbeat%4 == 0: penalty+=1
        if nowbeat%2 == 0: penalty+=1
        return penalty
    elif state=="SUBS":
        return 4

    assert 1==2 #なんじゃこりゃ
    return 1000

