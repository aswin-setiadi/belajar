from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from time import time as ttime
import timeit
from typing import Any, Callable, Generic, Optional, TypeVar

T = TypeVar("T")
U = TypeVar("U")


def outer(l: list[int]):
    print("out")

    def inner():
        print("in")
        print(l[0])

    return inner


def main1():
    # inner outer function experiment
    v = outer([1]) # will print out
    print(v)  # v is inner function, this will print outer.<locals>.inner
    v()  # will keep l ref hence when called still can print 1, will print in and 1


def main2():
    # timeit method/ var exploration
    # number= count of timer call, repeat= count of timeit call
    # basically number is 1 experiement how many number of repetition
    # repeat is how many experiment to do
    ans = timeit.repeat(outer([1, 2]), repeat=2, number=3)
    print(ans)
    print(min(ans)) # get fastest timing

def main3():
    # monads https://www.youtube.com/watch?v=Q0aVbqim5pE TODO watch finish

    class Functor:
        def __init__(self, value: int) -> None:
            self.value = value

        def map(self, func: Callable[[Any], Any]) -> Functor:
            return Functor(func(self.value))

    # see here why Generic[T] in Monad param
    # https://medium.com/@steveYeah/using-generics-in-python-99010e5056eb
    # must call Generic[T] instead of T else will raise base class type unknown
    class Monad(Generic[T]):
        def __init__(self, value: T) -> None:
            self.value = value

        # although returned data type of the Monad is different, still valid monad
        def bind(self, func: Callable[[T], Monad[U]]) -> Monad[U]:
            return func(self.value)

        # can remove staticmethod because init is ald there
        @staticmethod
        def unit(value: Any) -> Monad[Any]:
            return Monad(value)

    class Maybe(Generic[T]):
        def __init__(self, value: Optional[T]) -> None:
            self.value = value

        def bind(self, func: Callable[[T], Maybe[U]]) -> Maybe[T] | Maybe[U]:
            # we want to avoid applying func to non valid value
            return self if self.value is None else func(self.value)

        # pattern matching feature new in python
        # unlike data class, normal class like this, the field/ attribute is not ordered by default
        # so need below dunder field to dictate the arg ordering
        # this variable dictate/ map the first arg as "value"
        __match_args__ = ("value",)

        def __match__(self, other: Maybe[T]) -> bool:
            return self.value == other.value

    # these translate python exception model into monadic error handling
    def parse_int(value: str) -> Maybe[int]:
        try:
            return Maybe(int(value))
        except ValueError:
            return Maybe(None)

    def is_positive(value: int) -> Maybe[int]:
        return Maybe(value) if value > 0 else Maybe(None)

    def double(value: int) -> int:
        return 2* value
    
    def safe_divide(x: float, y: float) -> Maybe[float]:
        return Maybe(None) if y == 0 else Maybe(x / y)

    def add_one(x: int) -> int:
        return x + 1

    def multiply_by_two(x: int) -> int:
        return x * 2

    # monads are monoids in the category of endofunctor
    # monoids are sets of elements with a binary operation (commutative)
    # commutative property is a + b = b + a
    # binary operation takes 2 elemets and return a third
    # monoids has unit element as well (like 1 is unit element of multiplication)

    # example of monoid
    def add(x: int, y: int):
        # unit element is when y=0
        return x + y
    print(add(1, 2))  # 3

    f = Functor(5)
    g = f.map(add_one)
    print(g.value)  # 6
    h = g.map(multiply_by_two)
    print(h.value)  # 12
    

    assert isinstance(g, Functor)  # Preserving structure

    # Preserving composition
    # first is applied by mapping in order
    # second is map both method call in order
    # and order still preserved
    assert (
        f.map(add_one).map(multiply_by_two).value
        == f.map(lambda x: multiply_by_two(add_one(x))).value
    )

    monad = Monad(5)
    # left identity
    # unit(x).bind(f) == f(x)
    assert monad.bind(lambda x: Monad(add_one(x))).value == add_one(5)

    # right identity
    # m.bind(unit) == m
    assert monad.bind(Monad.unit).value == monad.value

    # associativity
    # m.bind(f).bind(g) == m.bind(lambda x: f(x).bind(g))
    assert (
        monad.bind(lambda x: Monad(add_one(x)))
        .bind(lambda x: Monad(multiply_by_two(x)))
        .value
        == monad.bind(
            lambda x: Monad(add_one(x)).bind(lambda x: Monad(multiply_by_two(x)))
        ).value
    )
    # from comment, associativity check should be:
    assert monad.bind(lambda x: Monad(add_one(multiply_by_two(x)))).value == add_one(
        multiply_by_two(monad.bind(lambda x: Monad(x)).value)
    )

    # from arjan sample
    result = (
        Maybe(10).bind(lambda x: safe_divide(x, 0)).bind(lambda x: safe_divide(x, 2))
    )
    print(result.value)  # None cause /0

    # Validate and process user input
    def validate_and_process(input_str: str) -> Maybe[str] | Maybe[int]:
        # double return int so need to use lambda to make output as Maybe
        return (
            Maybe(input_str).bind(parse_int).bind(is_positive).bind(lambda n: Maybe(double(n)))
        )
    
    inputs = ["5","-3","foo"]
    for i_s in inputs:
        print(f"Processing '{i_s}':")
        result= validate_and_process(i_s)
        match result:
            case Maybe(None):
                print(f"Invalid input: {i_s}!")
            case Maybe(value=int()):
                print(f"Result: {result.value}")
            #just default handling
            case _:
                print("Unexpected input!")

    print("Done!")

    # decorator based monad, can turn existing function to monad
    def maybe(func: Callable[..., Any]) -> Callable[...,Any]:
        def wrapper(*args: Any, **kwargs: Any)-> Any:
            try: 
                return Maybe(func(*args, **kwargs))
            # in real code, dont use general exception like this
            except Exception:
                return Maybe(None)
        return wrapper
    
    #now this become a monadic function
    @maybe
    def parse_float(value: str) -> float:
        return float(value)
    input_str= "3.5"
    result= Maybe(input_str).bind(parse_float)
    print(type(result)) # Maybe
    print(result.value) #3.5

    # can check returns library for python monad/ functional programming implementation
    # https://github.com/dry-python/returns

