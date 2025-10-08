import pytest
from GabesPythonToolBox.DataProsesing.PID import *

# Helper functions

def almost_equal(a, b, tol=1e-6):
    """Helper to compare floating point values."""
    return abs(a - b) < tol


def test_pid_proportional_only():
    pid = PID(P=2.0, I=0.0, D=0.0)
    output, P_, I_, D_, error, dt = pid.Update(current_value=3, set_value=5, dt=1.0)
    assert almost_equal(output, 4.0)
    assert almost_equal(P_, 4.0)
    assert almost_equal(I_, 0.0)
    assert almost_equal(D_, 0.0)


def test_pid_integral_accumulation():
    pid = PID(P=0.0, I=1.0, D=0.0)
    _, _, I1, _, _, _ = pid.Update(current_value=0, set_value=1, dt=1.0)
    _, _, I2, _, _, _ = pid.Update(current_value=0, set_value=1, dt=1.0)
    assert I2 > I1  # Integral should increase over time


def test_pid_derivative_response():
    pid = PID(P=0.0, I=0.0, D=1.0)
    pid.Update(current_value=0, set_value=1, dt=1.0)  # First call sets prev_error
    output, _, _, D_, _, _ = pid.Update(current_value=0.5, set_value=1, dt=1.0)
    # Derivative term should be negative (error decreasing)
    assert D_ < 0


def test_pid_integral_clamping():
    pid = PID(P=0.0, I=1.0, D=0.0, integral_limit=0.5)
    for _ in range(10):
        pid.Update(current_value=0, set_value=1, dt=1.0)
    assert abs(pid.integral) <= 0.5  # Clamped integral


def test_pid_reset_integral():
    pid = PID(P=0.0, I=1.0, D=0.0)
    pid.integral = 10
    pid.ResetIntegral()
    assert pid.integral == 0



# PID parameter modification


def test_pid_change_parameters():
    pid = PID(P=1.0, I=1.0, D=1.0)
    pid.Change(P_=2.0, I_=0.5, D_=0.1, integral_limit=5.0)
    assert pid.P == 2.0
    assert pid.I == 0.5
    assert pid.D == 0.1
    assert pid.integral_limit == 5.0


def test_pid_change_individual_terms():
    pid = PID()
    pid.ChangeP(1.5)
    pid.ChangeI(0.5)
    pid.ChangeD(0.1)
    assert pid.P == 1.5
    assert pid.I == 0.5
    assert pid.D == 0.1


def test_pid_factory_function_creates_pid():
    pid = NewPID(P=1, I=2, D=3)
    assert isinstance(pid, PID)
    assert pid.P == 1
    assert pid.I == 2
    assert pid.D == 3
