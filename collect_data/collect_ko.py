import os
import time

if __name__ == '__main__':
    os.system('depmod') # 重新生成depmod文件
    time.sleep(5)

    os.system('uname -r > uname.txt')
    f = open('uname.txt', 'r')
    uname = f.read().replace('\n', '')
    f.close()

    f = open('/lib/modules/' + uname + '/modules.dep') # 获取模块依赖关系
    depmod = f.read()
    f.close()

    mod_relation = {} # 去掉没被调用的文件形成新的调用关系表，以及复制文件
    copy_list = [] # 需要复制的文件列表
    depmod = depmod.split('\n')
    for a in depmod:
        a = a.replace(':', '').split()
        if len(a) > 1:
            head = a[0].split('/')[-1] # 去掉前缀
            mod_relation[head] = []
            copy_list.append(a[0])
            for b in a[1:]:
                mod_relation[head].append(b.split('/')[-1])
                copy_list.append(b)
    f = open('relation.txt', 'w') # 保存调用关系到文件
    f.write(str(mod_relation))
    f.close()
    copy_list = list(set(copy_list))
    for a in copy_list:
        doit = 'cp /lib/modules/' + uname + '/' + a + ' ./kos/'
        os.system(doit)