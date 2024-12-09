from GabesPythonToolBox.Utility.Debug import Debug
#Debug.add_group('LIB', True) #Uncoment for the debug mesages

import matplotlib.pyplot as plt
import time
import GabesPythonToolBox.DataProsesing.PID as GTB
import GabesPythonToolBox.Utility.DeltaTime as DT

# A simple system simulation (heater cartrage)
class SimpleSystem:
    def __init__(self, initial_value=0, gain=1, resistance=0.1, delay=0.1):
        self.current_value = initial_value
        self.gain = gain
        self.resistance = resistance  # Resistance to change
        self.delay = delay  # Time lag effect
        self.previous_value = initial_value

    def update(self, control_signal):
        """
        Updates the system's state based on the control signal with optional resistance and lag.
        """
        print(f"state: {self.current_value}")
        # Apply resistance if resistance > 0
        resistance_effect = self.resistance * self.current_value if self.resistance > 0 else 0

        # Calculate the next value considering gain and resistance
        next_value = self.gain * control_signal - resistance_effect
        # Apply delay if delay > 0
        if self.delay > 0:
            self.current_value = (1 - self.delay) * self.previous_value + self.delay * next_value
            self.previous_value = self.current_value
        else:
            self.current_value = next_value

    def get_value(self):
        return self.current_value

def test():
    deltaTime = DT.StartDeltaTime()
    deltaTime()
    # New PID controller
    pid = GTB.NewPID(P=9, I=20, D=0.005)
    SetResetIntegral = True #flag to enable reset integer on setpoint change
    
    # Simulated system
    system = SimpleSystem(initial_value=00, gain=1, resistance=.1, delay=.1)
    
    # Target setpoint
    setpoint = 100
    setpointDiff = 50
    required_hits = 5

    # Simulation parameters
    time_steps = 100
    time_delay = 0.1  # 100 ms per step

    # Simulate the system
    results = simulate(system, pid, setpoint, setpointDiff, time_delay, time_steps,required_hits, SetResetIntegral)

    #real time used
    print(f"\nreal time since start: {deltaTime()}s\n")

    # Plot the results
    graph(results)

def simulate(system, pid, setpoint, setpointDiff, time_delay, time_steps,required_hits,SetResetIntegral):
    orgSetpoint = setpoint
    tolerance = 0.1  # Define tolerance for hitting the setpoint
    results = []
    consecutive_hits = 0  # Track how many consecutive steps are within the tolerance
    resetIntegral = False

    for t in range(time_steps):
        hitTarget, result = simulateStep(system, pid, setpoint, tolerance, time_delay, t, resetIntegral)
        results.append(result)

        if hitTarget:
            consecutive_hits += 1
        else:
            consecutive_hits = 0  # Reset if the tolerance is missed

        if resetIntegral:
            resetIntegral = False

        # Change setpoint only if the target is maintained for the required number of steps
        if consecutive_hits >= required_hits:
            if setpoint == orgSetpoint:
                setpoint += setpointDiff
                if SetResetIntegral:
                    resetIntegral = True
            else:
                setpoint = orgSetpoint
                if SetResetIntegral:
                    resetIntegral = False
            consecutive_hits = 0  # Reset after switching setpoints

    return results

def simulateStep(system, pid, setpoint, tolerance, time_delay, t, resetIntegral):
    print(f"Step: {t}")
    current_value = system.get_value()
    control_signal = pid(current_value, setpoint, resetIntegral)
      
    # Update the system state
    system.update(control_signal)
        
    # Record data for analysis
    result = (t * time_delay, current_value, control_signal, setpoint)
        
    # Simulate real-time delay
    time.sleep(time_delay)

    # Check if the current value is within tolerance of the setpoint
    if abs(current_value - setpoint) < tolerance:
        return True, result

    return False, result

def graph(results):
    # Plot the results
    time_data, value_data, control_data, setpoints = zip(*results)
    
    plt.figure(figsize=(12, 6))
    
    # System response graph
    plt.subplot(2, 1, 1)
    plt.plot(time_data, value_data, label="System Value")
    plt.plot(time_data, setpoints, "r--", label="Dynamic Setpoint")  # Plot dynamic setpoint
    plt.xlabel("Time (s)")
    plt.ylabel("Value")
    plt.legend()
    plt.title("System Response")
    
    # Control signal graph
    plt.subplot(2, 1, 2)
    plt.plot(time_data, control_data, label="Control Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Control Signal")
    plt.legend()
    plt.title("Control Signal Over Time")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    test()
