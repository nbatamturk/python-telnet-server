#!/usr/bin/env python3

import subprocess
import time

APP_PATH = "/usr/telnet/telnet.py"

def start_server():
    while True:
        print("Starting: {}".format(APP_PATH))
        try:
            subprocess.run(["python3", APP_PATH], check=True)
        except subprocess.CalledProcessError as e:
            print("Application crashed with error: {}".format(e))
        print("Application has stopped, restarting in 5 seconds...")
        time.sleep(5)

if __name__ == "__main__":
    start_server()