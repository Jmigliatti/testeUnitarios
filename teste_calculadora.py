from calculadora import adicao, subtracao, multiplicacao, divisao

def test_adicao():
    assert adicao(2, 3) == 5
    assert adicao(-1, 1) == 0
    assert adicao(0, 0) == 0

def test_subtracao():
    assert subtracao(5, 3) == 2
    assert subtracao(0, 0) == 0
    assert subtracao(-1, 1) == -2

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(0, 5) == 0
    assert multiplicacao(-1, 1) == -1

def test_divisao():
    assert divisao(6, 3) == 2
    assert divisao(5, 2) == 2.5
    assert divisao(4, 2) == 2
    assert divisao(10, 2) == 5
    assert divisao(10, 3) == 3.3333333333333335
    assert divisao(0, 5) == 0
    assert divisao(0, 0) == "Não é possível dividir por zero!"
    assert divisao(5, 0) == "Não é possível dividir por zero!"
