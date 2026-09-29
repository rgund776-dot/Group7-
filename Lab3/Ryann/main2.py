from classes import PatientExam
from exceptions import TextFormatException, MissingValueException, MeasurementUnitException

#start with parsing out the csv info into instances of patientexam 
#do something about these exceptions

def parse_row(row: str) -> list:
    values = row.strip().split(",")
    exam_id = int(values[0])
    date = values[1]
    name = values[2]
    weight_str = float(values[3])
    height = float(values[4])

    if not weight_str:
            raise MissingValueException()

    if not isinstance(weight_str, (int, float)):
         raise TextFormatException()

    weight = float(weight_str)

    if height >= 3:
         raise MeasurementUnitException()

    return [exam_id, date, name, weight, height]

def main():
    input_file = open("data.csv", "r")
    patient_list = []
    try:
        input_file.readline()
        for row in input_file:
            try:
                exam_id, date, name, weight, height =  parse_row(row)
                patient_list.append(PatientExam)
            except MissingValueException:
                print(f'{exam_id} weight is empty')
            except TextFormatException:
                print(f'{exam_id} weight is not a number')
            except MeasurementUnitException:
                print(f'{exam_id} height is in incorrect units')
            except:
                print('unknown error has occured')
    finally:
        print(patient_list)
        input_file.close()

main()

#store patientexam objects in a list 
#compute stats
#print avg bmi of all patients
#print busiest month (most common)

#use code from labs 1 & 2 as base 
#def avg_BMI(BMI: float):
    #need to access

#def busy_month(exam_month: float)


#print(f"The average BMI of all patients seen is", avg_BMI)
#print(f"The busiest month is", busy_month)
