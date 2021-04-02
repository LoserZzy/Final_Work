f = open('same_module_list_none_rely', 'r')
mod_list = f.read().split()
f.close()
f = open('x86_modules_list', 'r')
mod_loc = f.read().split('\n')
f.close()
ana_result = {}
mm = ''
fs = ''
crypto = ''
block = ''
drivers = ''
lib = ''
sound = ''
net = ''
loc = {'mm':0, 'fs':0, 'crypto':0, 'block':0, 'drivers':0, 'lib':0, 'sound':0, 'net':0}
for a in range(len(mod_loc)):
    mod_loc[a] = mod_loc[a].split(':')[0]
for a in range(len(mod_list)):
    for b in range(len(mod_loc)):
        if mod_list[a] in mod_loc[b]:
            ana_result[mod_list[a]] = mod_loc[b].split('/')[1]
            loc[mod_loc[b].split('/')[1]] += 1
            if mod_loc[b].split('/')[1] == 'mm':
                mm = mm + mod_loc[b] + '\n'
            elif mod_loc[b].split('/')[1] == 'fs':
                fs = fs + mod_loc[b] + '\n'
            elif mod_loc[b].split('/')[1] == 'crypto':
                crypto = crypto + mod_loc[b] + '\n'
            elif mod_loc[b].split('/')[1] == 'block':
                block = block + mod_loc[b] + '\n'
            elif mod_loc[b].split('/')[1] == 'drivers':
                drivers = drivers + mod_loc[b] + '\n'
            elif mod_loc[b].split('/')[1] == 'lib':
                lib = lib + mod_loc[b] + '\n'
            elif mod_loc[b].split('/')[1] == 'sound':
                sound = sound + mod_loc[b] + '\n'
            elif mod_loc[b].split('/')[1] == 'net':
                net = net + mod_loc[b] + '\n'
            break

f = open('./modules/mm', 'w')
f.write(mm)
f.close()
f = open('./modules/fs', 'w')
f.write(fs)
f.close()
f = open('./modules/crypto', 'w')
f.write(crypto)
f.close()
f = open('./modules/block', 'w')
f.write(block)
f.close()
f = open('./modules/drivers', 'w')
f.write(drivers)
f.close()
f = open('./modules/lib', 'w')
f.write(lib)
f.close()
f = open('./modules/sound', 'w')
f.write(sound)
f.close()
f = open('./modules/net', 'w')
f.write(net)
f.close()

print(loc)