t = int(input())

for _ in range(t):
    n = int(input())
    spell = input().strip()

    result = ""

    for i in range(n - 1):
        if spell[i] > spell[i + 1]:
            result = spell[:i] + spell[i + 1:]
            break

    if result == "":
        result = spell[:n-1]

    print(result)