from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.components.data_ingestion import DataIngestion
from src.DimondPricePrediction.exception import customException
import sys
import os
import pandas as pd

obj = DataIngestion()
obj.initiate_data_ingestion()