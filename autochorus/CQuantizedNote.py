#coding: UTF-8

class CQuantizedNote(object):
	def __init__(self):
		self.tickSum = []	#合計tick値
		self.downBeat = -1;	#強拍判定（音名）
		
		for note in range(0, 12):
			self.tickSum.append(0)
			
	def __iadd__(self, op):	#+=用
		for note in range(0, 12):
			self.tickSum[note]+=op.tickSum[note]
			
		if self.downBeat ==	-1 :	#downbeatを持たない時のみ更新
			self.downBeat = op.downBeat
			
		return self
			
	def detthresholdnote(self, thresholdtick):	#閾値をこえたnoteを出力するー
		resultnote = -1
		for note in range(0, 12):
			if thresholdtick < self.tickSum[note]: resultnote = note
		return resultnote