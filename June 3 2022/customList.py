import random

class RandomNumbers:
            
    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        self.num = random.randint(0,100)
        return self.num
