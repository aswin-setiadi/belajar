import abc
import functools

def num_series(start, stop):
    l=[*range(start,stop)]
    total=functools.reduce(lambda a,b: a+b, l)
    #print(l)
    return total

def two_sigma_interview():
    for i in range(14,28):
        t1=num_series(1,i)
        t2=num_series(i,31)
        t3=num_series(i+1,31)
        average_payout1=(i-1)/30*t1
        average_payout2=(30-i+1)/30*t2 #inclusive of i so +1
        average_payout3=(30-i+1-1)/30*t3
        print(f"i={i} {average_payout1:.2f} {average_payout2:.2f} {average_payout3:.2f}")

class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        "load file"
        pass
    def extract_text(self, full_file_name: str) -> dict:
        "extract text"
        pass

class ParserMeta(type):
    """A Parser metaclass that will be used for parser class creation.
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text))

# this is a virtual base class
class UpdatedInformalParserInterface(metaclass=ParserMeta):
    """This interface is used for concrete classes to inherit from.
    There is no need to define the ParserMeta methods as any class
    as they are implicitly made available via .__subclasscheck__().
    """
    pass

class PdfParser(InformalParserInterface):
    """Extract pdf"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides informal interface load_data_source"""
        pass
    
    def extract_text(self, full_file_name: str) -> dict:
        """Overrides extract_text"""
        pass

class EmlParser(InformalParserInterface):
    """Extract text from an email"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override InformalParserInterface.extract_text()
        """
        pass

class PdfParserNew:
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides UpdatedInformalParserInterface.extract_text()"""
        pass

class EmlParserNew:
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override UpdatedInformalParserInterface.extract_text()
        """
        pass


class PersonMeta(type):
    """A person metaclass"""
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'name') and 
                callable(subclass.name) and 
                hasattr(subclass, 'age') and 
                callable(subclass.age))

class PersonSuper:
    """A person superclass"""
    def name(self) -> str:
        pass

    def age(self) -> int:
        pass

class Person(metaclass=PersonMeta):
    """Person interface built from PersonMeta metaclass."""
    pass

# Inheriting subclasses
class Employee(PersonSuper):
    """Inherits from PersonSuper
    PersonSuper will appear in Employee.__mro__
    """
    pass

class Friend:
    """Built implicitly from Person
    Friend is a virtual subclass of Person since
    both required methods exist.
    Person not in Friend.__mro__
    """
    def name(self):
        pass

    def age(self):
        pass

class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text))
    
class Double(metaclass=abc.ABCMeta):
    """Double precision floating point number."""
    pass


def tutorial_shape():
    class Rectangle:
        def __init__(self,l,w) -> None:
            self.length= l
            self.width= w

        def area(self):
            return self.length * self.width
        
        def perimeter(self):
            return 2*self.length+2*self.width
    
    class Square(Rectangle):
        def __init__(self, l) -> None:
            # param Square means lookup above that class
            super(Square, self).__init__(l, l)

    class Cube(Square):
        def surface_area(self):
            # param Square here means caller want to skip area method of Square, if any
            face_area= super(Square, self).area()
            return face_area * 6
        
        def volume(self):
            #super returns a proxy obj that delegate call to correct
            #class method
            face_area= super(Square, self).area()
            return face_area * self.length
        
    class Triangle:
        def __init__(self, b, h) -> None:
            self.base= b
            self.height= h

        def tri_area(self):
            return 0.5 * self.base * self.height
        
    class RightPyramid(Square, Triangle):
        def __init__(self, base, slant_height) -> None:
            self.base = base
            self.slant_height = slant_height
            super().__init__(self.base)

        def area(self):
            base_area= super().area() #should use rect area
            perimeter= super().perimeter() #should use rect area

            return 0.5 * perimeter * self.slant_height + base_area
        
        def area_2(self):
            base_area= super().area()
            triangle_area= super().tri_area()
            return triangle_area * 4 + base_area
        
    p= RightPyramid(2,4)
    #print(RightPyramid.__mro__) mro is metho resolution order
    print(p.area())

def tutorial_interface():
    # print(issubclass(PdfParser, InformalParserInterface))
    # print(PdfParser.__mro__)
    # print(issubclass(EmlParser, InformalParserInterface))
    # print(EmlParser.__mro__)

    # print(issubclass(PdfParserNew, UpdatedInformalParserInterface))
    # print(issubclass(EmlParserNew, UpdatedInformalParserInterface))
    # print(PdfParserNew.__mro__)
    # print(EmlParserNew.__mro__)

    # print(issubclass(Friend, Person)) #True
    # print(type(Friend))
    # print(type(Friend()))
    # print(isinstance(Friend, Person)) #False cause friend is type
    # print(isinstance(Friend(), Person)) #True cause Friend() is __main__.Friend obj which has required methods for Person (which is a virtual base class)
    # print(issubclass(PdfParserNew, FormalParserInterface)) #true
    # print(issubclass(EmlParserNew, FormalParserInterface)) #false
    # Double.register(float)
    # print(issubclass(float,Double))
    # print(isinstance(1.2, Double))
    pass
    
    
if __name__=="__main__":
    #tutorial_interface()
    tutorial_shape()