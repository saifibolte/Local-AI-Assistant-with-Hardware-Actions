import numpy as np
import sounddevice as sd
import torch

TTS_SAMPLE_RATE = 24000

class TTS:
    def __init__(self):
        print("[TTS] Loading Silero TTS...")
        self.model, _ = torch.hub.load(
            repo_or_dir="snakers4/silero-models",
            model="silero_tts",
            language="en",
            speaker="v3_en",
            trust_repo=True
        )
        self.speaker = "en_0"

    def speak(self, text):
        if not text or not text.strip():
            print("[TTS] (empty skipped)")
            return
        print(f"[assistant] {text}")
        try:
            audio = self.model.apply_tts(
                text=text,
                speaker=self.speaker,
                sample_rate=TTS_SAMPLE_RATE
            )
            audio = np.array(audio, dtype=np.float32)
            sd.stop()
            sd.play(audio, TTS_SAMPLE_RATE)
            sd.wait()
        except ValueError as e:
            print(f"[TTS error] {e} -- skipped.")
