import re
def validate_expression(expression):
    pattern = r'^[\d+\-*/()\s]+$'
    return bool(re.fullmatch(pattern, expression))