import sys
import logging

logging.basicConfig(
    stream=sys.stderr,
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
