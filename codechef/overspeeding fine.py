for _ in range(int(input())):
    speed = int(input())
    print(0 if speed <= 70 else 500 if speed > 70 and speed <= 100 else 2000)