import numpy as np

class Tilecoder:

	def __init__(self, env, num_tilings, num_tiles):
		self.num_tilings = num_tilings
		self.num_tiles = num_tiles
		self.env = env
		#arrays containing the upper and lower bounds (respectively) of each observation 
		self.max_values = env.observation_space.high
		self.min_values = env.observation_space.low

		self.dim = len(self.max_values)
		self.actions = env.action_space
		#length of weight vector
		self.n = self.num_tiles * self.env.action_space.n
		self.tile_size = np.divide(np.ones(self.dim), self.num_tiles -1)

	

	def features_to_tiles(self, features) {
		#values is the array that represents the current observation
		values = np.zeros(self.dim)
		for i in range(self.dim):
			values[i] = features[i]
		tile_matrix = np.zeros([self.num_tilings, self.dim])
		for i in range(self.num_tilings):
			for j in range (self.dim):
				tile_matrix[i,j] = int(values[j] / self.tile_size[j])
	

	}
