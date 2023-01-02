# -*- coding: latin-1 -*-
import random

sana = None

with open('sanat.txt', 'r') as file:
    allText = file.read()
    words = list(map(str, allText.split()))

    sana = (random.choice(words))
    print(sana)
    while '-' in sana or ' ' in sana or 'å' in sana or 'ö' in sana or 'ä' in sana:
        word = (random.choice(words))

sana = sana.upper()
print(sana)