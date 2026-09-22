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
    
    input_file = open("data.csv","r")
    output_file = open("output.csv","w")
    try:
        output_file.write("Name,Height,Weight,BMI\n")
        input_file.readline()

        for row in input_file:
            exam_id = row.split(",")[0] #buffer
            try:
                exam_id, date, name, weight, height = parse_row(row)
                bmi = compute_BMI(height, weight)
                output_file.write(f'{exam_id},{bmi}\n') #f is format

            except MissingValueException:
                print(f'{exam_id} weight is missing')
            except TextFormatException:
                print(f'{exam_id} weight is not a number')
            except MeasurementUnitException:
                print(f'{exam_id} height is in incorrect units')
            except:
                print('unexpected error')

    finally:
        print("done")
        input_file.close()
        output_file.close()

main()