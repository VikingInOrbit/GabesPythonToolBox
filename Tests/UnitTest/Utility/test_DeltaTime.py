import pytest

# TODO
from GabesPythonToolBox.Utility.DeltaTime import (
    DeltaTime,
    DeltaTimer,
    StartDeltaTime,
    StartDeltaTimer,
)
from Tests.UnitTestComon.UnitTestUtility import FakeClock, almost_equal


@pytest.fixture
def dt_with_fake_clock(monkeypatch):
    """Provide a DeltaTime instance that uses a controllable fake clock.

    Returns (dt, fake_clock)
    """
    fake = FakeClock()
    import GabesPythonToolBox.Utility.DeltaTime as dt_mod

    # replace the module's time.time with our fake clock
    monkeypatch.setattr(dt_mod.time, "time", fake.time)
    dt = dt_mod.DeltaTime()
    return dt, fake


# ------------------------------------
# DeltaTime Tests
# ------------------------------------
def test_deltatime_factory():
    # StartDeltaTimer is a factory for DeltaTimer; StartDeltaTime creates DeltaTime
    dt = StartDeltaTimer()
    assert isinstance(dt, DeltaTimer)


def test_deltatime_delta_matches_advance(dt_with_fake_clock):
    dt, fake = dt_with_fake_clock
    fake.advance(0.01)
    assert almost_equal(dt(), 0.01, tol=1e-9)


def test_deltatime_consecutive_call_is_zero(dt_with_fake_clock):
    dt, fake = dt_with_fake_clock
    fake.advance(0.01)
    _ = dt()
    assert almost_equal(dt(), 0.0, tol=1e-9)


@pytest.mark.parametrize("sleep_time", [0.005, 0.01, 0.05, 0.1, 1000.0])
def test_deltatime_parametrized_sleep(dt_with_fake_clock, sleep_time):
    dt, fake = dt_with_fake_clock
    fake.advance(sleep_time)
    assert almost_equal(dt(), sleep_time, tol=1e-9)


@pytest.mark.parametrize("step", [0.005, 0.01, 0.02, 0.05, 0.1, 1000.0])
def test_deltatime_avg_of_consecutive_steps(dt_with_fake_clock, step):
    dt, fake = dt_with_fake_clock
    n = 5
    for _ in range(n):
        fake.advance(step)
        dt()
    # advance and measure n deltas then assert the average equals the step
    # create n fresh deltas
    deltas = []
    for _ in range(n):
        fake.advance(step)
        deltas.append(dt())
    avg = sum(deltas) / len(deltas)
    assert almost_equal(avg, step, tol=1e-9)


# ------------------------------------
# DeltaTimer Tests
# ------------------------------------


def test_start_deltatime_factory_creates_deltatime():
    dt = StartDeltaTime()
    assert isinstance(dt, DeltaTime)


@pytest.mark.parametrize(
    "duration,advance,expected",
    [
        (0.03, 0.02, False),
        (0.03, 0.05, True),
        (0.0, 0.0, True),
    ],
)
def test_deltatimer_finish_behavior(dt_with_fake_clock, duration, advance, expected):
    dt, fake = dt_with_fake_clock
    timer = DeltaTimer(duration)
    timer.startTimer()
    fake.advance(advance)
    assert (timer() is True) == expected


def test_deltatimer_timeleft_decreases_after_start(dt_with_fake_clock):
    dt, fake = dt_with_fake_clock
    timer = DeltaTimer(0.05)
    timer.startTimer()
    before = timer.duration
    fake.advance(0.02)
    _ = timer()
    assert timer.timeLeft < before


def test_deltatimer_pause_preserves_timeleft(dt_with_fake_clock):
    dt, fake = dt_with_fake_clock
    timer = DeltaTimer(0.05)
    timer.startTimer()
    fake.advance(0.02)
    timer.pauseTimer()
    left = timer.getTimeLeft()
    fake.advance(0.02)
    assert almost_equal(left, timer.getTimeLeft(), tol=1e-9)


def test_deltatimer_continue_decreases_timeleft(dt_with_fake_clock):
    dt, fake = dt_with_fake_clock
    timer = DeltaTimer(0.05)
    timer.startTimer()
    fake.advance(0.02)
    timer.pauseTimer()
    left = timer.getTimeLeft()
    timer.continueTimer()
    fake.advance(0.02)
    assert timer.getTimeLeft() < left


def test_deltatimer_stop_sets_finished(dt_with_fake_clock):
    dt, fake = dt_with_fake_clock
    timer = DeltaTimer(0.05)
    timer.startTimer()
    timer.stopTimer()
    assert timer.Finished


@pytest.mark.parametrize("run", list(range(6)))
def test_deltatimer_recurrent_single_run(dt_with_fake_clock, run):
    dt, fake = dt_with_fake_clock
    timer = DeltaTimer(0.03)
    timer.startTimer()
    fake.advance(0.05)
    assert timer() is True


def test_deltatimer_negative_duration_finishes(dt_with_fake_clock):
    dt, fake = dt_with_fake_clock
    t = DeltaTimer(-0.01)
    t.startTimer()
    assert t() is True


def test_deltatimer_stop_before_finish(dt_with_fake_clock):
    dt, fake = dt_with_fake_clock
    timer = DeltaTimer(0.05)
    timer.startTimer()
    fake.advance(0.02)
    timer.stopTimer()
    assert timer() is True


def test_deltatimer_stop_after_finish(dt_with_fake_clock):
    dt, fake = dt_with_fake_clock
    timer = DeltaTimer(0.03)
    timer.startTimer()
    fake.advance(0.05)
    if timer() is not True:
        pytest.fail("Timer did not finish as expected before stop.")
    timer.stopTimer()
    assert timer.Finished


def test_deltatimer_start_before_finish(dt_with_fake_clock):
    dt, fake = dt_with_fake_clock
    timer = DeltaTimer(0.05)
    timer.startTimer()
    fake.advance(0.02)
    assert timer() is False


def test_deltatimer_start_after_finish(dt_with_fake_clock):
    dt, fake = dt_with_fake_clock
    timer = DeltaTimer(0.03)
    timer.startTimer()
    fake.advance(0.05)

    if timer() is not True:
        pytest.fail("Timer did not finish as expected before restart.")

    timer.startTimer()
    if timer.Finished is not False:
        pytest.fail("Timer did not reset correctly after finishing.")

    assert almost_equal(timer.getTimeLeft(), timer.duration, tol=1e-9)


def test_deltatimer_gettimeleft_updates(dt_with_fake_clock):
    dt, fake = dt_with_fake_clock
    timer = DeltaTimer(0.05)
    timer.startTimer()
    fake.advance(0.02)
    left_before = timer.timeLeft
    left_via_get = timer.getTimeLeft()
    assert left_via_get < left_before


def test_deltatimer_sets_Started_is_False_after_stop(dt_with_fake_clock):
    dt, fake = dt_with_fake_clock
    timer = DeltaTimer(0.05)
    timer.Update()
    assert timer.Started is True
