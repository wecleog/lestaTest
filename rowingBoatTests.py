import pytest
from rowingBoatAPI import RowingBoat


@pytest.fixture
def boat():
    return RowingBoat(max_passengers=2)

def test_place_on_water(boat):
    result = boat.place_on_water()
    assert boat.on_water is True
    assert result == "Лодка находится на воде."

def test_add_passenger(boat):
    result1 = boat.add_passenger()
    result2 = boat.add_passenger()
    result3 = boat.add_passenger()  # Третий пассажир не должен поместиться
    assert result1 == f"Добавлен 1 пассажир. Текущее количество пассажиров: 1."
    assert result2 == f"Добавлен 1 пассажир. Текущее количество пассажиров: 2."
    assert result3 == "Перегруз! Лодка может затонуть."

def test_remove_passenger(boat):
    boat.add_passenger()
    result = boat.remove_passenger()
    assert result == f"Пассажир удален. Текущее количество пассажиров: 0."

def test_row(boat):
    boat.place_on_water()
    result = boat.row("вперёд")
    assert result == f"Лодка движется {boat.direction}."

def test_row_without_water(boat):
    result = boat.row("назад")
    assert result == "Лодка должна быть на воде, чтобы грести!"

def test_check_leaks(boat):
    result = boat.check_leaks()
    if boat.is_leaking:
        assert result == "Лодка может перевернуться"
    else:
        assert result == "Лодка герметична."


