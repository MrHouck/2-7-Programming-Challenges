import numpy as np
import random
import re
from collections import defaultdict

import pickle

headlines = pickle.load(open("./reuters_headlines.pickle", 'rb'))
tokenized = []
for headline in headlines:
    for word in re.split('\W+', headline): #on my list compression hater arc
        tokenized.append(word)


markov = defaultdict(lambda: defaultdict(int))

last_word = tokenized[0].lower()
for word in tokenized[1:]:
    word = word.lower()
    markov[last_word][word] += 1
    last_word = word

def walk_markov(graph, distance = 5, start_node=None):
    if distance <= 0:
        return []
    
    if not start_node:
        start_node = random.choice(list(graph.keys()))
    
    weights = np.array(list(markov[start_node].values()),dtype=np.float64)
    weights /= weights.sum()

    choices = list(markov[start_node].keys())
    chosen_word = np.random.choice(choices, None, p=weights)
    return [chosen_word] + walk_markov(graph, distance=distance-1, start_node=chosen_word)

for i in range(10):
    print("The " + ' '.join(walk_markov(markov, distance=15, start_node="the")))