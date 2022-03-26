import random

round_number = 0


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value > 0:
            self.__health = value
        else:
            self.__health = 0

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} Health: {self.__health} ' \
               f'[{self.__damage}]'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        GameEntity.__init__(self, name, health, damage)


class Hero(GameEntity):
    def __init__(self, name, health, damage, skill):
        GameEntity.__init__(self, name, health, damage)
        self.__skill = skill

    @property
    def skill(self):
        return self.__skill

    @skill.setter
    def skill(self, value):
        self.__skill = value

    def apply_super_power(self, boss, heroes):
        raise NotImplementedError("Must be implemented")


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        Hero.__init__(self, name, health, damage, "HEAL")
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for h in heroes:
            if h.health > 0 and self != h:
                h.health = h.health + self.__heal_points


class Thor(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, "STUN THE ENEMY")

    def apply_super_power(self, boss, heroes):
        if round_number % 2 == 0:
            boss.damage = 0
        else:
            boss.damage = 70


class Witcher(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, "gives his life")

    def apply_super_power(self, boss, heroes):
        for h in heroes:
            if h.health == 0 and self != h:
                h.health = self.health
                self.health = 0
                print(f'    ____super power____')
                print(f'  {self.name}: give up your life for: {h.health} ')


class Hacker(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, "TAKE FROM THE ENEMY AND GIVE TO THE HEROES")

    def apply_super_power(self, boss, heroes):
        if round_number % 2 == 1:
            health_number = [50, 70]
            health = random.choice(health_number)
            self.health += health
            boss.health -= health
            print(f'    ____super power____')
            print(f'  {self.name}: transferring: {health} ')


class TrickyBastard(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, "PLAYING DEAD")

    def apply_super_power(self, boss, heroes):
        number = [1, 3, 5, 7, 9, 11, 13, 15, 17]
        round_number = random.choice(number)
        if round_number == number:
            TrickyBastard.health = 0
            TrickyBastard.damage = 0
        if round_number != number:
            TrickyBastard.health = 300
            TrickyBastard.damage = 20
            print(f'    ____super power____')
            print(f'    {self.name}: playing dead ')

    """If a bomber has less than 3/1 of life left, it explodes"""


class Bomber(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, "EXPLODE")

    def apply_super_power(self, boss, heroes):
        tenfold = 10
        a = tenfold * self.damage
        if self.health <= 70:
            boss.health -= a
            self.health = 0
            self.damage = 0
            print(f'    ____super power____')
            print(f'    {self.name}: bombing ')


def start():
    boss = Boss("♛ boss_AXE", 1000, 70)

    medic_1 = Medic("⚕ Elis", 200, 5, 15)
    thor = Thor("✪ Thor", 320, 15)
    wither = Witcher("♣ Daredevil", 300, 15)
    hacker = Hacker("◈ Hacker", 280, 10)
    tricky_bastard = TrickyBastard('☠ Goblin', 300, 20)
    bomber = Bomber("💣 Raid", 210, 25)

    heroes = [medic_1, thor, wither, hacker, tricky_bastard, bomber]

    print_stats(boss, heroes)

    while (not is_game_finished(boss, heroes)):
        play_round(boss, heroes)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss_hits(boss, heroes)
    heroes_hit(boss, heroes)
    heroes_skills(boss, heroes)
    print_stats(boss, heroes)


def boss_hits(boss, heroes):
    for h in heroes:
        if h.health > 0 and boss.health > 0:
            h.health = h.health - boss.damage


def heroes_hit(boss, heroes):
    for h in heroes:
        if h.health > 0 and boss.health > 0:
            boss.health = boss.health - h.damage


def heroes_skills(boss, heroes):
    for h in heroes:
        if h.health > 0 and boss.health > 0:
            h.apply_super_power(boss, heroes)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("heroes won!!!")
        return True

    all_heroes_dead = True
    for h in heroes:
        if h.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print("Boss won!!!")
    return all_heroes_dead


def print_stats(boss, heroes):
    print("------------ ROUND: " + str(round_number) + "------------")
    print(boss)
    for h in heroes:
        print(h)


start()
