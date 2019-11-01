# 3 billion base pairs
# A, G, T, C

import random

dna_pairs = []
def random_list_choice():
    a = random.randint(1,500)    # random number
    random_dna = []
    base_pairs = ['A', 'G', 'T', 'C']
    # repeat 5 time for each strand
    for i in range (5):
        # repeat x number of time and add to the array
        for i in range(a):
            x = random.choice(base_pairs)
        random_dna.append(x)
    return random_dna

def cycle_them(this):
    dna = []
    for i in range(this):
        dna_pairs = random_list_choice()
        x = ''
        for i in dna_pairs:
            x = str(x + i)
        dna.append(x)
    return dna


j = cycle_them(2)
print(j)

for i in j:
    file = open('dna.txt', 'a')
    file.write(i)
    file.write('\n')
    file.close()
