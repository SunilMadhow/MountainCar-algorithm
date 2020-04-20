#implementing example 1 from Sutton 2nd Edition, Chapter 12
import random
import gym
import numpy as np
from tilecoder import Tilecoder	

env = gym.make('MountainCar-v0')
print(env.observation_space.high)
print(env.observation_space.low)	

tiler = Tilecoder(env, 4, 4)
# tiler.print_vector(-.569, 0, 2)

num_episodes = 500
w = [0] * tiler.vector_length #weight vector

def dot_product(w, x): 
	inner_product = 0
	for i in range(len(w)):
		inner_product += w[i]*x[i]
	return inner_product

def Q(tiler, observation, w): #returns list of all q-values for the state
	Q = np.zeros(tiler.num_actions)
	for i in range(tiler.num_actions):
		Q[i] = dot_product(tiler.tilecode(observation, i), w)
	return i

alpha = .5/8 #stepsize
epsilon = .2

for episode in range(num_episodes):
	G = 0
	observation = env.reset()
	action = 0
	while True:
		print("observation = ", observation)
		if random.random() < epsilon:
			q_list = Q(tiler, observation, w)
			action = np.argmax(q_list)
		else:
			action = random.choice([0, 1, 2])
		state2, reward, done, info = env.step(action)
		observation = state2
		# if (done):
			# w += alpha(G - Q(tiler, )

