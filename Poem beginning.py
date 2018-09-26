# -*- coding: utf-8 -*-
"""
Author: Katherine Fresina
Description: This is a first draft of what will be a poem.
Programmer statement: To accumulate a group of nouns, verbs, adjectives and 
adverbs of create a poem describing the feeling of a 
forest in the late spring. 

"""

import random 

random.seed(2)

# list of nouns 
nouns= ["wilderness",
        "vines",
        "leaves", 
        "flora", 
        "path", 
        "sunlight", 
        "forest"]

# list of verbs
verbs= ["meanders", 
        "coils",
        "fall",
        "shimmers", 
        "filters",
        "enchants"]

# list of adjectives 
adjectives= ["effervescent", 
             "unsightly", 
             "shrouded", 
             "deep", 
             "dark", 
             "warm", 
             "majestic", 
             "primordial"]

# list of adverbs
adverbs= ["slowly", 
          "softly",
          "lightly",
          "quietly",]


noun = random.choice(nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)
adverb = random.choice(adverbs)
second_noun = random.choice(nouns)
second_verb = random.choice(verbs)
second_adjective = random.choice(adjectives)
second_adverb = random.choice(adverbs)



# string format
print "The {adj} {n} {adv} {v} the wander" .format(adj=adjective, n=noun, adv=adverb, 
           v=verb)
print "while the {sec_adj} {sec_n} {sec_adv} {sec_v} through viridian leaves.".format(sec_adj=second_adjective, sec_n=second_noun, sec_adv=second_adverb, 
           sec_v=second_verb)


#i=0
#for noun in nouns:
#    print nouns [i]
#    i=i
#    


