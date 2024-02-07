import logging
from ultralytics import YOLO
import os

current_folder = os.getcwd()
yaml_local_path = os.path.join(current_folder, 'datasets/data.yaml')

def train_model():
    try:
        # Load a model
        model = YOLO('yolov8n.yaml')  # build a new model from YAML
        model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
        model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

        # Train the model
        results = model.train(data=yaml_local_path, epochs=1, imgsz=640)

    except Exception as e:
        logging.error("Error in training model: {}".format(e))
        raise e