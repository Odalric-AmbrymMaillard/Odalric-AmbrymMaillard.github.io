import numpy as np
import KullbackLeiblerLib as kl
import scipy.stats as ss
from scipy.stats import beta

BERNOULLI = 'ber'
EXPONENTIAL = 'exp'
GAUSSIAN = 'gauss'
POISSON = 'poisson'

class FTL:
    def __init__(self,nbArms):
        self.A = nbArms
        self.clear()

    def clear(self):
        self.NbPulls = np.zeros(self.A)
        self.Means = np.ones(self.A)

    def chooseArmToPlay(self):
        return np.argmax(self.Means)

    def receiveReward(self,arm,reward):
        self.Means[arm] = (self.Means[arm]*self.NbPulls[arm]+reward)/(self.NbPulls[arm]+1.)
        self.NbPulls[arm] = self.NbPulls[arm] +1

    def name(self):
        return "FTL"
#
# def lowerBound(actionMeans, dist=BERNOULLI, var=1):
#     res = 0
#     optimalArm = np.argmax(actionMeans)
#     for a, mean in enumerate(actionMeans):
#         if a == optimalArm:
#             continue
#         if dist == BERNOULLI:
#             ...
#
#         res += (actionMeans[optimalArm] - actionMeans[a]) / denom
#     return res
#
class UCB:
    def __init__(self, nbArms):
        self.A = nbArms
        self.clear()

    def clear(self):
        self.NbPulls = np.zeros(self.A)
        self.Means = np.ones(self.A)

    def chooseArmToPlay(self):
        t = np.sum(self.NbPulls)
        if t == 0:
            return np.random.choice(self.A)

        delta_t = 1 / (t ** 2) * 1 / (t + 1)
        values = []
        for action, mean in enumerate(self.Means):
            if self.NbPulls[action] == 0:
                added_value = 0
            else:
                if self.NbPulls[action] > 0:
                    added_value =  np.sqrt(np.log(1/delta_t)/(2*self.NbPulls[action]))
                else:
                    added_value = np.Inf
            values.append(mean + added_value)

        max_actions = [i for i, x in enumerate(values) if x == np.max(values)]
        max_pulls = [self.NbPulls[a] for a in max_actions]
        select_index = np.argmin(max_pulls)
        return max_actions[select_index]

    def receiveReward(self, arm, reward):
        self.Means[arm] = (self.Means[arm]*self.NbPulls[arm]+reward)/(self.NbPulls[arm]+1.)
        self.NbPulls[arm] = self.NbPulls[arm] +1

    def name(self):
        return "UCB"

