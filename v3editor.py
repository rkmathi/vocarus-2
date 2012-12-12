# -*- coding: utf-8 -*-

from anote_list import AnoteList
from anote import *
from aeks import aeks
import xml.etree.ElementTree as ET
import autochorus.MAutoChorus as MAC
 
class V3Editor(object):
    """ V3Editorのファイル(vsqx)を扱うクラス
    """
 
    def __init__(self, vsqx, part):
        """
        Args:
            vsqx:   file
            part:   int
        """
        self._part = part
        self._vsqx = (vsqx)
        self.parse()
 
    def parse(self):
        """ vsqxファイルを受け取ってコーラスの音程を返す
        Args:
            vsqx:   file
        Rets:
            notes:  [int]
        """
        elem = ET.fromstring(self._vsqx)
        xmlns = '{http://www.yamaha.co.jp/vocaloid/schema/vsq3/}'
 
        masterTrack=elem.find(xmlns+"masterTrack")
        timesig=masterTrack.find(xmlns+"timeSig")
 
        self._nn = int(timesig.findtext(xmlns+"nume"))
        self._dd = int(timesig.findtext(xmlns+"denomi"))
 
        vsTrack = elem.find(xmlns + "vsTrack")
        musicalPart = vsTrack.find(xmlns + "musicalPart")
        anotes = AnoteList()
        for i, note in enumerate(musicalPart.findall(xmlns+"note")):
            time=note.findtext(xmlns+"posTick")     #相対開始時間
            length=note.findtext(xmlns+"durTick")   #音の長さ
            anote=note.findtext(xmlns+"noteNum")    #音の高さ
            anotes.append(Anote(int(time), int(anote), length=int(length)))
 
        soprano_notes = [n.note for n in anotes]
        packed = MAC.execAutoChorus(anotes, aeks(soprano_notes),
                                    self._nn, self._dd)[self._part]
        notes = [] 
        for p in packed:
            notes.append(p.note)
        return notes


"""
### FOR DEBUG
if __name__ == "__main__":
    _data = open("../vsqx/kirakira.vsqx", "rt").read()
    print V3Editor(_data, 1).parse()
"""
