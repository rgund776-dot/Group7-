from data_representation import DataTable
from predictors import MajorityClassPredictor, NearestNeighborPredictor
from exceptions import OutOfSampleError


def calculate_accuracy(predictions, actual):
    """
    Calculate prediction accuracy.
    """
    pass


def main():

    # Load datasets
    historical = DataTable("data/cancer_historical.csv")
    new_cases = DataTable("data/cancer_new_cases.csv")
    labels = DataTable("data/cancer_new_cases_labels.csv")


    # Create predictors
    mode_predictor = MajorityClassPredictor(historical)
    nn_predictor = NearestNeighborPredictor(historical)


    mode_predictions = []
    nn_predictions = []


    # Predict every new case
    for i in range(len(new_cases.data)):

        patient = new_cases.get_row(i)

        try:
            mode_predictions.append(
                mode_predictor.predict(patient)
            )

            nn_predictions.append(
                nn_predictor.predict(patient)
            )

        except OutOfSampleError as e:
            print(e)


    # Get true labels
    actual_labels = labels.get_column("TumorType")


    # Accuracy
    print(
        "Mode accuracy:",
        calculate_accuracy(mode_predictions, actual_labels)
    )

    print(
        "Nearest Neighbor accuracy:",
        calculate_accuracy(nn_predictions, actual_labels)
    )


if __name__ == "__main__":
    main()