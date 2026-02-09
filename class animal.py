class Animal:
    # ویژگی کلاسی
    zoo_name = "Tehran zoo"

    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(self.sound)

    def info(self):
        print(f"نام: {self.name}")
        print(f"گونه: {self.species}")
        print(f"سن: {self.age}")
        print(f"باغ‌وحش: {Animal.zoo_name}")

    def __str__(self):
        return f"{self.name} | گونه: {self.species} | سن: {self.age}"


# ایجاد شیر به عنوان یک نمونه از حیوانات
lion = Animal("شیر", "پستاندار", 5, "grrrrr!")

lion.info()
lion.make_sound()
print(lion)


#ارث بری از کلاس حیوانات

class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span

    # بازنویسی متد
    def make_sound(self):
        print(f"صدای پرنده: {self.sound}")

    def info(self):
        super().info()
        print(f"اندازه بال: {self.wing_span} متر")


# ایجاد یک نمونه از Bird
eagle = Bird("عقاب", "پرنده", 3, "جییییغ!", 2.1)

eagle.info()
eagle.make_sound()
print(eagle)
