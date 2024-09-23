import logging.config

import concurrent_log_handler  # noqa: F401
from dotenv import load_dotenv

load_dotenv(verbose=True)
logging.config.fileConfig("./log.conf", disable_existing_loggers=False)
