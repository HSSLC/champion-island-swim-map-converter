# champion-island-swim-map-converter
Converts Audacity label file to Google Doodle Champion Island swimming map javascript array.
  
If you overwrite Google Doodle Champion Island's javascript `kitsune.js`, you can custom your music game (swim) map by yourself.  
  
Those map is saved as array in `kitsune.js`, obviously, editing music game map in javascript is so hard, so I write this program to convert Audacity label to javascript array in that formatting.  
  
So you can editing the map in Audacity and convert to array.  
  
There is also a another program `midi_to_audacity_label.py`, that is for converting MIDI note to Audacity label.

# Usage
## Audacity label file to js array
Usage: `kitsune_map_generator.py INPUT_FILE`  
Output file will be named `output_map.txt`  
  
In Audacity, add a new label track and type command in label at timestamp.  
command is following:
* `w`: arrow up
* `a`: arrow left
* `s`: arrow down
* `d`: arrow right
* `end`: end of map, in array, note that type is 10 means map is ended
* `m{n}`: custom command, will be converted to note of type 9, I define this type of note means "change speed" in js
  
Or you can also custom your command by add `elif` to program.  

I also modifyed `kitsune.js`, add variable speed to swim map, when parsing to note of type 9, that will change speed to value of that note.  

## MIDI file to Audacity label
Usage: `midi_to_audacity_label.py INPUT_FILE TRACK_NUMBER OFFSET`  
Output file will be named `label_output.txt`  
`OFFSET` is for if there is some offset between MIDI and Audacity track (ms).
  
If you just adding a lot of note label in Audacity, some complex map will drives you crazy.  
  
So I also made this program to converts MIDI file to Audacity label.  
  
You can add note of MIDI in DAW like FL Studio ect... and using pitch to express the arrow direction of map.  
  
Default mapping is:
* C5: d
* C#5: s
* D5: w
* D#5: a
  
So you can add a lot of note on beat and convert to Audacity label and calibrate in Audacity.

## Example
![](https://upload.cc/i1/2021/07/31/UCor4t.png)  
^ editing notes in DAW.
![](https://upload.cc/i1/2021/08/02/7BUwDF.png)
^ convert to Audacity label to calibrate.
