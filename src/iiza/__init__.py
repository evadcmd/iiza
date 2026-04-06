import logging.config
from pathlib import Path

import concurrent_log_handler  # noqa: F401 # type: ignore
from dotenv import load_dotenv

load_dotenv(verbose=True)
Path(".log").mkdir(exist_ok=True)
logging.config.fileConfig("./log.conf", disable_existing_loggers=False)
