 # Working with files
 # Opened the file in Visual studio code and saved the file in a "rosalind.txt" format.
 # To access the file in read mode used the command below:
 `f = open('rosalind.txt', 'r')`
# As I opened and saved the file in VScode, the first line was labeled '1' and not zero, as a result I set the counter on 1(also as it was given in the return).
# Put the counter on even lines %2==0

  ======================================================================================  
counter = 1
for line in f:
    if counter %2 == 0:
        print(line)
    counter += 1

  ======================================================================================
Some things in life are bad, they can really make you mad

Other things just make you swear and curse

When you're chewing on life's gristle, don't grumble give a whistle

This will help things turn out for the best

Always look on the bright side of life

Always look on the right side of life

If life seems jolly rotten, there's something you've forgotten

And that's to laugh and smile and dance and sing

When you're feeling in the dumps, don't be silly, chumps

Just purse your lips and whistle, that's the thing

So, always look on the bright side of death

Just before you draw your terminal breath

Life's a counterfeit and when you look at it

Life's a laugh and death's the joke, it's true

You see, it's all a show, keep them laughing as you go

Just remember the last laugh is on you

Always look on the bright side of life

And always look on the right side of life

Always look on the bright side of life

And always look on the right side of life