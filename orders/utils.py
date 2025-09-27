import string
import secrets
from .model import Coupon
def generate_coupon_code(length = 10):
    characters = string.ascii_uppercase + string_digits
    while True:
        code = ''.join(secrets.choice(characters) for _ in range(length))
        if not Coupon.object.filter(code = code).exists():
            return code