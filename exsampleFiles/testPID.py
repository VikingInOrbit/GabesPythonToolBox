from GabesPythonToolBox.Utility.Debug import Debug
Debug.add_group('Showcase', True)

import matplotlib.pyplot as plt
import time
import GabesPythonToolBox.DataProsesing.PID as GTB
import GabesPythonToolBox.Utility.DeltaTime as DT

# A simple system simulation (heater cartridge)
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
        Debug.log(f"Step Update - state: {self.current_value}", "Info", group="Showcase")

        resistance_effect = self.resistance * self.current_value if self.resistance > 0 else 0
        next_value = self.gain * control_signal - resistance_effect

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
    
    pid = GTB.NewPID(P=9, I=20, D=0.005)
    SetResetIntegral = True  # flag to enable reset integral on setpoint change
    
    system = SimpleSystem(initial_value=0, gain=1, resistance=0.1, delay=0.1)
    
    setpoint = 100
    setpointDiff = 50
    required_hits = 5

    time_steps = 100
    time_delay = 0.1  # 100 ms per step

    Debug.log("Starting PID simulation", "Header", group="Showcase")
    results = simulate(system, pid, setpoint, setpointDiff, time_delay, time_steps, required_hits, SetResetIntegral)
    Debug.log(f"Simulation finished. Real time elapsed: {deltaTime():.2f}s", "End", group="Showcase")

    graph(results)


def simulate(system, pid, setpoint, setpointDiff, time_delay, time_steps, required_hits, SetResetIntegral):
    orgSetpoint = setpoint
    tolerance = 0.1
    results = []
    consecutive_hits = 0
    resetIntegral = False

    Debug.log("Simulation loop start", "Header", group="Showcase")

    for t in range(time_steps):
        hitTarget, result = simulateStep(system, pid, setpoint, tolerance, time_delay, t, resetIntegral)
        results.append(result)

        if hitTarget:
            consecutive_hits += 1
        else:
            consecutive_hits = 0

        if resetIntegral:
            resetIntegral = False

        # Switch setpoint after maintaining target
        if consecutive_hits >= required_hits:
            if setpoint == orgSetpoint:
                setpoint += setpointDiff
                if SetResetIntegral:
                    resetIntegral = True
                Debug.log(f"Setpoint changed to {setpoint}", "Info", group="Showcase")
            else:
                setpoint = orgSetpoint
                if SetResetIntegral:
                    resetIntegral = False
                Debug.log(f"Setpoint reverted to {setpoint}", "Info", group="Showcase")
            consecutive_hits = 0

    Debug.log("Simulation loop end", "End", group="Showcase")
    return results


def simulateStep(system, pid, setpoint, tolerance, time_delay, t, resetIntegral):
    Debug.log(f"Step {t} start", "Header", group="Showcase")

    current_value = system.get_value()
    control_signal = pid(current_value, setpoint, resetIntegral)

    system.update(control_signal)

    result = (t * time_delay, current_value, control_signal, setpoint)

    time.sleep(time_delay)

    if abs(current_value - setpoint) < tolerance:
        Debug.log(f"Step {t} hit target: {current_value:.2f} within tolerance of {setpoint}", "Info", group="Showcase")
        Debug.log(f"Step {t} end", "End", group="Showcase")
        return True, result

    Debug.log(f"Step {t} value: {current_value:.2f}, setpoint: {setpoint}", "Info", group="Showcase")
    Debug.log(f"Step {t} end", "End", group="Showcase")
    return False, result


def graph(results):
    time_data, value_data, control_data, setpoints = zip(*results)

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(time_data, value_data, label="System Value")
    plt.plot(time_data, setpoints, "r--", label="Dynamic Setpoint")
    plt.xlabel("Time (s)")
    plt.ylabel("Value")
    plt.legend()
    plt.title("System Response")

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