def main4():
    """typing T tutorial"""
    # here coder must aware x and func arg must be same type i.e. T
    def apply(x: T, func: Callable[[T], T]) -> None:
        v = func(x)
        print(v)
    # will print 2.5
    apply(5, lambda x: x / 2)

def main5():
    """
    https://peps.python.org/pep-0636/#matching-multiple-patterns
    test python match feature
    """
    values= input("pls input action and obj, e.g. drink water:")
    match values.split():
        case ["drink",obj]:
            print(f"sure I will drink {obj}")
        case ["drink", *objs]:
            print(f"{objs} are too many...")
        case _:
            pass

    class Button(Enum):
        LEFT=1
        RIGHT=2
        MIDDLE=3

    class Click:
        #data class have inherent attribute ordering but normal class don't
        #so need to add below, must match the class attributes not params
        __match_args__= ("position", "button")

        def __init__(self,pos:tuple[int,int],btn:Button) -> None:
            self.position: tuple[int,int]=pos
            self.button: Button=btn
            
    @dataclass
    class Click1:
        position: tuple[int,int]
        button: Button

    class Click2(Click):
        # must include parent attributes too
        __match_args__= ("position", "button","time")
        def __init__(self,pos: tuple[int,int],btn: Button, time: str=str(int(ttime()))):
            super().__init__(pos,btn)
            self.time: str=time

    def handle_clicks(obj: Click | Click1 | Click2):
        match obj:
            # if have name such as z, second or part must have z too
            # so this cant
            #case Click((x,y), z) | Click1((x,y), button=Button.LEFT):
            case Click2((x,y),button=Button.MIDDLE,time=t):
                print(f"clicked position at {x} {y} with middle button at time={t}")
            case Click((x,y), z):
                print(f"clicked position at {x} {y} button= {z}")
            case Click1((x,y),button=Button.LEFT) | Click1((x,y), button= Button.RIGHT):
                print(f"clicked at {x} {y} not using middle mouse button.")
            case _:
                print("unknown click...")
    # unnecessary isinstance call error, click2 is always instance of click
    # print(isinstance(Click2((1,2),Button.LEFT), Click))
    handle_clicks(Click((1,2),Button.LEFT))
    handle_clicks(Click1((3,4),Button.LEFT))
    handle_clicks(Click1((5,6), Button.MIDDLE))
    # Click2 is child of Click so captured by Click((x,y),z) case
    # so the case must put on top of the parent
    handle_clicks(Click2((5,6), Button.MIDDLE, "1")) 

    print("main5 ends")





if __name__ == "__main__":
    main1()
    main2()
    main3()
    main4()
    main5()
