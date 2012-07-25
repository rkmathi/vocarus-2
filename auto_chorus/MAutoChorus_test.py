#coding: UTF-8

import MAutoChorus
import copy
import anote_list
import anote

def notenumToStr(notenumber):
	dic = {
			0:"C  ", 1:"Cis", 2:"D  ", 3:"Es ", 4:"E  ", 5:"F  ",
			6:"Fis", 7:"G  ", 8:"As ", 9:"A  ", 10:"B  ", 11:"H  " 
		}
	return str(notenumber/12-3)+dic[notenumber%12]
		

anotes_dumy = anote_list.AnoteList()
anotes_dumy.append(anote.Anote(7680, 72, u"あ"))
anotes_dumy.append(anote.Anote(8620, 72, u"あ"))
anotes_dumy.append(anote.Anote(9580, 74, u"あ"))
anotes_dumy.append(anote.Anote(10580, 79, u"が"))
anotes_dumy.append(anote.Anote(11520, 72, u"が"))
anotes_dumy.append(anote.Anote(13440, 72, u"が"))

anotes_dumy[0].set_length(960)
anotes_dumy[1].set_length(940)
anotes_dumy[2].set_length(1000)
anotes_dumy[3].set_length(940)
anotes_dumy[4].set_length(1920)
anotes_dumy[5].set_length(120)

key = 1	#C-dur
numerator = 4
denominator = 4
res = MAutoChorus.execAutoChorus(anotes_dumy, key, numerator, denominator)

print u"もと"
for i in anotes_dumy:
	print i.note, i.length

print u"かえってきたの"
for i in range(0, len(anotes_dumy)):
	print res[0][i].note,res[1][i].note,res[2][i].note,res[3][i].note,u"→", res[0][i].length
print u"つまり"
for i in range(0, len(anotes_dumy)):
	for part in range(0, 4):
		print notenumToStr(res[part][i].note),
	print u"→", float(anotes_dumy[i].length)/480