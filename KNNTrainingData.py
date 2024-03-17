from KNNSample import KNNSample
import numpy as np
from collections import Counter


class KNNTrainingData:
    def __init__(self, knnsamplelist, k):
        self.data = knnsamplelist
        self.k = k

    # Returns string with label of the most occurring neighbours
    def assign(self, line):
        print(self.k)
        sample = KNNSample(line)
        distances = list()
        for x in self.data:
            dist = x.calculateDistance(sample)
            distances.append((x, dist))
        distances.sort(key=lambda tup: tup[1])
        neighbors = []
        for i in range(self.k):
            neighbors.append(distances[i][0].key)
        c = Counter(neighbors)
        # TODO Zamienic na max()
        return c.most_common(1)[0][0]
