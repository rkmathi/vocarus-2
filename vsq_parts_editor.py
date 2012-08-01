# -*- coding: utf-8 -*-

from vsq_parts import *
from tools import *
from normaltrack import *
from mastertrack import *
from header import *
from struct import *
from google.appengine.api import mail
from google.appengine.api import memcache
import datetime

class JST(datetime.tzinfo):
    """Time zone class

    JST(Japan Standard Time)
    """
    def utcoffset(self,dt):
        return datetime.timedelta(hours=9)
    def dst(self,dt):
        return datetime.timedelta(0)
    def tzname(self,dt):
        return "JST"


class VsqPartsEditor(object):
    """パートの操作をするクラス

    """

    def __init__(self, part, filename=None, binary=None):
        if filename:
            self.parse(part, filename=filename)
        elif binary:
            self.parse(part, binary=binary)

    @property
    def anotes(self):
        return self.current_track.anotes

    def parse(self, part, filename=None, binary=None):
        """VSQファイルをパースする

        Args:
            part: part data
            filename: VSQファイルのパス
            binary: VSQファイルのバイナリデータ
        """
        self._fp = open(filename, 'r') if filename else tools.FakeFile(binary)
        self.header = Header(self._fp)
        self.master_track = MasterTrack(self._fp)
        track_num = self.header.data['track_num'] - 1
        self._part = part
        self.nn, self.dd, _, _ = self.master_track.beat
#!!!
        #print "part=>",part
        #sys.exit()
#!!!
        self.normal_tracks = [NormalTrack(self._fp, self.nn, self.dd, part)
                                for i in range(track_num)]
        self.unapply_dict = {}
        pre_measure = int(self.normal_tracks[0].data['Master']['PreMeasure'])
        time_div = self.header.data['time_div']
        self.start_time = int(self.nn / float(2 ** self.dd) *
                          4 * pre_measure * time_div)
        self.end_time = self.start_time
        for track in self.normal_tracks:
            et = track.anotes[-1].end
            self.end_time = max(et, self.end_time)
        self.select_track(0)

    def unparse(self, filename=None):
        """現在のデータをアンパースして、VSQファイルとして書きこむ

        Args:
            filename: 書き込むVSQファイルのパス
        Returns:
            filenameが指定されなかった場合はバイナリ
        """

        # Mail send
        message = mail.EmailMessage(
                sender="vocarus net <vocarus.lab+net@gmail.com>",
                subject="Somebody used vocarus!")
        message.to = "vocarus.lab@gmail.com"
        message.body="""Somebody uploaded '%s' at %s
""" % (memcache.get('vsq_name'), datetime.datetime.now(JST()))
        message.send()

        binary = self.header.unparse()
        binary += self.master_track.unparse()
        for track in self.normal_tracks:
            binary += track.unparse()
        if filename:
            open(filename, 'w').write(binary)
        else:
            return binary

    def select_track(self, n):
        """操作対象トラックを変更する

        Args:
            n: トラック番号
        """
        if n < len(self.normal_tracks):
            self.current_track = self.normal_tracks[n]

