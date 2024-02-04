from collections import deque
from random import random, shuffle

class Place:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return Place(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Place(self.x - other.x, self.y - other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self
    def length(self):
        return abs(self.x) + abs(self.y)
    def to_string(self):
        return f"({self.x},{self.y})"

MOVE = "UDLR"
GUARD = "udlr"
DIRECTION = [Place(-1, 0), Place(1, 0), Place(0, -1), Place(0, 1)]

pets = []
humen = []
guards = []
cant_use = []
ju = list(range(4))
finished = 0
phase = 0
go = -1
now_step = 0
now_x_min, now_x_max, now_y_min, now_y_max = 0, 29, 0, 29
WORKER_MINUS = True

N = int(input())
for _ in range(N):
    x, y, t = map(lambda x: int(x) - 1, input().split())
    pets.append([Place(x, y), t])
M = int(input())
for _ in range(M):
    x, y = map(lambda x: int(x) - 1, input().split())
    humen.append(Place(x, y))

m_places = [0 for _ in range(M)]
m_places_end = [0 for _ in range(M)]
WORKER = M

def can_put(p: Place):
    if p.x >= 30 or p.x < 0 or p.y >= 30 or p.y < 0:
        return False
    for pet in pets:
        if (pet[0] - p).length() <= 1:
            return False
    for human in humen:
        if human == p:
            return False
    for guard in guards:
        if guard == p:
            return False
    for i in cant_use:
        if i == p:
            return False
    return True

def can_move(p):
    if p.x >= 30 or p.x < 0 or p.y >= 30 or p.y < 0:
        return False
    for guard in guards:
        if p == guard:
            return False
    return True

def nearest(p_1, p_2):
    if p_1 == p_2:
        return -1
    q = deque()
    dis = [[[-1, -1] for _ in range(30)] for _ in range(30)]
    dis[p_1.x][p_1.y] = [0, p_1]
    q.append(p_1)
    while q:
        now = q.popleft()
        shuffle(ju)
        for i in ju:
            next = now + DIRECTION[i]
            if can_move(next) and dis[next.x][next.y][0] == -1:
                dis[next.x][next.y] = [dis[now.x][now.y][0] + 1, now]
                q.append(next)
    now = p_2
    while dis[now.x][now.y][1] != p_1:
        now = dis[now.x][now.y][1]
    return DIRECTION.index(now - p_1)

def pet_count(x_min, y_min, x_max, y_max):
    ans = 0
    for i in range(N):
        if x_min <= pets[i][0].x and pets[i][0].x <= x_max and y_min <= pets[i][0].y and pets[i][0].y <= y_max:
            ans += 1
    return ans

def dog_count(x_min, y_min, x_max, y_max):
    ans = 0
    for i in range(N):
        if x_min <= pets[i][0].x and pets[i][0].x <= x_max and y_min <= pets[i][0].y and pets[i][0].y <= y_max and pets[i][1] == 3:
            ans += 1
    return ans

def human_count():
    ans = 0
    for i in range(WORKER):
        if humen[i] == m_places[i]:
            ans += 1
    return ans == WORKER

def new_phase(x_min, y_min, x_max, y_max, phase):
    global WORKER, finished, go, now_step, WORKER_MINUS
    now_step = 0
    finished, go = 0, -1
    WORKER_MINUS = dog_count(x_min, y_min, x_max, y_max) != 0
    if WORKER_MINUS:
        WORKER -= 1
    if phase % 2 == 0:
        for i in range(WORKER):
            m_places[i] = Place((x_min + x_max) // 2, int((y_max - y_min + 1) * i / WORKER) + y_min)
            m_places_end[i] = Place((x_min + x_max) // 2, int((y_max - y_min + 1) * (i + 1) / WORKER - 2) + y_min)
        if WORKER_MINUS:
            m_places[WORKER] = Place(x_max, y_max)
    if phase % 2 == 1:
        for i in range(WORKER):
            m_places[i] = Place(int((x_max - x_min + 1) * i / WORKER) + x_min, (y_min + y_max) // 2)
            m_places_end[i] = Place(int((x_max - x_min + 1) * (i + 1) / WORKER - 2) + x_min, (y_min + y_max) // 2)
        if WORKER_MINUS:
            m_places[WORKER] = Place(x_max, y_max)

def calc(human_no, step):
    global finished, go, phase
    # 自分の下が柵をおける状態にあるか
    if humen[human_no] == m_places[human_no] and can_put(humen[human_no] + DIRECTION[go]) and go != -1:
        guards.append(humen[human_no] + DIRECTION[go])
        if m_places[human_no] != m_places_end[human_no]:
            if phase % 2 == 0:
                m_places[human_no] += Place(0, 1)
            else:
                m_places[human_no] += Place(1, 0)
        else:
            finished += 1
        return GUARD[go]
    # 目標地点に向かう
    dir = nearest(humen[human_no], m_places[human_no])
    if dir != -1:
        cant_use.append(humen[human_no] + DIRECTION[dir])
        return MOVE[dir]
    # やることがないので待機
    return "."

def otori_calc(human_no):
    # 目標地点に向かう
    dir = nearest(humen[human_no], m_places[human_no])
    if dir != -1:
        cant_use.append(humen[human_no] + DIRECTION[dir])
        return MOVE[dir]
    # やることがないので待機
    return "."

new_phase(now_x_min, now_y_min, now_y_max, now_y_max, 0)
for step in range(300):
    now_step += 1
    output = ""
    cant_use = []
    for i in range(M):
        if i < WORKER:
            output += calc(i, step)
        else:
            output += otori_calc(i)
    print(output)

    if step == 299:
        print()
        break
    # 位置の更新処理
    pets_move = input().split()
    for i in range(M):
        if output[i] in MOVE:
            humen[i] += DIRECTION[MOVE.index(output[i])]
    for i in range(N):
        for j in range(len(pets_move[i])):
            if pets_move[i][j] in MOVE:
                pets[i][0] += DIRECTION[MOVE.index(pets_move[i][j])]

    now_pet =  pet_count(now_x_min, now_y_min, now_x_max, now_y_max) + dog_count(now_x_min, now_y_min, now_x_max, now_y_max)
    border = now_pet * max(0.2, (0.7 - now_step / 150))
    if human_count() and go == -1:
        if phase % 2 == 0:
            mid = now_x_min + now_x_max // 2
            area_pet = [pet_count(now_x_min, now_y_min, mid - 1, now_y_max), pet_count(mid + 1, now_y_min, now_x_max, now_y_max)]
            area_dog = [dog_count(now_x_min, now_y_min, mid - 1, now_y_max), dog_count(mid + 1, now_y_min, now_x_max, now_y_max)]
            print(f"#{area_pet[0]} {area_dog[0]} {area_pet[1]} {area_dog[1]}, {border}")
            if (area_pet[0] + area_dog[0]) - (area_pet[1] + area_dog[1]) > border:
                go = 0
            elif (area_pet[1] + area_dog[1]) - (area_pet[0] + area_dog[0]) > border:
                go = 1
        else:
            mid = now_y_min + now_y_max // 2
            area_pet = [pet_count(now_x_min, now_y_min, now_x_max, mid - 1), pet_count(now_x_min, mid + 1, now_x_max, now_y_max)]
            area_dog = [dog_count(now_x_min, now_y_min, now_x_max, mid - 1), dog_count(now_x_min, mid + 1, now_x_max, now_y_max)]
            print(f"#{area_pet[0]} {area_dog[0]} {area_pet[1]} {area_dog[1]}, {border}")
            if (area_pet[0] + area_dog[0]) - (area_pet[1] + area_dog[1]) > border:
                go = 2
            elif (area_pet[1] + area_dog[1]) - (area_pet[0] + area_dog[0]) > border:
                go = 3
    if finished == WORKER:
        if go == 0:
            now_x_min = mid
        elif go == 1:
            now_x_max = mid
        elif go == 2:
            now_y_min = mid
        elif go == 3:
            now_y_max = mid
        if pet_count(now_x_min, now_y_min, now_x_max, now_y_max) > 1:
            phase += 1
            if go % 2 == 0 and WORKER_MINUS:
                WORKER += 1
        new_phase(now_x_min, now_y_min, now_x_max, now_y_max, phase)