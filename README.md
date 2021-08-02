# champion-island-swim-map-converter
Converts Audacity label file to Google Doodle Champion Island swimming map javascript array
  
If you overwrite Google Doodle Champion Island's javascript `kitsune.js`, you can custom your music game (swim) map by yourself.  
  
Those map is saved as array in `kitsune.js`, obviously, editing music game map in javascript is so hard, so I write this program to convert Audacity label to javascript array in that formatting.  
  
So you can editing the map in Audacity and convert to array.  

# Usage
## File type of input
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

## Args
`kitsune_map_generator.py INPUT_FILE`  
output file will be named `output_map.txt`

## Example
![](https://upload.cc/i1/2021/08/02/7BUwDF.png)
