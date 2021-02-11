
import random

random.seed(42)

def shuffle_under_seed(ls):
  # Shuffle the list ls using the seed `seed`
  random.shuffle(ls)
  return ls
    
def unshuffle_list(shuffled_ls):
  n = len(shuffled_ls)
  perm = [i for i in range(1, n + 1)]
  shuffled_perm = shuffle_under_seed(perm)
  zipped_ls = list(zip(shuffled_ls, shuffled_perm))
  zipped_ls.sort(key=lambda x: x[1])
  ls = [a for (a, b) in zipped_ls]
  return ls