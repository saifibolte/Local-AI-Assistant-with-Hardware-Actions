import json
from vosk import Model, KaldiRecognizer

ASR_SAMPLE_RATE = 16000

class ASR:
    def __init__(self, model_path):
        print("[ASR] Loading Vosk model...")
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, ASR_SAMPLE_RATE)

    def transcribe(self, audio_bytes):
        if self.recognizer.AcceptWaveform(audio_bytes):
            res = self.recognizer.Result()
        else:
            res = self.recognizer.PartialResult()
        j = json.loads(res)
        return j.get("text", "")
