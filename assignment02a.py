"""
Assignment 2-A
==============

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""


def poem():

    a = 'This is the '
    b = 'That lay in the house that Jack built.'
    c = 'That ate the malt'
    d = 'That killed the rat,'
    e = 'That worried the cat,'
    f = 'That tossed the dog,'
    g = 'This is the cow with the crumpled horn,'
    h = 'That milked the cow with the crumpled horn,'
    i = 'That kissed the maiden all forlorn,'
    j = 'That married the man all tattered and torn,'
    k = 'That waked the priest all shaven and shorn,'
    l = 'That kept the cock that crowed in the morn,'
    m = 'This is the farmer sowing his corn,'
    n = 'house that Jack built.'
    return (f"{a}{n}\n\n{a}malt\n{b}\n\n{a}rat,\n{c}\n{b}\n\n{a}cat,\n{d}\n{c}\n{b}\n\n"
            f"{a}dog,\n{e}\n{d}\n{c}\n{b}\n\n{g}\n{f}\n{e}\n{d}\n{c}\n{b}\n\n{a}{i[16:]}\n{h}\n{f}\n{e}\n{d}\n{c}\n{b}\n\n"
            f"{a}{j[17:]}\n{i}\n{h}\n{f}\n{e}\n{d}\n{c}\n{b}\n\n{a}{k[15:]}\n{j}\n{i}\n{h}\n{f}\n{e}\n{d}\n{c}\n{b}\n\n"
            f"{a}{l[14:]}\n{k}\n{j}\n{i}\n{h}\n{f}\n{e}\n{d}\n{c}\n{b}\n\n{m}\n{l}\n{k}\n{j}\n{i}\n{h}\n{f}\n{e}\n{d}\n{c}\n{b}\n")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
