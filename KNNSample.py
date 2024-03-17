import numpy as np


class KNNSample:

    def __init__(self, line):
        self.key = line.split(",")[-1]
        self.dataarr = line.split(",")[0:-1]

    # returns distance between two points
    def calculateDistance(self, knnsample):
        result = 0
        for x in range(len(self.dataarr)):
            tmp = (float(self.dataarr[x]) - float(knnsample.dataarr[x])) ** 2
            result += tmp
        result = result ** 0.5

        return result

    def __str__(self):
        return str(self.dataarr) + " " + self.key
