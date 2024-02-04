def to_list(string):
    ans = []
    now_str = string[0]
    now_count = 1
    for i in string[1:]:
        if now_str == i:
            now_count += 1
        else:
            ans.append([now_str, now_count])
            now_str = i
            now_count = 1
    ans.append([now_str, now_count])
    return ans


S = list(input())
T = list(input())
S_2 = to_list(S)
T_2 = to_list(T)
if len(S_2) == len(T_2):
    for i in range(len(S_2)):
        if S_2[i][0] != T_2[i][0]:
            print("No")
            break
        else:
            if S_2[i][1] != T_2[i][1]:
                if S_2[i][1] > T_2[i][1] or S_2[i][1] == 1:
                    print("No")
                    break
    else:
        print("Yes")
else:
    print("No")
