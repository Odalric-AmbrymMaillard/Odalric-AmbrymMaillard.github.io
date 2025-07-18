import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

from tictactoe_env import TicTacToeEnv, DRAW
from utils import play, Agent, agent_vs_agent

env = TicTacToeEnv()


class DummyAgent(Agent):
    """Dummy TicTacToe agent that plays randomly.
    """
    def __init__(self, env, player=1, params={}):
        self._env = env
        self.player = player  # index of the player

    def play(self):
        """Syntax: play should be a method with no argument
        except self.
        In the present example, it simply calls the env attribute
        and use it to sample a feasible action.
        """
        return self.env.sample()


from qlearning import QFunction, QLearningAgent, random_vs_Q_learning, Q_learning_vs_random

GAMMA = 0.99
n_episodes = int(1e4)
learning_rate = 0.05
epsilon_greedy = 0.9
epsilon_greedy_decay_freq = 50
epsilon_greedy_decay_factor = 0.9

Q_opt_Q_learning_cross, stats = random_vs_Q_learning(
    env,
    n_episodes,
    learning_rate,
    epsilon_greedy,
    epsilon_greedy_decay_freq,
    epsilon_greedy_decay_factor,
    gamma=GAMMA,
)

Q_opt_Q_learning_nought, stats = Q_learning_vs_random(
    env,
    n_episodes,
    learning_rate,
    epsilon_greedy,
    epsilon_greedy_decay_freq,
    epsilon_greedy_decay_factor,
    gamma=GAMMA,
)


from mcts import MCTS


class MCTSPureExploration(MCTS):
    def __init__(self, player=1):
        super().__init__(player=player)

    def search_heuristic(self, node):
        """Pure exploration, uniformly choose how to
        explore the game tree.
        """
        # All children of node should already be expanded:
        assert all(n in self.children for n in self.children[node])

        return np.random.choice(list(self.children[node]))


class MCTSUCT(MCTS):
    def __init__(self, player=1, exploration_param=1.0):
        self.exploration_param = exploration_param
        super().__init__(player=player)

    def search_heuristic(self, node):
        """Upper Confidence bound for Trees.
        Balance exploration and exploitation in the game tree.
        """
        # All children of node should already be expanded:
        assert all(n in self.children for n in self.children[node])

        # children is a dictionary of node -> set of children,
        # where node is a TicTacToeEnv, and the chidlren are
        # TicTacToeEnv corresponding to boards that are
        # one action away from node.

        # self.W is a dictionary of node -> backpropagated rewards
        # self.N is a dictionary of node -> backpropagated number of visits

        def uct(n):
            "Upper confidence bound for trees"
            return self.W[n] / self.N[n] + self.exploration_param * np.sqrt(
                np.log(self.N[node]) / self.N[n]
            )

        return max(self.children[node], key=uct)



class MCTSAgent(Agent):
    """TicTacToe template agent that plays according to MCTS.
    """

    def __init__(self, env, player=1, params={'n_playouts': 1}):
        self.env = env
        self.player = player  # index of the player
        self.n_playouts = params.get('n_playouts', 1)
        # To be implemented in child class
        self.game_tree = None

    def play(self):
        """Syntax: play should be a method without argument
        except self.
        """
        # Need to copy environment, so that MCTS internal simulations
        # do not affect the game being played
        env_copy = deepcopy(env)
        for _ in range(self.n_playouts):
            self.game_tree.playout(env_copy)
        return self.game_tree.choose(env_copy)


class MCTSPureExplorationAgent(MCTSAgent):
    """TicTacToe agent that plays according to MCTS Pure Exploration.
    """

    def __init__(self, env, player=1, params={'n_playouts': 1}):
        super().__init__(env=env, player=player, params=params)
        self.game_tree = MCTSPureExploration(player=player)


class MCTSUCTAgent(MCTSAgent):
    """TicTacToe agent that plays according to MCTS UCT.
    """

    def __init__(self, env, player=1, params={'n_playouts': 1, 'exploration_param': 1.0}):
        super().__init__(env=env, player=player, params=params)
        exploration_param = params.get('exploration_param', 1.0)
        self.game_tree = MCTSUCT(player=player, exploration_param=exploration_param)




env.render()

def q1():
    # Example game: each player plays randomly
    print("Example game: each player plays randomly")
    # Always reset the environment at the start of a game
    # (Remark : the reset method returns the initial state
    # of the envionment, i.e the board in the present case)
    env.reset()
    done = False
    while not done:
        # Draw a position uniformly at random among the
        # remaining possible choices
        pos = env.sample()
        board, reward, done, _ = env.step(pos)
        # Display the board
        env.render()

    winner = board.check_state()
    if winner == DRAW:
        print("**      DRAW      **")
    elif winner == 1:
        print("**      O WINS      **")
    else:
        print("**      X WINS      **")


def q2():
    print("Play against DUMMY agent. Available input in the API: [1-9], 'quit', 'switch'")
    # Available input in the API: [1-9], 'quit', 'switch'
    play(DummyAgent, game_env=env)

    print("DUMMY vs DUMMY agents")
    agent_vs_agent(env, DummyAgent, DummyAgent, n_episodes=100, params1={}, params2={}, plot=True)

def q3():
    print("Play Agianst QLEARNING Agent. Available input in the API: [1-9], 'quit', 'switch'")
    play(QLearningAgent, game_env=env, params={'Q': Q_opt_Q_learning_cross.Q})

def q4():
    env.reset()

    agent1 = DummyAgent(env, player=1)
    agent2 = MCTSUCTAgent(env, player=2, params={'n_playouts': 20, 'exploration_param': 1.0})


    print("MCTS vs DUMMY agents")
    n_episodes = 10

    for episode in range(n_episodes):
        done = False
        _ = env.reset()
        turn = 0

        while not done:
            if turn % 2 == 0:
                action = agent1.play()
            else:
                action = agent2.play()

            _, _, done, _ = env.step(action)

            turn += 1

            if done:
                break

        winner = env.board.check_state()
        if winner == DRAW:
            print("**      DRAW        **")
        elif winner == 1:
            print("**      O WINS      **")
        else:
            print("**      X WINS      **")


    game_tree = agent2.game_tree
    children = game_tree.children
    print('Total number of nodes: {}\n'.format(len(children)))
    for node, successors in children.items():
        print('Node: {} wins, {} visits'.format(game_tree.W[node], game_tree.N[node]))
        node.render()
        for successor in successors:
            print('Child: {} wins, {} visits'.format(game_tree.W[successor], game_tree.N[successor]))
            successor.render()
        print('----------------------\n\n')

def q6():

    print("DUMMY vs MCTS agents")
    # agent_vs_agent(env, DummyAgent, MCTSPureExplorationAgent, n_episodes=10, params1={}, params2={'n_playouts': 20}, plot=True)
    agent_vs_agent(env, DummyAgent, MCTSUCTAgent, n_episodes=10, params1={}, params2={'n_playouts': 20}, plot=True)

def q7():
    print("Play against MCTS agent. Available input in the API: [1-9], 'quit', 'switch'")
    play(MCTSUCTAgent, game_env=env, params={'n_playouts': 50})

def q8():
    print("MCTS vs QLearning agent")
    agent_vs_agent(env, MCTSUCTAgent, QLearningAgent, n_episodes=10, params1={'n_playouts': 50}, params2={'Q': Q_opt_Q_learning_cross.Q}, plot=True)





q1()
#q2()
q4()
q6()
#q7()
#q8()




