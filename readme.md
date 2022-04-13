```
pip install mujoco
pip install dm_control
```

Fix for GL error:

Taken from https://github.com/deepmind/dm_control/issues/283
```
import ctypes
import ctypes.util
ctypes.CDLL(ctypes.util.find_library('GL'), ctypes.RTLD_GLOBAL)
```