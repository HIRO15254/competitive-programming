c = int(input())
past = int(input())
now = 0
for i in range(c - 1):
    now = int(input())
    if now == past:
        print("stay")
    elif now < past:
        print("down " + str(past - now))
    else:
        print("up " + str(now - past))
    past = now
