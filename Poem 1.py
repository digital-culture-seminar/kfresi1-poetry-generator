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
first_poem = "The {adj} {n} {adv} {v} the wanderer while the {sec_adj} {sec_n}\
 {sec_adv} {sec_v} through viridian leaves." .format(adj=adjective, n=noun,\
 adv=adverb,v=verb, sec_adj=second_adjective, sec_n=second_noun,\
 sec_adv=second_adverb, sec_v=second_verb)
 
random.seed()
path = random.randint(1,3)
path = path

second_poem = "The wanderer meets a fork in the road. Path {path} is \
followed." .format(path=path)
 
if path == 2:
    third_poem = "A waterfall appears through the trees."
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
else:
    third_poem = "The wanderer then comes upon a clearing."

import markovify

with open ("the woods.txt") as textfile: 
    woods = textfile.read()
    
woods_model = markovify.Text(woods) 
fourth_poem = woods_model.make_sentence() 

random.seed(2)

third_noun = random.choice(nouns)
third_verb= random.choice(verbs)
third_adjective= random.choice(adjectives)
third_adverb= random.choice(adverbs)

fifth_poem = "The {third_adj} {third_n} {third_adv} {third_v}.".format\
(third_adj=adjective, third_n=third_noun, third_adv=third_adverb,\
 third_v=third_verb)

# export markdown

with open("poem.md", "w") as p:

    # write first part of poem
    p.write("## Wandering")
    p.write("\n")
    p.write("---")
    p.write("\n")
    p.write("```")
    p.write(first_poem)
    p.write("```") 
    p.write("\n")

    # write second part of poem
    p.write("\n")
    p.write("```")
    p.write(second_poem)
    p.write("```") 
    p.write("\n")

    # write third part of poem
    p.write("\n")
    p.write("```")
    p.write(third_poem)
    p.write("```") 
    p.write("\n")

    # write fourth part of poem
    p.write("\n")
    p.write("```")
    p.write(fourth_poem)
    p.write("```") 
    p.write("\n")
    
    # write fifth part of poem
    p.write("\n")
    p.write("```")
    p.write(fifth_poem)
    p.write("```") 
    p.write("\n")


# text to speech

#tts = gTTS(first_poem + second_poem + third_poem + fourth_poem + fifth_poem\
#           , lang='en')
#
#
#
## write audio file
#
#tts.save("wandering.mp3")
#
#
#
## play audio file
#
#playsound("wandering.mp3")


