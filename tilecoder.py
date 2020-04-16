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

	def normalize(self, features): #normalize to range [0, 1] to make tilecoding easier (super lazy and probably bad)
		for i in range(0, len(features)):
			features[i] = (features[i] - self.min_values[i])/(self.max_values[i] - self.min_values[i])


	def features_to_tiles(self, features):
		one_hot = [0] *self.num_tiles* self.num_tiles * self.num_tilings
		print(len(one_hot))
		#a one_hot vector with precisely as many ones as there are tilings, with a one corrosponding to the data
		#being present in that tile
		self.normalize(features)
		for i in range(1, self.num_tilings+1):
			print("-----Tiling", i)
			index = -1

			tile_span = 1/(self.num_tiles-1)
			print("tile_span = ", tile_span)
			offset_x = i * tile_span / self.num_tilings
			offset_y = 1.5 * offset_x
			print(offset_x)
			
			x = features[0] + offset_x
			y = features[1] + offset_y 
			
			print("x = ", x)
			print("y = ", y)

			n = floor((x /tile_span)+1)
			j = floor((y /tile_span)+1)

			position = n + 4*(j-1)
			print("n =", floor(n))
			print("j = ", floor(j))
			print("plosition = ", floor(position))
			
			index = (int)(self.num_tiles*self.num_tiles*(i-1) + floor(position))
			print(index)
			one_hot[index] = 1

		return one_hot

	def print_vector(self, x, y):
		vector = self.features_to_tiles([x,y])
		print(vector)

