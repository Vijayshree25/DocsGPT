import re

def is_valid_email(email):
    """Return True if the email is valid."""
    if not isinstance(email, str):
        return False

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


# Example
print(is_valid_email("test@example.com"))  # True
print(is_valid_email("invalid@com"))       # False
