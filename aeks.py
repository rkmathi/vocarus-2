# -*- coding: utf-8 -*-

import sys
import copy

def pentatonic(code, note_list):
    note_names = {'c':0, 'cis':1, 'd':2, 'dis':3, 'e':4, 'f':5,
                  'fis':6, 'g':7, 'gis':8, 'a':9, 'b':10, 'h':11}
    inter2 = [2, 2, 3, 2, 0]
    count = 0
    for i in range(0, len(note_list)):
        tmp = code
        for k in range(0, 5):
            if note_names[note_list[i][0]] == tmp%12:
                count += 1
            tmp += inter2[k]
    return count


def aeks(notes):
    """Automatic Estimation of Key Signature(AEKS)

    Args:
        notes: Soprano notes (IntegerList)
    Returns:
        key: Key Signature (Integer)
    """

    # C<-2->D, D<-2->E, E<-1->F, F<-2->G, G<-2->A, A<-2->H
    inter = [2, 2, 1, 2, 2, 2, 1]

    # C->0, Cis->1, D->2, Dis->3, E->4, F->5,
    # Fis->6, G->7, Gis->8, A->9, B->10, H->11
    note_name  = ['c', 'cis', 'd', 'dis', 'e', 'f',
                  'fis', 'g', 'gis', 'a', 'b', 'h']
    note_names = {'c':0, 'cis':1, 'd':2, 'dis':3, 'e':4, 'f':5,
                  'fis':6, 'g':7, 'gis':8, 'a':9, 'b':10, 'h':11}
    note_occur = {'c':0, 'cis':0, 'd':0, 'dis':0, 'e':0, 'f':0,
                  'fis':0, 'g':0, 'gis':0, 'a':0, 'b':0, 'h':0}

    # Count times that notes appear.
    for n in notes:
        note_occur[note_name[(n)%12]] += 1

    # Make dictionary sorted.
    note_sorted = sorted(note_occur.items(),
                         key=lambda (k, v): (v, k),
                         reverse=True)

    # Pop tuples which values are 0.
    note2_list = []
    for n in note_sorted:
        if n[1] != 0:
            note2_list.append([n[0], n[1]])
        else:
            pass

# !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! #
    #print "note2_list==>",note2_list,"<br/>"
    #for i in range(0, 7):
    #    print "note_names[note2_list[",i,"][0]]",note_names[note2_list[i][0]],"<br />"
# !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! !! #

    max = [-1, -1]
    for i in range(0, len(note2_list)):
        count = 0
        for t in range(0, len(note2_list)):
            code = note_names[note2_list[i][0]]
            for j in range(0, 7):
                if note_names[note2_list[t][0]] == (code%12):
                    count += 1
                code += inter[j]
        if count == len(note2_list):
            penta = pentatonic(note_names[note2_list[i][0]], note2_list)
            if max[1] < penta:
                max[0] = note_names[note2_list[i][0]]
                max[1] = penta

    key = max[0] + 1
    return key

