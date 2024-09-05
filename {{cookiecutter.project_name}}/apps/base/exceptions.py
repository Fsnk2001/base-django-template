class CustomException(Exception):
    """Base class for custom exceptions."""

    def __init__(self, message: str, status_code: int = 400, details: dict = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.details = details or {}


class NotFoundError(CustomException):
    """Raised when a resource is not found."""

    def __init__(self, message="The requested resource was not found. Please check the resource ID and try again."):
        super().__init__(message, status_code=404)


class PermissionDeniedError(CustomException):
    """Raised for permission denied errors."""

    def __init__(self, message="You do not have the required permissions to perform this action. Please contact "
                               "support if you believe this is an error."):
        super().__init__(message, status_code=403)
