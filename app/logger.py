import logging 
import os 
 
 
def get_logger(name): 
    """Create a logger that writes to the screen AND to logs/app.log.""" 
    os.makedirs("logs", exist_ok=True) 
 
    logger = logging.getLogger(name) 
    if logger.handlers:  # already set up, don't add twice 
        return logger 
 
    logger.setLevel(os.getenv("LOG_LEVEL", "INFO")) 
    fmt = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s") 
 
    screen = logging.StreamHandler() 
    screen.setFormatter(fmt) 
 
    diary = logging.FileHandler("logs/app.log", encoding="utf-8") 
    diary.setFormatter(fmt) 
 
    logger.addHandler(screen) 
    logger.addHandler(diary) 
    return logger
