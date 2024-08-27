import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = random.randint(10, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name}! Здоровье {other.name}: {other.health}")

    def is_alive(self):
        return self.health > 0


class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.health += 20
        self.rage_active = False

    def attack(self, other):
        if self.rage_active:
            damage = random.randint(25, self.attack_power + 15)
            self.rage_active = False
            print(f"{self.name} использует ярость и наносит огромный урон!")
        else:
            damage = random.randint(15, self.attack_power + 5)
        other.health -= damage
        print(f"{self.name} наносит мощный удар по {other.name}! Здоровье {other.name}: {other.health}")

    def rage(self):
        self.rage_active = True
        print(f"{self.name} активирует ярость, его следующая атака будет сильнее!")


class Mage(Hero):
    def attack(self, other):
        damage = random.randint(10, self.attack_power + 10)
        other.health -= damage
        print(f"{self.name} выпускает огненную стрелу в {other.name}! Здоровье {other.name}: {other.health}")

    def heal(self):
        heal_amount = random.randint(10, 30)
        self.health += heal_amount
        print(f"{self.name} лечится на {heal_amount} единиц! Здоровье {self.name}: {self.health}")


class Game:
    def __init__(self, player_name, player_class, computer_name):
        if player_class == "воин":
            self.player = Warrior(player_name)
            print(f"Игрок выбрал класс: Воин")
        elif player_class == "маг":
            self.player = Mage(player_name)
            print(f"Игрок выбрал класс: Маг")
        else:
            raise ValueError("Неверный класс персонажа!")

        # Компьютер случайно выбирает класс
        self.computer = random.choice([Warrior(computer_name), Mage(computer_name)])
        computer_class = "Воин" if isinstance(self.computer, Warrior) else "Маг"
        print(f"Компьютер выбрал класс: {computer_class}")

    def start(self):
        print(f"Начало игры! {self.player.name} против {self.computer.name}")

        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            print("\nВаш ход!")
            action = input("Выберите действие (атака, лечение или ярость): ").strip().lower()
            if action == "атака":
                self.player.attack(self.computer)
            elif action == "лечение" and isinstance(self.player, Mage):
                self.player.heal()
            elif action == "ярость" and isinstance(self.player, Warrior):
                self.player.rage()
            else:
                print("Неизвестное действие! Вы пропускаете ход.")

            if not self.computer.is_alive():
                break

                # Ход компьютера
            print("\nХод компьютера!")
            if isinstance(self.computer, Mage) and random.random() < 0.4:
                self.computer.heal()
            elif isinstance(self.computer, Warrior) and random.random() < 0.4:
                self.computer.rage()
            else:
                self.computer.attack(self.player)

            # Определение победителя
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

def choose_class():
    print("Выберите класс персонажа:")
    print("1. Воин:\nЗдоровье - 120 ед\nАтака - 15-25 ед \nСпособность -'Ярость' - урон от следующей атаки увеличен")
    print()
    print("2. Маг:\nЗдоровье - 100 ед\nОгненная стрела - 10-30 ед\nСпособность - 'Лечение' - восстанавливает здоровье")
    print()
    choice = input("Введите номер выбранного класса (1 или 2): ")
    if choice == "1":
        return "воин"
    elif choice == "2":
        return "маг"
    else:
        print("Некорректный выбор! Попробуйте еще раз.")
        return choose_class()

# Пример использования
player_name = "Игрок"
player_class = choose_class()
game = Game(player_name, player_class, "Компьютер")
game.start()