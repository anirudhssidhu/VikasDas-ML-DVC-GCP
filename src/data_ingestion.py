import pandas as pandas
import os
from sklearn.model_selection import train_test_split
import logging


# Ensure the "logs" directory exists
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

