from abc import ABC, abstractmethod
import math

from exceptions import OutOfSampleError


class Predictor(ABC):

    def __init__(self, historical_data):
        """
        Store historical DataTable.
        """
        self.historical_data = historical_data
        
    def check_patient(self, patient):
        """
        Check whetehr patient featuers fall within historical min and max
        """
        for column in self.historical_data.get_column_names():
            if column == "TumorType":
                continue
            
            value = patient[column]
            
            minimum = self.historical_data.get_column_min(column)
            maximum = self.historical_data.get_column_max(column)
            
            if value < minimum or value > maximum: 
                raise OutOfSampleError(
                    f"{column} with value {value} is outside "
                    f"historical range [{minimum}, {maximum}]"
                )

    @abstractmethod
    def predict(self, patient):
        """
        Make a prediction for one patient.
        """
        pass


class MajorityClassPredictor(Predictor):

    def __init__(self, historical_data):
        super().__init__(historical_data)
        
        tumor_types = historical_data.get_column("TumorType")
        
        benign_count = tumor_types.count(0.0)
        malignant_count = tumor_types.count(1.0)
        
        if benign_count >= malignant_count:
            self.majority_class = 0 
        else:
            self.majority_class = 1 

    def predict(self, patient):
        """
        Always return the most common historical TumorType.
        """
        self.check_patient(patient)
        return self.majority_class 


class NearestNeighborPredictor(Predictor):

    def __init__(self, historical_data):
        super().__init__(historical_data)

    def distance(self, patient1, patient2):
        """
        Calculate Euclidean distance using Feature1-Feature9 only.
        """
        total = 0 
        
        for i in range(1,10):
            column = "Feature" + str(i)
            
            difference = patient1[column] - patient2[column]
            total = total + difference ** 2 
        
        return math.sqrt(total)

    def predict(self, patient):
        """
        Find closest historical patient and return its TumorType.
        """
        self.check_patient(patient)
        
        closest_patient = None 
        smallest_distance = None 
        
        for historical_patient in self.historical_data.data:
            current_distance = self.distance(
                patient, historical_patient 
            )
            
            if (smallest_distance is None or 
                current_distance < smallest_distance):
                smallest_distance = current_distance 
                closest_patient = historical_patient 
                
        return int(closest_patient["TumorType"])