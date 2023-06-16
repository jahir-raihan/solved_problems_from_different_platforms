import random


class RandomizedSet:

    def __init__(self):
        self.set = {}

    def insert(self, val: int) -> bool:
        try:
            tmp = self.set[val]
            self.set[val] = 1
            if tmp == 0:
                return True
            return False
        except:
            self.set[val] = 1
            return True

    def remove(self, val: int) -> bool:
        try:
            tmp = self.set[val]
            if tmp > 0:
                self.set[val] = 0
                return True
            return False
        except:
            return False

    def getRandom(self) -> int:
        lst = [k for k in self.set.keys() if self.set[k] > 0]
        return lst[random.randint(0, len(lst) - 1)]