# -*- coding: utf-8 -*-
import os
import sqlite3
 
from idaapi import *
from idautils import *
from idc import *
path = 'F:/ZzyWork/Final_Work//'
outcome = path + 'outcome/temporary_info.txt'

if __name__=="__main__":
    idc.Wait()
    func_loc = Functions()
    func_loc = list(func_loc) 
    f = open(outcome, 'w')

    func_info = {'extern':[], 'define':[]}
    for loc in func_loc:
        # print loc, 'loc'
        v = idc.GetDisasm(loc)
        v = v.split(' ')[0]
        if v == 'IMPORT':
            func_info['extern'].append(GetFunctionName(loc))
        else:
            func_info['define'].append(GetFunctionName(loc))
        # print str(func_info), 'func_info'

    seg_start = list(Segments())[-1]
    seg_end = SegEnd(seg_start)
    for a in range(seg_start, seg_end, 4):
        v = idc.GetDisasm(a)
        v = v.split(' ')
        # print v
        if v[0] == 'IMPORT':
            func_info['extern'].append(v[1])


    f = open(outcome, 'w')
    f.write(str(func_info))
    f.close()
    
    idc.Exit(0)