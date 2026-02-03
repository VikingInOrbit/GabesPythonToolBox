from ..DataProsesing.map import *
from ..Utility.Debug import *


class PID:
    def __init__(
        self,
        P: float = 0,
        I: float = 0,
        D: float = 0,
        integral_limit: float = None,
        Debug_enable: bool = False,
    ):  # P = proportional , I = integral , D = derivitive will hrt preformence if true "Debug_enable"
        self.P = P
        self.I = I
        self.D = D
        self.prev_value = 0  # To store previous error for derivative calculation
        self.integral = 0  # To store accumulated error for integral calculation
        self.integral_limit = integral_limit  # max +- the integral can be

        self.Debug_enable = Debug_enable

        if self.Debug_enable:
            Debug.log(f"PID init", "Header", group="LIB")
            Debug.log(f"P: {self.P}, I: {self.I}, D: {self.D}", "Info", group="LIB")
            Debug.log(f"PID init", "End", group="LIB")

    def __call__(
        self,
        current_value: float,
        set_value: float,
        dt: float,
        resetIntegral: bool = False,
    ) -> float:
        """
        Called to compute the PID output based on the current and set values.

        current_value: The current measured value.
        set_value: The target value.
        reset Integral: set Intergal error to 0
        """
        if self.Debug_enable:
            Debug.log(f"PID call", "Header", group="LIB")
            Debug.log(
                f"With current_value: {current_value}, set_value: {set_value}, resetIntegral: {resetIntegral}",
                "Info",
                group="LIB",
            )

        if resetIntegral:
            if self.Debug_enable:
                Debug.log(f"Reseting Integral", "Info", group="LIB")
            self.ResetIntegral()

        if self.Debug_enable:
            Debug.log(f"PID call", "End", group="LIB")
        return self.Update(current_value, set_value, dt)

    def start(self):
        if self.Debug_enable:
            Debug.log(f"PID start", "Header", group="LIB")
            Debug.log(f"Starting Delta Time", "Info", group="LIB")
        if self.Debug_enable:
            Debug.log(f"PID start", "End", group="LIB")

    def Update(self, current_value, set_value, dt) -> float:
        """
        Compute PID output based on current_value and set_value.
        Uses prev_error for D term to handle dynamic setpoints.
        """
        if self.Debug_enable:
            Debug.log(f"PID Update", "Header", group="LIB")
            Debug.log(f"get Delta Time: {dt}", "Info", group="LIB")

        # Calculate the current error
        error = set_value - current_value
        if self.Debug_enable:
            Debug.log(f"error: {error}", "Info", group="LIB")

        # Calculate PID output
        P_ = self.CalcP(error)
        I_ = self.CalcI(error, dt)
        D_ = self.CalcD(current_value, set_value, dt)

        output = P_ + I_ + D_

        if self.Debug_enable:
            Debug.log(f"output: {output}", "Info", group="LIB")

        # Update previous error for next derivative calculation
        self.prev_error = error

        if self.Debug_enable:
            Debug.log(f"PID Update", "End", group="LIB")
        return output, P_, I_, D_, error, dt

    def CalcP(self, error: float) -> float:
        """
        Proportional term: P = Kp * error
        """
        if self.Debug_enable:
            Debug.log(f"CalcP", "Header", group="LIB")
        val = self.P * error

        if self.Debug_enable:
            Debug.log(f"val: {val}", "Info", group="LIB")
            Debug.log(f"CalcP", "End", group="LIB")
        return val

    def CalcI(self, error: float, dt) -> float:
        """
        Integral term: I = Ki * integral of error
        Integral is the val of all past errors over time.
        """
        if self.Debug_enable:
            Debug.log(f"CalcI", "Header", group="LIB")
        self.integral += error * dt  # Accumulate the error over time

        if self.integral_limit:

            if self.Debug_enable:
                Debug.log(
                    f"before integral: {self.integral}, limit: {self.integral_limit}",
                    "Info",
                    group="LIB",
                )
            self.integral = Clamp(
                self.integral, -self.integral_limit, self.integral_limit
            )
            if self.Debug_enable:
                Debug.log(
                    f"after integral: {self.integral}, limit: {self.integral_limit}",
                    "Info",
                    group="LIB",
                )

        val = self.I * self.integral
        if self.Debug_enable:
            Debug.log(f"val: {val}", "Info", group="LIB")
            Debug.log(f"CalcI", "End", group="LIB")
        return val

    def CalcD(self, current_value: float, set_value: float, dt: float) -> float:
        """
        Derivative term: D = Kd * rate of change of error
        """
        if self.Debug_enable:
            Debug.log(f"CalcD", "Header", group="LIB")

        dt = max(dt, 1e-6)  # Prevent division by zero
        error = set_value - current_value

        # Calculate derivative using prev_error
        derivative = (error - getattr(self, "prev_error", 0)) / dt
        val = self.D * derivative

        if self.Debug_enable:
            Debug.log(f"derivative: {derivative}", "Info", group="LIB")
            Debug.log(f"val: {val}", "Info", group="LIB")
            Debug.log(f"CalcD", "End", group="LIB")

        return val

    def ResetIntegral(self) -> None:
        """
        Resets the integral term to prevent wind-up or drift.
        """
        if self.Debug_enable:
            Debug.log(f"ResetIntegral", "Header", group="LIB")
        self.integral = 0
        if self.Debug_enable:
            Debug.log(f"ResetIntegral", "End", group="LIB")

    def Change(
        self,
        P_: float = None,
        I_: float = None,
        D_: float = None,
        integral_limit: float = None,
    ) -> None:
        """
        Change internal PID parameters dynamically.
        """
        if self.Debug_enable:
            Debug.log("Change", "Header", group="LIB")

        if P_ is not None:
            self.P = P_
            if self.Debug_enable:
                Debug.log(f"Changed P to {self.P}", "Info", group="LIB")

        if I_ is not None:
            self.I = I_
            if self.Debug_enable:
                Debug.log(f"Changed I to {self.I}", "Info", group="LIB")

        if D_ is not None:
            self.D = D_
            if self.Debug_enable:
                Debug.log(f"Changed D to {self.D}", "Info", group="LIB")

        if integral_limit is not None:
            self.integral_limit = abs(integral_limit)  # ensure positive
            if self.Debug_enable:
                Debug.log(
                    f"Set integral limit to {self.integral_limit}", "Info", group="LIB"
                )

        if self.Debug_enable:
            Debug.log("Change", "End", group="LIB")

    def ChangeP(self, P_: float) -> float:
        """
        Change the proportional gain.
        """
        if self.Debug_enable:
            Debug.log(f"ChangeP", "Header", group="LIB")
        self.P = P_
        if self.Debug_enable:
            Debug.log(f"ChangeP", "End", group="LIB")

    def ChangeI(self, I_: float) -> float:
        """
        Change the integral gain.
        """
        if self.Debug_enable:
            Debug.log(f"ChangeI", "Header", group="LIB")
        self.I = I_
        if self.Debug_enable:
            Debug.log(f"ChangeI", "End", group="LIB")

    def ChangeD(self, D_: float) -> float:
        """
        Change the derivitive gain.
        """
        if self.Debug_enable:
            Debug.log(f"ChangeD", "Header", group="LIB")
        self.D = D_
        if self.Debug_enable:
            Debug.log(f"ChangeD", "End", group="LIB")

    def Change_integral_limit(self, integral_limit: float):
        """
        Change the integral_limit.
        """
        if self.Debug_enable:
            Debug.log(f"Change_integral_limit", "Header", group="LIB")
        self.integral_limit = integral_limit
        if self.Debug_enable:
            Debug.log(f"Change_integral_limit", "End", group="LIB")


# Factory function to create a new PID controller instance
def NewPID(P=0, I=0, D=0, integral_limit: float = None, Debug_enable: bool = False):
    """
    make a new PID Controller with starting values P,I,D

    :param P: Proporsional Gain
    :param I: Integral Gain
    :param D: Derivitive Gain
    :return: A PID Controller
    """
    Debug.log(f"NewPID", "Header", group="LIB")
    Debug.log(f"P: {P}, I: {I}, D: {D}", "Info", group="LIB")
    newPID = PID(P, I, D, integral_limit, Debug_enable=Debug_enable)

    Debug.log(f"Starting PID", "Info", group="LIB")
    newPID.start()
    Debug.log(f"NewPID", "End", group="LIB")
    return newPID
