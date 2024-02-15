from steps.ingest_data import ingest_df
from steps.data_exploration import data_explore
from steps.model_train import train_model
from steps.model_track import model_track
from steps.delete_folder import delete_runs


def train_pipeline():
    ingest_df()
    data_explore()
    train_model()
    model_track()
    delete_runs()
    print("----------Done Experiment----------")
