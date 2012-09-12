#coding: UTF-8
import MUnderThree
import CHarmony
import CTone
import sys

ham = []
key = 1	#C dur

sop = CTone.CTone(72 + key - 1, key)		#引数：notenumber, key
ham.append(CHarmony.CHarmony(1, key, sop))
sop = CTone.CTone(72 + key - 1, key)
ham.append(CHarmony.CHarmony(1, key, sop))
sop = CTone.CTone(74 + key - 1, key)
ham.append(CHarmony.CHarmony(1, key, sop))
sop = CTone.CTone(79 + key - 1, key)
ham.append(CHarmony.CHarmony(1, key, sop))
sop = CTone.CTone(72 + key - 1, key)
ham.append(CHarmony.CHarmony(4, key, sop))

ham[0].setChord(1)
ham[1].setChord(6)
ham[2].setChord(2)
ham[3].setChord(5)
ham[4].setChord(1)

MUnderThree.autoUnderThree(ham)