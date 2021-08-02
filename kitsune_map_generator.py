import sys

source = open(sys.argv[1])
output = open('output_map.txt', 'w')

output.write('[')

notetype = {'a': 3, 'w': 0, 'd': 1, 's': 2}

notes = []

for line in source.read().split('\n'):
    if line == '':
        continue
    print(line)
    spl = line.split('\t')
    ti = float(spl[0]) * 1000
    notelabel = spl[2]
    ty = notetype.get(notelabel)
    if not ty == None:
        notes.append({'type': ty, 'time': ti})
    elif notelabel.startswith('m'):
        notes.append({'type': 9, 'value': notelabel[1:], 'time': ti})
    elif notelabel == 'end':
        notes.append({'type': 10, 'time': ti})
        break

notes.sort(key=lambda x: x['time'])
note_str = ', '.join(['{%s}' % ', '.join(['%s: %s' % (x, note[x]) for x in note.keys()]) for note in notes])
output.write(note_str)
output.write(']')

output.close()
