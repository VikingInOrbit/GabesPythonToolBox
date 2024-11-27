from ..Utility import DeltaTime as DT

class PID:
    def __init__(self, P: float = 0, I: float = 0, D: float = 0): #P = proportional , I = integral , D = derivitive
        self.P = P
        self.I = I
        self.D = D
        self.prev_error = 0  # To store previous error for derivative calculation
        self.integral = 0  # To store accumulated error for integral calculation

        self.deltaTimer = None

    def __call__(self, current_value: float, set_value: float, resetIntegral: bool = False):
        """
        Called to compute the PID output based on the current and set values.
        
        current_value: The current measured value.
        set_value: The target value.
        reset Integral: The time difference between the current and the previous value.
        """

        if resetIntegral:
            self.ResetIntegral()

        return self.Update(current_value, set_value)
    
    def start(self):
        self.deltaTimer = DT.StartDeltaTime()

    def Update(self,current_value, set_value):
        dt = self.deltaTimer()

        # Calculate the error
        error = set_value - current_value

        # Calculate the PID output
        output = self.CalcP(error) + self.CalcI(error, dt) + self.CalcD(error, dt)

        # Update previous error for next derivative calculation
        self.prev_error = error

        return output

    def CalcP(self, error: float):
        """
        Proportional term: P = Kp * error
        """
        return self.P * error

    def CalcI(self, error: float, dt):
        """
        Integral term: I = Ki * integral of error
        Integral is the sum of all past errors over time.
        """
        self.integral += error * dt  # Accumulate the error over time
        return self.I * self.integral

    def CalcD(self, error: float, dt):
        """
        Derivative term: D = Kd * rate of change of error
        Derivative is the change in error divided by time.
        """
        derivative = (error - self.prev_error) / dt if dt > 0 else 0
        return self.D * derivative
    
    def ResetIntegral(self):
        """
        Resets the integral term to prevent wind-up or drift.
        """
        self.integral = 0

    def ChangeP(self, P_: float):
        """
        Change the proportional gain.
        """
        self.P = P_
    def ChangeI(self, I_: float):
        """
        Change the integral gain.
        """
        self.I = I_
    def ChangeD(self, D_: float):
        """
        Change the derivitive gain.
        """
        self.D = D_

# Factory function to create a new PID controller instance
def NewPID(P=0, I=0, D=0):
    """
    make a new PID Controller with starting values P,I,D
    
    :param P: Proporsional Gain
    :param I: Integral Gain
    :param D: Derivitive Gain
    :return: A PID Controller
    """
    newPID = PID(P, I, D)
    newPID.start()
    return newPID
