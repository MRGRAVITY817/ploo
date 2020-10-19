import random
from fractions import Fraction
from music21 import stream, harmony

def get_pitch(chord):
  return [str(p) for p in harmony.ChordSymbol(chord).pitches]

def rand_length(bar_length=4, max_length=4, division=4):
  lengths = []
  tmp_max = max_length
  for x in range(0, division):
    lengths.append(tmp_max)
    tmp_max /= 2
  combination = []
  acc = 0
  while acc < bar_length: 
    choice_menu = list(filter(lambda x: x <= bar_length-acc, lengths))
    item = random.choice(choice_menu)
    combination.append(item)
    acc += item 
  return combination

def merge_parts(parts):
  new_score = stream.Score()
  for p in parts:
    new_score.append(p)
  new_score.chordify()
  return new_score
    
def save(input_score, path):
  input_score.write('midi', fp=f'{path}/hoons.midi') 
