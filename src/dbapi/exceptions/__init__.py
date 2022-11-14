class WrongDBNameException(Exception):
    def __init__(self, message="Wrong Database Name") -> None:
        super().__init__(message)
