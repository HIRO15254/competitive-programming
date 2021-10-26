S = input()
# ネストの深さ数える
NEST = 0
now_nest = 0
for i in range(len(S)):
    if S[i] == "(":
        now_nest += 1
        NEST = max(NEST, now_nest)
    elif S[i] == ")":
        now_nest -= 1

for i in range(NEST):
    str_next = []
    now_nest = 0
    nest_queue = []
    for j in range(len(S)):
        if S[j] == "(":
            now_nest += 1
            NEST = max(NEST, now_nest)
            if now_nest != NEST - i:
                str_next.append(S[j])
        elif S[j] == ")":
            if now_nest == NEST - i:
                str_next.append("".join(nest_queue))
                nest_queue.reverse()
                str_next.append("".join(nest_queue))
                nest_queue = []
            else:
                str_next.append(S[j])
            now_nest -= 1
        else:
            if now_nest == NEST - i:
                nest_queue.append(S[j])
            else:
                str_next.append(S[j])
    S = "".join(str_next)
print(S)
