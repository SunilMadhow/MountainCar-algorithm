#implementing example 1 from Sutton 2nd Edition, Chapter 12

import gym
import tilecoder

env = gym.make('MountainCar-v0')

tiler = Tilecoder(env, 4, 4)

