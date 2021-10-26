S = input()
words = []
strbuf = []
ans = []
for i in range(len(S)):
    strbuf.append(S[i])
    if S[i].isupper():
        if len(strbuf) != 1:
            words.append("".join(strbuf).lower())
            strbuf.clear()
words.sort()
for i in range(len(words)):
    strlist = list(words[i])
    strlist[0] = strlist[0].upper()
    strlist[-1] = strlist[-1].upper()
    ans.append("".join(strlist))
print("".join(ans))
