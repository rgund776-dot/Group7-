# this line imports some custom exceptions for use in this lab
# raise/handle them just like Exception, ValueError, or any other type of exception
from exceptions import TextFormatException, MissingValueException, MeasurementUnitException

def compute_BMI(height: float, weight: float) -> float:
    return weight/(height**2)

def parse_row(row: str) -> list:
    values = row.strip().split(",") 
    exam_id = int(values[0])
    date = values[1]
    name = values[2]
    weight_str = values[3]

    if not weight_str:
        raise MissingValueException()
    try:
        weight = float(weight_str)
    except ValueError:
        raise TextFormatException()

    height = float(values[4])

    if height >= 3:
        raise MeasurementUnitException()
    
    return [exam_id, date, name, weight, height] 


def main():
    input_file = open("data.csv", "r")
    output_file = open('output.csv', 'w')
    try:
        output_file.write('Exam ID, BMI\n')
        input_file.readline()
        for row in input_file:
            try:
                exam_id, date, name, weight, height =  parse_row(row)
                bmi = compute_BMI(height, weight)
                output_file.write(f'{exam_id}, {bmi}\n')
            except MissingValueException:
                print(f'{exam_id} weight is empty')
            except TextFormatException:
                print(f'{exam_id} weight is not a number')
            except MeasurementUnitException:
                print(f'{exam_id} height is in incorrect units')
            except:
                print('unknown error has occured')
    finally:
        input_file.close()
        output_file.close()

main()