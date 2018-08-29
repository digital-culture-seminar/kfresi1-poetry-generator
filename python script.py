# -*- coding: utf-8 -*-
"""
Author: Katherine Fresina
Description: python text generator
Date: 8-28-2018
"""
import random 
random.seed()

# list of nouns
nouns = ["ocean", "sand", "water", "sun", "trees", "palms"]

# list of verbs
verbs = ["swim", "run", "play", "sleep", "read"]

# list of adjectives
adjectives = ["blue", "green", "hot", "lazy", "bright"]





noun = random.choice(nouns)
verb = random.choice(verbs)
adjectives = random.choice(adjectives)
second_adjectives = random.choice(adjectives)

# word poem
print "the " + adjectives + " " + noun + " "
# for loop iterate through verbs
for verb in verbs:
    whitespace= " " * i
    print whitespace + verb
    i = i + 1

## concatenation
#print "the" " " + noun + " "+ adjectives +", " + second_adjectives + " " + noun + " " + verb 
#
## string format
#print "The {adj} {n} {v}." .format(adj=adjectives, n=noun, v=verb)


#i=0
#for noun in nouns:
#
#    print nouns [i]
#    i=i+1

