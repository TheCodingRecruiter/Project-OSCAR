# 3 billion base pairs
# A, G, T, C

import random

def complet_random():
    a = random.randint(1,100)
    # print(a)
    for i in range(a):
        b = random.randint(1,100)
        # print(b)
        for i in range(b):
            c = random.randint(1,100)
            # print(c)
    return c

dna_pairs = []
def random_list_choice(list):
    a = complet_random()
    for i in range(a):
        x = random.choice(list)
    dna_pairs.append(x)

base_pairs = ['A', 'G', 'T', 'C']
how_many_pairs = 5
for i in range(how_many_pairs):
    random_list_choice(base_pairs)

dna_cycles = 2
dna = []
for i in range(dna_cycles):
    x = ''
    for i in dna_pairs:
        x = str(x + i)
    dna.append(x)


print(dna)
# print(f'This DNA Strand has {how_many_pairs} pairs: {x}')
