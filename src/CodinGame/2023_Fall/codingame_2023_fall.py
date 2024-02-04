import math


# Score points by scanning valuable fish faster than your opponent.
class Creature:
    x = -1
    y = -1

    def __init__(self):
        self.rad = {}

    def reset(self):
        self.x = -1
        self.y = -1

    def pos(self, x, y):
        self.x = x
        self.y = y

    def radar(self, drone_id, radar):
        self.rad[drone_id] = radar

    def dist(self, x, y):
        if (self.x == -1):
            return -1
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)


class Fish(Creature):
    col = 0
    typ = 0

    scanned = False
    foe_scanned = False
    drone_scanned = []

    def __init__(self, col, typ):
        super().__init__()
        self.col = col
        self.typ = typ

    def reset(self):
        super().reset()
        self.scanned = False
        self.foe_scanned = False
        self.drone_scanned = []

    def set_scanned(self):
        self.scanned = True

    def set_foe_scanned(self):
        self.foe_scanned = True

    def set_drone_scanned(self, drone_id):
        self.drone_scanned.append(drone_id)

    def need_scan(self):
        return not self.scanned and self.drone_scanned == []


class Monster(Creature):
    aggressive = False

    def reset(self):
        super().reset()
        self.aggressive = False

    def set_aggressive(self):
        self.aggressive = True


class Drone:
    x = 0
    y = 0
    battery = 0
    job = 0
    phase = 0

    def pos(self, x, y, bat):
        self.x = x
        self.y = y
        self.battery = bat

    def dist(self, x, y):
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)


def is_fish(id):
    return id in fishes.keys()


fishes = {}
monsters = {}
my_drones = {}
DRONE_SPEED = 600
DRONE_BATTERY_MAX = 30


def get_input():
    # 入力ここから
    for fish in fishes.values():
        fish.reset()

    my_score = int(input())
    foe_score = int(input())

    my_scan_count = int(input())
    for i in range(my_scan_count):
        creature_id = int(input())
        fishes[creature_id].set_scanned()

    foe_scan_count = int(input())
    for i in range(foe_scan_count):
        creature_id = int(input())
        fishes[creature_id].set_foe_scanned()

    my_drone_count = int(input())
    for i in range(my_drone_count):
        drone_id, drone_x, drone_y, emergency, battery = [int(j) for j in input().split()]
        if drone_id not in my_drones.keys():
            my_drones[drone_id] = Drone()
        my_drones[drone_id].pos(drone_x, drone_y, battery)

    foe_drone_count = int(input())
    for i in range(foe_drone_count):
        drone_id, drone_x, drone_y, emergency, battery = [int(j) for j in input().split()]

    drone_scan_count = int(input())
    for i in range(drone_scan_count):
        drone_id, creature_id = [int(j) for j in input().split()]
        if (drone_id in my_drones.keys()):
            fishes[creature_id].set_drone_scanned(drone_id)
        else:
            fishes[creature_id].set_foe_scanned()

    visible_creature_count = int(input())
    for i in range(visible_creature_count):
        creature_id, creature_x, creature_y, creature_vx, creature_vy = [int(j) for j in input().split()]
        if is_fish(creature_id):
            fishes[creature_id].pos(creature_x, creature_y)
        else:
            monsters[creature_id].pos(creature_x, creature_y)

    radar_blip_count = int(input())
    for i in range(radar_blip_count):
        inputs = input().split()
        drone_id = int(inputs[0])
        creature_id = int(inputs[1])
        radar = inputs[2]
        if is_fish(creature_id):
            fishes[creature_id].radar(drone_id, radar)
        else:
            monsters[creature_id].radar(drone_id, radar)


creature_count = int(input())
for i in range(creature_count):
    creature_id, color, _type = [int(j) for j in input().split()]
    if (_type != -1):
        fishes[creature_id] = Fish(color, _type)
    else:
        monsters[creature_id] = Monster()

phase = 0
init = True

while True:
    get_input()
    if init:
        drone_1, drone_2 = my_drones.values()
        if (drone_1.x < drone_2.x):
            drone_1.job = 0
            drone_2.job = 1
        else:
            drone_1.job = 1
            drone_2.job = 0

    for d in my_drones.values():
        # 初期位置につく
        if d.phase == 0:
            light = 1 if d.battery == DRONE_BATTERY_MAX else 0
            if d.job == 0:
                print("MOVE", 2000, 2000, light, "phase 0")
                if d.dist(2000, 2000) <= DRONE_SPEED:
                    d.phase = 1
            else:
                print("MOVE", 8000, 2000, light, "phase 0")
                if d.dist(8000, 2000) <= DRONE_SPEED:
                    d.phase = 1
        elif d.phase == 1:
            light = 1 if d.battery == DRONE_BATTERY_MAX else 0
            print("MOVE", d.x, d.y + 400, light, "phase 1")
