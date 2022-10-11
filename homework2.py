class Hero:
    def __init__(self, hp, damage, nickname, name):
        self.hp = hp
        self.damage = damage
        self.nickname = nickname
        self.name = name
    def heal(self):
        print(self.hp + 100)
    def two_damage(self):
        print(self.damage + 50)
    def greetings(self):
        print('my name is ' + self.nickname)
    def brand_phrase(self):
        print(self.name)
p1 = Hero(nickname='Sokol',damage= 50, hp = 100,name='good will win')
p1.greetings()
print(p1.hp)
p1.heal()
print(p1.damage)
p1.two_damage()
print(p1.name)
class Air(Hero):
    pass
air=Air(nickname='airman',damage= 50, hp = 100,name='герой воздушной окрестности')
print(air.name)
class Space(Hero):
    def __init__(self, nickname, damage, hp, name, fly):
        super().__init__(nickname, damage, hp, name,)
        self.fly = fly
    def brand_phrasee(self):
        print('fly in the True_phrase')
    def Gen_X(self):
        print('')
        pass
space= Space(nickname='airman',damage= 50, hp = 100,name='герой космической окрестности',fly='False')
print(space.name, space.fly)
space.brand_phrasee()
space.Gen_X()
class Earthen(Hero):
    pass
earth=Earthen(nickname='airman',damage= 50, hp = 100,name='герой землянной окрестности')
print(earth.name)