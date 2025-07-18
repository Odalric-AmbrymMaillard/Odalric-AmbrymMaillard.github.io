import Environments_StochasticBandits as env
import Algorithms_Baselines as alg
import Algorithms_MyStrategy as myalg
import Experiments_MakeBanditExperiments as xps
import time
import numpy as np
import matplotlib.pyplot as plt
from math import log

def runTest(bandit, learners, timeHorizon=1000):
    filename = str(int(time.time())) + bandit.name()

    all_avg_regrets= {}
    for learner in learners:
        onelearner = learners[learner](bandit.A)
        regrets = xps.OneBanditOneLearnerMultipleRun(bandit, onelearner, timeHorizon, num_runs=100)
        xps.visualize_regrets(regrets, learner,filename=filename+"-"+onelearner.name())
        all_avg_regrets[learner]=np.mean(regrets, axis=0)

    T = np.arange(timeHorizon) + 1
    plt.figure(figsize=(10, 10))
    for learner in learners:
        plt.plot(T, all_avg_regrets[learner], label=learner)
    plt.legend(fontsize=24)
    plt.show()
    plt.savefig(filename + '.png')

# Gaussian bandit with big variance
means = [0.2,0.4,0.6]
bandit = env.StochasticBandit(nbArms=len(means))
bandit.createBernoulliArmsFromMeans(means)
learners = {"FTL": alg.FTL, "UCB": alg.UCB, "TS": alg.TS}
runTest(bandit, learners)
