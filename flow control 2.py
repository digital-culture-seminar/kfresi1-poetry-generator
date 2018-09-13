# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 15:26:04 2018

@author: kfres
"""

# -*- coding: utf-8 -*-

import random

#names = ["Alice", "Sam"]
#name = random.choice(names)
#
#pronouns = ["he", "she", "it"]
#pronoun = random.choice(pronouns)
#
#
#
#
#
##print pronoun.capitalize() + " " + name
#
##print "One day {name} went to the store. {pronoun} paid for some bread. {name} went home then {pronoun} made some toast".format(name=name, pronoun=pronoun) 
#
#roll = random.randint(1,6)
#print "{name} rolled a {roll}".format(name=name, roll=roll)
#
#if roll == 1:
##     print "success! " + pronoun + " rolled a " + str(roll)
##     print "success! {pronoun} rolled a {roll}".fromat (pronoun=pronoun, roll=roll)
#    print "bad luck!"
#elif roll == 6:
#    print "good luck!"
#else:
#    print "not so bad luck..."
#    

#practice story 

name = ["Stormy", "Sunny", "Cloud"]
name = random.choice(names)

pronouns = ["he", "she"]
pronoun = random.choice(pronouns)

scan = random.randint(10,50)
scan = scan


    
print "{name} scanned a {scan}".format(name=names, scan=scan)
#
#print "One day {name} went to the store to buy a shirt. /
#       While on the way, {pronoun} discounted clothing at a store in the mall. /
#       Examining the ad /closer, {name} noticed that discount was not listed /
#       until the coupon was / scanned that the store. {pronoun} read that the /
#       amounts could be / between 10 to 50 percent off. When {name} presented / 
#       the coupon the / cashier scanned the page.".format(name=name, pronoun=pronoun)


print "One day {name} went to the store to buy a shirt. While on the way, {pronoun} saw an ad in the paper with a coupon for discounted clothing at a store in the mall. Examining the ad closer, {pronoun} noticed that discount was not listed until the coupon was scanned that the store. {name} read that the amounts could be between 10 to 50 percent off. When {pronoun} presented the coupon, the cashier scanned a {scan} percent discount.".format(name=name, pronoun=pronoun, scan=scan)

if scan == 10-25:
    print "{name} decided not to buy the shirt.".format(name=name)
    
else:
    print "{name} decided to buy the shirt.".format(name=name)
