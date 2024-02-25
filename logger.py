import sys
import logging


logger = logging.getLogger(__name__)

#create formatter
formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s"
)

# create handler 
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('app.log')

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)


# logging.basicConfig(level=default_level,
#                     #filename=default_path,
#                     format="%(asctime)s - %(levelname)s - %(message)s")

# stream_handler.setLevel(logging.DEBUG)
# logger.addHandler(stream_handler)
logger.handlers = [stream_handler, file_handler]
logger.setLevel(logging.DEBUG)