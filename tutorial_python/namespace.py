class Foo(object):
    """A simple namespace class with a `get` method to access members"""

    @classmethod
    def get(cls, member_name: str):
        """Get a member by name"""
        if not member_name.startswith("__") and member_name != "get":
            try:
                return getattr(cls, member_name)
            except AttributeError:
                pass
        raise ValueError("Unknown %r member: %r" % (cls.__name__, member_name))

    # -- the "members" --

    a = 1

    @staticmethod
    def welcome(name: str):
        return "greetings, %s!" % name

    @staticmethod
    def wave(name: str):
        return "(silently waving, %s)" % name


w = Foo.get("welcome")  # <function Foo.welcome at 0x000002D7E36998A0>
a = Foo.get("a")  # 1
Foo.get("unknown")  # ValueError: Unknown 'Foo' member: 'unknown'
