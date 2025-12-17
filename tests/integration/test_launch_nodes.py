import subprocess
import time
import os
import signal

def test_nodes_launch_and_exit_cleanly():
    env = os.environ.copy()
    env["ROS_DOMAIN_ID"] = "99"

    process = subprocess.Popen(
        ["ros2", "launch", "amr_nav", "sim_headless.launch.py"],
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    time.sleep(5)

    process.send_signal(signal.SIGINT)
    process.wait(timeout=10)

    assert process.returncode == 0
