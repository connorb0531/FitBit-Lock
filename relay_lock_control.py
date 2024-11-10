import os
from dotenv import load_dotenv
from gpiozero import OutputDevice
import time

load_dotenv()

LOCK_PIN = int(os.getenv('LOCK_PIN'))

relay = OutputDevice(LOCK_PIN)


def unlock_door():
    relay.on()
    print("Door is unlocked")


def lock_door():
    relay.off()
    print("Door is locked")


def timed_unlock(duration=15):
    unlock_door()
    time.sleep(duration)
    lock_door()


if __name__ == "__main__":
    timed_unlock(3)
