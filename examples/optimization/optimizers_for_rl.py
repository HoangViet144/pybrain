""" 
Illustrating how to use optimization algorithms in a reinforcement learning framework.
"""

__author__ = 'Tom Schaul, tom@idsia.ch'


from pybrain.rl.environments.cartpole.balancetask import BalanceTask
from pybrain.tools.shortcuts import buildNetwork
from pybrain.optimization import HillClimber, CMAES
from pybrain.rl.agents.optimization import OptimizationAgent
from pybrain.rl.experiments.episodic import EpisodicExperiment


# any episodic task
task = BalanceTask()
task.env.randomInitialization = False # enforcing deterministic behavior

# any neural network controller
net = buildNetwork(task.outdim, 1, task.indim)

# any optimization algorithm to be plugged in
learner = HillClimber(storeAllEvaluations = True)
#learner = CMAES(storeAllEvaluations = True)

# the agent
agent = OptimizationAgent(net, learner)

# now, link those elements with an experiment and learn for a number of episodes.
exp = EpisodicExperiment(task, agent)
exp.doEpisodes(200)

print len(agent.learner._allEvaluations)
print agent.learner._bestFound()