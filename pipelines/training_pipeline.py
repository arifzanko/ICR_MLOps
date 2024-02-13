from steps.ingest_data import ingest_df
from steps.model_train import train_model


def train_pipeline():
    #ingest_df()
    train_model()
    print("Done")
