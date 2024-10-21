import os

from gymnasium.envs.registration import register

__version__ = "0.0.1"

ASSETS_PATH = os.path.join(os.path.dirname(__file__), "assets", "low_cost_robot_6dof")
BASE_LINK_NAME = "link_1"
EE_LINK_NAME = "link_6"
koch_default_qpos = [0.0245438, 0.7195878, 1.4773341, 0.2975618, -1.5053105, -0.78539515]

register(
    id="LiftCube-v0",
    entry_point="gym_lowcostrobot.envs:LiftCubeEnv",
    max_episode_steps=500,
)

register(
    id="PickPlaceCube-v0",
    entry_point="gym_lowcostrobot.envs:PickPlaceCubeEnv",
    max_episode_steps=500,
)

register(
    id="PushCube-v0",
    entry_point="gym_lowcostrobot.envs:PushCubeEnv",
    max_episode_steps=500,
)

register(
    id="ReachCube-v0",
    entry_point="gym_lowcostrobot.envs:ReachCubeEnv",
    max_episode_steps=500,
)

register(
    id="StackTwoCubes-v0",
    entry_point="gym_lowcostrobot.envs:StackTwoCubesEnv",
    max_episode_steps=500,
)

register(
    id="PushCubeLoop-v0",
    entry_point="gym_lowcostrobot.envs:PushCubeLoopEnv",
    max_episode_steps=500,
)
