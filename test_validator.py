val="01012345678a"

pattern="^01[016789][1-9]\\d{6,7}$"
import views

"""
010
011
016
017
018
019
"""

import re

def validate_phone_number(number):
    if not re.match(pattern,number):
        return False
    return True

print(validate_phone_number('0101878'))