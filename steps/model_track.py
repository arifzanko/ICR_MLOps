import mlflow
from typing import Any
import os
from pathlib import Path
import configparser
import os
import csv

confp = configparser.RawConfigParser()
confp.read(os.path.abspath(os.path.join(Path(__file__).absolute(), os.pardir)) + '/config.ini')
num_of_epochs = confp.get("train","num_of_epochs")
image_size = confp.get("train","image_size")

def create_mlflow_experiment(experiment_name: str, artifact_location: str, tags:dict[str,Any]) -> str:
    """
    Create a new mlflow experiment with the given name and artifact location.
    """

    try:
        experiment_id = mlflow.create_experiment(
            name=experiment_name, artifact_location=artifact_location, tags=tags
        )
    except:
        print(f"Experiment {experiment_name} already exists.")
        experiment_id = mlflow.get_experiment_by_name(experiment_name).experiment_id

    return experiment_id


def get_mlflow_experiment(experiment_id:str=None, experiment_name:str=None) -> mlflow.entities.Experiment:
    """
    Retrieve the mlflow experiment with the given id or name.

    Parameter:
    -----------
    experiment_id: str
        The id of the experiment to retrieve.
    experiment_name: str
        The name of the experiment to retrieve.

    Returns:
    -----------
    experiment: mlflow.entities.Experiment
        The mlflow experiment with the given id or name.
    """
    if experiment_id is not None:
        experiment = mlflow.get_experiment(experiment_id)
    elif experiment_name is not None:
        experiment = mlflow.get_experiment_by_name(experiment_name)
    else:
        raise ValueError("Either experiment_id or experiment_name must be provided.")
    return experiment

def get_metrics():
    current_path = os.getcwd()
    train_output_path = "runs/detect/train/results.csv"

    last_row = None
    csv_file_path = os.path.join(current_path, train_output_path)
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            last_row = row

    train_box_loss = float(last_row[1].replace(" ",""))
    train_cls_loss = float(last_row[2].replace(" ", ""))
    train_dfl_loss = float(last_row[3].replace(" ", ""))
    metrics_precision_B = float(last_row[4].replace(" ", ""))
    metrics_recall_B = float(last_row[5].replace(" ", ""))
    metrics_mAP50_B = float(last_row[6].replace(" ", ""))
    
    metrics = {
    "train_box_loss": train_box_loss,
    "train_cls_loss": train_cls_loss,
    "train_dfl_loss": train_dfl_loss,
    "metrics_precision_B" : metrics_precision_B,
    "metrics_recall_B" : metrics_recall_B,
    "metrics_mAP50_B" : metrics_mAP50_B
    }

    return metrics

if __name__ == "__main__":

    experiment_id = create_mlflow_experiment(
        experiment_name="icr",
        artifact_location="icr_artifacts",
        tags={"env":"dev", "version":"1.0.0"},
    )

    experiment = get_mlflow_experiment(experiment_id=experiment_id)
    with mlflow.start_run(run_name="testing", experiment_id=experiment.experiment_id) as run:

        parameters = {
            "epochs": num_of_epochs,
            "image_size": image_size,
        }
        mlflow.log_params(parameters)

        metrics = get_metrics()
        mlflow.log_metrics(metrics)

        print("run_id: {}".format(run.info.run_id))
        print("experiment_id: {}".format(run.info.experiment_id))