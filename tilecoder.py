import numpy as np
from math import floor

class Tilecoder:

	def __init__(self, env, num_tilings, num_tiles):
		self.num_tilings = num_tilings
		self.num_tiles = num_tiles
		self.env = env
		#arrays containing the upper and lower bounds (respectively) of each observation 
		self.max_values = env.observation_space.high
		self.min_values = env.observation_space.low

		self.dim = len(self.max_values) #WLOG mountaincar statespace has a dimensionality of 2 (position and velocity)
		self.actions = env.action_space


	def features_to_tiles(self, features):
		one_hot = [0] * self.num_tiles * self.num_tilings * self.dim 
		print(len(one_hot))
		#a one_hot vector with precisely as many ones as there are tilings, with a one corrosponding to the data
		#being present in that tile

		for i in range(0, self.num_tilings):
			for f in range(0, len(features)):
				tile_span = (self.max_values[f] - self.min_values[f])/(self.num_tiles - 1)

				offset = i * self.num_tiles / self.num_tilings
				datum = features[f]
				datum = datum + offset #to do -> optimize asymmetric staggering of tilings
				datum = datum/tile_span
				print ("x = ", x)
				index = self.num_tiles*self.num_tilings*max(f-1, 0) + floor(datum)
				print("index = {}", index)
				one_hot[index] = 1

		return one_hot

	def print_vector(self, x, y):
		vector = self.features_to_tiles([x,y])
		print(vector)

