import pylab as pl
import numpy as np
from tqdm import tqdm


def OneBanditOneLearnerOneRun(bandit, learner, timeHorizon):
    arms = []
    rewards = []
    regrets = []
    cumulativeregrets = []
    cumulativeregret = 0
    for t in range(0, timeHorizon):
        arm = learner.chooseArmToPlay()
        reward, expectedInstantaneousRegret = bandit.GenerateReward(arm)
        learner.receiveReward(arm, reward)
        # Update statistics
        arms.append(arm)
        rewards.append(reward)
        regrets.append(expectedInstantaneousRegret)
        cumulativeregret = cumulativeregret + expectedInstantaneousRegret
        cumulativeregrets.append(cumulativeregret)
    return arms, rewards, regrets, cumulativeregrets


def OneBanditOneLearnerMultipleRun(bandit, learner, timeHorizon, num_runs):
    total_regrets = []
    for run in tqdm(range(num_runs)):
        learner.clear()
        rms, rewards, regrets, cumulativeregrets = OneBanditOneLearnerOneRun(bandit, learner, timeHorizon)
        total_regrets.append(cumulativeregrets)
    return np.array(total_regrets)


def visualize_regrets(total_regrets, title,filename):
    upper = np.quantile(total_regrets, 0.75, axis=0)
    lower = np.quantile(total_regrets, 0.25, axis=0)

    Rg = total_regrets[:, -1]
    avg_Rg = np.mean(total_regrets, axis=0)
    fig, (ax1, ax2) = pl.subplots(1, 2, figsize=[15, 4])
    ax1.set_ylabel("Cumulative regret", fontsize=16)
    ax1.hist(Rg, 30)
    fig.suptitle(title, fontsize=16)
    ax2.set_xlabel("Time steps", fontsize=16)
    ax2.set_ylabel("Cumulative regret", fontsize=16)
    ax2.plot(range(0, len(avg_Rg)), avg_Rg, label='Avg regret')
    ax2.plot(range(0, len(avg_Rg)), lower, c='b', label="25% quantile")
    ax2.plot(range(0, len(avg_Rg)), upper, c='b', label="75% quantile")
    pl.legend()
    pl.savefig(filename + '.png')
    pl.show()


def plotOneBanditOneLearnerOneRun(name, arms, rewards, regrets, cumulativeregrets, show=True):
    pl.figure(1)
    pl.clf()
    pl.xlabel("Arms", fontsize=16)
    pl.ylabel("Arm histogram", fontsize=16)
    pl.hist(arms, max(arms) + 1)
    if (show):
        pl.show()
    else:
        pl.savefig("./Figure-" + name + "-Arm histogram" + '.pdf')

    pl.figure(2)
    pl.clf()
    pl.xlabel("Time steps", fontsize=16)
    pl.ylabel("Instantaenous rewards", fontsize=16)
    pl.plot(range(0, len(rewards)), rewards, 'black', linewidth=0, marker='.', markeredgewidth=1,
            markerfacecolor='none', markersize=1)
    if (show):
        pl.show()
    else:
        pl.savefig("./Figure-" + name + "-Instantaenous rewards" + '.pdf')

    pl.figure(3)
    pl.clf()
    pl.xlabel("Regret values", fontsize=16)
    pl.ylabel("Instantaenous Regret histogram", fontsize=16)
    pl.hist(regrets, 50)
    if (show):
        pl.show()
    else:
        pl.savefig("./Figure-" + name + "-Instantaenous Regret histogram" + '.pdf')

    pl.figure(4)
    pl.clf()
    pl.xlabel("Time steps", fontsize=16)
    pl.ylabel("Cumulative regret", fontsize=16)
    pl.plot(range(0, len(cumulativeregrets)), cumulativeregrets, 'black', linewidth=1, marker='.', markeredgewidth=1,
            markerfacecolor='none', markersize=4)
    if (show):
        pl.show()
    else:
        pl.savefig("./Figure-" + name + "-Cumulative regret" + '.pdf')
