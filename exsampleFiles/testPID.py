from GabesPythonToolBox.Utility.Debug import Debug
Debug.add_group('Showcase', True)
Debug.add_group('LIB', True)

path = "exsampleFiles/temp/log/"
Debug.set_log_enabled(path, enabled=False)

import matplotlib.pyplot as plt
import GabesPythonToolBox.DataProsesing.PID as GTB
import GabesPythonToolBox.Utility.DeltaTime as DT
import GabesPythonToolBox.DataProsesing.map as map


# A simple system simulation (heater cartridge)
class SimpleSystem:
    def __init__(self, initial_value=0, gain=1, resistance=0.1, delay=0.1, min_control_signal: float = None,
                 max_control_signal: float = None):
        self.current_value = initial_value
        self.gain = gain
        self.resistance = resistance  # Resistance to change
        self.delay = delay  # Time lag effect
        self.previous_value = initial_value
        self.min_control_signal = min_control_signal
        self.max_control_signal = max_control_signal

    def update(self, control_signal):
        """Update system state based on control signal (no real-time delay)."""
        Debug.log(f"Step Update - state: {self.current_value}", "Info", group="Showcase")

        control_signal = map.Clamp(control_signal,minOutput=self.min_control_signal,maxOutput=self.max_control_signal)

        Debug.log(f"Control signal: {control_signal}", "Info", group="Showcase")

        # Simulate physical response with delay and resistance
        resistance_effect = self.resistance * self.current_value if self.resistance > 0 else 0
        next_value = self.gain * control_signal - resistance_effect

        if self.delay > 0:
            new_value = (1 - self.delay) * self.current_value + self.delay * next_value
            self.previous_value = self.current_value
            self.current_value = new_value
        else:
            self.current_value = next_value

        return control_signal

    def get_value(self):
        return self.current_value


def test():
    """Run PID simulation in simulated time (no waiting)."""
    deltaTime = DT.StartDeltaTime()
    deltaTime()  # reset timer

    min_control_signal=None
    max_control_signal=None

    pid = GTB.NewPID(P=8, I=10,D=0.0, integral_limit=None, Debug_enable=False)

    SetResetIntegral = False  # flag to enable reset integral on setpoint change



    system = SimpleSystem(initial_value=0, gain=1, resistance=0.1, delay=0.1, min_control_signal=min_control_signal, max_control_signal=max_control_signal)
    
    pid.prev_value = system.get_value()

    setpoint = 10
    setpointDiff = 5
    required_hits = 10

    sim_time = 10.0  # total simulated seconds
    time_delay = 0.01  # simulated timestep (Δt)
    time_steps = int(sim_time / time_delay)

    Debug.log("Starting PID simulation", "Header", group="Showcase")
    results = simulate(system, pid, setpoint, setpointDiff, time_delay, time_steps, required_hits, SetResetIntegral)
    Debug.log(f"Real time elapsed: {deltaTime():.4f}s, Sim time elapsed: {sim_time}s", "Info", group="Showcase")
    Debug.log(f"Simulation finished. ", "End", group="Showcase")

    graph(results)
    val_graph(results)



def simulate(system, pid, setpoint, setpointDiff, time_delay, time_steps, required_hits, SetResetIntegral):
    orgSetpoint = setpoint
    tolerance = 0.1
    results = []
    consecutive_hits = 0
    resetIntegral = False

    Debug.log("Simulation loop start", "Header", group="Showcase")

    for t in range(time_steps):
        # Simulated dt is constant per step
        dt = time_delay
        hitTarget, result = simulateStep(system, pid, setpoint, tolerance, time_delay, t, resetIntegral, dt)
        results.append(result)

        if hitTarget:
            consecutive_hits += 1
        else:
            consecutive_hits = 0

        if resetIntegral:
            resetIntegral = False

        # Change setpoint after stable period
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


def simulateStep(system, pid, setpoint, tolerance, time_delay, t, resetIntegral, dt):
    Debug.log(f"Step {t} start", "Header", group="Showcase")

    current_value = system.get_value()

    control_signal,P_,I_,D_,error, dt = pid(current_value, setpoint, dt, resetIntegral)
    

    corrected_control_signal = system.update(control_signal)

    #print(f"control_signal: {control_signal},P: {P_},I: {I_},D: {D_},error: {error}, dt {dt}, control_signal: {control_signal}, corrected_control_signal: {corrected_control_signal}")

    result = (t * time_delay, current_value, control_signal, setpoint,P_,I_,D_,error, dt,corrected_control_signal)

    # No real-time delay — fully simulated time
    # time.sleep(time_delay)  <-- removed

    if abs(current_value - setpoint) < tolerance:
        Debug.log(f"Step {t} hit target: {current_value:.2f} within tolerance of {setpoint}", "Info", group="Showcase")
        Debug.log(f"Step {t} end", "End", group="Showcase")
        return True, result

    Debug.log(f"Step {t} value: {current_value:.2f}, setpoint: {setpoint}", "Info", group="Showcase")
    Debug.log(f"Step {t} end", "End", group="Showcase")
    return False, result


def graph(results):
    (time_data, value_data, control_data, setpoints,
     P_data, I_data, D_data, error_data, dt_data,corrected_control_signal_data) = zip(*results)

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(time_data, value_data, label="System Value")
    plt.plot(time_data, setpoints, "r--", label="Dynamic Setpoint")
    plt.xlabel("Simulated Time (s)")
    plt.ylabel("System Value")
    plt.legend()
    plt.title("PID System Response")

    plt.subplot(2, 1, 2)
    plt.plot(time_data, corrected_control_signal_data, label="Control Signal")
    plt.xlabel("Simulated Time (s)")
    plt.ylabel("Control Signal")
    plt.legend()
    plt.title("PID Control Output")

    plt.tight_layout()
    plt.show()

def val_graph(results):
    # Unpack results
    (time_data, value_data, control_data, setpoints,
     P_data, I_data, D_data, error_data, dt_data,corrected_control_signal_data) = zip(*results)

    plt.figure(figsize=(14, 10))
    plt.style.use('dark_background')

    # PID contributions, error, setpoint, control signals
    plt.plot(time_data, P_data, color="#00FF44", linestyle="-", alpha=1, linewidth=1, label="P term")
    plt.plot(time_data, I_data, color="#00BFFF", linestyle="-", alpha=1, linewidth=1, label="I term")
    plt.plot(time_data, D_data, color="#FF44C1", linestyle="-", alpha=1, linewidth=1, label="D term")
    plt.plot(time_data, error_data, color="#FF0000", linestyle="--", alpha=0.5, linewidth=1, label="Error")
    plt.plot(time_data, setpoints, color="#FFFFFF", linestyle="--", alpha=0.5, linewidth=4, label="Setpoint")
    plt.plot(time_data, control_data, color="#FF0000", linestyle="-", alpha=0.2, linewidth=5, label="Control Signal")
    plt.plot(time_data, corrected_control_signal_data, color="#B05BFF", linestyle="-.", alpha=0.7, linewidth=2, label="Corrected Control Signal")
    plt.plot(time_data, value_data, color="#FF7300", linestyle="-", alpha=1, linewidth=1, label="sys value")

    plt.xlabel("Simulated Time (s)")
    plt.ylabel("PID / System Signals")
    plt.title("PID Internal Terms, Error, Setpoint, and Control Signals")
    plt.legend()
    plt.grid(alpha=0.3)  # optional: light grid for reference
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    test()
