import copy
oldice = [1, 2, 3, 4, 5, 6]
dice = [1, 2, 3, 4, 5, 6]
ans = 1
N = int(input())
for i in range(N):
    oldice = copy.deepcopy(dice)
    Q = input()
    if Q == "East":
        dice[0] = oldice[3]
        dice[2] = oldice[0]
        dice[5] = oldice[2]
        dice[3] = oldice[5]
    elif Q == "West":
        dice[0] = oldice[2]
        dice[2] = oldice[5]
        dice[5] = oldice[3]
        dice[3] = oldice[0]
    elif Q == "South":
        dice[0] = oldice[4]
        dice[1] = oldice[0]
        dice[5] = oldice[1]
        dice[4] = oldice[5]
    elif Q == "North":
        dice[0] = oldice[1]
        dice[1] = oldice[5]
        dice[5] = oldice[4]
        dice[4] = oldice[0]
    elif Q == "Right":
        dice[1] = oldice[2]
        dice[2] = oldice[4]
        dice[4] = oldice[3]
        dice[3] = oldice[1]
    elif Q == "Left":
        dice[1] = oldice[3]
        dice[2] = oldice[1]
        dice[4] = oldice[2]
        dice[3] = oldice[4]
    ans += dice[0]
print(ans)
