import random
from fractions import Fraction
from music21 import stream, harmony, chord, note, scale

'''
We will make random chord progressions based on 
some of the most famous scores in the Real book.
'''

alice_in_wonderlands = 'Dm7 G7 CM7 FM7 Bdim7 E7 Am7 E-7 Dm7 G7 Em7 Am7 Dm7 G7 Em7 A7'.split()
autumn_leaves = "Am7 D7 GM7 CM7 F#dim7 B7 Em Em Am7 D7 GM7 CM7 F#dim7 B7 Em Em".split()

# Make a new chord progression based on original
def slice_bar(bar_list_16): 
  bar_list = []
  checkpoint = 0
  for i in range(0, 4):
    bars = bar_list_16[checkpoint:checkpoint+4]
    random.shuffle(bars)
    bar_list.append(bars)
    checkpoint += 4
  return bar_list
 

