import importlib
import logging.config
from pathlib import Path

from dotenv import load_dotenv

importlib.import_module("concurrent_log_handler")

load_dotenv(verbose=True)
Path(".log").mkdir(exist_ok=True)
logging.config.fileConfig("./log.conf", disable_existing_loggers=False)
