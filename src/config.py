import os
from pathlib import Path

repo_dir = str(Path(os.getcwd()).parent)

MODEL_DIR = os.path.join(repo_dir, 'models')
MODEL_VERSION = 0.1
MODEL_VERSION_NOTE = "supervised learing model for time-series"

LOG_DIR = os.path.join(repo_dir, 'logs')