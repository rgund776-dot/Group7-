
class PatientExam:
    
    def __init__(self, exam_id: int, date: str, name: str, weight: int, height: float):
        self.exam_id = exam_id
        self.date = date 
        self.name = name
        self.weight = weight 
        self.height = height 
        
        
def get_bmi(self) -> float:
    return self.weight / (self.height ** 2) 

def get_exam_month(self) -> int: 
    return int(self.date.split("/"[0])
               
