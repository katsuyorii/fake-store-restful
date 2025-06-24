import re
import phonenumbers


REGEX_PASSWORD = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?_&])[A-Za-z\d@$!%*#?_&]{8,}$"

def validation_password_complexity(password: str) -> str:
    if not re.fullmatch(REGEX_PASSWORD, password):
        raise ValueError(
            'Password must be at least 8 characters long, contain at least one letter, '
            'one number and one special character from @$!%*#?_&'
        )
    
    return password

def validation_valid_phone_number(phone_number: str) -> str:
    try:
        parsed = phonenumbers.parse(phone_number, None)

        if not phonenumbers.is_valid_number(parsed):
            raise ValueError('Phone number is not valid')
        
        formatted_phone_number = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)

        return formatted_phone_number
    except phonenumbers.NumberParseException:
        raise ValueError('Incorrect phone number format')
