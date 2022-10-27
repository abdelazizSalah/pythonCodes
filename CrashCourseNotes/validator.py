# this is a module contains the regular expresions
import re


def validate_email_address(email):
    if len(email) > 7:
        return bool(re.match('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email))
