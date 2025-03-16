class RowingBoat:
    def __init__(self, max_passengers: int):
        self.max_passengers = max_passengers
        self.current_passengers = 0
        self.on_water = False
        self.direction = None
        self.is_leaking = False

    def place_on_water(self):
        self.on_water = True
        return "Лодка находится на воде."

    def add_passenger(self):
        if self.current_passengers + 1 > self.max_passengers:
            return "Перегруз! Лодка может затонуть."
        self.current_passengers += 1
        return f"Добавлен 1 пассажир. Текущее количество пассажиров: {self.current_passengers}."

    def remove_passenger(self):
        if self.current_passengers > 0:
            self.current_passengers -= 1
        return f"Пассажир удален. Текущее количество пассажиров: {self.current_passengers}."

    def row(self, direction):
        if not self.on_water:
            return "Лодка должна быть на воде, чтобы грести!"
        self.direction = direction  # Устанавливаем направление
        return f"Лодка движется {self.direction}."

    def check_leaks(self):
        return "Лодка герметична." if not self.is_leaking else "Лодка может перевернуться"
