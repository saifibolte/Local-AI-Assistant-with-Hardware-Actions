import time

try:
    import RPi.GPIO as GPIO
except (ImportError, RuntimeError):
    GPIO = None  # fallback for non-Pi environments

PIN_MAP = {
    "LIGHT": 17,
    "FAN": 27,
    "SERVO": 18
}

class RaspberryPiGPIO:
    def __init__(self):
        if GPIO is None:
            raise RuntimeError("RPi.GPIO not available. Run this only on Raspberry Pi with --mode rpi")

        GPIO.setmode(GPIO.BCM)
        for device, pin in PIN_MAP.items():
            if device == "SERVO":
                GPIO.setup(pin, GPIO.OUT)
            else:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, GPIO.LOW)
        print("[GPIO_RPI] Initialized.")

    def control(self, device, cmd):
        if GPIO is None:
            print("[GPIO_RPI] Skipped (not running on Pi).")
            return

        pin = PIN_MAP[device]

        if device in ["LIGHT", "FAN"]:
            if cmd == "ON":
                GPIO.output(pin, GPIO.HIGH)
            elif cmd == "OFF":
                GPIO.output(pin, GPIO.LOW)
            elif cmd == "BLINK" and device == "LIGHT":
                for _ in range(3):
                    GPIO.output(pin, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pin, GPIO.LOW)
                    time.sleep(0.5)

        elif device == "SERVO" and cmd == "WAVE":
            servo = GPIO.PWM(pin, 50)   # 50Hz PWM
            servo.start(0)
            for angle in [0, 90, 0]:
                duty = 2 + (angle / 18)
                servo.ChangeDutyCycle(duty)
                time.sleep(0.5)
            servo.stop()

        print(f"[GPIO_RPI] {device} => {cmd}")

    def cleanup(self):
        if GPIO:
            GPIO.cleanup()
            print("[GPIO_RPI] Cleaned up.")
