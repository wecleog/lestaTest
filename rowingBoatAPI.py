class RowingBoat:
    def __init__(self, max_passengers: int):
        self.max_passengers = max_passengers
        self.current_passengers = 0
        self.on_water = False

    def place_on_water(self):
        self.on_water = True
        return "Лодка находится на воде."

    def add_passenger(self, weight: int):
        if self.current_passengers + 1 > self.max_passengers:
            return "Перегруз! Лодка может затонуть."
        self.current_passengers += 1
        return f"Добавлен 1 пассажир. Текущее количество пассажиров: {self.current_passengers}."

    def remove_passenger(self):
        self.current_passengers = max(0, self.current_passengers)
        return f"Пассажир удален. Текущая нагрузка: {self.current_passengers} кг."

    def row(self, direction: str):
        if not self.on_water:
            return "Лодка должна быть на воде, чтобы грести!"
        return f"Лодка движется {direction}."

    def check_leaks(self):
        return "Лодка герметична."
