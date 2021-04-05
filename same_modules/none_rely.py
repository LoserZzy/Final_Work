none_rely = []
f = open('x86_modules_list', 'r')
r = f.read()
f.close()
r = r.split('\n')
del r[-1]
for a in r:
    if a.split(':')[1] == '':
        none_rely.append(a.split(':')[0])
f = open('x86_none_rely', 'w')
f.write(str(none_rely))
f.close()
print('x86', len(none_rely))

none_rely = []
f = open('arm_modules_list', 'r')
r = f.read()
f.close()
r = r.split('\n')
del r[-1]
for a in r:
    if a.split(':')[1] == '':
        none_rely.append(a.split(':')[0])
f = open('arm_none_rely', 'w')
f.write(str(none_rely))
f.close()
print('arm', len(none_rely))

none_rely = []
f = open('mips_modules_list', 'r')
r = f.read()
f.close()
r = r.split('\n')
del r[-1]
for a in r:
    if a.split(':')[1] == '':
        none_rely.append(a.split(':')[0])
f = open('mips_none_rely', 'w')
f.write(str(none_rely))
f.close()
print('mips', len(none_rely))

f = open('same_module_list_none_rely', 'r')
r = f.read().split()
f.close()
print(len(r))