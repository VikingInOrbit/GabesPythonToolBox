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
class DeltaTimer(): 
    def __init__(self,duration):
        self.timeLeft = 0
        self.duration = duration
        self.Started = False
        self.Finished = False
        self.Stoped = False
        self.deltaTimer = None

    def __call__(self):
        """
        Updates the timer and returns True if the timer has finished, False otherwise.
        """

        return self.Update()
    
    def Update(self):
        if self.Stoped is True:
            return self.Finished

        if self.Started is False: #if hasent startet jet start the timer
            self.startTimer() # Start the timer if not started
            return False
        
        self.timeLeft -= self.deltaTimer() #update time

        if self.timeLeft <= 0:
            self.Finished = True
            self.stopTimer()

        return self.Finished
        

    def getTimeLeft(self) -> float:
        """
        Returns the time left in the timer.
        """
        if self.deltaTimer is not None:
            self.Update()
        return self.timeLeft
    
    def startTimer(self) -> None:
        """
        Starts or restarts the timer.
        """
        self.timeLeft = self.duration
        self.deltaTimer = StartDeltaTime()
        self.Started = True
        self.Finished = False
        self.Stoped = False

    def stopTimer(self) -> None:
        """
        Stops the timer immediately.
        """
        self.Stoped = True
        self.Finished = True
        self.deltaTimer = None

    def pauseTimer(self) -> None:
        """
        Pauses the timer without resetting it.
        """
        if self.Started and not self.Finished:
            self.Update()
            self.deltaTimer = None  # Clear deltaTimer since it's paused
            

    def continueTimer(self)  -> None:
        """
        Resumes the timer from where it was paused.
        """
        if not self.Stoped and not self.Finished and (self.timeLeft > 0):
            self.deltaTimer = StartDeltaTime()  # Reinitialize deltaTimer to start tracking again
            self.Update()
        

def StartDeltaTimer(input):
    return DeltaTimer(input)

def test_timer_functionality(timer: DeltaTimer, duration: float, label: str = "") -> None:
    """
    Helper function to test a timer's functionality by running it to completion.
    """
    print(f"--- {label} ---")
    timer.startTimer()
    print(f"Timer started.\n states: Started : {timer.Started}, Finished : {timer.Finished}, Stoped : {timer.Stoped}")
    print(f"Timer started. Duration: {duration:.2f} seconds.")
    while not timer():
        print(f"Time left: {timer.getTimeLeft():.2f} seconds.")
        sleep(0.5)
    
    print(f"Timer finished.\n states: Started : {timer.Started}, Finished : {timer.Finished}, Stoped : {timer.Stoped}")

def test_stop_timer(timer: DeltaTimer) -> None:
    """
    Helper function to test stopping the timer.
    """
    print("--- Stop Test ---")
    timer.startTimer()
    print(f"Timer started.\n states: Started : {timer.Started}, Finished : {timer.Finished}, Stoped : {timer.Stoped}")
    print(f"Timer started. Time left: {timer.getTimeLeft():.2f} seconds.")
    sleep(2)
    print(f"Time left after 2 seconds: {timer.getTimeLeft():.2f} seconds.")
    timer.stopTimer()
    print(f"Timer stopped. Time left: {timer.getTimeLeft():.2f} seconds.")
    print(f"states: Started : {timer.Started}, Finished : {timer.Finished}, Stoped : {timer.Stoped}")
    sleep(2)
    print(f"Time left after 2 seconds post-stop: {timer.getTimeLeft():.2f} seconds.\n")

    print(f"Timer finished.\n states: Started : {timer.Started}, Finished : {timer.Finished}, Stoped : {timer.Stoped}")

def test_pause_resume_timer(timer: DeltaTimer) -> None:
    """
    Helper function to test pausing and resuming the timer.
    """
    print("--- Pause and Resume Test ---")
    timer.startTimer()
    print(f"Timer started.\n states: Started : {timer.Started}, Finished : {timer.Finished}, Stoped : {timer.Stoped}")
    print(f"Timer started. Time left: {timer.getTimeLeft():.2f} seconds.")
    sleep(1)
    print(f"Time left after 1 second: {timer.getTimeLeft():.2f} seconds.")
    timer.pauseTimer()
    print("Timer paused.")
    sleep(1)
    print(f"Time left after pause: {timer.getTimeLeft():.2f} seconds.")
    timer.continueTimer()
    print("Timer continued.")
    while not timer():
        print(f"Time left: {timer.getTimeLeft():.2f} seconds.")
        sleep(0.5)
    print("Timer finished after resume.\n")

    print(f"Timer finished.\n states: Started : {timer.Started}, Finished : {timer.Finished}, Stoped : {timer.Stoped}")

def test() -> None:
    print("Testing DeltaTimer class...")
    
    # Initialize a timer with 3-second duration
    timer = StartDeltaTimer(3)

    # Test: Running the timer to completion twice
    print(f"\n----------------------------------------\n")
    test_timer_functionality(timer, 3, "First Run")

    print(f"\n----------------------------------------\n")
    test_timer_functionality(timer, 3, "Second Run")

    # Test: Stopping the timer
    print(f"\n----------------------------------------\n")
    test_stop_timer(timer)

    # Test: Pausing and resuming the timer
    print(f"\n----------------------------------------\n")
    test_pause_resume_timer(timer)

    print(f"\n----------------------------------------\n")
    print(f"\n----------------------------------------\n")
    print("All tests completed.")

if __name__ == "__main__":
    test()
