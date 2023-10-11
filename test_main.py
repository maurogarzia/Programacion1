import pytest
from TPS import TPN5Funciones

@pytest.mark.parametrize("a,res",[
    (44905166,True)
    (44567890,True)
    (34567,False)
    (123456789,False)
])

def test_devolver_DNI(a,res):
    assert TPN5Funciones.devolver_DNI(a) == res
#------------------------------------------------------
@pytest.mark.parametrize("a,res",[
    ("hola mundo","mundo")
    ("adios mundo","mundo")
    ("mucho gusto", "gusto")
    ("Soy hincha de River","River")
])

def test_devolverPalabra(a,res):
    assert TPN5Funciones.devolverPalabra(a) == res
#------------------------------------------------------
@pytest.mark.parametrize("a,b,res",[
    (3,6,6)
    (8,4,8)
    (7,49,49)
    (16,16,16)
])

def test_multiplos(a,b,res):
    assert TPN5Funciones.multiplos(a,b) == res
#------------------------------------------------------
@pytest.mark.parametrize("a,b,res",[
    (15,20,17.5)
    (20,30,25)
    (11,17,14)
    (8,15,11.5)
])

def test_temp(a,b,res):
    assert TPN5Funciones.temp(a,b) == res
#------------------------------------------------------
@pytest.mark.parametrize("a,res",[
    ("hola","h o l a")
    ("ayer a la tarde","a y e r  a  l a  t a r d e")
    ("java script","j a v a  s c r i p t")
    ("pytest","p y t e s t")
])

def test_separar(a,res):
    assert TPN5Funciones.separar(a) == res
#------------------------------------------------------
@pytest.mark.parametrize("a,b,res",[
    ("usuario1","asdasd",True)
    ("Usario1","asddas",False)
    ("usuario 1","asdasd",False)
    ("usuario1","asdas",False)
])

def test_login(a,b,res):
    assert TPN5Funciones.login(a,b) == res
#------------------------------------------------------
@pytest.mark.parametrize("a,b,res",[
    (3,2,3.605551275463989)
    (12,4,12.649110640673518)
    (2,2,2.8284271247461903)
    (32,28, 42.5205832509386)
])

def test_modulo(a,b,res):
    assert TPN5Funciones.modulo(a,b) == res
#------------------------------------------------------
@pytest.mark.parametrize("a,b,res",[
    (4,2,0)
    (345,3,1)
    (12332,2,2)
    (3333,3,4)
])

def test_frecuencia(a,b,res):
    assert TPN5Funciones.frecuencia(a,b) == res
#------------------------------------------------------
@pytest.mark.parametrize("a,res",[
    (2,True)
    (15,False)
    (135,False)
    (17,True)
])

def test_es_primo(a,res):
    assert TPN5Funciones.es_primo(a) == res
#------------------------------------------------------
@pytest.mark.parametrize("a,res",[
    ([1,3,2],3)
    ([5,4],2)
    ([3,6,7,9],4)
    ([1,2,9,8,6],5)
])

def test_contador(a,res):
    assert TPN5Funciones.contador(a) == res