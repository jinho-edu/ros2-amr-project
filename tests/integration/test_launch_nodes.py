import os
import subprocess
import signal
import time

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

    # 프로세스가 중간에 죽지 않았는지 확인
    assert process.poll() is None, "ros2 launch crashed during startup"

    process.send_signal(signal.SIGINT)
    process.wait(timeout=10)

    # SIGINT 종료는 정상
    assert process.returncode in (0, 1, 130)
