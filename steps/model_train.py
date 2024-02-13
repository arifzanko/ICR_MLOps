import logging
import configparser
from pathlib import Path
from ultralytics import YOLO
import os

logging.basicConfig(level=logging.INFO, format='%(message)s')
confp = configparser.RawConfigParser()
confp.read(os.path.abspath(os.path.join(Path(__file__).absolute(), os.pardir)) + '/config.ini')

current_folder = os.getcwd()
yaml_local_path = os.path.join(current_folder, 'datasets/data.yaml')
num_of_epochs = int(confp.get("train","num_of_epochs"))
image_size = int(confp.get("train", "image_size"))

def train_model():
    """
    Train the model

    Args:
        num_of_epochs: number of epochs
        image_size: number of image size
    Returns:
        folder created in runs
    """
    try:
        # Load a model
        model = YOLO('yolov8n.yaml')  # build a new model from YAML
        model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
        model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

        # Train the model
        results = model.train(data=yaml_local_path, epochs=num_of_epochs, imgsz=image_size)

    except Exception as e:
        logging.error("Error in training model: {}".format(e))
        raise e