class Animal:
    clsatb = "test"

    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    def modify(self):
        Dog.clsatb = "changed"


if __name__ == "__main__":
    a = Animal("cat")
    print(a)  # <__main__.Animal object at 0x000002462B053850>
    print(type(a))  # <class '__main__.Animal'>
    d = Dog("bopi")
    print(d.clsatb)
    dd = Dog
    print(type(dd))
    print(dd)
    print(dd.clsatb)
    d.modify()
    print(dd.clsatb)
    print(d.clsatb)
