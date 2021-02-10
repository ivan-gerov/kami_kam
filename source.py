#!/usr/local/bin/python
# -*- coding: utf8

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

def main():
    QUESTION = str(input("Kami-san, what is the greatest band in the world? "))
    possible_answers = ["Tool sa nais!",
                        "MEGUSHA",
                        "Ne znam, milichko, no shte ti izpratq nude pics i shte cuddle-vam step asap",
                        "<3"]
    if QUESTION in possible_answers:
        try:
            with open("encoded_message_for_Kami.txt", encoding="utf8", mode="r") as f:
                message = f.read()
        except Exception as e:
            print(e)
            raise Exception("Миличко, моля те, намери файла 'encoded_message_for_Kami.txt' и го сложи в същата папка като source.py")

        message = [char for char in message]
        message = unshuffle_list(message)
        print("".join(message))
    else:
        print("Unfortunately, this was a wrong answer...\n")
        print(f"Possible answers:")
        for id_, answer in enumerate(possible_answers):
            print(f"{id_+1}. {answer}")

if __name__ == "__main__":
    main()