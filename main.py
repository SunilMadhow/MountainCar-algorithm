import gym
env = gym.make('MountainCar-v0')
for i in env.action_space:
	print(i);
