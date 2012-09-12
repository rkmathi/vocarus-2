#coding: UTF-8
import CTone

keydic = {
		0:"Non",
		1:"C dur", 2:"Cis dur", 3:"D dur", 4:"Es dur", 5:"E dur", 6:"F dur",
		7:"Fis dur", 8:"G dur",9:"As dur", 10:"A dur", 11:"B dur", 12:"H dur"
	}

try:
	print "Tonic Test!!!!(harfdegreescale)"
	for slidekey in range(1, 13):
		notenumber = 72 - 1 + slidekey		#C3～H3
		key = slidekey
		tone = CTone.CTone(notenumber, key)
		expected = keydic[key]		#調
		actual = keydic[tone.key]
		#print u"調:", actual
		assert expected == actual
		expected = 1				#音度
		actual = tone.degree
		#print u"音度:", actual
		assert expected == actual
		expected = 3				#オクターヴ
		actual = tone.octave
		#print u"オクターヴ:", actual
		assert expected == actual
		expected = notenumber		#NoteNumber
		actual = tone.getNoteNumber()
		#print u"NoteNumber:", actual
		assert expected == actual
		print u"おｋ（＾ω＾）\n"
		
	print "Subdominant Test!!!!(harfdegreescale)"
	for slidekey in range(1, 13):
		notenumber = 77 - 1 + slidekey		#F3～E5
		key = slidekey
		tone = CTone.CTone(notenumber, key)
		expected = keydic[key]		#調
		actual = keydic[tone.key]
		#print u"調:", actual
		assert expected == actual
		expected = 4				#音度
		actual = tone.degree
		#print u"音度:", actual
		assert expected == actual
		expected = 3				#オクターヴ
		actual = tone.octave
		#print u"オクターヴ:", actual
		assert expected == actual
		expected = notenumber		#NoteNumber
		actual = tone.getNoteNumber()
		#print u"NoteNumber:", actual
		assert expected == actual
		print u"おｋ（＾ω＾）\n"	
	
	print "G2 in C dur Test!!!!"
	notenumber = 67	#G2
	key = 1
	tone = CTone.CTone(notenumber, key)
	expected = keydic[key]		#調
	actual = keydic[tone.key]
	print u"調:", actual
	assert expected == actual
	expected = 5				#音度
	actual = tone.degree
	print u"音度:", actual
	assert expected == actual
	expected = 2				#オクターヴ
	actual = tone.octave
	print u"オクターヴ:", actual
	assert expected == actual
	expected = notenumber		#NoteNumber
	actual = tone.getNoteNumber()
	print u"NoteNumber:", actual
	assert expected == actual
	print u"おｋ（＾ω＾）\n"
	
	print "C3 in F dur Test!!!!"
	notenumber = 72	#C3
	key = 6
	tone = CTone.CTone(notenumber, key)
	expected = keydic[key]		#調
	actual = keydic[tone.key]
	print u"調:", actual
	assert expected == actual
	expected = 5				#音度
	actual = tone.degree
	print u"音度:", actual
	assert expected == actual
	expected = 2				#オクターヴ
	actual = tone.octave
	print u"オクターヴ:", actual
	assert expected == actual
	expected = notenumber		#NoteNumber
	actual = tone.getNoteNumber()
	print u"NoteNumber:", actual
	assert expected == actual
	print u"おｋ（＾ω＾）\n"
	
	print "C3 in A dur Test!!!!"
	notenumber = 73	#Cis3
	key = 10
	tone = CTone.CTone(notenumber, key)
	expected = keydic[key]		#調
	actual = keydic[tone.key]
	print u"調:", actual
	assert expected == actual
	expected = 3				#音度
	actual = tone.degree
	print u"音度:", actual
	assert expected == actual
	expected = 2				#オクターヴ
	actual = tone.octave
	print u"オクターヴ:", actual
	assert expected == actual
	expected = notenumber		#NoteNumber
	actual = tone.getNoteNumber()
	print u"NoteNumber:", actual
	assert expected == actual
	print u"おｋ（＾ω＾）\n"
	
	print "A1 in G dur Test!!!!"
	notenumber = 57	#A1
	key = 8
	tone = CTone.CTone(notenumber, key)
	expected = keydic[key]		#調
	actual = keydic[tone.key]
	print u"調:", actual
	assert expected == actual
	expected = 2				#音度
	actual = tone.degree
	print u"音度:", actual
	assert expected == actual
	expected = 1				#オクターヴ
	actual = tone.octave
	print u"オクターヴ:", actual
	assert expected == actual
	expected = notenumber		#NoteNumber
	actual = tone.getNoteNumber()
	print u"NoteNumber:", actual
	assert expected == actual
	print u"おｋ（＾ω＾）\n"
	
	print u"おまけおまけ"
	notenumber = 0
	key = 0
	tone = CTone.CTone(notenumber, key)
	actual = tone.degree
	print u"音度:", actual

except Exception as e:
	print u"おいィ？"
	print u"type:" + str(type(e))
	print u"args:" + str(e.args)
	print u"message:" , e.message
	print u"eのなかみ:" + str(e)
	print u"正しいの→", expected
