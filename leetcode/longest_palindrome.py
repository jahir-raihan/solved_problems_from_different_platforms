s = "a"

odds = 0
for ch in set(s):
    if s.count(ch) & 1:
        odds += 1
print(len(s) - odds + bool(odds))
