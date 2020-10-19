from music21 import stream, note, pitch, instrument
import random
from fractions import Fraction
from . import bass_drum, mid_drum, high_drum

class Drum:
  def __init__(self, time_sig, is_rand):
    self.time_sig = int(Fraction(time_sig)*4)
    self.is_rand = is_rand
    self.score = stream.Score(id="Drums")
    self.score.insert(0, self.get_part('bass'))
    self.score.insert(0, self.get_part('mid'))
    self.score.insert(0, self.get_part('high'))
    self.score.chordify()
  # Common Utiltiy to make a bar
  def make_bar(self, sound, bar):
    note_bar = []
    for b in bar: 
      if b>0:
        note_bar.append(note.Note(sound, quarterLength=b))
      else:
        note_bar.append(note.Rest(quarterLength=b))
    return note_bar 
  # Bass groove
  def bass_bar(self):
    sound = 'C1'
    bar = []
    bar = bass_drum.make_lines(self.time_sig, self.is_rand)
    return self.make_bar(sound, bar)
  # Mid groove
  def mid_bar(self):
    sound = 'D1'
    bar = []
    bar = mid_drum.make_lines(self.time_sig, self.is_rand)
    return self.make_bar(sound, bar)
  # High groove
  def high_bar(self): 
    sound = 'F#1'
    bar = []
    bar = high_drum.make_lines(self.time_sig)
    return self.make_bar(sound, bar)
  # Make a part
  def get_part(self, part):
    new_part = stream.Part()
    for i in range(1, 9):
      bar = stream.Measure(number=i)
      if part=="bass":
        bar.append(self.bass_bar())
      elif part=="mid":
        bar.append(self.mid_bar())
      elif part=="high":
        bar.append(self.high_bar())
      new_part.append(bar)
    return new_part