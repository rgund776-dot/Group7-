from data_representation import DataTable
from predictors import MajorityClassPredictor, NearestNeighborPredictor
from exceptions1 import OutOfSampleError

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"

def calculate_accuracy(predictions, actual):
    """
    Calculate prediction accuracy.
    """
    pass


def main():

    # test = DataTable(DATA_DIR / "test.csv")
    # get_value= test.get(1, 'Feature3')
    # print('value ',get_value)
    # get_column = test.get_column('TumorType')
    # print('column ',get_column)
    # get_row = test.get_row(2)
    # print('row ',get_row)
    # get_column_names = test.get_column_names()
    # print('names ',get_column_names)
    # get_column_average = test.get_column_average('Feature1')
    # print('average ',get_column_average)
    # get_column_min = test.get_column_min('Feature3')
    # print('min ',get_column_min)
    # get_column_max = test.get_column_max('Feature3')
    # print('max ',get_column_max)

    # Load datasets
    historical = DataTable(DATA_DIR / "cancer_historical1.csv")
    new_cases = DataTable(DATA_DIR / "cancer_new_cases1.csv")
    labels = DataTable(DATA_DIR / "cancer_new_cases_labels1.csv")

    # Create predictors
    mode_predictor = MajorityClassPredictor(historical)
    nn_predictor = NearestNeighborPredictor(historical)


    test_patient = new_cases.get_row(1)
    test_other = historical.get_row(1)
    mode_predictor.predict(test_patient)

    nn_predictor.distance(test_patient, test_other)
    nn_predictor.predict(test_patient)

    # mode_predictions = []
    # nn_predictions = []


    # # Predict every new case
    # for i in range(len(new_cases.data)):

    #     patient = new_cases.get_row(i)
        

    #     try:
    #         mode_predictions.append(
    #             mode_predictor.predict(patient)
    #         )

    #         nn_predictions.append(
    #             nn_predictor.predict(patient)
    #         )

    #     except OutOfSampleError as e:
    #         print(e)


    # # Get true labels
    # actual_labels = labels.get_column("TumorType")


    # # Accuracy
    # print(
    #     "Mode accuracy:",
    #     calculate_accuracy(mode_predictions, actual_labels)
    # )

    # print(
    #     "Nearest Neighbor accuracy:",
    #     calculate_accuracy(nn_predictions, actual_labels)
    # )


if __name__ == "__main__":
    main()