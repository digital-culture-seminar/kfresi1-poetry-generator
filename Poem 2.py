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
#third_noun = random.choice(nouns)
#third_verb= random.choice(verbs)
#third_adjective= random.choice(adjectives)
#third_adverb= random.choice(adverbs)


# string format
random.seed()

path = random.randint(1,3)
path = path   

poem = "The {adj} {n} {adv} {v} the wanderer while the {sec_adj} {sec_n}\
 {sec_adv} {sec_v} through viridian leaves. The wander meets a fork in the road.\
 Path {path} is followed." .format(adj=adjective, n=noun,\
 adv=adverb,v=verb, sec_adj=second_adjective, sec_n=second_noun,\
 sec_adv=second_adverb, sec_v=second_verb, path=path)
 
if path == 2:
    print "A waterfall appears through the trees."
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
else:
    print "The wander then comes upon a clearing."


 
with open("poem.md", "w") as p:
    p.write("## Title")
    p.write("\n")
    p.write("```")
    p.write(poem)
    p.write("```")

    
#print "while the {sec_adj} {sec_n} {sec_adv} {sec_v} through viridian\
# leaves.".format(sec_adj=second_adjective, sec_n=second_noun, sec_adv=second_adverb, 
#           sec_v=second_verb)



#i=0
#for noun in nouns:
#    print nouns [i]
#    i=i
#   
#add random if else to my poem 
#random.seed()
#path = random.randint(1,3)
#path = path

#print "The wander meets a fork in the road. Path {path} is \
#followed." .format(path=path)
# 
#if path == 2:
#    print "A waterfall appears through the trees."
#
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
#else:
#    print "The wander then comes upon a clearing."

import markovify

with open ("the woods.txt") as textfile: 
    woods = textfile.read()
    
woods_model = markovify.Text(woods) 
print woods_model.make_sentence() 

random.seed(2)

third_noun = random.choice(nouns)
third_verb= random.choice(verbs)
third_adjective= random.choice(adjectives)
third_adverb= random.choice(adverbs)

print "The {third_adj} {third_n} {third_adv} {third_v}.".format\
(third_adj=adjective, third_n=third_noun, third_adv=third_adverb,\
 third_v=third_verb)

#add markovify to my poem

#
#with open ("alice.txt") as textfile: 
#    carroll = textfile.read()
#    
#with open ("poe.txt") as textfile: 
#    poe = textfile.read()
#    
##print carroll
#
#carroll_model = markovify.Text(carroll)  
#poe_model = markovify.Text(poe) 
#
#synthesized_model = markovify.combine([carroll_model, poe_model], [1,1])
#
#print synthesized_model.make_sentence()


#with open ("poe.txt") as textfile: 
#    poe = textfile.read()
#
#with open ("the raven.txt") as textfile: 
#    raven = textfile.read()
#    
##print raven
#
#raven_model = markovify.Text(raven)  
#poe_model = markovify.Text(poe) 
#
#synthesized_model = markovify.combine([raven_model, poe_model], [1,1])
#
#print synthesized_model.make_sentence()


