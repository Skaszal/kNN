import numpy as np


class KNNSample:

    def __init__(self, line):
        self.key = line.split(",")[-1]
        self.dataarr = np.array(line.split(",")[0:-1])

    def calculateDistance(self, knnsample):
        # returns distance between two points
        return np.linalg.norm(self.dataarr - knnsample)
