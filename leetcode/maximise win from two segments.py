prizePositions = [1, 1, 2, 2, 3, 3, 5]
k = 2
freq = [0] * len(prizePositions)

for i in prizePositions:
    freq[i] += 1
print(freq)

# We'll try it out next time.
