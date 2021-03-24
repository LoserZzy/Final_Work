same = []
f = open('x86_modules_list', 'r')
x86 = f.read()
f.close()
x86 = x86.split('\n')
del x86[-1]
# print(x86)
for a in range(len(x86)):
    x86[a] = x86[a].split(':')[0].split('/')[-1]
# print(x86)

f = open('mips_modules_list', 'r')
mips = f.read()
f.close()
mips = mips.split('\n')
del mips[-1]
# print(mips)
for a in range(len(mips)):
    mips[a] = mips[a].split(':')[0].split('/')[-1]

f = open('arm_modules_list', 'r')
arm = f.read()
f.close()
arm = arm.split('\n')
del arm[-1]
# print(arm)
for a in range(len(arm)):
    arm[a] = arm[a].split(':')[0].split('/')[-1]

# print(len(arm), len(mips), len(x86))

f = open('same_module_list', 'w+')
for a in mips:
    if a in x86 and a in arm:
        f.write(a + ' ')
f.close()