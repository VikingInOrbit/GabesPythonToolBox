import pytest

from GabesPythonToolBox.DataProsesing.PID import *
from Tests.UnitTestComon.UntTestUtility import almost_equal


@pytest.mark.parametrize(
    "Debug_enable",
    [
        (False),
        (True),
    ],
)
def test_pid_proportional_only(Debug_enable):
    pid = PID(P=2.0, I=0.0, D=0.0, Debug_enable=Debug_enable)
    output, P_, I_, D_, error, dt = pid.Update(current_value=3, set_value=5, dt=1.0)
    assert almost_equal(output, 4.0)
    assert almost_equal(P_, 4.0)
    assert almost_equal(I_, 0.0)
    assert almost_equal(D_, 0.0)


@pytest.mark.parametrize(
    "Debug_enable",
    [
        (False),
        (True),
    ],
)
def test_pid_integral_accumulation(Debug_enable):
    pid = PID(P=0.0, I=1.0, D=0.0, Debug_enable=Debug_enable)
    _, _, I1, _, _, _ = pid.Update(current_value=0, set_value=1, dt=1.0)
    _, _, I2, _, _, _ = pid.Update(current_value=0, set_value=1, dt=1.0)
    assert I2 > I1  # Integral should increase over time


@pytest.mark.parametrize(
    "Debug_enable",
    [
        (False),
        (True),
    ],
)
def test_pid_derivative_response(Debug_enable):
    pid = PID(P=0.0, I=0.0, D=1.0, Debug_enable=Debug_enable)
    pid.Update(current_value=0, set_value=1, dt=1.0)  # First call sets prev_error
    output, _, _, D_, _, _ = pid.Update(current_value=0.5, set_value=1, dt=1.0)
    # Derivative term should be negative (error decreasing)
    assert D_ < 0


@pytest.mark.parametrize(
    "Debug_enable",
    [
        (False),
        (True),
    ],
)
def test_pid_integral_clamping(Debug_enable):
    pid = PID(P=0.0, I=1.0, D=0.0, integral_limit=0.5, Debug_enable=Debug_enable)
    for _ in range(10):
        pid.Update(current_value=0, set_value=1, dt=1.0)
    assert abs(pid.integral) <= 0.5  # Clamped integral


@pytest.mark.parametrize(
    "Debug_enable",
    [
        (False),
        (True),
    ],
)
def test_pid_reset_integral(Debug_enable):
    pid = PID(P=0.0, I=1.0, D=0.0, Debug_enable=Debug_enable)
    pid.integral = 10
    pid.ResetIntegral()
    assert pid.integral == 0


@pytest.mark.parametrize(
    "Debug_enable",
    [
        (False),
        (True),
    ],
)
def test_pid_change_parameters(Debug_enable):
    pid = PID(P=1.0, I=1.0, D=1.0, Debug_enable=Debug_enable)
    pid.Change(P_=2.0, I_=0.5, D_=0.1, integral_limit=5.0)
    assert pid.P == 2.0
    assert pid.I == 0.5
    assert pid.D == 0.1
    assert pid.integral_limit == 5.0


@pytest.mark.parametrize(
    "Debug_enable",
    [
        (False),
        (True),
    ],
)
def test_pid_change_individual_terms(Debug_enable):
    pid = PID(Debug_enable=Debug_enable)
    pid.ChangeP(1.5)
    pid.ChangeI(0.5)
    pid.ChangeD(0.1)
    assert pid.P == 1.5
    assert pid.I == 0.5
    assert pid.D == 0.1


@pytest.mark.parametrize(
    "Debug_enable",
    [
        (False),
        (True),
    ],
)
def test_pid_factory_function_creates_pid(Debug_enable):
    pid = NewPID(P=1, I=2, D=3, Debug_enable=Debug_enable)
    assert isinstance(pid, PID)
    assert pid.P == 1
    assert pid.I == 2
    assert pid.D == 3


@pytest.mark.parametrize(
    "Debug_enable",
    [
        (False),
        (True),
    ],
)
def test_call_resets_integral_and_returns_tuple(Debug_enable):
    pid = PID(P=0.0, I=2.0, D=0.0, Debug_enable=Debug_enable)
    # accumulate some integral
    pid.Update(current_value=0, set_value=1, dt=1.0)
    pid.Update(current_value=0, set_value=1, dt=1.0)
    assert pid.integral != 0

    ret = pid.__call__(current_value=0, set_value=1, dt=1.0, resetIntegral=True)
    # __call__ forwards to Update and should return the update tuple
    assert isinstance(ret, tuple)
    assert len(ret) == 6
    # ResetIntegral flag should zero the integral
    assert pid.integral == 1


@pytest.mark.parametrize(
    "Debug_enable",
    [
        (False),
        (True),
    ],
)
def test_call_matches_update_return(Debug_enable):
    pid = PID(P=2.0, I=0.5, D=0.1, Debug_enable=Debug_enable)
    expected = pid.Update(current_value=1.0, set_value=3.0, dt=0.5)

    # new instance to ensure __call__ invokes same logic as Update (no prior state)
    pid2 = PID(P=2.0, I=0.5, D=0.1, Debug_enable=Debug_enable)
    got = pid2.__call__(current_value=1.0, set_value=3.0, dt=0.5)

    assert len(got) == len(expected) == 6
    # compare numeric floats with tolerance, others by equality
    for a, b in zip(expected, got):
        if isinstance(a, float):
            assert almost_equal(a, b)
        else:
            assert a == b


@pytest.mark.parametrize(
    "Debug_enable",
    [
        (False),
        (True),
    ],
)
def test_change_integral_limit_sets_value(Debug_enable):
    pid = PID(Debug_enable=Debug_enable)
    pid.Change_integral_limit(-2.5)
    assert pid.integral_limit == -2.5

    pid.Change_integral_limit(3.0)
    assert pid.integral_limit == 3.0
