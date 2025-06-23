import re


REGEX_PASSWORD = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?_&])[A-Za-z\d@$!%*#?_&]{8,}$"

def validation_password_complexity(password: str) -> str:
    if not re.fullmatch(REGEX_PASSWORD, password):
        raise ValueError(
            'Password must be at least 8 characters long, contain at least one letter, '
            'one number and one special character from @$!%*#?_&'
        )
    
    return password