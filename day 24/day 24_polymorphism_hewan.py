class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Halo, aku adalah kucing. Namaku {self.name}. Usiaku {self.age} tahun.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Halo, aku adalah anjing. Namaku {self.name}. Usiaku {self.age} tahun.")

    def make_sound(self):
        print("Guk Guk")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Puppy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
