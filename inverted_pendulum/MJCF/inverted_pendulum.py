import os
import time

import mujoco
import mujoco.viewer

script_dir = os.path.dirname(os.path.abspath(__file__))


m = mujoco.MjModel.from_xml_path("inverted_pendulum.xml")
d = mujoco.MjData(m)

with mujoco.viewer.launch_passive(m, d) as viewer:
    start = time.time()

    while viewer.is_running():
        step_start = time.time()
        mujoco.mj_step(m, d)
        viewer.sync()

        time_until_next_step = m.opt.timestep - (time.time() - step_start)
        if time_until_next_step > 0:
            time.sleep(time_until_next_step)
