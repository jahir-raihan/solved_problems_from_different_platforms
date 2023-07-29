t = int(input())

for _ in range(t):
    n = int(input())

    arr = [int(i) for i in input().split()]

    operations = []

    i = 1
    while i < n:
        if arr[i] < arr[i - 1]:
            right_max = arr[i]
            right_max_idx = i
            for j in range(i + 1, n):
                if arr[j] >= arr[i] and arr[j] > arr[i - 1]:
                    right_max = max(right_max, arr[j])
                    right_max_idx = j

            if right_max_idx == i:
                value = arr[i-1]

                while arr[i] <= arr[i - 1]:
                    arr[i] += arr[i - 1]
                    operations.append([i+1, i])

            else:
                while arr[i] < arr[i-1]:
                    arr[i] += right_max
                    operations.append([i+1, right_max_idx + 1])
        i += 1
    print(len(operations))
    for i, i1 in operations:
        print(i, i1)
