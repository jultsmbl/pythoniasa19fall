"""
Assignment 1-A
==============

Update the Python script below to make it more compact and readable; use at least variables and f-strings.
For those who are already familiar with Python – write the best code you can to conform to the Zen of Python.

"""
a = 'This is the '
b = 'That lay in the house that Jack built.'
c = 'That ate the malt '
d = 'That kill"d the rat,'
e = 'That worried the cat, '
f = 'That toss"d the dog, '
g = 'This is the cow with the crumpled horn,'
h = 'That milk"d the cow with the crumpled horn,'
i = 'That kissed the maiden all forlorn,  '
j = 'That married the man all tatter"d and torn, '
k = 'That waked the priest all shaven and shorn, '
l = 'That kept the cock that crow"d in the morn, '
m = 'This is the farmer sowing his corn, '

poem = '''
print(a + b[16:] + '\n' + '\n' + a + c[13:] + '\n' + b + '\n')
print(f"{a}rat,\n{c}\n{b}\n")
print(f"{a}cat,\n{d}\n{c}\n{b}\n")
print(f"{a}dog,\n{e}\n{d}\n{c}\n{b}\n")
print(f"{g}\n{f}\n{e}\n{d}\n{c}\n{b}\n")
print(f"{a}{i[16:]}\n{h}\n{f}\n{e}\n{d}\n{c}\n{b}\n")
print(f"{a}{j[17:]}\n{i}\n{h}\n{f}\n{e}\n{d}\n{c}\n{b}\n")
print(f"{a}{k[15:]}\n{j}\n{i}\n{h}\n{f}\n{e}\n{d}\n{c}\n{b}\n")
print(f"{a}{l[14:]}\n{k}\n{j}\n{i}\n{h}\n{f}\n{e}\n{d}\n{c}\n{b}\n")
print(f"{m}\n{l}\n{k}\n{j}\n{i}\n{h}\n{f}\n{e}\n{d}\n{c}\n{b}\n")
This is the house that Jack built.

This is the malt 
That lay in the house that Jack built.

This is the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cow with the crumpled horn, 
That toss'd the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the maiden all forlorn, 
That milk'd the cow with the crumpled horn, 
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the priest all shaven and shorn, 
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milked the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cock that crow'd in the morn, 
That waked the priest all shaven and shorn, 
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn, 
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the farmer sowing his corn, 
That kept the cock that crow'd in the morn, 
That waked the priest all shaven and shorn,
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That killed the rat, 
That ate the malt 
That lay in the house that Jack built.
'''

print(poem)
