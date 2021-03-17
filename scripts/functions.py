# -*- coding: utf-8 -*-
import os
import sqlite3
 
from idaapi import *
from idautils import *
from idc import *
path = 'C:/Users/10110/Documents/ZzyWork/Final_Work/'
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
        if v == 'extrn':
            func_info['extern'].append(GetFunctionName(loc))
        else:
            func_info['define'].append(GetFunctionName(loc))
        # print str(func_info), 'func_info'
    f = open(outcome, 'w')
    f.write(str(func_info))
    f.close()
    
    idc.Exit(0)