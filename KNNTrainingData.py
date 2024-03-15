from KNNSample import KNNSample
import numpy as np

class KNNTrainingData:
    def __init__(self, knnsamplelist, k):
        self.data = knnsamplelist
        self.k = k

    #TODO
    def assign(self, sample):
        sample = KNNSample(sample)

        for x in self.data:
            distances = np.linalg.norm(x - sample)

        nn_ids = distances.argsort()[self.k]
        return self.data[0].key