import re
def validPhoneNumber(phoneNumber):
    x = re.fullmatch(r'\(\d{3}\) \d{3}-\d{4}', phoneNumber)
    return bool(x)