#coding: UTF-8
import CTone

class CHarmony:
	def __init__(self, length, key, sop):
		gomi = CTone.CTone(-1,0)

		self.length = length
		self.key = key
		self.chord = 0
		self.note = [gomi,gomi,gomi,gomi]
		self.note[0] = sop
		
	def setChord(self, chord):
		self.chord = chord
		
	def getUnderThreeSolutionArray(self):		#解候補をかえしますー
		underThreeSA = []
			
		if(self.chord == 0):
			gomi = CTone.CTone(-1, self.key)
			for index in range(0,12):
				underThreeSA.append([gomi, gomi, gomi, gomi])			#ごみ
			return underThreeSA
	
		bassSA = self.getBassSolutionArray()
		innerSA = self.getInnerSolutionArray()

		for bass in bassSA:
			if bass.degree == self.chord :		#基本形ですー
				underThreeSA.append([self.note[0]] + innerSA[0] + [bass])	#密集配置
				underThreeSA.append([self.note[0]] + innerSA[1] + [bass])	#開離配置
				underThreeSA.append([self.note[0]] + innerSA[2] + [bass])	#オクターブ配置
			else:								#転回形ですー(一転)
				underThreeSA.append([self.note[0]] + innerSA[3] + [bass])	#開離配置１
				underThreeSA.append([self.note[0]] + innerSA[4] + [bass])	#オクターブ配置
				underThreeSA.append([self.note[0]] + innerSA[5] + [bass])	#開離配置２

		return underThreeSA
		
	def getBassSolutionArray(self):				#Bass解候補をかえしますー（４つ）
		bassMin = 57		#A1をBassの最低音として設定しますー
		bassMax = 80		#Gis3をBassの最高音として設定しますー
		
		bassSolutionArray = []
		if(self.chord == 0):					#おやすみ用処理
			for index in range(0, 4):
				bassSolutionArray.append(CTone.CTone(-1, self.key))	#ごみ
			return bassSolutionArray
		
		octave = 1	#条件に合致するものは1~3の値しかとりえないのでおｋ
		while octave <= 3:
			bassSolution = CTone.CTone(-1, self.key)				#ごみ
			bassSolution.setOctDeg(octave, self.chord)				#基本形
			noteNum = bassSolution.getNoteNumber()
			if bassMin <= noteNum and noteNum <= bassMax:
				bassSolutionArray.append(bassSolution)
			
			bassSolution = CTone.CTone(-1, self.key)				#ごみ		
			bassSolution.setOctDeg(octave, (self.chord+2-1)%7+1)	#第一転回形
			noteNum = bassSolution.getNoteNumber()
			if bassMin <= noteNum and noteNum <= bassMax:
				bassSolutionArray.append(bassSolution)

			octave += 1	
		return bassSolutionArray
		
	def getInnerSolutionArray(self):				#内声の解候補セットをかえしますー（６つ）
		
		innerSolutionArray = []
		if(self.chord == 0):						#おやすみ用処理
			for index in range(0, 6):
				innerSolutionArray.append([CTone.CTone(-1, self.key),CTone.CTone(-1, self.key)])	#ごみ
			return innerSolutionArray
			
		sopO = self.note[0].octave
		sopD = self.note[0].degree
		for i in range(0, 7):
			assert i<3 #三和音にしてくださいNE
			if(sopD == (self.chord+i*2-1)%7+1):
				sopCT = i*2+1	#何音ですか～？？
				break
				

		#基本形
		#密集配置
		altoSolution = CTone.CTone(-1, self.key)				#ごみ
		tenorSolution = CTone.CTone(-1, self.key)				#ごみ
		altoSolution.setOctDeg(sopO, sopD - (3 if sopCT==1 else 2))
		tenorSolution.setOctDeg(sopO, sopD - (4 if sopCT==5 else 5))
		altoSolution.normalize()
		tenorSolution.normalize()
		innerSolutionArray.append([altoSolution,tenorSolution])
		#開離配置
		altoSolution = CTone.CTone(-1, self.key)				#ごみ
		tenorSolution = CTone.CTone(-1, self.key)				#ごみ
		altoSolution.setOctDeg(sopO, sopD - (4 if sopCT==5 else 5))
		tenorSolution.setOctDeg(sopO, sopD - (10 if sopCT==1 else 9))
		altoSolution.normalize()
		tenorSolution.normalize()
		innerSolutionArray.append([altoSolution,tenorSolution])
		#オクターブ配置
		altoSolution = CTone.CTone(-1, self.key)				#ごみ
		tenorSolution = CTone.CTone(-1, self.key)				#ごみ
		altoSolution.setOctDeg(sopO, sopD - (5 if sopCT==1 else 2))
		tenorSolution.setOctDeg(sopO, sopD - 7)
		altoSolution.normalize()
		tenorSolution.normalize()
		innerSolutionArray.append([altoSolution,tenorSolution])
		#第一転回形		#SopranoとBassが三音重複の場合は未定義につき変なのを返すので、、そのつもりで。
		#開離配置１
		altoSolution = CTone.CTone(-1, self.key)				#ごみ
		tenorSolution = CTone.CTone(-1, self.key)				#ごみ
		altoSolution.setOctDeg(sopO, sopD - (3 if sopCT==1 else 4))
		tenorSolution.setOctDeg(sopO, sopD - (10 if sopCT==1 else 11))
		altoSolution.normalize()
		tenorSolution.normalize()
		innerSolutionArray.append([altoSolution,tenorSolution])
		#オクターブ配置
		altoSolution = CTone.CTone(-1, self.key)				#ごみ
		tenorSolution = CTone.CTone(-1, self.key)				#ごみ
		altoSolution.setOctDeg(sopO, sopD - (3 if sopCT==1 else 4))
		tenorSolution.setOctDeg(sopO, sopD - 7)
		altoSolution.normalize()
		tenorSolution.normalize()
		innerSolutionArray.append([altoSolution,tenorSolution])
		#開離配置２
		altoSolution = CTone.CTone(-1, self.key)				#ごみ
		tenorSolution = CTone.CTone(-1, self.key)				#ごみ
		altoSolution.setOctDeg(sopO, sopD - 7)
		tenorSolution.setOctDeg(sopO, sopD - (10 if sopCT==1 else 11))
		altoSolution.normalize()
		tenorSolution.normalize()
		innerSolutionArray.append([altoSolution,tenorSolution])
		
		return innerSolutionArray
		
	def getChordSolutionArray(self):
		sop_deg = self.note[0].degree
		if sop_deg == -1 :
			return [0,0,0]

		chordSolutionArray = []
		for i in range(0, 3) :
			chordSolutionArray.append((sop_deg-1-2*i+7)%7+1)
		
		return chordSolutionArray

	def show(self):
		print "length:", self.length
		print "key:", self.key
		print "chord:", self.chord
		print u"そぷらの:", self.note[0].getNoteNumber()
		print u"あると:", self.note[1].getNoteNumber()
		print u"てなー:", self.note[2].getNoteNumber()
		print u"ばす:", self.note[3].getNoteNumber()
		print ""