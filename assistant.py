import time
import sounddevice as sd
import numpy as np

from intents import detect_hardware_actions, is_small_talk
from asr import ASR
from tts import TTS

CHUNK_SECONDS = 4
ASR_SAMPLE_RATE = 16000

def record_audio(duration=CHUNK_SECONDS, fs=ASR_SAMPLE_RATE):
    print(f"[record] Recording {duration}s... Speak now.")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="int16")
    sd.wait()
    return recording.flatten().tobytes()

class LocalVoiceAssistant:
    def __init__(self, vosk_model_path, gpio_backend):
        self.asr = ASR(vosk_model_path)
        self.tts = TTS()
        self.gpio = gpio_backend
        print("[init] Assistant Ready.")

    def run_loop(self):
        print("=== Local Voice Assistant (Ctrl+C to quit) ===")
        while True:
            try:
                raw = record_audio()
                text = self.asr.transcribe(raw)
                if not text:
                    print("[asr] No speech detected.")
                    continue
                print(f"[asr] \"{text}\"")

                hw_actions = detect_hardware_actions(text)
                if hw_actions:
                    for hw in hw_actions:
                        self.gpio.control(*hw)
                    devices = " and ".join([hw[0] for hw in hw_actions])
                    reply = f"Okay, {devices} set to {hw_actions[0][1]}."
                    self.tts.speak(reply)
                    continue

                reply = is_small_talk(text)
                if reply:
                    self.tts.speak(reply)
                else:
                    print("[intent] Command not recognizable.")
                    self.tts.speak("Command not recognizable.")

            except KeyboardInterrupt:
                print("\n[exit] Goodbye.")
                self.gpio.cleanup()
                break
