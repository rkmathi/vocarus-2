#coding: UTF-8
import CHarmony
import CTone

keydic = {
		0:"Non",
		1:"C dur", 2:"Cis dur", 3:"D dur", 4:"Es dur", 5:"E dur", 6:"F dur",
		7:"Fis dur", 8:"G dur",9:"As dur", 10:"A dur", 11:"B dur", 12:"H dur"
	}

print u"ＳＡＡＡＡＡNoteNumberは57～80にはいっているかＮＡ？？？？(BASS範囲てすと)"		
for key in range(1, 13):
	print u"keyは", key, u"だよっ！"
	ham = []

	sop = CTone.CTone(72, key)		#引数：notenumber, key
	ham.append(CHarmony.CHarmony(1, key, sop))
	sop = CTone.CTone(72, key)
	ham.append(CHarmony.CHarmony(1, key, sop))
	sop = CTone.CTone(79, key)
	ham.append(CHarmony.CHarmony(1, key, sop))
	sop = CTone.CTone(79, key)
	ham.append(CHarmony.CHarmony(1, key, sop))
	sop = CTone.CTone(72, key)
	ham.append(CHarmony.CHarmony(4, key, sop))

	ham[0].setChord(0)
	ham[1].setChord(1)
	ham[2].setChord(1)
	ham[3].setChord(5)
	ham[4].setChord(1)

	#print u"次っ（＾＊＊＾）"
	result = ham[0].getBassSolutionArray()
	assert len(result) == 4		#Bassの候補が4つじゃない件について（＾・・＾）
	result = ham[1].getBassSolutionArray()
	assert len(result) == 4		#Bassの候補が4つじゃない件について（＾・・＾）
	for index in range(0, 4):	#範囲のちぇっく
		#print result[index].octave
		#print result[index].degree
		assert 57<=result[index].getNoteNumber()
		assert result[index].getNoteNumber()<=80
print u"おｋ（＾－－＾）"
print u"(内声てすと)"	
for key in range(1, 2):
	print u"keyは", key, u"だよっ！"
	ham = []

	sop = CTone.CTone(72+key-1, key)		#引数：notenumber, key
	ham.append(CHarmony.CHarmony(1, key, sop))
	sop = CTone.CTone(72+key-1, key)
	ham.append(CHarmony.CHarmony(1, key, sop))
	sop = CTone.CTone(79+key-1, key)
	ham.append(CHarmony.CHarmony(1, key, sop))
	sop = CTone.CTone(79+key-1, key)
	ham.append(CHarmony.CHarmony(1, key, sop))
	sop = CTone.CTone(72+key-1, key)
	ham.append(CHarmony.CHarmony(4, key, sop))

	ham[0].setChord(0)
	ham[1].setChord(1)
	ham[2].setChord(1)
	ham[3].setChord(5)
	ham[4].setChord(1)

	result = ham[0].getInnerSolutionArray()
	assert len(result) == 6		#内声の候補が6つじゃない件について（＾・・＾）
	result = ham[1].getInnerSolutionArray()
	assert len(result) == 6		#内声の候補が6つじゃない件について（＾・・＾）
	#for index in range(0, 6):	#己の目でデバッグするがよい！
	#	print ham[1].note[0].octave, result[index][0].octave, result[index][1].octave
	#	print ham[1].note[0].degree, result[index][0].degree, result[index][1].degree
	#	print ""

print u"おｋ（＾－－＾）"
print u"(下三声てすと)"	
for key in range(1, 2):
	print u"keyは", key, u"だよっ！"
	ham = []

	sop = CTone.CTone(72+key-1, key)		#引数：notenumber, key
	ham.append(CHarmony.CHarmony(1, key, sop))
	sop = CTone.CTone(72+key-1, key)
	ham.append(CHarmony.CHarmony(1, key, sop))
	sop = CTone.CTone(79+key-1, key)
	ham.append(CHarmony.CHarmony(1, key, sop))
	sop = CTone.CTone(79+key-1, key)
	ham.append(CHarmony.CHarmony(1, key, sop))
	sop = CTone.CTone(72+key-1, key)
	ham.append(CHarmony.CHarmony(4, key, sop))

	ham[0].setChord(1)
	ham[1].setChord(6)
	ham[2].setChord(2)
	ham[3].setChord(5)
	ham[4].setChord(1)
	
	#result = ham[0].getUnderThreeSolutionArray()
	#assert len(result) == 12		#下三声の候補が12つじゃない件について（＾・・＾）
	#print u"↓↓C3にⅠの和音を組み合わせた結果がこれだよ！！"
	#for index in range(0, 12):	#己の目でデバッグするがよい！
	#	print result[index][0].octave, result[index][1].octave, result[index][2].octave, result[index][3].octave
	#	print result[index][0].degree, result[index][1].degree, result[index][2].degree, result[index][3].degree
	#	print ""

	result = ham[1].getUnderThreeSolutionArray()
	assert len(result) == 12		#下三声の候補が12つじゃない件について（＾・・＾）
	print u"↓↓C3にⅥの和音を組み合わせた結果がこれだよ！！"
	for index in range(0, 12):	#己の目でデバッグするがよい！
		print result[index][0].octave, result[index][1].octave, result[index][2].octave, result[index][3].octave
		print result[index][0].degree, result[index][1].degree, result[index][2].degree, result[index][3].degree
		print ""

key = 1
ham = []

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
	
#autoUnderThree(ham)