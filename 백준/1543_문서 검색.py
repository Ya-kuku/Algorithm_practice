file = input()
word = input()
idx = 0
ans = 0
while idx < len(file) - len(word) + 1:
    if file[idx:idx+len(word)] == word:
        ans += 1
        idx += len(word)
    else:
        idx += 1
print(ans)