R, C = map(int, input().split())
grid = [
    "bbbbbbbbbbbbbbb",
    "bwwwwwwwwwwwwwb",
    "bwbbbbbbbbbbbwb",
    "bwbwwwwwwwwwbwb",
    "bwbwbbbbbbbwbwb",
    "bwbwbwwwwwbwbwb",
    "bwbwbwbbbwbwbwb",
    "bwbwbwbwbwbwbwb",
    "bwbwbwbbbwbwbwb",
    "bwbwbwwwwwbwbwb",
    "bwbwbbbbbbbwbwb",
    "bwbwwwwwwwwwbwb",
    "bwbbbbbbbbbbbwb",
    "bwwwwwwwwwwwwwb",
    "bbbbbbbbbbbbbbb",
]
if grid[R - 1][C - 1] == "b":
    print("black")
else:
    print("white")