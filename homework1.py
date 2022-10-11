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
