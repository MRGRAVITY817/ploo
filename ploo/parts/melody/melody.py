import random
from fractions import Fraction
from music21 import stream, chord, note
from commons import rand_length, get_pitch

class Melody:
  def __init__(self, progs, time_sig):
    self.progs = progs
    self.time_sig = int(Fraction(time_sig)*4)
    self.part = self.get_part()
  # Let's make a bar mixed with notes and chords
  def mix_note_chord(self, chord_list, groove):
    pick_list = [0, 1, 2]
    mix_list = []
    for g in groove:
      pick = random.choice(pick_list)
      if pick==0:
        mix_list.append(note.Rest(quarterLength=g))
      elif pick==1:
        mix_list.append(note.Note(random.choice(chord_list), quarterLength=g))
      else:
        mix_list.append(chord.Chord(chord_list[:-1], quarterLength=g))
    return mix_list
  # Soprano Part
  def soprano_bar(self, chord, num_id, prog_type='mixed'):
    bar = stream.Measure(number=num_id)
    groove = rand_length(bar_length=self.time_sig, max_length=2, division=3)
    chord_list = get_pitch(chord)
    if prog_type == 'mono':
      for g in groove: 
        bar.append(note.Note(random.choice(chord_list), quarterLength=g))
    elif prog_type == 'mixed':
      bar.append(self.mix_note_chord(chord_list=chord_list, groove=groove))
    return bar
  # Alto Part
  def alto_bar(self, chord, num_id, prog_type="mixed"):
    bar = stream.Measure(number=num_id)
    groove = rand_length(bar_length=self.time_sig, max_length=2, division=3)
    chord_list = get_pitch(chord)
    if prog_type == 'mono':
      for g in groove: 
        bar.append(note.Note(random.choice(chord_list), quarterLength=g))
    elif prog_type == 'mixed':
      bar.append(self.mix_note_chord(chord_list=chord_list, groove=groove))
    return bar
  # Make a part
  def get_part(self):
    sop_part = stream.Part()
    alt_part = stream.Part()
    count = 1
    for p in self.progs:
      sop_part.append(self.soprano_bar(chord=p, num_id=count))
      alt_part.append(self.alto_bar(chord=p, num_id=count))
      count += 1
    return [sop_part, alt_part]



  

 

  
