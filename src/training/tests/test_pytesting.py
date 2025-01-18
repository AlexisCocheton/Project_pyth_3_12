import pytest

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4

class Test_class:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "lower")

#exercice 1
def add(a,b):
    return a+b

def test_add():
    assert add (1,2) == 3  

#exercice 2
#il suffit de rajouter test_ devant lle nom du fichier

#exercice 3

def is_even(n):
    return n % 2 == 0

@pytest.mark.parametrize("n,expected",[
(1, False),
(2, True),
(3, False),
] )
def test_is_even(n, expected):
    assert is_even(n) == expected


#exercice 4

@pytest.fixture
def list_somme():
    return [1,2,3,4,5]

def test_somme(list_somme):
    assert sum(list_somme) == 15


#exercice 5

@pytest.fixture(scope="module")
def ouverture_fermeture():
    print("ouverture de la bdd")
    yield 
    print("fermeture de la bdd")


def test_is_ouverture(ouverture_fermeture):
    print("on manipule la bbd ou verifie la connection")


def divide(a,b):
    if b==0: 
        raise ValueError("zero")
    return a/b

def test_divide():
    with pytest.raises(ValueError, match="zero"):
        divide(10, 0)









