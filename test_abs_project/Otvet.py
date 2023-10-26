import pytest
# Описываем все функции заданные в задании
def sum(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Делить на ноль нельзя")
    return a / b

def sub(a, b):
    return a - b

# Проверяем функции с помощью автотестов
# Тест для функции сложения
def test_sum():
    result = sum(3, 5)
    assert result == 8  # Проверяем, что результаты равны ожидаемому значению
# Тест для функции умножения
def test_mul():
    result = mul(4, 6)
    assert result == 24
# Тест для функции деления
def test_div():
    result = div(8, 2)
    assert result == 4.0
# Тест для обработки деления на ноль
def test_div_by_zero():
    with pytest.raises(ValueError):  # Проверяем, что ожидается исключение ValueError
        div(6, 0)

# Тест для функции вычитания
def test_sub():
    result = sub(10, 3)
    assert result == 7