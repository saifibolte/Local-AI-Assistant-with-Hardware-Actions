import time

class SimulatedGPIO:
    def __init__(self):
        print("[GPIO_SIM] Initialized (no real hardware).")

    def control(self, device, cmd):
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[GPIO_SIM] {ts} -> {device} => {cmd}")

    def cleanup(self):
        print("[GPIO_SIM] Cleaned up.")
