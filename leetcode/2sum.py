target = int(input())
numbers = [int(i) for i in input().split()]


def get_sum(n, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        c = numbers[l] + numbers[r]
        if c == target:
            return [l + 1, r + 1]
        elif c < target:
            l += 1
        else:
            r -= 1


print(get_sum(numbers, target))