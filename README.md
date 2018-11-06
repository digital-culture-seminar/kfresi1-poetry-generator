# Poetry Repository
---

## Artist Statement 

Art is a major part of my life. It provides an escape and a way of understanding myself and the world around me. I find a new piece of myself with every work I create. Every time the pen touches the paper, the brush touches the canvas, or the needle touches the fabric a journey is begun, the wandering starts. So much of life is about control, restraint and reason. Art is about freedom, exploration and wandering. 

As an artist I have always been drawn to nature for inspiration in my work. I have a strong interest in the natural world and the colors and forms found therein. The woods and the beach are where I find peace and this is a powerful driving force in my art and design work. This will once again be the inspiration for my creative journey through this class. As I began brainstorming for material to write a poem I looked once again to the forest. The intent of my poem is to describe the feeling of a lush forest in late spring. The words are chosen to describe the colors, temperature, lighting, and feeling of a forest and are combined to describe a wandering journey through the forest. 

 


## Steps to Poem Construction 
1. String format with list of nouns, verbs, adverbs and adjectives
2. Random chance with three paths and two possible outcomes
3. Markovify
4. Final string format for a conclusion

### Step One
The poem is constructed using several methods. 

The first step was to gather words that come to mind when contemplating a forest. I have accumulated a list of nouns, verbs, adverbs, and adjectives. These focus on words that describe the temperature, lighting, foliage, and color of the forest. These words were then put into sentence form using string format to formulate the first portion of the poem. The intent is that these words will combine to create a feeling and environment of the natural world.

### Step Two
The second step of the process includes chance statements. There are three options for the wanderer to travel and two resulting destinations. This will add to the journey of the poem. If path two is chosen, the wanderer will come to a waterfall. If path one or three are chosen then the wanderer will come to a clearing. 

random.seed()
path = random.randint(1,3)
path = path

second_poem = "The wanderer meets a fork in the road. Path {path} is followed." .format(path=path)
 
if path == 2:
    third_poem = "A waterfall appears through the trees."

else:
    third_poem = "The wanderer then comes upon a clearing."

### Step Three
The third part of the poem is constructed using Markovify. Several literary works were used and gave varying results. The poem that gave the best results for my poem concept was The Way Through the Woods by Rudyard Kipling. 

### Step Four
For the final step, and the final line in the poem, I chose to create one more sentence from the original set of nouns, verbs, adjectives, and adverbs. This sentence is intended to match the first one. The journey through the woods have come to an end and the wanderer has come full circle. 

### Example of Code
Example one
    # write first part of poem
    
    p.write("## Wandering")
    
    p.write("\n")
    
    p.write("---")
    
    p.write("\n")
    
    p.write("```")
    
    p.write(first_poem)
    
    p.write("```") 
    
    p.write("\n")

## Poem 

 _Version One_
>The effervescent forest slowly enchants the wander
>while the warm sunlight softly filters through viridian leaves.
>The wander meets a fork in the road. Path 2 is followed.
>A waterfall appears through the trees.

 _Version Two_
>The effervescent forest slowly enchants the wander
>while the warm sunlight softly filters through viridian leaves.
>The wander meets a fork in the road. Path 2 is followed.
>A waterfall appears through the trees.
>The effervescent path slowly shimmers.

### Wandering
---
The effervescent forest slowly enchants the wanderer 
while the warm sunlight softly filters through viridian leaves.
The wanderer meets a fork in the road. Path 2 is followed.
A waterfall appears through the trees.
But there is no road through the woods Seventy years ago.
The effervescent forest slowly enchants.

#### Poem Link 
[Wandering](poem.md)


## Other Poem Results 

>The dark wilderness softly filters the wander
>while the warm flora softly shimmers through viridian leaves.
>The wander meets a fork in the road. Path 3 is followed.
>The wander then comes upon a clearing.

>The unsightly sunlight lightly filters
>while the primordial vines quietly filters through viridian leaves.
>The wander meets a fork in the road. Path 3 is followed.
>The wander then comes upon a clearing.

>The warm path slowly enchants
>while the shrouded wilderness slowly fall through viridian leaves.
>The wander meets a fork in the road. Path 1 is followed.
>The wander then comes upon a clearing.

## Markov Chain Examples 

>This I sat divining, with my head at ease reclining On the pallid bust of Pallas just above my chamber door.
>Leave my loneliness unbroken!--quit the bust above my chamber door-- Perched and sat and nothing more.

>And this was the reason that, long ago, In a kingdom by the sea.
>But the Raven, never flitting, still is sitting--still is sitting On the cushion's velvet lining that the lamp-light gloating o'er, >_She_ shall press, ah, nevermore!
>This I sat divining, with my head at ease reclining On the pallid bust of Pallas just above my door!

>As she said this, she was now, and she heard it muttering to itself ‘The Duchess!

>I was a child, In this kingdom by the sea, In her sepulchre there by the sea.

## Poem With Markov Chain

>The effervescent forest slowly enchants the wander
>while the warm sunlight softly filters through viridian leaves.
>The wander meets a fork in the road. Path 2 is followed.
>A waterfall appears through the trees.
>The effervescent path slowly shimmers.
>‘I couldn’t help it,’ said the March Hare.

>The effervescent forest slowly enchants the wander
>while the warm sunlight softly filters through viridian leaves.
>The wander meets a fork in the road. Path 2 is followed.
>A waterfall appears through the trees.
>The effervescent path slowly shimmers.
>‘Oh, you can’t swim, can you?’ he added, turning to the Classics master, though.

>The effervescent forest slowly enchants the wanderer while the warm sunlight softly filters through viridian leaves.
>The wanderer meets a fork in the road. Path 2 is followed.
>A waterfall appears through the trees.
>It is underneath the coppice and heath, And the badgers roll at ease, There was once a road through the woods Before they planted the trees.
>The effervescent forest slowly enchants.

>The effervescent forest slowly enchants the wanderer while the warm sunlight softly filters through viridian leaves.
>The wanderer meets a fork in the road. Path 1 is followed.
>The wanderer then comes upon a clearing.
>Yet, if you enter the woods Before they planted the trees.
>The effervescent forest slowly enchants.

