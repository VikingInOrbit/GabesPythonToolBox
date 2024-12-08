from ..Utility import DeltaTime as DT
from ..Utility.Debug import *


class PID:
    def __init__(self, P: float = 0, I: float = 0, D: float = 0): #P = proportional , I = integral , D = derivitive
        self.P = P
        self.I = I
        self.D = D
        self.prev_error = 0  # To store previous error for derivative calculation
        self.integral = 0  # To store accumulated error for integral calculation

        self.deltaTimer = None

        Debug.log(f"PID init","Header",group="LIB")
        Debug.log(f"P: {self.P}, I: {self.I}, D: {self.D}","Info",group="LIB")
        Debug.log(f"PID init","End",group="LIB")

    def __call__(self, current_value: float, set_value: float, resetIntegral: bool = False):
        """
        Called to compute the PID output based on the current and set values.
        
        current_value: The current measured value.
        set_value: The target value.
        reset Integral: The time difference between the current and the previous value.
        """
        Debug.log(f"PID call","Header",group="LIB")
        Debug.log(f"With current_value: {current_value}, set_value: {set_value}, resetIntegral: {resetIntegral}","Info",group="LIB")

        if resetIntegral:
            Debug.log(f"Reseting Integral","Info",group="LIB")
            self.ResetIntegral()

        Debug.log(f"PID call","End",group="LIB")
        return self.Update(current_value, set_value)
    
    def start(self):
        Debug.log(f"PID start","Header",group="LIB")
        Debug.log(f"Starting Delta Time","Info",group="LIB")
        self.deltaTimer = DT.StartDeltaTime()
        Debug.log(f"PID start","End",group="LIB")

    def Update(self,current_value, set_value):
        Debug.log(f"PID Update","Header",group="LIB")
        dt = self.deltaTimer()
        Debug.log(f"get Delta Time: {dt}","Info",group="LIB")

        # Calculate the error
        error = set_value - current_value
        Debug.log(f"error: {error}","Info",group="LIB")

        # Calculate the PID output
        output = self.CalcP(error) + self.CalcI(error, dt) + self.CalcD(error, dt)
        Debug.log(f"output: {output}","Info",group="LIB")

        # Update previous error for next derivative calculation
        self.prev_error = error

        Debug.log(f"PID Update","End",group="LIB")
        return output

    def CalcP(self, error: float):
        """
        Proportional term: P = Kp * error
        """
        Debug.log(f"CalcP","Header",group="LIB")
        sum = self.P * error
        
        Debug.log(f"sum: {sum}","Info",group="LIB")
        Debug.log(f"CalcP","End",group="LIB")
        return sum

    def CalcI(self, error: float, dt):
        """
        Integral term: I = Ki * integral of error
        Integral is the sum of all past errors over time.
        """
        Debug.log(f"CalcI","Header",group="LIB")
        self.integral += error * dt  # Accumulate the error over time
        sum = self.I * self.integral
        Debug.log(f"sum: {sum}","Info",group="LIB")
        Debug.log(f"CalcI","End",group="LIB")
        return sum

    def CalcD(self, error: float, dt):
        """
        Derivative term: D = Kd * rate of change of error
        Derivative is the change in error divided by time.
        """
        Debug.log(f"CalcD","Header",group="LIB")
        derivative = (error - self.prev_error) / dt if dt > 0 else 0
        sum = self.D * derivative
        Debug.log(f"sum: {sum}","Info",group="LIB")
        Debug.log(f"CalcD","End",group="LIB")
        return sum
    
    def ResetIntegral(self):
        """
        Resets the integral term to prevent wind-up or drift.
        """
        Debug.log(f"ResetIntegral","Header",group="LIB")
        self.integral = 0
        Debug.log(f"ResetIntegral","End",group="LIB")

    def ChangeP(self, P_: float):
        """
        Change the proportional gain.
        """
        Debug.log(f"ChangeP","Header",group="LIB")
        self.P = P_
        Debug.log(f"ChangeP","End",group="LIB")

    def ChangeI(self, I_: float):
        """
        Change the integral gain.
        """
        Debug.log(f"ChangeI","Header",group="LIB")
        self.I = I_
        Debug.log(f"ChangeI","End",group="LIB")

    def ChangeD(self, D_: float):
        """
        Change the derivitive gain.
        """
        Debug.log(f"ChangeD","Header",group="LIB")
        self.D = D_
        Debug.log(f"ChangeD","End",group="LIB")

# Factory function to create a new PID controller instance
def NewPID(P=0, I=0, D=0):
    """
    make a new PID Controller with starting values P,I,D
    
    :param P: Proporsional Gain
    :param I: Integral Gain
    :param D: Derivitive Gain
    :return: A PID Controller
    """
    Debug.log(f"NewPID","Header",group="LIB")
    Debug.log(f"P: {P}, I: {I}, D: {D}","Info",group="LIB")
    newPID = PID(P, I, D)

    Debug.log(f"Starting PID","Info",group="LIB")
    newPID.start()
    Debug.log(f"NewPID","End",group="LIB")
    return newPID
