class Animal:
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def sound(self):
        print("could bark")

    def run(self):
        print("could run")


class Cat(Animal):
    def __init__(self, name, color, age, sex, hair="短毛"):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex
        self.hair = hair

    def Catch(self):
        print("会抓老鼠")

    def sound(self):
        print("喵喵叫")


class Dog(Animal):
    def __init__(self, name, color, age, sex, hair="长毛"):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex
        self.hair = hair

    def look(self):
        print("会看家")

    def sound(self):
        print("汪汪叫")

# cat=Cat("小猫","白蓝","四个月","男","短毛")
# print(f"名字是{cat.name}")
# print(f"颜色是{cat.color}")
# print(f"年龄是{cat.age}")
# print(f"性别是{cat.sex}")
# print(f"毛是{cat.hair}")
# cat.Catch()
# dog=Dog("小狗","白色","三个月","女","长毛")
# print(f"名字是{dog.name}")
# print(f"颜色是{dog.color}")
# print(f"年龄是{dog.age}")
# print(f"性别是{dog.sex}")
# print(f"毛是{dog.hair}")
# dog.look()
