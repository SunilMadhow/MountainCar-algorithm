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
# w = [0] * tiler.vector_length #weight vector

def Q(tiler, observation, w): #returns list of all q-values for the state
	Q = np.zeros(tiler.num_actions)
	for i in range(tiler.num_actions):
		Q[i] = np.dot(tiler.tilecode(observation, i), w)
	return Q

discount = 1
alpha = .15/tiler.num_tilings  #stepsize
w = np.zeros(tiler.vector_length)
records = []
# w = np.load('weights2.txt.npy') #parametrizing vector
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
			# print("final reward = {reward}".format(reward=reward))
			observation = env.reset()
			records.append(G)
			# print ("Episode {ep} : Reward = {re}".format(ep = episode, re = G))
			# np.save('weights2.txt', w)
			# print(w)
			break

		action = 0
		if random.random() > epsilon:
			q_list = Q(tiler, observation, w)
			action = np.argmax(q_list)

		else:
			action = random.choice([0, 1, 2])
		
		prime = np.dot(tiler.tilecode(observation, action), w)
		# print("prime = {p}".format(p=prime))
		# print("timestep = {t}".format(t=G))
		# print("prediction = {p}".format(p=prediction))
		# print("reward = {p}".format(p=reward))
		delta = reward + discount*prime - prediction
		# print("delta = {d}".format(d = delta))
		w_p = w
		# print(w)
		w = w + alpha*delta*x_s
		# if np.any([i > 0 for i in w]):
			# print("weight, index = {l}".format(l = [(i, w[i]) for i in range(0, len(w)) if w[i] > 0]))
			# print(w_p)
			# print("-------")
			# print(w)

			# exit()
		# print(w)
		x_s = tiler.tilecode(observation, action)

		prediction = np.dot(tiler.tilecode(observation, action), w)

	hundred_sum = hundred_sum + G

	if episode % 100 == 0 and episode >= 100:
		print("Average reward over 100 episodes = {k}".format(k = hundred_sum/100))
		if sum(records[episode - 100:episode])/100 >= -110:
				print("Solved in {d} episodes!".format(d = episode + 1))
				break
		hundred_sum = 0