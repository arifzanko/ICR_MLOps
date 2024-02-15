import os
import shutil
import logging

def delete_runs():
    current_path = os.getcwd()
    datasets_folder = os.path.join(current_path, "datasets")
    runs_folder = os.path.join(current_path, "runs")
    data_test_image = os.path.join(current_path, "data_test_analysis.png")
    data_train_image = os.path.join(current_path, "data_train_analysis.png")
    data_valid_image = os.path.join(current_path, "data_valid_analysis.png")

    # Delete the datasets folder and its contents
    shutil.rmtree(datasets_folder, ignore_errors=True)

    # Delete the runs folder and its contents
    shutil.rmtree(runs_folder, ignore_errors=True)

    # Delete the data_test_analysis.png file
    if os.path.exists(data_test_image):
        os.remove(data_test_image)

    # Delete the data_train_analysis.png file
    if os.path.exists(data_train_image):
        os.remove(data_train_image)

    # Delete the data_valid_analysis.png file
    if os.path.exists(data_valid_image):
        os.remove(data_valid_image)

    logging.info("Data deleted.")