from enum import Enum, IntEnum


class Shape(IntEnum):
    CIRCLE = 1
    SQUARE = 2
    RECTANGLE = 2


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 2


class EnumDict(Enum):
    First = {"a": 1}
    Ten = {"a": 1}
    Hundred = {"b": 1}
    Thousand = {"a": 2}


def main():
    print(Shape.CIRCLE)  # 1
    print(Shape(1))  # 1
    print(Color.RED)  # Color.RED obj
    print(Color(1))  # Color.RED obj
    print(Color.RED.name)  # "RED" str
    print(Color.RED.value)  # 1 int
    print(list(reversed(Color)))  # [Color.GREEN, Color.RED] intenum make order by value
    print(len(Shape))  # 2
    # print(Shape(3))  # ValueError
    print(type(Color))  # EnumType
    print(type(Color(1)))  # Color
    print(type(Color.RED))  # Color
    print(Shape.RECTANGLE)  # 2
    print(Color.GREEN)
    print(Color.BLUE)  # Color.GREEN, blue will be alias of green (green declared first)
    print(EnumDict.First)  # EnumDict.First
    print(EnumDict.Ten)  # EnumDict.First, although different dict but dict content same
    # warning says will always false cause they don't overlap but it print True
    print(EnumDict.First == EnumDict.Ten)
    print(EnumDict.First is EnumDict.Ten)  # True
    print(EnumDict.First == EnumDict.Hundred)  # False
    print(EnumDict.First is EnumDict.Hundred)  # False
    print(EnumDict.First == EnumDict.Thousand)  # False
    print(EnumDict.First is EnumDict.Thousand)  # False


if __name__ == "__main__":
    main()
