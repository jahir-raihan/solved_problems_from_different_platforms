dic = {
    'b': 'BattleShip',
    'c': 'Cruiser',
    'd': 'Destroyer',
    'f': 'Frigate'
}

for i in range(int(input())):
    print(dic[input().lower()])