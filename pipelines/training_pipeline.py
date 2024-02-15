from steps.ingest_data import ingest_df
from steps.data_exploration import data_explore
from steps.model_train import train_model
from steps.model_track import model_track


def train_pipeline():
    #ingest_df()
    data_explore()
    #train_model()
    model_track()
    print("----------Done Experiment----------")
