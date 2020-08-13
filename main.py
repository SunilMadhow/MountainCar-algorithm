#implementing example 1 from Sutton, Chapter 12
#Semi gradient 1-step Sarsa with function approximation
import random
import gym
import numpy as np
from tilecoder import Tilecoder	

np.seterr('ignore')

env = gym.make('MountainCar-v0')
print(env.observation_space.high)
print(env.observation_space.low)	
print(env.action_space)

tiler = Tilecoder(env, 7, 14)
# tiler.print_vector(-.569, 0, 2)
# tiler.print_vector(-.3, .07, 1)
num_episodes = 100000000

def Q(tiler, observation, w): #returns list of all q-values for the state over all actions
	Q = np.zeros(tiler.num_actions)
	for i in range(tiler.num_actions):
		Q[i] = np.dot(tiler.tilecode(observation, i), w)
	return Q

discount = 1
alpha = .32/tiler.num_tilings  
w = np.zeros(tiler.vector_length)
records = []
hundred_sum = 0
G = 0
for episode in range(num_episodes):


	observation = env.reset()

	action = np.argmax(Q(tiler, observation, w))

	epsilon = 0
	prediction = np.dot(tiler.tilecode(observation, action), w)
	x_s = tiler.tilecode(observation, action)
	G = 0
	while True:
		# env.render()
		state2, reward, done, info = env.step(action)
		G = G + reward
		observation = state2

		if done:
			w  = w + alpha*(reward - prediction)*x_s
			observation = env.reset()
			records.append(G)
			if sum(records[episode - 100:episode])/100 >= -110:
				print("Solved in {d} episodes!".format(d = episode + 1))
				break
			break

		action = 0
		if random.random() > epsilon:
			q_list = Q(tiler, observation, w)
			action = np.argmax(q_list)

		else:
			action = random.choice([0, 1, 2])
		
		prime = np.dot(tiler.tilecode(observation, action), w)
		delta = reward + discount*prime - prediction
		w = w + alpha*delta*x_s
		x_s = tiler.tilecode(observation, action)
		prediction = np.dot(tiler.tilecode(observation, action), w)

	hundred_sum = hundred_sum + G

	if episode % 100 == 0 and episode >= 100:
		# epsilon /= 2
		print("Average reward over 100 episodes = {k}".format(k = hundred_sum/100))
		hundred_sum = 0