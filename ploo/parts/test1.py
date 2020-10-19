from music21 import stream
import commons
import progressions
from melody import Melody
from drums import Drum 
from bass import Bass

'''
progs = 'Dm7 G7 CM7 FM7 Bdim7 E7 Am7 E-7 Dm7 G7 Em7 Am7 Dm7 G7 Em7 A7'.split()
time_sig = "3/4"
'''
progs = "Am7 D7 GM7 CM7 F#dim7 B7 Em Em Am7 D7 GM7 CM7 F#dim7 B7 Em Em".split()
time_sig = "4/4"

filepath = "../inst/"

def auto_compose(progs, time_sig, path):
  progs = progressions.slice_bar(progs)
  st1 = stream.Stream()
  # Get Parts
  m_part = Melody(progs=progs, time_sig=time_sig).part
  b_part = Bass(progs=progs, time_sig=time_sig).part
  d_part = Drum(progs=progs, time_sig=time_sig).score
  # Append Parts
  st1.insert(0, m_part)
  st1.insert(0, b_part)
  st1.insert(0, d_part)
  commons.save(input_score=st1, path=filepath) 

auto_compose(progs=progs, time_sig=time_sig, path=filepath)