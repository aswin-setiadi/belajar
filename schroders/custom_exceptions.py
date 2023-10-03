"""Custom Exceptions Module"""


class DuplicateKeyException(Exception):
    def __init__(self) -> None:
        super().__init__(f"Duplicate key found.")


class InvalidKeyPadLayoutException(Exception):
    def __init__(self) -> None:
        super().__init__(f"Keypad layout is invalid, minimum size is 2x3 or 3x2.")


class InvalidMaxDepthException(Exception):
    def __init__(self) -> None:
        super().__init__(f"max_depth can't be less than 0.")


class InvalidMaxVowelException(Exception):
    def __init__(self) -> None:
        super().__init__(f"max_vowel can't be less than 0.")
