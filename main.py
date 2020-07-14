#implementing example 1 from Sutton, Chapter 12
#Semi gradient 1-step Sarsa with function approximation
import random
import gym
import numpy as np
from tilecoder import Tilecoder	

np.seterr('ignore')

env = gym.make('MountainCar-v0').env
print(env.observation_space.high)
print(env.observation_space.low)	
print(env.action_space)

tiler = Tilecoder(env, 8, 8)
# tiler.print_vector(-.569, 0, 2)
tiler.print_vector(-.3, .07, 1)
num_episodes = 500
# w = [0] * tiler.vector_length #weight vector

def Q(tiler, observation, w): #returns list of all q-values for the state
	Q = np.zeros(tiler.num_actions)
	for i in range(tiler.num_actions):
		Q[i] = np.dot(tiler.tilecode(observation, i), w)
	return Q


alpha = .5/8 #stepsize
w = np.zeros(tiler.vector_length) #parametrizing vector

for episode in range(num_episodes):
	G = 0
	observation = env.reset()
	action = random.choice([0, 1, 2])
	gradient = np.zeros(tiler.vector_length)
	
	epsilon = 0
	prediction = np.dot(tiler.tilecode(observation, action), w)
	x_s = tiler.tilecode(observation, action)
	while True:
		# env.render()

		state2, reward, done, info = env.step(action)
		observation = state2

		if done:
			w  = w + (reward - prediction)*x_s
			observation = env.reset()
			prevG = G
			print ("Episode {ep} : Reward = {re}".format(ep = episode, re = G))
			break

		if random.random() > epsilon:
			q_list = Q(tiler, observation, w)
			action = np.argmax(q_list)

		else:
			action = random.choice([0, 1, 2])
		
		G = G + reward
		prime = np.dot(tiler.tilecode(observation, action), w)
		delta = reward + prime - prediction
		w = w + alpha*delta*x_s
		# print(w)
		x_s = tiler.tilecode(observation, action)
		prediction = np.dot(tiler.tilecode(observation, action), w)