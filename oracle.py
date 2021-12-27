import random, pathlib,os
from pathlib import Path
from random import choice

#Full path to the directory holding the deck
deck = '/path/goes/here/'

#Choose a random card from the deck.
path: Path = Path(deck)
# Convert path.iterdir() to a list - choice needs something to iterate
random_card = choice(list(path.iterdir()))

#Open the card in its default program.
os.system('cd /')
#On Mac, use:
os.system('open ' + str(random_card))

#On Windows, use:
#os.system('start ' + str(random_card))
