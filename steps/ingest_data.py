import logging
import boto3
import os
import configparser
from pathlib import Path
import yaml
from tqdm import tqdm

logging.basicConfig(level=logging.INFO, format='%(message)s')
confp = configparser.RawConfigParser()
confp.read(os.path.abspath(os.path.join(Path(__file__).absolute(), os.pardir)) + '/config.ini')

aws_access_key_id = confp.get("aws","aws_access_key_id")
aws_secret_access_key = confp.get("aws","aws_secret_access_key")
bucket_name = confp.get("s3","bucket")
datasets_path_s3 = confp.get("s3", "datasets_path")
datasets_folder_local = "datasets"

class IngestData:
    """
    Ingesting the data from the S3
    """
    def __init__(self, datasets_path_s3: str):
        """
        Args:
            datasets_path: path to datasets folder
        """
        self.datasets_path_s3 = datasets_path_s3
    
    def create_folder(self):
        """
        Create folder for store datasets
        """
        current_folder = os.getcwd()
        datasets_path_local = os.path.join(current_folder, datasets_folder_local)
        if not os.path.exists(datasets_path_local):
            os.makedirs(datasets_path_local)
            logging.info(f"Folder {datasets_folder_local} created")
        
        # Create subfolders train, test, and valid
        subfolders = ['train', 'test', 'valid']
        for subfolder in subfolders:
            subfolder_path = os.path.join(datasets_path_local, subfolder)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
                logging.info(f"Subfolder {subfolder} created inside {datasets_folder_local}")
        
            # Create 'images' folder
            images_folder_path = os.path.join(subfolder_path, 'images')
            if not os.path.exists(images_folder_path):
                os.makedirs(images_folder_path)
            
            # Create 'labels' folder
            labels_folder_path = os.path.join(subfolder_path, 'labels')
            if not os.path.exists(labels_folder_path):
                os.makedirs(labels_folder_path)

        # Create data.yaml file
        data_yaml_path = os.path.join(datasets_path_local, 'data.yaml')
        if not os.path.exists(data_yaml_path):
            data_yaml_content = {}  # You can customize the content as needed
            with open(data_yaml_path, 'w') as yaml_file:
                yaml.dump(data_yaml_content, yaml_file)
                logging.info(f"data.yaml file created inside {datasets_folder_local}")


    def get_data_test(self):
        """
        Ingesting the data test from the datasets_path
        """
        test_s3_path_labels = 'lpskor/icr/test/labels/'
        current_folder = os.getcwd()
        test_folder_path_labels = os.path.join(current_folder, 'datasets/test/labels')

        s3 = boto3.client('s3', aws_access_key_id = aws_access_key_id, aws_secret_access_key = aws_secret_access_key)
        objects = s3.list_objects(Bucket=bucket_name, Prefix=test_s3_path_labels)['Contents']
        for index, obj in enumerate(objects):
            if index == 0:
                continue  # Skip the first iteration
            key = obj['Key']
            local_file_path = os.path.join(test_folder_path_labels, os.path.basename(key))
            s3.download_file(bucket_name, key, local_file_path)
            # print(f'Downloaded: {key} to {local_file_path}')
        logging.info(f"Finish download test labels {test_folder_path_labels}")


        test_s3_path_images = 'lpskor/icr/test/images/'
        current_folder = os.getcwd()
        test_folder_path_images = os.path.join(current_folder, 'datasets/test/images')
        objects = s3.list_objects(Bucket=bucket_name, Prefix=test_s3_path_images)['Contents']
        for index, obj in enumerate(objects):
            if index == 0:
                continue  # Skip the first iteration
            key = obj['Key']
            local_file_path = os.path.join(test_folder_path_images, os.path.basename(key))
            s3.download_file(bucket_name, key, local_file_path)
            # print(f'Downloaded: {key} to {local_file_path}')
        logging.info(f"Finish download test images {test_folder_path_images}")
    
    def get_data_train(self):
        """
        Ingesting the data train from the datasets_path
        """
        train_s3_path_labels = 'lpskor/icr/train/labels/'
        current_folder = os.getcwd()
        train_folder_path_labels = os.path.join(current_folder, 'datasets/train/labels')

        s3 = boto3.client('s3', aws_access_key_id = aws_access_key_id, aws_secret_access_key = aws_secret_access_key)
        objects = s3.list_objects(Bucket=bucket_name, Prefix=train_s3_path_labels)['Contents']
        for index, obj in enumerate(objects):
            if index == 0:
                continue  # Skip the first iteration
            key = obj['Key']
            local_file_path = os.path.join(train_folder_path_labels, os.path.basename(key))
            s3.download_file(bucket_name, key, local_file_path)
            # print(f'Downloaded: {key} to {local_file_path}')
        logging.info(f"Finish download train labels {train_folder_path_labels}")


        train_s3_path_images = 'lpskor/icr/train/images/'
        current_folder = os.getcwd()
        train_folder_path_images = os.path.join(current_folder, 'datasets/train/images')
        objects = s3.list_objects(Bucket=bucket_name, Prefix=train_s3_path_images)['Contents']
        for index, obj in enumerate(objects):
            if index == 0:
                continue  # Skip the first iteration
            key = obj['Key']
            local_file_path = os.path.join(train_folder_path_images, os.path.basename(key))
            s3.download_file(bucket_name, key, local_file_path)
            # print(f'Downloaded: {key} to {local_file_path}')
        logging.info(f"Finish download train images {train_folder_path_images}")


    def get_data_valid(self):
        """
        Ingesting the data valid from the datasets_path
        """
        valid_s3_path_labels = 'lpskor/icr/valid/labels/'
        current_folder = os.getcwd()
        valid_folder_path_labels = os.path.join(current_folder, 'datasets/valid/labels')

        s3 = boto3.client('s3', aws_access_key_id = aws_access_key_id, aws_secret_access_key = aws_secret_access_key)
        objects = s3.list_objects(Bucket=bucket_name, Prefix=valid_s3_path_labels)['Contents']
        for index, obj in enumerate(objects):
            if index == 0:
                continue  # Skip the first iteration
            key = obj['Key']
            local_file_path = os.path.join(valid_folder_path_labels, os.path.basename(key))
            s3.download_file(bucket_name, key, local_file_path)
            # print(f'Downloaded: {key} to {local_file_path}')
        logging.info(f"Finish download valid labels {valid_folder_path_labels}")


        valid_s3_path_images = 'lpskor/icr/valid/images/'
        current_folder = os.getcwd()
        valid_folder_path_images = os.path.join(current_folder, 'datasets/valid/images')
        objects = s3.list_objects(Bucket=bucket_name, Prefix=valid_s3_path_images)['Contents']
        for index, obj in enumerate(objects):
            if index == 0:
                continue  # Skip the first iteration
            key = obj['Key']
            local_file_path = os.path.join(valid_folder_path_images, os.path.basename(key))
            s3.download_file(bucket_name, key, local_file_path)
            # print(f'Downloaded: {key} to {local_file_path}')
        logging.info(f"Finish download valid images {valid_folder_path_images}")

    def get_yaml_file(self):
        """
        Ingesting the yaml file from the datasets_path
        """
        yaml_s3_path = 'lpskor/icr/data.yaml'
        current_folder = os.getcwd()
        yaml_local_path = os.path.join(current_folder, 'datasets/data.yaml')

        s3 = boto3.client('s3', aws_access_key_id = aws_access_key_id, aws_secret_access_key = aws_secret_access_key)
        objects = s3.list_objects(Bucket=bucket_name, Prefix=yaml_s3_path)['Contents']
        s3.download_file(bucket_name, yaml_s3_path, yaml_local_path)
        logging.info(f"Finish download yaml labels {yaml_local_path}")


def ingest_df():
    """
    Ingesting the data from the datasets_path

    Args:
        datasets_path: path to the data
    Returns:
        datasets folder created: the ingested data 
    """

    try:
        ingest_data = IngestData(datasets_path_s3)
        ingest_data.create_folder()
        ingest_data.get_data_test()
        ingest_data.get_data_train()
        ingest_data.get_data_valid()
        ingest_data.get_yaml_file()
    except Exception as e:
        logging.error(f"Error while ingesting data: {e}")
        raise e