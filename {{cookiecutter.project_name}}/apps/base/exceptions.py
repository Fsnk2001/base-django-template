class CustomException(Exception):
    def __init__(self, message: str, status_code, details: dict = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.details = details or {}


class ValidationError(CustomException):
    def __init__(self, message, details=None):
        super().__init__(message, status_code=400, details=details)


class NotFoundError(CustomException):
    def __init__(self, message="The requested resource was not found. Please check the resource ID and try again."):
        super().__init__(message, status_code=404)


class PermissionDeniedError(CustomException):
    def __init__(self, message="You do not have the required permissions to perform this action. Please contact "
                               "support if you believe this is an error."):
        super().__init__(message, status_code=403)
