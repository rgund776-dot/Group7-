
class PatientExam:
    def __init__(self, exam_id: int, date: str, name: str, weight: int, height: float):
        self.exam_id = exam_id
        self.date = date
        self.name = name
        self.weight = weight
        self.height = height

    def get_BMI(self, height: float, weight: float) -> None:
        return self.weight/(self.height**2)
    #make list of bmi? 
        
    def get_exam_month(self, exam_month: int) -> None:


#date = month/day/year eg 12/19/2002
#part that changes month number to month name?