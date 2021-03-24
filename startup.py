import os
from settings import *

outcome_name = 'temporary_info.txt'
scripts_x86 = 'functions_x86.py'
scripts_mips = 'functions_mips.py'
scripts_arm = 'functions_arm.py'
func_info_name = 'funcinfo.txt'
depmod_info = 'modules.dep'
final_info_name = 'final_info.txt'
arch_info = 'arch_info.txt'


# 获取模块依赖关系数据部分
def mod_relate_raw():
    modules = {}
    f = open(path_outcome + depmod_info, 'r')
    depmod = f.read()
    f.close()
    depmod = depmod.replace(':', '').split('\n')
    for a in range(len(depmod)):
        depmod[a] = depmod[a].split()
        if len(depmod[a]) > 1:
            modules[depmod[a][0]] = []
            for b in range(1, len(depmod[a])):
                modules[depmod[a][0]].append(depmod[a][b])
        elif len(depmod[a]) == 1:
            # print(depmod[a][0])
            modules[depmod[a][0]] = []
        else:
            pass
    # for a in modules:
    #     print (a, modules[a])
    return modules



# 获取函数调用数据部分
def func_call_info(modules):
    f = open(path_outcome + arch_info, 'r')
    arch = f.read()
    if 'x86' in arch: # x86版本
        modfunc_info = {}
        for m in modules:
            # print(path_file + m)
            doit = path_ida + "idaq64 -c -A -S" + path_scripts + scripts_x86 + ' ' + path_file + m
            # print(doit)
            os.system(doit)
            f = open(path_outcome + outcome_name, 'r')
            r = f.read().replace('\n', '')
            # print(r)
            modfunc_info[m] = dict(eval(r))
            f.close()
        f = open(path_outcome + func_info_name, 'w')
        f.write(str(modfunc_info))
        f.close()

    elif 'mips' in arch:
        modfunc_info = {}
        for m in modules:
            # print(path_file + m)
            doit = path_ida + "idaq64 -c -A -S" + path_scripts + scripts_mips + ' ' + path_file + m
            # print(doit)
            os.system(doit)
            f = open(path_outcome + outcome_name, 'r')
            r = f.read().replace('\n', '')
            # print(r)
            modfunc_info[m] = dict(eval(r))
            f.close()
        f = open(path_outcome + func_info_name, 'w')
        f.write(str(modfunc_info))
        f.close()

    else:
        modfunc_info = {}
        for m in modules:
            # print(path_file + m)
            doit = path_ida + "idaq64 -c -A -S" + path_scripts + scripts_arm + ' ' + path_file + m
            # print(doit)
            os.system(doit)
            f = open(path_outcome + outcome_name, 'r')
            r = f.read().replace('\n', '')
            # print(r)
            modfunc_info[m] = dict(eval(r))
            f.close()
        f = open(path_outcome + func_info_name, 'w')
        f.write(str(modfunc_info))
        f.close()


# 数据比对处理部分
def compare_and_analyze(modules):
    ana_result = {}
    f = open(path_outcome + func_info_name, 'r')
    r = f.read()
    modfunc_info = dict(eval(r))
    f.close()
    for a in modules:
        print(a)
        ana_result[a] = {}
        if len(modules[a]) > 0:
            for b in modules[a]:
                ana_result[a][b] = []
            a_ext = modfunc_info[a]['extern']
            # print(a_ext)
            a_rely = modules[a]
            for b in a_ext:
                for c in a_rely:
                    if b in modfunc_info[c]['define']:
                        ana_result[a][c].append(b)
            # print(ana_result)
    f = open(path_outcome + final_info_name, 'w')
    for a in ana_result:
        f.write((str(a) + ':' + str(ana_result[a]) + '\n'))
    f.close()




if __name__ == '__main__':
    # modules = mod_relate_raw()
    # print(modules)
    # func_call_info(modules)
    # compare_and_analyze(modules)