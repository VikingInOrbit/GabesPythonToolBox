import time
from time import sleep

class DeltaTime():
    def __init__(self):
        self.prev_time = time.time()

    def __call__(self):
        """
        Calculates the time difference (dt) between the current and previous call.
        """

        current_time = time.time()  # Get the current time
        dt = current_time - self.prev_time  # Time difference
        self.prev_time = current_time  # Update the previous time
        return dt
        
def StartDeltaTime():
    return DeltaTime()

def test() -> None:
    deltaTimer = StartDeltaTime()

    while True:
        sleep(1)
        print(f"Time sinse last press: {deltaTimer()}")
        print()


if __name__ == "__main__":
    test()