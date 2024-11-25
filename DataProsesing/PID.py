class PID:
    def __init__(self, P=0, I=0, D=0): #P = proportional , I = integral , D = derivitive
        self.P = P
        self.I = I
        self.D = D
        self.prev_error = 0  # To store previous error for derivative calculation
        self.integral = 0  # To store accumulated error for integral calculation

    def __call__(self, current_value, set_value):
        """
        Called to compute the PID output based on the current and set values.
        
        current_value: The current measured value.
        set_value: The target value.
        dt: The time difference between the current and the previous value.
        """

        dt = deltaTime()

        # Calculate the error
        error = set_value - current_value

        # Calculate the PID output
        output = self.CalcP(error) + self.CalcI(error, dt) + self.CalcD(error, dt)

        # Update previous error for next derivative calculation
        self.prev_error = error

        return output

    def CalcP(self, error):
        """
        Proportional term: P = Kp * error
        """
        return self.P * error

    def CalcI(self, error, dt):
        """
        Integral term: I = Ki * integral of error
        Integral is the sum of all past errors over time.
        """
        self.integral += error * dt  # Accumulate the error over time
        return self.I * self.integral

    def CalcD(self, error, dt):
        """
        Derivative term: D = Kd * rate of change of error
        Derivative is the change in error divided by time.
        """
        derivative = (error - self.prev_error) / dt if dt > 0 else 0
        return self.D * derivative

    def ChangeP(self, P_):
        """
        Change the proportional gain.
        """
        self.P = P_
    def ChangeP(self, I_):
        """
        Change the integral gain.
        """
        self.I = I_
    def ChangeP(self, D_):
        """
        Change the derivitive gain.
        """
        self.D = D_

# Factory function to create a new PID controller instance
def NewPID(P=0, I=0, D=0):
    return PID(P, I, D)
