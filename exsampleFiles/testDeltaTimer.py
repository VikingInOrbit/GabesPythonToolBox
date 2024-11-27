import GabesPythonToolBox.Utility.DeltaTime as DT


def test_timer_functionality(timer: DT.DeltaTimer, duration: float, label: str = "") -> None:
    """
    Helper function to test a timer's functionality by running it to completion.
    """
    print(f"--- {label} ---")
    timer.startTimer()
    print(f"Timer started.\n states: Started : {timer.Started}, Finished : {timer.Finished}, Stoped : {timer.Stoped}")
    print(f"Timer started. Duration: {duration:.2f} seconds.")
    while not timer():
        print(f"Time left: {timer.getTimeLeft():.2f} seconds.")
        DT.sleep(0.5)
    
    print(f"Timer finished.\n states: Started : {timer.Started}, Finished : {timer.Finished}, Stoped : {timer.Stoped}")

def test_stop_timer(timer: DT.DeltaTimer) -> None:
    """
    Helper function to test stopping the timer.
    """
    print("--- Stop Test ---")
    timer.startTimer()
    print(f"Timer started.\n states: Started : {timer.Started}, Finished : {timer.Finished}, Stoped : {timer.Stoped}")
    print(f"Timer started. Time left: {timer.getTimeLeft():.2f} seconds.")
    DT.sleep(2)
    print(f"Time left after 2 seconds: {timer.getTimeLeft():.2f} seconds.")
    timer.stopTimer()
    print(f"Timer stopped. Time left: {timer.getTimeLeft():.2f} seconds.")
    print(f"states: Started : {timer.Started}, Finished : {timer.Finished}, Stoped : {timer.Stoped}")
    DT.sleep(2)
    print(f"Time left after 2 seconds post-stop: {timer.getTimeLeft():.2f} seconds.\n")

    print(f"Timer finished.\n states: Started : {timer.Started}, Finished : {timer.Finished}, Stoped : {timer.Stoped}")

def test_pause_resume_timer(timer: DT.DeltaTimer) -> None:
    """
    Helper function to test pausing and resuming the timer.
    """
    print("--- Pause and Resume Test ---")
    timer.startTimer()
    print(f"Timer started.\n states: Started : {timer.Started}, Finished : {timer.Finished}, Stoped : {timer.Stoped}")
    print(f"Timer started. Time left: {timer.getTimeLeft():.2f} seconds.")
    DT.sleep(1)
    print(f"Time left after 1 second: {timer.getTimeLeft():.2f} seconds.")
    timer.pauseTimer()
    print("Timer paused.")
    DT.sleep(1)
    print(f"Time left after pause: {timer.getTimeLeft():.2f} seconds.")
    timer.continueTimer()
    print("Timer continued.")
    while not timer():
        print(f"Time left: {timer.getTimeLeft():.2f} seconds.")
        DT.sleep(0.5)
    print("Timer finished after resume.\n")

    print(f"Timer finished.\n states: Started : {timer.Started}, Finished : {timer.Finished}, Stoped : {timer.Stoped}")

def test() -> None:
    print("Testing DeltaTimer class...")
    
    # Initialize a timer with 3-second duration
    timer = DT.StartDeltaTimer(3)

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
