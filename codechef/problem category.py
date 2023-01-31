# cook your dish here
for i in range(int(input())):
    n = int(input())
    if (1 <= n < 100):
        print('Easy')
    elif (100 <= n < 200):
        print('Medium')
    elif 200 <= n <= 300:
        print('Hard')
