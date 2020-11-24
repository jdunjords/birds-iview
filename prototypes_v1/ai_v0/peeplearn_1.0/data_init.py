'''
Start with 3 classes
	1) 035.Purple_Finch
	2) 073.Blue_Jay
	3) 191.Red_headed_Woodpecker

Organize data into train, validation, test

per class:  50 train,  5 valid,  5 test
    total: 150 train, 15 valid, 15 test
'''

import os
import shutil
import random
import glob

os.chdir('3birds/')

# randomly take 150 images for training
for c in random.sample(glob.glob('Purple_Finch/*'), 50):
	shutil.move(c, 'train/Purple_Finch')
for c in random.sample(glob.glob('Blue_Jay/*'), 50):
	shutil.move(c, 'train/Blue_Jay')
for c in random.sample(glob.glob('Red_headed_Woodpecker/*'), 50):
	shutil.move(c, 'train/Red_headed_Woodpecker')

# randomly take 15 images for validation
for c in random.sample(glob.glob('Purple_Finch/*'), 5):
	shutil.move(c, 'valid/Purple_Finch')
for c in random.sample(glob.glob('Blue_Jay/*'), 5):
	shutil.move(c, 'valid/Blue_Jay')
for c in random.sample(glob.glob('Red_headed_Woodpecker/*'), 5):
	shutil.move(c, 'valid/Red_headed_Woodpecker')

# randomly take 15 images for test
for c in random.sample(glob.glob('Purple_Finch/*'), 5):
	shutil.move(c, 'test/Purple_Finch')
for c in random.sample(glob.glob('Blue_Jay/*'), 5):
	shutil.move(c, 'test/Blue_Jay')
for c in random.sample(glob.glob('Red_headed_Woodpecker/*'), 5):
	shutil.move(c, 'test/Red_headed_Woodpecker')

