import traceback
from src.logger import logger

class CustomException(Exception):
    """Custom exception class that logs error details automatically."""
    
    def __init__(self, message: str):
        super().__init__(message)
        # Log the exception message and full traceback
        tb = traceback.format_exc()
        full_message = f"{message}\nTraceback:\n{tb}" if tb.strip() != "NoneType: None" else message
        logger.error(full_message)
