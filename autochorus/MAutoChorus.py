# -*- coding: utf-8 -*-

import copy
import math
import CTone
import CHarmony
import CQuantizedNote
import MUnderThree
import MChord

def execAutoChorus_dumy(anotes):
    result = []
    for part in range(0, 4):
        result.append(copy.deepcopy(anotes))
    for soprano in result[0]:
        soprano.note = 84
    for soprano in result[1]:
        soprano.note = 79
    for soprano in result[2]:
        soprano.note = 76
    for soprano in result[3]:
        soprano.note = 72
    return result


def execAutoChorus(anotes ,key, numerator, denominator):
    #引数はanotes, 調, 分子, 分母
    minimumunit = 1920 / denominator  #分解脳を拍子の分母で割りますー(全音＝1920)
    qNList = noteQuantization(anotes, minimumunit)
    hamList = melodyrestoration(anotes, qNList, key, denominator, numerator)
    MChord.autoChord(hamList)
    MUnderThree.autoUnderThree(hamList)
    return mapping(anotes, hamList, minimumunit)


def noteQuantization(anotes, minimumunit):
    noteidx_max = len(anotes)
    noteidx = 0     #元ノートのいんでっくす
    hamidashi = 0   #はみ出しTick
    notename = -1   #音名

    listLen = int(math.ceil(float(anotes[len(anotes) - 1].get_end()) /
                  minimumunit))
    qNList = []     #りすと

    qnote = CQuantizedNote.CQuantizedNote()
    for qi in range(0, listLen):
        qnote.downBeat = notename

        #左の式が先に評価されるとうれしいな～ｖ
        while (noteidx < noteidx_max) and (anotes[noteidx].get_start() <
                                           (qi+1)*minimumunit):
            notename = anotes[noteidx].note%12
            if(qnote.downBeat == -1):
                qnote.downBeat = notename
            qnote.tickSum[notename]+=anotes[noteidx].get_length()
            noteidx += 1

        if(notename != -1): #無音の場合ははみ出し処理しないですー
            hamidashi = anotes[noteidx-1].get_end() - (qi+1) * minimumunit

        qNList.append(qnote)
        qnote = CQuantizedNote.CQuantizedNote()
        if(hamidashi>0): #はみ出し処理班
            qNList[qi].tickSum[notename] -= hamidashi
            qnote.tickSum[notename] += hamidashi
        else: #ぴったりのときは音名更新のため
            notename = -1

    return qNList


def melodyrestoration(anotes, qNList, key, denominator, numerator):
    minimumunit = 1920 / denominator #分解脳を拍子の分母で割りますー(全音＝1920)
    bar = int(math.ceil(float(len(qNList))/numerator))
    #print u"Shosetsu:", bar

    while len(qNList) < bar*numerator: #小節境界までかくちょうしましう～
        qNList.append(CQuantizedNote.CQuantizedNote())
    sopList = []
# !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! #
    #for q in qNList:
    #    print q.downBeat
# !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! #
    for bi in range(0, bar):
        melodyrestration_unit(qNList, sopList, bi*numerator,
                              numerator, minimumunit)
    noteidx = 0
    noteidx_max = len(anotes)
    sumlength = 0
    hamList = []
    for sop in sopList:
        sumlength+=sop[1] #sop[1]は長さですー
        sop_notenumber = -1
        while noteidx<noteidx_max and anotes[noteidx].get_start()<sumlength:
            if anotes[noteidx].note%12 == sop[0]: #sop[0]はnotenumber%12ですー
                #下パートを作りやすいように音高が高いものを採用
                if anotes[noteidx].note > sop_notenumber:
                    sop_notenumber = anotes[noteidx].note
            noteidx += 1

        #はみ出し分は戻しますー
        while noteidx != 0 and anotes[noteidx-1].get_end()>sumlength:
            noteidx -= 1

        tone_sop = CTone.CTone(sop_notenumber, key)
        hamList.append(CHarmony.CHarmony(sop[1]/minimumunit, key, tone_sop))
    return hamList


def melodyrestration_unit(qNList, sopList, qnote_index, numerator, minimumunit):
    nonkey = -1
    qnote_unit = CQuantizedNote.CQuantizedNote()
    for beat in range(0, numerator):
        qnote_unit += qNList[qnote_index + beat]

    soprano_note = qnote_unit.detthresholdnote(minimumunit*numerator/2)

    if soprano_note == -1:
        assert (numerator > 0 or numerator <= 4) #無理なのです；
        if numerator == 4:
            #強拍不一致
            if qNList[qnote_index].downBeat != qNList[qnote_index + 2].downBeat:
                melodyrestration_unit(qNList, sopList, qnote_index, 2,
                                      minimumunit)
                melodyrestration_unit(qNList, sopList, qnote_index+2, 2,
                                      minimumunit)
            else:
                soprano_note = qNList[qnote_index].downBeat
                sopList.append((soprano_note, minimumunit*numerator))
        elif numerator == 3:
            melodyrestration_unit(qNList, sopList, qnote_index   , 1,
                                  minimumunit)
            melodyrestration_unit(qNList, sopList, qnote_index+1 , 1,
                                  minimumunit)
            melodyrestration_unit(qNList, sopList, qnote_index+2 , 1,
                                  minimumunit)
        elif numerator == 2:
            melodyrestration_unit(qNList, sopList, qnote_index   , 1,
                                  minimumunit)
            melodyrestration_unit(qNList, sopList, qnote_index+1 , 1,
                                  minimumunit)
        elif numerator == 1:
            soprano_note = qNList[qnote_index].downBeat
            sopList.append((soprano_note, minimumunit*numerator))
    else :
        sopList.append((soprano_note, minimumunit*numerator))
    return


def mapping(anoteList, hamList, minimumunit): #まっぴんぐ♪
    result = []
    for part in range(0, 4):
        result.append(copy.deepcopy(anoteList))

    ratio = 2 # シンコペーション対策用パラメェタ
    ham_cnt = 0
    ham_pos = 0
    for i in range(0, len(anoteList)):
        while anoteList[i].get_start() >= (hamList[ham_cnt].length*minimumunit + ham_pos):
            ham_pos += hamList[ham_cnt].length * minimumunit
            ham_cnt += 1
        # こっちは必ず正の値をとりましう
        len1 = (hamList[ham_cnt].length*minimumunit+ham_pos) -\
                anoteList[i].get_start()
        # こっちはマイナスをとることがありましう(０もあるよ！)
        len2 = anoteList[i].get_end() - (hamList[ham_cnt].length*minimumunit +\
                                         ham_pos)
        #divided by 0!!なのです！！
        assert len1 != 0
        #一定割合以上後ろが重くなっちゃったとき；
        if (float(len2) / len1) > ratio:
            nexco = 1
        #こっちが普通～
        else:
            nexco = 0

        for part in range(0, 4):
            if hamList[ham_cnt+nexco].note[part].getNoteNumber() != -1:
                result[part][i].note = hamList[ham_cnt+nexco].note[part].getNoteNumber()

    return result
