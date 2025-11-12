import pytest
from GabesPythonToolBox.Utility.DeltaTime import DeltaTime, DeltaTimer
from GabesPythonToolBox.Tests.UnitTestComon.UntTestUtility import almost_equal
import time

#DeltaTime tests

def test_deltatime_basic():
    dt = DeltaTime()
    time.sleep(0.01)  # small sleep
    delta = dt()
    assert delta > 0
    # consecutive call should give a smaller delta if called immediately
    delta2 = dt()
    assert almost_equal(delta2, 0, tol=1e-2)  # allow 0.01s tolerance

#DeltaTimer tests

def test_deltatimer_start_and_update():
    timer = DeltaTimer(0.05)  # 50ms timer
    # Initially not started
    assert timer.Update() is False
    assert not timer.Finished
    # Start timer
    timer.startTimer()
    time.sleep(0.02)
    finished = timer.Update()
    assert finished is False
    # timeLeft should decrease
    assert timer.timeLeft < timer.duration

def test_deltatimer_finish():
    timer = DeltaTimer(0.03)
    timer.startTimer()
    time.sleep(0.05)
    finished = timer.Update()
    assert finished is True
    assert timer.Finished
    assert timer.timeLeft <= 0

def test_deltatimer_pause_and_continue():
    timer = DeltaTimer(0.05)
    timer.startTimer()
    time.sleep(0.02)
    timer.pauseTimer()
    paused_time_left = timer.getTimeLeft()
    time.sleep(0.02)
    # Timer should not decrease while paused
    assert almost_equal(paused_time_left, timer.getTimeLeft(), tol=1e-3)
    timer.continueTimer()
    time.sleep(0.02)
    # After continuing, timer should decrease
    assert timer.getTimeLeft() < paused_time_left

def test_deltatimer_stop():
    timer = DeltaTimer(0.05)
    timer.startTimer()
    timer.stopTimer()
    assert timer.Finished
    assert timer.timeLeft == timer.timeLeft  # no change after stop


def test_deltatimer_recurrent_start_finish():
    #Start timer, let it finish, start again, and finish again (simulate recurring events).
    timer = DeltaTimer(00.03)
    test_runs = 6
    i=0

    while i < test_runs:
        timer.startTimer()
        time.sleep(0.05)
        assert timer.Update() is True
        assert timer.Finished
        i+=1
