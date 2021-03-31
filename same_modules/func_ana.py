f = open('same_module_list_none_rely', 'r')
mod_list = f.read().split()
f.close()
f = open('x86_modules_list', 'r')
mod_loc = f.read().split('\n')
f.close()
ana_result = {}
loc = {'mm':0, 'fs':0, 'crypto':0, 'block':0, 'drivers':0, 'lib':0, 'sound':0, 'net':0}
for a in range(len(mod_loc)):
    mod_loc[a] = mod_loc[a].split(':')[0]
for a in range(len(mod_list)):
    for b in range(len(mod_loc)):
        if mod_list[a] in mod_loc[b]:
            ana_result[mod_list[a]] = mod_loc[b].split('/')[1]
            loc[mod_loc[b].split('/')[1]] += 1
            if mod_loc[b].split('/')[1] == 'lib':
                print(mod_loc[b])
            break

# f = open('mod_loc', 'w')
# f.write(str(ana_result))
# f.close()

print(loc)