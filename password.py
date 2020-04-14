#!/usr/bin/python

import argparse
import random
import math

# éxtrait des mots de mots.txt
def words_from_file():
  f = open('mots.txt', 'r')
  lines = f.readlines()
  f.close()

  words = [line[:-1] for line in lines]
  return words

def random_word(words):
  r = random.SystemRandom()
  return r.choice(words)

def random_words(words, n):
  chosen = []
  for i in range(n):
    new_word = random_word(words)
    chosen.append(new_word)
  return chosen

def entropy_per_word(words):
  n = len(words)
  return math.log(n, 2)

def args():
  parser = argparse.ArgumentParser(description='Génère aléatoirement des mots de passe')
  parser.add_argument('-n', '--num', help='Nombre de mots à génerer. Par défault sur 5.', type=int, default=5)
  args = parser.parse_args()
  return args

def run(num):
  words = words_from_file()
  chosen = random_words(words, num)
  entropy = entropy_per_word(words)
  total_entropy = entropy*num

  print ("Mots choisis:")
  for word in chosen:
    print "  " + word
  print "Par mots : " + str(entropy)
  print "Total : " + str(total_entropy)

if __name__ == '__main__':
  args = args()
  n = args.num
  run(n)
