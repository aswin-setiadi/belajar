from enum import Enum, IntEnum


class Shape(IntEnum):
    CIRCLE = 1
    SQUARE = 2


class Color(Enum):
    RED = 1
    GREEN = 2


def main():
    print(Shape.CIRCLE)  # 1
    print(Shape(1))  # 1
    print(Color.RED)  # Color.RED obj
    print(Color(1))  # Color.RED
    print(Color.RED.name)  # "RED" str
    print(Color.RED.value)  # 1 int
    print(list(reversed(Color)))  # [Color.GREEN, Color.Red]
    print(len(Shape))
    print(Shape(3))  # ValueError


if __name__ == "__main__":
    main()
