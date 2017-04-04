import os
import sys
import random

otazky = open('otazky.txt', 'r')

quiz = { otazky.read()}
otazka = (random.choice(list(quiz.keys())))#  (random.choice( list(my_dict.keys())))
print(otazka)
otazky.close()
