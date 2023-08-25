class Animal:
    def __init__(self, language) -> None:
        self.lang = language

    def speak(self):
        print(f"speaking in {self.lang}")


class Mamal:
    def __init__(self, language) -> None:
        self.lang = language

    def speak(self):
        print(f"speaking in {self.lang} with mouth")


# superclass method resolution start from left for multi inheritance
class Human(Animal, Mamal):
    pass


if __name__ == "__main__":
    h = Human("English")
    h.speak()
