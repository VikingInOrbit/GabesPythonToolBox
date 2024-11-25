import matplotlib.pyplot as plt
import time

# Import the PID implementation
import GabrielsPythonToolBox.DataProsesing.PID as GTB

# A simple system simulation (e.g., a heater temperature control)
class SimpleSystem:
    def __init__(self, initial_value=0, gain=1):
        self.current_value = initial_value
        self.gain = gain  # How quickly the system responds

    def update(self, control_signal):
        """
        Updates the system's state based on the control signal.
        """
        # Simulate the system response (basic proportional system with gain)
        self.current_value += self.gain * control_signal

    def get_value(self):
        return self.current_value

def test():
    # New PID controller
    pid = GTB.NewPID(P=1, I=0, D=0)
    
    # Simulated system
    system = SimpleSystem(initial_value=0, gain=1)
    
    # Target setpoint
    setpoint = 100
    setpointDiff = 50
    required_hits = 5

    # Simulation parameters
    time_steps = 50
    time_delay = 0.1  # 100 ms per step

    # Simulate the system
    results = simulate(system, pid, setpoint, setpointDiff, time_delay, time_steps,required_hits)

    # Plot the results
    graph(results)

def simulate(system, pid, setpoint, setpointDiff, time_delay, time_steps,required_hits):
    orgSetpoint = setpoint
    tolerance = 0.1  # Define tolerance for hitting the setpoint
    results = []
    consecutive_hits = 0  # Track how many consecutive steps are within the tolerance

    for t in range(time_steps):
        hitTarget, result = simulateStep(system, pid, setpoint, tolerance, time_delay, t)
        results.append(result)

        if hitTarget:
            consecutive_hits += 1
        else:
            consecutive_hits = 0  # Reset if the tolerance is missed

        # Change setpoint only if the target is maintained for the required number of steps
        if consecutive_hits >= required_hits:
            if setpoint == orgSetpoint:
                setpoint += setpointDiff
            else:
                setpoint = orgSetpoint
            consecutive_hits = 0  # Reset after switching setpoints

    return results

def simulateStep(system, pid, setpoint, tolerance, time_delay, t):
    print(f"Step: {t}")
    current_value = system.get_value()
    control_signal = pid(current_value, setpoint)
      
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
