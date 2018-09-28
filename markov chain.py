# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:01:09 2018

markov chain
"""

# import libraries
import markovify

# get raw text as string
with open ("ANNABEL LEE text for class.txt") as f: 
    text = f.read()


# build the model
text_model = markovify.NewlineText(text) #text_model = markovify.Text(text)

# print three randomly-generated sentences of no more than 140 characters
for i in range(3):
    print text_model.make_short_sentence(140)