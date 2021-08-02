import mido
import sys

mid = mido.MidiFile(sys.argv[1].strip('"'))
track_num = int(sys.argv[2])
offset = float(sys.argv[3])
output = open('label_output.txt', 'w')


metatrack = mid.tracks[0]
tempo = mido.tempo2bpm(metatrack[0].tempo)
track = mid.tracks[track_num]

nowtime = offset

for message in track:
    if message.is_meta:
        continue
    nowtime += 60 / tempo / mid.ticks_per_beat * message.time
    if message.type == 'note_on':
        notetype = {60: 'd', 61: 's', 62: 'w', 63: 'a'}[message.note]
        print('%s %s' % (nowtime, notetype))
        output.write('%s\t%s\t%s\n' % (nowtime, nowtime, notetype))

output.close()
