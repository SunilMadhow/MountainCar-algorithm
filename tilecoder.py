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
		self.high = self.max_values - self.min_values
		self.low = self.min_values - self.min_values

		self.dim = len(self.max_values) 
		self.actions = env.action_space
		self.num_actions = 3

		self.vector_length = self.num_tiles* self.num_tiles * self.num_tilings * self.num_actions
		print("Output will be vector of length {leng}".format(leng = self.vector_length))

		self.tile_span_x = (self.high[0] - self.low[0])/(self.num_tiles-1)
		self.tile_span_y = (self.high[1] - self.low[1])/(self.num_tiles-1)
		print("Tilespans are {spans}".format(spans=(self.tile_span_x, self.tile_span_y)))

	def normalize(self, features): 
		normalized = [0]*len(features)
		for i in range(0, len(features)):
			normalized[i] = (features[i] - self.min_values[i])
		return normalized

	def tilecode(self, raw_features, action):
		# print("-------CALL TO TILECODE------------")
		# print("action = {act}".format(act = action))
		one_hot = np.zeros(self.num_tiles* self.num_tiles * self.num_tilings * self.num_actions)
		# print("featuers from inside fcall = ", raw_features)
		features = self.normalize(raw_features)
		for i in range(1, self.num_tilings+1):
			# print("Features: {f}".format(f = features))

			offset_x = (i-1) * self.tile_span_x / self.num_tilings
			offset_y = (i -1) * self.tile_span_y * 1.03/ self.num_tilings
			
			x = features[0] + offset_x
			y = features[1] + offset_y 
			# print("offset data = {tup}".format(tup = (x, y)))

			n = min(floor((x /self.tile_span_x)+1), self.num_tiles)
			j = min(floor((y /self.tile_span_y)+1), self.num_tiles)
			# print("Tiles for offset = {tils}".format(tils = (n, j)))

			position = n + self.num_tiles*(j-1)
			# print("Index within tile = {inderx}".format(inderx = position))
			
			index = (int)(self.num_tiles*self.num_tiles*(i-1)*self.num_actions + int(position) + action*self.num_tiles*self.num_tiles)
			# print("index = {ind}".format(ind = index))
			one_hot[index -1] = 1

		return one_hot


	def print_vector(self, x, y, a):
		vector = self.tilecode([x,y], a)