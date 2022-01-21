from easy_ml import create_directory_if_not_exists
import kaggle
from helpers import DIR_DATASETS


def download_kaggle_datasets(dataset="subhamjain/loan-prediction-based-on-customer-behavior",dir_name="LOAN_PREDICTION"):
    
    dir_path = DIR_DATASETS.joinpath(dir_name)
    create_directory_if_not_exists(dir_path)

    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset, path=dir_path, unzip=True)

    return dir_path