from abc import ABC, abstractmethod
import math

from exceptions1 import OutOfSampleError


class Predictor(ABC):

    def __init__(self, historical_data):
        """
        Store historical DataTable.
        """
        self.historical_data = historical_data

    @abstractmethod
    def predict(self, patient):
        """
        Make a prediction for one patient.  
        """
        pass


class MajorityClassPredictor(Predictor):

    def __init__(self, historical_data):
        super().__init__(historical_data)
        self.majority_class = None
        # TODO: calculate most common TumorType

    def predict(self, patient):
        """
        Always return the most common historical TumorType.
        """
        TumorType_column = self.historical_data.get_column("TumorType")
        # print(TumorType_column)
        counts = {
            "benign" : 0, # 0.0
            "malignant": 0 #1.0
        }
        for value in TumorType_column:
                if value == 0.0:
                    counts["benign"] += 1
                if value == 1.0:
                    counts["malignant"] += 1

        self.majority_class = max(counts, key=counts.get)
        # print(counts)
        # print(self.majority_class)
        return self.majority_class


class NearestNeighborPredictor(Predictor):

    def __init__(self, historical_data):
        super().__init__(historical_data)

    def distance(self, patient1, patient2):
        """
        Calculate Euclidean distance using Feature1-Feature9 only.
        """
        feature_names = [name for name in self.historical_data.get_column_names() if name != "TumorType"]
        total = 0.0
        for feature in feature_names:
            total += (patient1[feature] - patient2[feature])**2
        return math.sqrt(total)

    def predict(self, patient):
        """
        Find closest historical patient and return its TumorType.
        """
        tumor_type = None
        smallest_distance = None
        patient2 = self.historical_data.get_row(i)
        for i in range(len(self.historical_data.data)):
            distance
        pass