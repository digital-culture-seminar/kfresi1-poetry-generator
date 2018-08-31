# -*- coding: utf-8 -*-
"""
Author: Katherine Fresina
Description: This is a first draft of what will be a poem.
Programmer statement: To accumulate a group of nouns, verbs, adjectives and 
adverbs of create a poem describing the feeling of a 
forest in the late spring. 

"""

import random 

random.seed()

# list of nouns 
nouns= ["tree", 
        "flora", 
        "vines", 
        "path", 
        "squirrel", 
        "wilderness", 
        "forest", 
        "sunlight"]

# list of verbs
verbs= ["Filters", 
        "coils", 
        "shimmers", 
        "scampers", 
        "filters", 
        "Meanders"]

# list of adjectives 
adjectives= ["Effervescent", 
             "unsightly", 
             "shrouded", 
             "deep", 
             "dark", 
             "cool", 
             "majestic", 
             "primordial"]

# list of adverbs
adverbs= ["slowly", 
          "quietly",
          "softly"]


noun = random.choice(nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)
adverb = random.choice(adverbs)

# string format
print "The {adj} {n} {adv} {v}." .format(adj=adjective, n=noun, adv=adverb, 
           v=verb)