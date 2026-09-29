list_months = {
    "01": "January",
    "02": "Feburary",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

class PatientExam:
    def __init__(self, exam_id: int, date: str, name: str, weight: int, height: float):
        self.exam_id = exam_id
        self.date = date
        self.name = name
        self.weight = weight
        self.height = height

    def get_BMI(self, height: float, weight: float) -> None:
        return self.weight/(self.height**2)
        
    def get_exam_month(self, exam_month: int) -> None:
        return list_months[self.date]
