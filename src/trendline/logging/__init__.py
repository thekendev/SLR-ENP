import os
import logging

# Setup logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "src/trendline/logging/logs"
log_filepath = os.path.join(log_dir, "running_log.log")

# 💡 Only create directory if it truly doesn't exist
if not os.path.exists(log_dir):
    os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("src")