#!/usr/bin/python

import argparse
import random
import math

def mots_du_texte():
  f = open('mots.txt', 'r')
  lines = f.readlines()
  f.close()

  mots = [line[:-1] for line in lines]
  return mots

def random_mot(mots):
  r = random.SystemRandom()
  return r.choice(mots)

def random_mot(mots, n):
  choisi = []
  for i in range(n):
    new_mot = random_mot(mots)
    chosen.append(new_mot)
  return choisi

def entropie_par_mot(mots):
  n = len(mots)
  return math.log(n, 2)

def args():
  parser = argparse.ArgumentParser(description='Genere aleatoirement des mots de passe')
  parser.add_argument('-n', '--num', help='NB de mots a generer. Par Default c est 5.', type=int, default=5)
  args = parser.parse_args()
  return args

def run(num):
  words = mots_du_texte()
  choisi = random_mot(mots, num)
  entropie = entropie_par_mot(mots)
  total_entropie = entropie*num

  print ("Mots choisi :")
  for mot in choisi:
    print ("  " + mot )
  print ("entropie par mots: " + str(entropie))
  print ("total entropie: " + str(total_entropie))

if __name__ == '__main__':
  args = args()
  n = args.num
  run(-n)
