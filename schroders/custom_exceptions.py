"""Custom Exceptions Module"""


class InvalidKeyPadLayoutException(Exception):
    def __init__(self) -> None:
        super().__init__(f"Keypad layout is invalid, minimum size is 2x3 or 3x2")
