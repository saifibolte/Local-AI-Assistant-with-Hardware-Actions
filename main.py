import argparse
from assistant import LocalVoiceAssistant
from gpio_sim import SimulatedGPIO
from gpio_rpi import RaspberryPiGPIO

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model-path", required=True)
    p.add_argument("--mode", choices=["sim", "rpi"], default="sim", help="GPIO mode: sim or rpi")
    args = p.parse_args()

    gpio_backend = SimulatedGPIO() if args.mode == "sim" else RaspberryPiGPIO()

    assistant = LocalVoiceAssistant(vosk_model_path=args.model_path, gpio_backend=gpio_backend)
    assistant.run_loop()

if __name__ == "__main__":
    main()
