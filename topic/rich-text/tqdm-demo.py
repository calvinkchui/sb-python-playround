# Process-bar
# https://github.com/tqdm/tqdm


from tqdm import tqdm
from time import sleep

for i in tqdm(range(1000)):
    sleep(0.01)