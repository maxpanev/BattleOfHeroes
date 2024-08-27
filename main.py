import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = random.randint(10, self.attack_power)  # Случайный урон от 10 до 20
        other.health -= damage
        print(f"{self.name} атакует {other.name}! Здоровье {other.name}: {other.health}")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print(f"Начало игры! {self.player.name} против {self.computer.name}")

        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            print("\nВаш ход!")
            action = input("Выберите действие (атака): ").strip().lower()

            if action == "атака":
                self.player.attack(self.computer)
            else:
                print("Неизвестное действие! Вы пропускаете ход.")

            if not self.computer.is_alive():
                break

            # Ход компьютера
            print("\nХод компьютера!")
            self.computer.attack(self.player)

        # Определение победителя
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


# Пример использования
game = Game("Игрок", "Компьютер")
game.start()