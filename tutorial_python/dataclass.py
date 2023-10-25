from dataclasses import dataclass, field


class EmployeeVanilla:
    def __init__(self, name, emp_id, age, city) -> None:
        self.name = name
        self.emp_id = emp_id
        self.age = age
        self.city = city

    def __repr__(self):
        return "employee (name={}, emp_id={}, age={}, city={})".format(
            self.name, self.emp_id, self.age, self.city
        )

    def __eq__(self, __value: object) -> bool:
        return (self.name, self.emp_id, self.age, self.city) == (
            __value.name,
            __value.emp_id,
            __value.age,
            __value.city,
        )


@dataclass
class Employee:
    name: str
    emp_id: str
    age: int
    item_count: int = field(default=2)
    city: str = field(default="Earth")
    # init= False will raise error if we supply arg/ kwarg when instantiating Employee
    items: list = field(default_factory=list, init=False)

    def __post_init__(self):
        self.items = [None for _ in range(self.item_count)]


def test_employeevanilla():
    emp1 = EmployeeVanilla("Aswin", "1", 31, "Jakarta")
    emp2 = EmployeeVanilla("Nikhil", "2", 28, "MP")
    emp3 = EmployeeVanilla("Aswin", "1", 31, "Jakarta")

    print(emp1)
    print("emp1 == emp2? ", emp1 == emp2)
    print("emp1 == emp3? ", emp1 == emp3)


def test_employee():
    # items will be None because overriden by __post_init__
    emp1 = Employee("Aswin", "1", 31, 1, city="Jakarta")
    emp2 = Employee("Nikhil", "2", 28, 3, "MP")
    emp3 = Employee("Aswin", "1", 31, 1, "Jakarta")
    emp4 = Employee("Sandi", "3", 36, 2, "Muara Karang")

    print(emp1)
    print(emp4)
    print("emp1 == emp2? ", emp1 == emp2)
    print("emp1 == emp3? ", emp1 == emp3)


if __name__ == "__main__":
    # https://www.geeksforgeeks.org/understanding-python-dataclasses/
    test_employeevanilla()
    print("######")
    test_employee()
