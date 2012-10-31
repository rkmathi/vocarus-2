#coding: UTF-8

class CTone(object):
	def __init__(self, notenum, key):
		self.key = key											#調だよ
		#print notenum
		#print key
		if(notenum == -1):			#おやすみ用
			self.degree = -1
			self.octave = -5
			return

		if key == 0 :
			key = 1												#０のときはC durと同じ扱いで。
		elif key < 0:
			key = -key	#マイナスはmoll

		ofsetNote = notenum - (key - 1)
		tonic = (ofsetNote / 12) * 12 + key - 1
		self.degree = self.notenumToDegree(notenum - tonic)		#音度だよ
		self.octave = (tonic / 12) - 3							#オクターブだよ（直下の主音のオクターブ値として定義）
			
	def getNoteNumber(self):									#NoteNumberを返すよ
		if(self.degree == -1):		#おやすみ用
			return -1
	
		key = self.key
		if key == 0 :
			key = 1												#０のときはC durと同じ扱いで。
		elif key < 0:
			key = -key	#マイナスはmoll

		notenumber = (self.octave + 3) * 12 + key - 1	#tonic
		notenumber+= self.degreeToHarfDegree(self.degree)
		return notenumber
		
	def	setOctDeg(self, octave, degree):
		self.octave = octave
		self.degree = degree
		
	def notenumToDegree(self, notenum):							#音度を返すよ
		dic = {
			0:1, 1:1,
			2:2,
			3:3, 4:3,
			5:4, 6:4,
			7:5,
			8:6, 9:6,
			10:7,11:7
		}
		return dic[notenum%12]
		
	def degreeToHarfDegree(self, degree):						#主音からの半音程を返すよ
		durdic = {
			1:0,
			2:2,
			3:4,
			4:5,
			5:7,
			6:9,
			7:11
		}
		molldic = {
			1:0,
			2:2,
			3:3,
			4:5,
			5:7,
			6:8,
			7:11
		}
		if self.key<0 :return molldic[degree]
		return durdic[degree]
		
	def normalize(self):		#度数が下抜けしてしまったのみ対処する簡易版
		while self.degree < 1:
			self.degree += 7
			self.octave -= 1
	
		
	def	show(self):
		print self.getNoteNumber()
