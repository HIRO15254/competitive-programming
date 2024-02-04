import sys
import math


class enemy:
    def __init__(self, _id, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for):
        self._id = _id
        self.x = x
        self.y = y
        self.shield_life = shield_life
        self.is_controlled = is_controlled
        self.health = health
        self.vx = vx
        self.vy = vy
        self.near_base = near_base
        self.threat_for = threat_for

    def distance(self, x, y):
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)


class hero:
    def __init__(self, x, y, shield_life, is_controlled):
        self.x = x
        self.y = y
        self.shield_life = shield_life
        self.is_controlled = is_controlled
        self.target = -1


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# base_x: The corner of the map representing your base
base_x, base_y = [int(i) for i in input().split()]
heroes_per_player = int(input())  # Always 3
heroes = dict()

# game loop
while True:
    for i in range(2):
        # health: Your base health
        # mana: Ignore in the first league; Spend ten mana to cast a spell
        health, mana = [int(j) for j in input().split()]
    entity_count = int(input())  # Amount of heros and monsters you can see
    enemies = dict()
    for i in range(entity_count):
        # _id: Unique identifier
        # _type: 0=monster, 1=your hero, 2=opponent hero
        # x: Position of this entity
        # shield_life: Ignore for this league; Count down until shield spell fades
        # is_controlled: Ignore for this league; Equals 1 when this entity is under a control spell
        # health: Remaining health of this monster
        # vx: Trajectory of this monster
        # near_base: 0=monster with no target yet, 1=monster targeting a base
        # threat_for: Given this monster's trajectory, is it a threat to 1=your base, 2=your opponent's base, 0=neither
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]
        if _type == 0:
            enemies[_id] = enemy(_id, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for)
        elif _type == 1:
            if len(heroes) == heroes_per_player:
                heroes[_id].x = x
                heroes[_id].y = y
                heroes[_id].shield_life = shield_life
                heroes[_id].is_controlled = is_controlled
            else:
                heroes[_id] = hero(x, y, shield_life, is_controlled)

    for h in heroes.values():
        if h.target not in enemies.keys():
            shortest = 10 ** 10
            for e in enemies.values():
                if e.distance(h.x, h.y) < shortest:
                    h.target = e._id
                    shortest = e.distance(h.x, h.y)
        print(h.target)
        print(f"MOVE {enemies[h.target].x} {enemies[h.target].y}")
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)
        # In the first league: MOVE <x> <y> | WAIT; In later leagues: | SPELL <spellParams>;
