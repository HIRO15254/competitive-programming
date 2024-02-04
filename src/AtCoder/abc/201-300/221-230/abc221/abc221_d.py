N = int(input())
st = []
en = []
ans = [0 for _ in range(N)]
for _ in range(N):
    A, B = map(int, input().split(" "))
    st.append(A)
    en.append(A + B)
st.append(10**100)
en.append(10**100)
st.sort()
en.sort()
st_c = 0
en_c = 0
now = 1
active = 0
while st_c != N or en_c != N:
    if st[st_c] < en[en_c]:
        if active != 0:
            ans[active - 1] += st[st_c] - now
        active += 1
        now = st[st_c]
        st_c += 1
    else:
        if active != 0:
            ans[active - 1] += en[en_c] - now
        active -= 1
        now = en[en_c]
        en_c += 1
print(" ".join(map(str, ans)))
