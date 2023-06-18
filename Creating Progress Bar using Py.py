'''

Create Progress Bar using Python

'''

# import the necessary module !

from tqdm import tqdm, trange
from time import sleep

for i in trange(5): #Change the value here
    sleep(0.4)

# OR

for i in tqdm(range(5)):
    sleep(0.4)