class WrongDBNameException(Exception):
    def __init__(self, message="Wrong Database Name. Please check .env") -> None:
        super().__init__(message)
