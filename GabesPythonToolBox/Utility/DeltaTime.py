import time

from ..Utility.Debug import *


class DeltaTime:
    def __init__(self):
        Debug.log(f"DeltaTime init", "Header", group="LIB")
        self.prev_time = time.time()
        Debug.log(f"DeltaTime init", "End", group="LIB")

    def __call__(self):
        """
        Calculates the time difference (dt) between the current and previous call.
        """
        Debug.log(f"DeltaTime call", "Header", group="LIB")

        current_time = time.time()  # Get the current time
        dt = current_time - self.prev_time  # Time difference
        self.prev_time = current_time  # Update the previous time

        Debug.log(f"deta time: {dt}", "Info", group="LIB")
        Debug.log(f"DeltaTime call", "End", group="LIB")
        return dt


def StartDeltaTime():
    """
    ceates a DeltaTime Object that returns the time elapsed between calls

    :return: DeltaTime Object
    """
    Debug.log(f"Start Delta Time", "Header", group="LIB")
    Debug.log(f"Start Delta Time", "End", group="LIB")
    return DeltaTime()


class DeltaTimer:
    def __init__(self, duration):
        Debug.log(f"DeltaTimer init", "Header", group="LIB")
        Debug.log(f"make a Timer with duration: {duration}", "Info", group="LIB")
        self.timeLeft = 0
        self.duration = duration
        self.Started = False
        self.Finished = False
        self.Stoped = False
        self.deltaTimer = None

        Debug.log(f"DeltaTimer init", "End", group="LIB")

    def __call__(self):
        """
        Updates the timer and returns True if the timer has finished, False otherwise.
        """
        Debug.log(f"DeltaTimer call", "Header", group="LIB")
        Debug.log(f"DeltaTimer call", "End", group="LIB")

        return self.Update()

    def Update(self):
        Debug.log(f"DeltaTimer Update", "Header", group="LIB")

        if self.Stoped is True:
            Debug.log(f"Timer is finished", "Info", group="LIB")
            Debug.log(f"DeltaTimer Update", "End", group="LIB")
            return self.Finished

        if self.Started is False:  # if hasent startet jet start the timer
            Debug.log(f"Starting", "Info", group="LIB")
            self.startTimer()  # Start the timer if not started
            Debug.log(f"DeltaTimer Update", "End", group="LIB")
            return False

        Debug.log(f"chek time left", "Info", group="LIB")
        self.timeLeft -= self.deltaTimer()  # update time
        Debug.log(f"time left: {self.timeLeft}", "Info", group="LIB")

        if self.timeLeft <= 0:
            Debug.log(f"timer finished", "Info", group="LIB")
            self.Finished = True
            self.stopTimer()

        Debug.log(f"DeltaTimer Update", "End", group="LIB")
        return self.Finished

    def getTimeLeft(self) -> float:
        """
        Returns the time left in the timer.
        """
        Debug.log(f"Get Time Left", "Header", group="LIB")
        Debug.log(f"chek time left", "Info", group="LIB")
        if self.deltaTimer is not None:
            self.Update()
        Debug.log(f"Get Time Left", "End", group="LIB")
        return self.timeLeft

    def startTimer(self) -> None:
        """
        Starts or restarts the timer.
        """
        Debug.log(f"Start Timer", "Header", group="LIB")
        self.timeLeft = self.duration
        Debug.log(f"Starting DeltaTime", "Info", group="LIB")
        self.deltaTimer = StartDeltaTime()
        self.Started = True
        self.Finished = False
        self.Stoped = False
        Debug.log(f"Start Timer", "End", group="LIB")

    def stopTimer(self) -> None:
        """
        Stops the timer immediately.
        """
        Debug.log(f"Stop Timer", "Header", group="LIB")
        self.Stoped = True
        self.Finished = True
        self.deltaTimer = None
        Debug.log(f"Stop Timer", "End", group="LIB")

    def pauseTimer(self) -> None:
        """
        Pauses the timer without resetting it.
        """
        Debug.log(f"Pause Timer", "Header", group="LIB")
        if self.Started and not self.Finished:
            self.Update()
            self.deltaTimer = None  # Clear deltaTimer since it's paused
        Debug.log(f"Pause Timer", "End", group="LIB")

    def continueTimer(self) -> None:
        """
        Resumes the timer from where it was paused.
        """
        Debug.log(f"Continue Timer", "Header", group="LIB")
        if not self.Stoped and not self.Finished and (self.timeLeft > 0):
            self.deltaTimer = (
                StartDeltaTime()
            )  # Reinitialize deltaTimer to start tracking again
            self.Update()
        Debug.log(f"Continue Timer", "End", group="LIB")


def StartDeltaTimer(time: float = 10):
    """
    ceates a DeltaTimer Object that returns true if time elapsed is more or equal to set time

    :param time: number of secunds until timer is finished
    :return: DeltaTimer Object
    """
    Debug.log(f"StartDeltaTimer", "Header", group="LIB")
    Debug.log(f"Start Delta Timer with duration: {time}", "Info", group="LIB")
    Debug.log(f"StartDeltaTimer", "End", group="LIB")
    return DeltaTimer(time)
