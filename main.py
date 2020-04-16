#implementing example 1 from Sutton 2nd Edition, Chapter 12
import random
import gym
from tilecoder import Tilecoder	

env = gym.make('MountainCar-v0')
print(env.observation_space.high)
print(env.observation_space.low)	

tiler = Tilecoder(env, 4, 4)
tiler.print_vector(.4, -.035)
