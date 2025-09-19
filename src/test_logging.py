from logger import logger
from exception import CustomException

# Test info and error logging
logger.info("This is a test info message")
logger.error("This is a test error message")

# Test exception logging
try:
    x = 1 / 0  # This will raise ZeroDivisionError
except Exception:
    raise CustomException("Division by zero occurred in test")
