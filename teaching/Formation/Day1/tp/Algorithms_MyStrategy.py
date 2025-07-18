import numpy as np

class Fancy:
    def __init__(self,nbArms,maxReward=1.):
#         ...
        self.clear()

    def clear(self):
        pass
#         ...

    def chooseArmToPlay(self):
        pass
#         return ...

    def receiveReward(self,arm,reward):
        pass
#         ...

    def name(self):
        return "myFancyStrategy"