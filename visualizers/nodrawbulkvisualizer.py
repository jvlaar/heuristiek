import copy
from datahelper import DataHelper


class NoDrawBulkVisualizer:
    def __init__(self, area, algorithm, runs):
        self.area = area
        self.algorithm = algorithm
        self.originalArea = copy.deepcopy(area)
        self.originalAlgorithm = copy.copy(algorithm)
        self.runs = 0
        self.dataHelper = DataHelper()
        self.maxRuns = runs

    def on_execute(self):
        # Keep making steps until the algorithm is done
        while self.algorithm.isDone is False:
            self.algorithm.execute()

        if self.algorithm.isDone is True and self.runs < self.maxRuns:
            # reset to a fresh start
            self.area = copy.deepcopy(self.originalArea)
            self.algorithm = copy.copy(self.originalAlgorithm)
            self.algorithm.area = self.area
            # Save the area after every run
            self.dataHelper.writeArea(self.area)
            self.runs += 1
            self.on_execute()