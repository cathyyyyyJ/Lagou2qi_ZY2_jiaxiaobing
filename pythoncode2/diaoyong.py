from main import Cat
from main import Dog
import yaml

if __name__ == "__main__":
    cat = Cat("小猫", "白蓝", "四个月", "男", "短毛")
    cat.Catch()
    print(f"{cat.name} {cat.color} {cat.age} {cat.sex} {cat.hair}")
    dog = Dog("小狗", "白色", "三个月", "女", "长毛")
    dog.look()
    print(f"{dog.name} {dog.color} {dog.age} {dog.sex} {dog.hair}")

    with open("anminals.yml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        # print(datas)
        cat1 = Cat(datas["猫猫"]['name'], datas["猫猫"]['color'], datas["猫猫"]['age'], datas["猫猫"]['sex'])
        # print(datas["猫猫"]['name'])
        print(f"{cat1.name} {cat1.color} {cat1.age} {cat1.sex} {cat1.hair}")
