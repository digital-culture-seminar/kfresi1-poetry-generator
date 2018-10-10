# -*- coding: utf-8 -*-
"""
Created on Tus Aug 21 
@author: Katherine 
License: CC-BY-SA 4.0
Description: a simple python script
This is a temporary script file.
"""
mylist = []
for i in range(0,10):
    mylist.append("hello world" + str(i))
    print mylist
    print mylist[i]

with open("poem.md", "w") as p:
    for item in mylist:
        p.write (item) 
        p. write("/n")
# set variables
#world_adjective = "new"

# print statement 
#poem = "hello {adj} world!".format(adj=world_adjective)

#with open("poem.md", "w") as p:
#    p.write("## Title")
#    p.write("\n")
#    p.write("```")
#    p.write(poem)
#    p.write("```")

#with open("poem.md", "w") as p:
#  for i in range(1,10):
#    poem ="hello world" + str(i)
#    print poem 
#    p.write(poem)
#    p.write("\n")
    
#with open("poem.md", "w") as p:
#    p.write("""
### Title
# ```
#{poem}
#```
#""".format(poem=poem))





#poem = "I am starting a {adj} class." .format(adj=world_adjective)
#
#with open("poem.md", "w") as p:
#    p.write(poem)
