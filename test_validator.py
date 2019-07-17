val="01012345678"

pattern="01[016789][1-9]\\d{6,7}"

"""
010
011
016
017
018
019
"""

import re

if re.match(pattern,val):
    print("matched")
else:
    print("invalid")