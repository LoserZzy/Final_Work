# -*- coding: utf-8 -*-
import os
import sqlite3
 
from idaapi import *
from idautils import *
from idc import *
path = 'F:/ZzyWork/Final_Work/'
outcome = path + 'outcome/temporary_info.txt'

if __name__=="__main__":
    idc.Wait()
    func_loc = Functions()
    func_loc = list(func_loc) 
    f = open(outcome, 'w')

    func_info = {'extern':{}, 'define':[]}

    for loc in func_loc:
        # print(GetDisasm(loc))
        v = idc.GetDisasm(loc)
        v = v.split(' ')[0]
        if v == 'extrn':
            func_info['extern'][(GetFunctionName(loc))] = 0
            end_addr = FindText(MinEA(), SEARCH_DOWN, 0, 0, 'Segment type: Pure data')
            cur_addr = end_addr
            while cur_addr <= MaxEA():
                cur_addr = FindText(cur_addr, SEARCH_UP, 0, 0, GetFunctionName(loc))
                if cur_addr > MaxEA():
                    break
                else:
                    r = GetDisasm(cur_addr).split()
                    # print(GetFunctionName(loc), r)
                    if len(r) >= 2 and r[0] == 'call' and r[1].replace(';', '') == GetFunctionName(loc):
                        func_info['extern'][GetFunctionName(loc)] += 1
                cur_addr = PrevHead(cur_addr)
                # print(cur_addr)
        else:
            func_info['define'].append(GetFunctionName(loc))
        # print str(func_info), 'func_info'

    f = open(outcome, 'w')
    f.write(str(func_info))
    f.close()
    
    idc.Exit(0)