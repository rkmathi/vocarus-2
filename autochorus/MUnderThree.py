# -*- coding: utf-8 -*-

import sys
import CTone

def autoUnderThree(hamList):
    solutionSpace = 12 #候補は12本で処理しますか，，
    gomi = CTone.CTone(-1, hamList[0].key)
    oyasumi = "(_ _)zZZ"

    resultAr = []
    currentAr = []

    predictionN = []
    predictionC = []

    penaltyCurrentAr = []
    penaltySumAr = []
    for index in range(0, solutionSpace):
        resultAr.append([]) #解
        currentAr.append([]) #現在の解候補たち
        predictionN.append([gomi, gomi, gomi, gomi])
        predictionC.append([gomi, gomi, gomi, gomi])
        penaltyCurrentAr.append(0) #ぺなるてぃなう
        penaltySumAr.append(0) #ぺなるてぃ積算

    # fw = open('underr3.txt', 'w')

    for ham in hamList: #predictionN[iN]を頼りに連結すべきresult[]を選びますー
        predictionN = ham.getUnderThreeSolutionArray() #候補列挙

        if(ham.chord == 0): #おやすみの場合，，，
            for iN in range(0, solutionSpace):
                #おやすみの場合は固定-1なので安心ですー
                currentAr[iN] = resultAr[iN] + [predictionN[iN]]
        else:
            for iN in range(0, solutionSpace):
                minimumpenalty = sys.maxint #最小値ですー
                selected = 0
                for iC in range(0, solutionSpace):
                    penalty = calculatePenaltyUnderThree(predictionC[iC],
                                                         predictionN[iN],
                                                         ham.chord)
                    penalty = penalty + penaltySumAr[iC]

                    if penalty < minimumpenalty: #ペナルティを最小化するよーに
                        minimumpenalty = penalty
                        selected = iC

                #＼選ばれたのはresult[selected]でした，，，／
                currentAr[iN] = resultAr[selected] + [predictionN[iN]]
                penaltyCurrentAr[iN] = minimumpenalty
            predictionC = predictionN #現在に持ってきます

        for index in range(0, solutionSpace):
            resultAr[index] = currentAr[index]
            penaltySumAr[index] = penaltyCurrentAr[index]

#でばっぐしゅつりょく
            #for part in range(0, 4):
                #print ""
                # fw.write('\n')
                #for time in range(0, len(resultAr[index])):
                    #if (resultAr[index][time][part].degree == -1):
                    #    print oyasumi,
                        # fw.write(oyasumi)
                    #else:
                    #    print "("+str(resultAr[index][time][part].degree)+","+\
                    #             str(resultAr[index][time][part].octave)+")",
                        # fw.write("("+str(resultAr[index][time][part].degree)+
                        #       ","+str(resultAr[index][time][part].octave)+")")
            #print u"pena: ", penaltySumAr[index]
            # fw.write("pena: "+str(penaltySumAr[index])+"\n")

        #print ""
        # fw.write('\n')
    # fw.close()

    #結果～
    minimumpenalty = sys.maxint #最小値ですー
    selected = 0 #選ばれたのｈ（ｒｙ

    for iC in range(0, solutionSpace):
        penalty = penaltySumAr[iC]
        if penalty<minimumpenalty: #ペナルティを最小化するよーに，，，，
            minimumpenalty = penalty
            selected = iC

    for time in range(0, len(hamList)):
        for part in range(1, 4):
            hamList[time].note[part] = resultAr[selected][time][part]
        # hamList[time].show()

    return

#ルールが読みやすくなって生まれ変わりました！！
def calculatePenaltyUnderThree(current, next, chord):
    penalty = 0

    for part in range(1, 3): #内声に関して
        diff = ((next[part].octave*7+next[part].degree) -
                (next[3].octave*7+next[3].degree))
        if(diff<0): #Bassを下回るのはよろしくない。
            penalty += 10 * (-diff)

        if(chord != next[3].degree): #転回形（一転しかないはずだけどね）
            #一転での三音重複は不可
            if(next[0].degree == next[3].degree or 
               next[1].degree == next[3].degree):
                penalty += 1000 #内声配置の都合上おかしい値を返すので高めに設定

    #休符であれば以降の前の音と関係するペナルティはかけないように、、、
    if(current[2].degree == -1):
        return penalty

    motion = [0,0,0,0] #進行情報
    for part in range(0, 4): #全部声部に対して
        #度数差分を符号付きで
        motion[part] = ((next[part].octave*7+next[part].degree) -
                        (current[part].octave*7+current[part].degree))

    for part in range(1, 4): #下三声に対して
        penalty += abs((motion[part]) / 2) #差分ペナルテぃ

        if(current[part].degree == 7): #導音ならば
            #限定進行すべし。
            if(current[part].octave+1!=next[part].octave or next[part].degree!=1):
                #Ⅶ→ⅢがあるのでBassのD進行は許しておく
                if(not(part==3 and next[3].degree == 3 and (next[0].degree==7 or
                                                            next[1].degree==7 or
                                                            next[2].degree==7))):
                    penalty += 100

    for part in range(0, 3): #上三声に対して
        #連続１・８度はあうと（本来総当たりしたいとこですががが（＾ω＾＃
        if(current[part].degree == current[3].degree and
           next[part].degree == next[3].degree):
            #保留またはオクターブ進行の場合は許しておく
            if((not(current[part].degree == next[part].degree or
                    current[3].degree == next[3].degree)) or
                    (motion[part]<0 and motion[3]<0 or
                     motion[part]>0 and motion[3]>0)): #（ただし並行以外に限る）
                penalty += 100

    if(abs(motion[0])>2): #ソプラノが跳躍進行するとき
        #バスとソプラノが並行のとき
        if(motion[0]<0 and motion[3]<0 or motion[0]>0 and motion[3]>0):
            #並達５・８度を禁ずる
            if((next[0].degree - next[3].degree+7)%7 + 1 == 5 or
                next[0].degree - next[3].degree + 1== 1):
                penalty += 100

    return penalty

