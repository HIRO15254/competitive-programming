N, M = map(int, input().split())
S = input()
T = input()


def is_prefix(S, T):
    try:
        return S.index(T) == 0
    except ValueError:
        return False


def is_suffix(S, T):
    try:
        return S[len(S) - len(T):] == T
    except ValueError:
        return False


print(3 - (2 if is_prefix(T, S) else 0) - (1 if is_suffix(T, S) else 0))
