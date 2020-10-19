import random
from fractions import Fraction
from music21 import stream, chord, note, instrument
import random
from commons import rand_length, get_pitch

class Bass:
  def __init__(self, progs, time_sig):
    self.progs = progs
    self.time_sig = int(Fraction(time_sig)*4)
    self.score = self.get_score()
  # Make a bar
  def bass_bar(self, chord, num_id):
    bar = stream.Measure(number=num_id)
    groove = rand_length(bar_length=self.time_sig, max_length=1, division=2)
    chord_list = get_pitch(chord)
    for g in groove: 
      bar.append(note.Note(random.choice(chord_list), quarterLength=g))
    return bar
  # Make a part
  def get_score(self):
    part = stream.Part()
    count = 1
    for p in self.progs:
      part.append(self.bass_bar(chord=p, num_id=count))
      count += 1
    score = stream.Score()
    score.insert(instrument.Bass())
    score.insert(0, part)
    return score 

