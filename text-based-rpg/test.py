#import winsound 
#winsound.PlaySound("C:/Users/nicol/Projecten/text_based_rpg/snore.wav",  winsound.SND_FILENAME)


import sys
import time
import winsound

import os
absolute_path = os.path.dirname(__file__)

q = "You're in the middle of your cell, picking your nose instead of your brain."
		

def print_clean(sentence): 
    winsound.PlaySound(absolute_path + "./sounds/typewriter.wav",  winsound.SND_FILENAME|winsound.SND_ASYNC)
    for word in sentence: 
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.03)
    winsound.PlaySound(None, winsound.SND_PURGE)

print_clean(q)