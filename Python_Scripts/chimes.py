import time
import subprocess
import itertools
'''
sudo apt-get install sox
'''
curtime = time.localtime()
chords = [
    [415.30,369.99,329.63,246.94],
    [329.63,369.99,415.30,329.63],
    [415.30,329.63,369.99,246.94],
    [246.94,369.99,415.30,329.63],
    [329.63,329.63,329.63,329.63]
    ]
if curtime.tm_hour > 12:
 hour = curtime.tm_hour - 12
else:
  hour = curtime.tm_hour
if  0 <= curtime.tm_min <= 14:
  for row in itertools.islice(chords,0,1):
    for note in row:
      subprocess.check_output(['play','-n','synth','1.66','pluck',str(note)])
if  15 <= curtime.tm_min <= 29:
  for row in itertools.islice(chords,0,2):
    for note in row:
      subprocess.check_output(['play','-n','synth','2','pluck',str(note)])
if  30 <= curtime.tm_min <= 44:
  for row in itertools.islice(chords,0,3):
    for note in row:
      subprocess.check_output(['play','-n','synth','2','pluck',str(note)])
if  45 <= curtime.tm_min <= 60:
  for row in itertools.islice(chords,0,4):
    for note in row:
      subprocess.check_output(['play','-n','synth','2','pluck',str(note)])
for hr in range(0,hour):
     subprocess.check_output(['play','-n','synth','2','pluck',str(329.63)])
