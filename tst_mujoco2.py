import distutils.util
import os
import subprocess

import ctypes
import ctypes.util
ctypes.CDLL(ctypes.util.find_library('GL'), ctypes.RTLD_GLOBAL)

if subprocess.run('nvidia-smi').returncode:
  raise RuntimeError(
      'Cannot communicate with GPU. '
      'Make sure you are using a GPU Colab runtime. '
      'Go to the Runtime menu and select Choose runtime type.')


from dm_control import suite
env = suite.load('cartpole', 'swingup')
os.environ["MUJOCO_GL"] = "egl"
pixels = env.physics.render()