def test(data: dict) -> str:
    pass


class Person:
    name = "steve"

class A:
    def getname(Person: person) -> str:
        return person.name


class B(A):
    def getname(str: person) -> str:
        return person.name

def getPersonLogic(a_or_b):
    if a_or_b == 'a':
        return A
    else:
        return B


logic = getPersonLogic("a")
logic.getName()