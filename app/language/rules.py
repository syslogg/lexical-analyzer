REGEX_RULES = [
    ("OPERATION", r'(\*\*|\+|\-|\*|\/)'),
    ("NUMBER", r'[+-]?[0-9]+'),
    ("OPEN_PARENTHESES", r'\('),
    ("CLOSE_PARENTHESES", r'\)'),
    ("EOL", r';'),
    ("NEW_LINE", r'\n'),
    ('ERROR_CODE', r'.')
]

VALUES_OPERATIONS = {"+" : "SUM",
                     "-" : "SUBTRACTION",
                     "*" : "MULTIPLY",
                     "/" : "DIVISION",
                     "**": "EXPONENTIAL"}