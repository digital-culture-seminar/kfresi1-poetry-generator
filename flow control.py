# -*- coding: utf-8 -*-

import random

names = ["Alice", "Sam"]
name = random.choice(names)

pronouns = ["he", "she", "it"]
pronoun = random.choice(pronouns)





#print pronoun.capitalize() + " " + name

#print "One day {name} went to the store. {pronoun} paid for some bread. {name} went home then {pronoun} made some toast".format(name=name, pronoun=pronoun) 

roll = random.randint(1,6)
print "{name} rolled a {roll}".format(name=name, roll=roll)

if roll == 1:
#     print "success! " + pronoun + " rolled a " + str(roll)
#     print "success! {pronoun} rolled a {roll}".fromat (pronoun=pronoun, roll=roll)
    print "bad luck!"
elif roll == 6:
    print "good luck!"
else:
    print "not so bad luck..."