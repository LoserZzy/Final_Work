import os

def this_rely(origin_loc, pid): # 递归查找和获取依赖文件
    doit = 'readelf -d ' + origin_loc + ' > temporary_file'
    os.system(doit)
    f = open('temporary_file', 'r')
    readin = f.read().split('\n')
    f.close()
    rely = []
    for a in readin:
        if '(NEEDED)' in a:
            rely.append(a.split('[')[1].replace(']', ''))
    
    for a in rely:
        doit = ' whereis ' + a + ' > temporary_file'
        os.system(doit)
        f = open('temporary_file', 'r')
        readin = f.read()
        f.close()
        if readin.split(':')[1] == '':
            continue
        readin = readin.split(': ')[1].replace('\n', '').split()
        for b in readin:
            if a in b and b.split(a)[1] == '':
                loc = b
                doit = 'cp ' + loc + ' ./' + pid + '/'
                os.system(doit)
                this_rely(loc, pid)
                break

    return rely

if __name__ == '__main__':
    pid = str(input())
    doit = 'mkdir ' + pid
    os.system(doit)
    doit = 'cp -L /proc/' + pid + '/exe ./' + pid + '/exe'
    os.system(doit)

    loc = './' + pid + '/exe'
    this_rely(loc, pid)