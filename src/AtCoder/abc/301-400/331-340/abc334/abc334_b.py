A, M, L, R = map(int, input().split())
L_2 = L + (M - (L + 10 ** 9 * M - A) % M) % M
R_2 = R - (R + 10 ** 9 * M - A) % M
print((R_2 - L_2) // M + 1)
