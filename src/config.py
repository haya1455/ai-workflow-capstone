import os
from pathlib import Path

repo_dir = str(Path(__file__).parent.resolve())

MODEL_DIR = os.path.join(repo_dir, 'models')
MODEL_VERSION = 0.1
MODEL_VERSION_NOTE = "supervised learing model for time-series"

LOG_DIR = os.path.join(repo_dir, 'logs')

DATA_DIR = os.path.join(repo_dir, 'data')