from classes import PatientExam

# test for month is under 12, weight and height are correct units, no missing values

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def parse_file(file_path: str) -> list:
    with open(file_path, 'r') as file:
        lines = file.read()
        exams = []
        for patient in lines.splitlines()[1:]:
            # print(f'patient: {patient}')
            patient_data = patient.split(',')
            try:
                # check for missing values
                if len(patient_data) != 5:
                    raise ValueError(f'Invalid number of values in row: {patient}')
                # weight check
                if not patient_data[3].isdigit():
                    raise ValueError(f'Weight is not an integer in row: {patient}')
                # height check
                if not is_float(patient_data[4]):
                    raise ValueError(f'Height is not a valid number in row: {patient}')
                if not float(patient_data[4]) <= 3.0:
                    raise ValueError(f'Height is not in meters in row: {patient}')
                # month check
                if not (1 <= int(patient_data[1].split("/")[0]) <= 12):
                    raise ValueError(f'Invalid date in date field in row: {patient}')
            except Exception as e:
                raise Exception(e)

            exam = PatientExam(
                int(patient_data[0]),
                patient_data[1],
                patient_data[2],
                int(patient_data[3]),
                float(patient_data[4])
            )
            exams.append(exam)
    return exams

def avg_bmi(exams: list) -> float:
    total_bmi = 0
    for exam in exams:
        total_bmi += exam.get_BMI()
    return total_bmi / len(exams)

def busiest_month(exams: list) -> int:
    month_counts = {}
    for exam in exams:
        month = exam.get_exam_month()
        if month in month_counts:
            month_counts[month] += 1
        else:
            month_counts[month] = 1
    busiest_month = max(month_counts, key=month_counts.get)
    return busiest_month


def main():
    try:
        exams = parse_file('./patient_data.csv')
        average_bmi = avg_bmi(exams)
        print(f'Average BMI: {average_bmi:.2f}')
        busiest_month_num = busiest_month(exams)
        print(f'Busiest Month: {busiest_month_num}')
    except Exception as e:
        raise Exception(f'error in file: {e}')

main()
# your code here