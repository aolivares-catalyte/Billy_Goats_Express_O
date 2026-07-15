class IncorrectDateFormat(Exception):
    """Raised when the date format does not match YYYY-MM-DD HH:MM:SS TZ."""
    pass

class DuplicatePurchaseError(Exception):
    """Raised when a purchase with the same ID already exists."""
    pass

class DuplicateDrinkError(Exception):
    """Raised when a drink with the same ID or unique identifier already exists."""
    pass

class DuplicateBakedGoodError(Exception):
    """Raised when a baked good with the same ID or unique identifier already exists."""
    pass

class BakedGoodNotFoundError(Exception):
    """Raised when a baked good cannot be found."""
    pass

class DuplicateCustomerError(Exception):
    """Raised when a customer with the same ID or unique identifier already exists."""
    pass

class DuplicateIngredientError(Exception):
    """Raised when an ingredient with the same ID or unique identifier already exists."""
    pass

class IngredientNotFoundError(Exception):
    """Raised when an ingredient cannot be found."""
    pass

class InvalidEmailError(Exception):
    """Raised when an email address is not in a valid format."""
    pass

class DuplicateEmailError(Exception):
    """Raised when an email address is already associated with an existing customer."""
    pass
