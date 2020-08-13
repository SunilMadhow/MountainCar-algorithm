import numpy as np

class tiler:

	def __init__(self, num_tilings, num_tiles, environment)
		# num_tilings : the number of tilings that will be superimposed
		# num_tiles   : an array with a value for the no. of tiles used for each dimension 
		# environment : the openai environment

		self.num_tilings = num_tilings
		self.num_tiles = num_tiles

		self.max_values = environment.observation_space.high
		self.min_values = environment.observation_space.low

		self.dimension = len(max_values)
		self.actions = env.action_space
		self.num_actions = len(self.actions)

		self.vector_length = self.num_tiles* self.num_tiles * self.num_tilings * self.num_actions

		self.tile_widths = [0] * self.dim
		for i in range(self.dim):
			self.tile_widths[i] = (self.max_values[i] - self.min_values[i])/self.num_tiles[i]

	def tilecode(self, features, action):
		out = np.zeros(self.vector_length)

		for i in range(1, num_tilings+1):
			active_tiles = [0] * reduce((lambda x, y: x *y), num_tiles)
			for j in range(self.dim):
				pass
				# (features[i] - self.min_values[i])//self.tile_widths[i]





