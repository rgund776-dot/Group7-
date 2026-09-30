
class PatientExam:
    def __init__(self, patient_exam_id: int, patient_date: str, patient_name: str, patient_weight: int, patient_height: float):
        self.exam_id = patient_exam_id
        self.date = patient_date
        self.name = patient_name
        self.weight = patient_weight
        self.height = patient_height

    def get_BMI(self):
        return self.weight / (self.height ** 2)

    def get_exam_month(self):
        return int(self.date.split("/")[0])
    
    def __str__(self):
        return f'PatientExam(exam_id: {self.exam_id}, date: {self.date}, name: {self.name}, weight: {self.weight}, height: {self.height})'
    
    def __repr__(self):
        return f'PatientExam(exam_id: {self.exam_id}, date: {self.date}, name: {self.name}, weight: {self.weight}, height: {self.height})'