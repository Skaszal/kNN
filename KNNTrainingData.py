from KNNSample import KNNSample
import numpy as np


class KNNTrainingData:
    def __init__(self, knnsamplelist, k):
        self.data = knnsamplelist
        self.k = k

    # TODO
    def assign(self, sample):
        sample = KNNSample(sample)
        distances = list()
        for x in self.data:
            x = KNNSample(x)
            dist = x.calculateDistance(sample)
            distances.append(x, dist)
        distances.sort(key=lambda tup: tup[1])
        neighbors = []
        for i in range(self.k):
            neighbors.append(distances[i][0])

        return neighbors
