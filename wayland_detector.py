#!/usr/bin/env python
# Wayland Detector
# Developer: Titus Johnson

import os
import platform

RED = "\033[31m"
RESET = "\033[0m"


def print_red_and_exit(text):
    print(f"{RED}{text}{RESET}")
    exit()


if platform.system() != "Linux":
    print_red_and_exit("Execution failed because this code can only be run on Linux.")

try:
    session_id = os.popen("loginctl").read().replace("-", "").split()[5]
    session = (
        os.popen(f"loginctl show-session {session_id} -p Type")
        .read()
        .lower()
        .replace("type=", "")
        .rstrip()
    )
except:
    print_red_and_exit(
        "Execution of loginctl failed. It is possible that systemd is not installed."
    )
