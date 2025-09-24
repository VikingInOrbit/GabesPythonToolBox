from GabesPythonToolBox.Utility.Debug import Debug
Debug.add_group('Showcase', True)

import time
import GabesPythonToolBox.Utility.DeltaTime as DT

Debug.log("Delta Timer Showcase", "Header", group="Showcase")
Debug.log("", "None", group="Showcase")

def test_timer_functionality(timer: DT.DeltaTimer, duration: float, label: str = "") -> None:
    """
    Helper function to test a timer's functionality by running it to completion.
    """
    Debug.log(f"Test Timer Functionality {label}", "Header", group="Showcase")

    timer.startTimer()
    Debug.log("Timer started", "Info", group="Showcase")
    Debug.log(f"Current states: Started={timer.Started}, Finished={timer.Finished}, Stopped={timer.Stoped}", "Info", group="Showcase")
    Debug.log(f"Duration: {duration:.2f} seconds", "Info", group="Showcase")

    while not timer():
        Debug.log(f"Time left: {timer.getTimeLeft():.2f} seconds", "Info", group="Showcase")
        time.sleep(0.5)

    Debug.log("Timer finished", "Info", group="Showcase")
    Debug.log(f"Final states: Started={timer.Started}, Finished={timer.Finished}, Stopped={timer.Stoped}", "Info", group="Showcase")

    Debug.log(f"Test Timer Functionality {label}", "End", group="Showcase")


def test_stop_timer(timer: DT.DeltaTimer) -> None:
    """
    Helper function to test stopping the timer.
    """
    Debug.log("Test Stop Timer", "Header", group="Showcase")

    timer.startTimer()
    Debug.log(f"Timer started. States: Started={timer.Started}, Finished={timer.Finished}, Stopped={timer.Stoped}", "Info", group="Showcase")
    Debug.log(f"Time left: {timer.getTimeLeft():.2f} seconds", "Info", group="Showcase")

    time.sleep(2)
    Debug.log(f"Time left after 2 seconds: {timer.getTimeLeft():.2f} seconds", "Info", group="Showcase")

    timer.stopTimer()
    Debug.log(f"Timer stopped. Time left: {timer.getTimeLeft():.2f} seconds", "Info", group="Showcase")
    Debug.log(f"States after stop: Started={timer.Started}, Finished={timer.Finished}, Stopped={timer.Stoped}", "Info", group="Showcase")

    time.sleep(2)
    Debug.log(f"Time left after 2 seconds post-stop: {timer.getTimeLeft():.2f} seconds", "Info", group="Showcase")

    Debug.log("Test Stop Timer", "End", group="Showcase")


def test_pause_resume_timer(timer: DT.DeltaTimer) -> None:
    """
    Helper function to test pausing and resuming the timer.
    """
    Debug.log("Test Pause and Resume Timer", "Header", group="Showcase")

    timer.startTimer()
    Debug.log(f"Timer started. States: Started={timer.Started}, Finished={timer.Finished}, Stopped={timer.Stoped}", "Info", group="Showcase")
    Debug.log(f"Time left: {timer.getTimeLeft():.2f} seconds", "Info", group="Showcase")

    time.sleep(1)
    Debug.log(f"Time left after 1 second: {timer.getTimeLeft():.2f} seconds", "Info", group="Showcase")

    timer.pauseTimer()
    Debug.log("Timer paused", "Info", group="Showcase")

    time.sleep(1)
    Debug.log(f"Time left after pause: {timer.getTimeLeft():.2f} seconds", "Info", group="Showcase")

    timer.continueTimer()
    Debug.log("Timer continued", "Info", group="Showcase")

    while not timer():
        Debug.log(f"Time left: {timer.getTimeLeft():.2f} seconds", "Info", group="Showcase")
        time.sleep(0.5)

    Debug.log(f"Timer finished. States: Started={timer.Started}, Finished={timer.Finished}, Stopped={timer.Stoped}", "Info", group="Showcase")

    Debug.log("Test Pause and Resume Timer", "End", group="Showcase")


def test() -> None:
    Debug.log("Main Test Function", "Header", group="Showcase")

    # Initialize a timer with 3-second duration
    timer = DT.StartDeltaTimer(3)

    # Test: Running the timer to completion twice
    test_timer_functionality(timer, 3, "First Run")
    test_timer_functionality(timer, 3, "Second Run")

    # Test: Stopping the timer
    test_stop_timer(timer)

    # Test: Pausing and resuming the timer
    test_pause_resume_timer(timer)

    Debug.log("All tests completed", "Info", group="Showcase")
    Debug.log("Main Test Function", "End", group="Showcase")


if __name__ == "__main__":
    test()
