class IncorrectDateFormat(Exception):
    """Raised when the date formate does not match YYYY-MM-DD HH:MM:SS TZ"""
    pass
class DuplicatePurchaseError(Exception):
    """Raised when there has been a purchase with a certain id already created"""
    pass
class DuplicateDrinkError(Exception):
    pass
