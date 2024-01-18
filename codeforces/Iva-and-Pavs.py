arr = [15, 14, 17, 42, 24]
pref = [15, 0, 0, 0, 0]
for i in range(1, 5):
    pref[i] = pref[i-1] & arr[i]
print(pref)