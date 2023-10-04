# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person("mayank", 21)
person2 = Person.fromBirthYear("mayank", 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))


class TestMethodDecorator:
    """
    class method and static method bound to the class
    static method does not have implicit first argument like cls/ self
    all class in python are instance of type
    """

    value = 1

    def __init__(self) -> None:
        self.instance_value = 1

    @classmethod
    def get_value_class(cls):
        print(cls.value)
        print(TestMethodDecorator.value)

    @staticmethod
    def get_value_static():
        print(TestMethodDecorator.value)

    def get_value_instance(self):
        return self.instance_value

    def set_value_instance(self, v: int):
        TestMethodDecorator.value = v

    @classmethod
    def set_value_class(cls, v: int):
        TestMethodDecorator.value = v

    @staticmethod
    def set_value_static(v: int):
        TestMethodDecorator.value = v


if __name__ == "__main__":
    tmd = TestMethodDecorator()
    TestMethodDecorator.get_value_class()
    tmd.get_value_instance()
    tmd.get_value_class()
    tmd.get_value_static()
    TestMethodDecorator.get_value_static()
    TestMethodDecorator.set_value_class(2)
    TestMethodDecorator.get_value_class()
    tmd.get_value_instance()
    TestMethodDecorator.get_value_static()
    TestMethodDecorator.set_value_static(3)
    TestMethodDecorator.get_value_class()
    tmd.get_value_instance()
    TestMethodDecorator.get_value_static()
