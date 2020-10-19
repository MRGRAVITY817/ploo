import random

def make_lines(time_sig, is_rand):
  bar = []
  # Make basic bass drum line
  if time_sig==3:
    bar.append(1)
    bar.append(-1)
    bar.append(-1)
  elif time_sig==4:
    bar.append(1)
    bar.append(-1)
    bar.append(1)
    bar.append(-1)
  # If random, shuffle the line list
  if is_rand==True:
    coin = [-1, 1]
    bar[0] = random.choice(coin)
  return bar