#
# class KLUCB:
#     def __init__(self, nbArms, dist=BERNOULLI, variance=1):
#         self.A = nbArms
#         self.clear()
#         self.dist = dist
#         self.variance = variance
#
#     def clear(self):
#         self.NbPulls = np.zeros(self.A)
#         self.Means = np.ones(self.A)
#
#     def f(self, t):
#         return np.log(t) + 3 * np.log(np.log(t))
#
#     def chooseArmToPlay(self):
#         for a in range(self.A):
#             if self.NbPulls[a] == 0:
#                 return a
#         t = np.sum(self.NbPulls)
#         ubs = []
#         for a, mean in enumerate(self.Means):
#             if self.dist == BERNOULLI:
#                 ub = kl.klucbBern(mean, self.f(t)/self.NbPulls[a])
#             elif self.dist == GAUSSIAN:
#                 ub = kl.klucbGauss(mean, self.f(t)/self.NbPulls[a], self.variance)
#             ubs.append(ub)
#
#         return np.argmax(ubs)
#
#     def receiveReward(self, arm, reward):
#         self.Means[arm] = (self.Means[arm]*self.NbPulls[arm]+reward)/(self.NbPulls[arm]+1.)
#         self.NbPulls[arm] = self.NbPulls[arm] +1
#
#     def name(self):
#         return "KL-UCBBern"
#
# class UCBPeeling:
#     def __init__(self, nbArms):
#         self.A = nbArms
#         self.clear()
#
#     def clear(self):
#         self.NbPulls = np.zeros(self.A)
#         self.Means = np.ones(self.A)
#
#     def chooseArmToPlay(self):
#         t = np.sum(self.NbPulls)
#         for a in range(self.A):
#             if self.NbPulls[a] == 0:
#                 return a
#
#         values = []
#         for a, mean in enumerate(self.Means):
#             if self.NbPulls[a] == 0:
#                 added_value = 0
#             else:
#                 alpha = 2
#                 added_value =...
#
#             values.append(mean + added_value)
#
#         max_actions = [i for i, x in enumerate(values) if x == np.max(values)]
#
#         max_pulls = [self.NbPulls[a] for a in max_actions]
#         select_index = np.argmin(max_pulls)
#         return max_actions[select_index]
#
#     def receiveReward(self, arm, reward):
#         self.Means[arm] = (self.Means[arm]*self.NbPulls[arm]+reward)/(self.NbPulls[arm]+1.)
#         self.NbPulls[arm] = self.NbPulls[arm] +1
#
#     def name(self):
#         return "UCB Peeling"
#
# class UCBLaplace:
#     def __init__(self, nbArms):
#         self.A = nbArms
#         self.clear()
#
#     def clear(self):
#         self.NbPulls = np.zeros(self.A)
#         self.Means = np.ones(self.A)
#
#     def chooseArmToPlay(self):
#         t = np.sum(self.NbPulls)
#         if t == 0:
#             return np.random.choice(self.A)
#
#         values = []
#         for a, mean in enumerate(self.Means):
#             if self.NbPulls[a] == 0:
#                 added_value = 0
#             else:
#                 added_value =  ...
#
#             values.append(mean + added_value)
#
#         max_actions = [i for i, x in enumerate(values) if x == np.max(values)]
#         max_pulls = [self.NbPulls[a] for a in max_actions]
#         select_index = np.argmin(max_pulls)
#         return max_actions[select_index]
#
#     def receiveReward(self, arm, reward):
#         self.Means[arm] = (self.Means[arm]*self.NbPulls[arm]+reward)/(self.NbPulls[arm]+1.)
#         self.NbPulls[arm] = self.NbPulls[arm] +1
#
#     def name(self):
#         return "UCB Laplace"
#
class TS:
    def __init__(self, nbArms):
        self.A = nbArms
        self.clear()

    def clear(self):
        self.NbPulls = np.zeros(self.A)
        self.params = [(2, 2) for i in range(self.A)]

    def chooseArmToPlay(self):
        for a in range(self.A):
            if self.NbPulls[a] == 0:
                return a
        samples = []
        for arm in range(self.A):
            a, b = self.params[arm]
            if a <= 0 or b <= 0:
                print(a, b)
            sample = beta.rvs(a, b, size=1)
            samples.append(sample)
        return np.argmax(samples)

    def receiveReward(self, arm, reward):
        self.NbPulls[arm] = self.NbPulls[arm] +1
        a, b = self.params[arm]
        a = a + reward
        b = b + 1 - reward
        if b <= 0:
            b = 1e-6
        if a <= 0:
            a = 1e-6
        self.params[arm] = (a, b)

    def name(self):
        return "TS-Bern"

# class Besa:
#     def __init__(self, nbArms):
#         self.A = nbArms
#         self.clear()
#
#     def clear(self):
#         self.NbPulls = np.zeros(self.A)
#         self.samples = [[] for arm in range(self.A)]
#
#     def compete(self, arm1, arm2):
#         n_samples = int(self.NbPulls[arm2])
#         if self.NbPulls[arm1] < self.NbPulls[arm2]:
#             n_samples = int(self.NbPulls[arm1])
#
#         arm1_values = np.random.choice(self.samples[int(arm1)], n_samples, replace=False)
#         arm2_values = np.random.choice(self.samples[int(arm2)], n_samples, replace=False)
#         mean_arm1 = np.mean(arm1_values)
#         mean_arm2 = np.mean(arm2_values)
#         if mean_arm1 < mean_arm2:
#             return arm2
#         return arm1
#
#     def chooseArmToPlay(self):
#         for a in range(self.A):
#             if self.NbPulls[a] == 0:
#                 return a
#         list_arms = np.arange(self.A)
#         np.random.shuffle(list_arms)
#         best_arm = list_arms[0]
#         for arm in list_arms[1:]:
#             best_arm = self.compete(best_arm, arm)
#         return best_arm
#
#     def receiveReward(self, arm, reward):
#         self.NbPulls[arm] += 1
#         self.samples[arm].append(reward)
#
#     def name(self):
#         return "Besa"
    
    

