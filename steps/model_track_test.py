import mlflow
from typing import Any

# https://www.youtube.com/watch?v=bwhcEi3fryM&list=PLQqR_3C2fhUUkoXAcomOxcvfPwRn90U-g&index=3

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


if __name__ == "__main__":
    # experiment_id = create_mlflow_experiment("testing_mlflow1", "testing_mlflow1_artifacts", {"env":"dev", "version":"1.0.0"})
    # print(f"Experiment ID: {experiment_id}")

    # experiment = get_mlflow_experiment(experiment_id="0")
    # print("Name: {}".format(experiment.name))

    experiment_id = create_mlflow_experiment(
        experiment_name="testing_mlflow1",
        artifact_location="testing_mlflow1_artifacts",
        tags={"env":"dev", "version":"1.0.0"},
    )

    experiment = get_mlflow_experiment(experiment_id=experiment_id)
    print("Name: {}".format(experiment.name))
    with mlflow.start_run(run_name="testing", experiment_id=experiment.experiment_id) as run:

        parameters = {
            "learning_rate": 0.01,
            "epochs": 10,
            "batch_size": 100,
            "loss_function": "mse",
            "optimizer": "adam"
        }
        mlflow.log_params(parameters)

        metrics = {
            "mse": 0.01,
            "mae": 0.01,
            "rmse": 0.01
        }

        mlflow.log_metrics(metrics)

        print("run_id: {}".format(run.info.run_id))
        print("experiment_id: {}".format(run.info.experiment_id))


