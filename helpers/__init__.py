import warnings
from pathlib import Path
import os
import pandas as pd
from datetime import datetime 
from easy_ml import create_directory_if_not_exists

DIR_PACKAGE = Path(__file__).resolve().parent  # ../easy_ml/easy_ml
DIR_BASE = DIR_PACKAGE.parent  # ../easy_ml/

# ../learning/DATA
DIR_DATA = DIR_BASE.joinpath("DATA")

# ../learning/DATA/KAGGLE
DIR_KAGGLE = DIR_DATA.joinpath("KAGGLE")

# ../learning/DATA/KAGGLE/DATASETS
DIR_DATASETS = DIR_KAGGLE.joinpath("DATASETS")

# ../learning/DATA/KAGGLE/COMPETITIONS
DIR_COMPETITIONS = DIR_KAGGLE.joinpath("COMPETITIONS")

# ../leanring/DATA/SAMPLE
DIR_SAMPLE = DIR_DATA.joinpath("SAMPLE")

create_directory_if_not_exists(DIR_DATA)
create_directory_if_not_exists(DIR_SAMPLE)
create_directory_if_not_exists(DIR_KAGGLE)
create_directory_if_not_exists(DIR_DATASETS)
create_directory_if_not_exists(DIR_COMPETITIONS)


name = "helpers"

pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)
pd.set_option("display.max_colwidth", 25)
pd.options.display.float_format = "{:.2f}".format
pd.options.mode.chained_assignment = None




