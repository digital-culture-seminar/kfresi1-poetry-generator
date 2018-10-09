# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:01:09 2018

markov chain
"""

# import libraries
import markovify


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


#print carroll_model.make_sentence()


#print carroll_model.make_short_sentence(50)

#for i in range(3):
#    print carroll_model.make_sentence()
#    print " "
    
with open ("poe.txt") as textfile: 
    poe = textfile.read()

with open ("the raven.txt") as textfile: 
    raven = textfile.read()
    
#print raven

raven_model = markovify.Text(raven)  
poe_model = markovify.Text(poe) 

synthesized_model = markovify.combine([raven_model, poe_model], [1,1])

print synthesized_model.make_sentence()
#
#
print raven_model.make_sentence(1)
#
#
##print raven_model.make_short_sentence(10)