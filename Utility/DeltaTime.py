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
