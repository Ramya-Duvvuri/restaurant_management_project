import logging
import re
from email.utils import parseaddr
logger = logging.getLogger(__name__)
EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0.9-.]
def is_valid_email(email:str) -> bool:
    try:
        if not email:
            return False
        if re.match(EMAIL_REGEX,addr) is None:
            return False
        return True
    except Exception as e:
        logger.error(f"Error validating email'{email}':{e}")
        return False
