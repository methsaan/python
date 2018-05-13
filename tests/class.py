#! /usr/bin/python3

class Dog:
    def __init__(self, breed, color, age):
        self.breed = breed
        self.color = color
        self.age = age
    def eat(self):

        print("Munch munch")
    def bark(self):
        if self.age > 20:
            print("Ruwruwruw")
        else:
            print("RUF! RUF! RUF! RUF! RUF! Grrr")
bruno = Dog("beagle", ["black", "white", "brown"], 2)
bruno.eat()
print(bruno.breed)
print(bruno.color[0])
brunosAge = int(input("How old is Bruno? "))
bruno.age = brunosAge
print(bruno.age)
bruno.bark()
