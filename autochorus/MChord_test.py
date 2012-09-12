#coding: UTF-8

import CHarmony
import CTone
import MChord

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

MChord.autoChord(ham)