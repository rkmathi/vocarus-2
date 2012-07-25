# -*- coding: utf-8 -*-

import anote_list
import anote
import copy

# DUMMY Method
def execAutoChorus(anotes):
    result = []
    for part in range(0, 4):
        result.append(copy.deepcopy(anotes))
    for soprano in result[0]:
        soprano.note = 84
    for soprano in result[1]:
        soprano.note = 79
    for soprano in result[2]:
        soprano.note = 76
    for soprano in result[3]:
        soprano.note = 72
    return result

