# 🎙️ Raspberry Pi Voice Assistant

This project is a **local voice assistant** for Raspberry Pi that can recognize speech, detect intents, and control hardware devices (Light, Fan, Servo) through GPIO.  
It supports both **real Raspberry Pi GPIO** mode and **simulation mode** for testing without hardware.

---

## 🏗️ System Architecture

![System Architecture](https://github.com/saifibolte/Local-AI-Assistant-with-Hardware-Actions/blob/adade25ce4ae1279b9fc54004dd00698f3e8d29a/figures/System%20Architecture.drawio.png)

### Flow:
1. **User speaks** → Microphone captures audio.
2. **Vosk STT** converts audio → text.
3. **Intent Detector**:
   - Routes small-talk → GPT2 restricted + TTS.
   - Routes device commands → GPIO Interface.
4. **GPIO Handler Layer**:
   - `--mode sim` → Simulated GPIO.
   - `--mode rpi` → Real Raspberry Pi GPIO.
5. **Output**:
   - Voice reply via **Silero TTS**.
   - Device control (Light, Fan, Servo).

---

## 📂 Project Structure
```
.
├── asr.py              # Speech-to-text (Vosk)
├── assistant.py        # Main assistant logic
├── gpio_rpi.py         # Real Raspberry Pi GPIO handler
├── gpio_sim.py         # Simulated GPIO handler
├── intents.py          # Intent detection (commands + small-talk)
├── tts.py              # Text-to-speech (Silero)
├── main.py             # Entry point
├── System Architecture.drawio.png
└── requirements.txt    # Dependencies
```

---

## ⚙️ Installation

### 1. Clone repo & install dependencies
```bash
git clone https://github.com/your-repo/pi-voice-assistant.git
cd pi-voice-assistant
pip install -r requirements.txt
```

### 2. Download Vosk Model
```bash
mkdir models
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip -d models/
```

---

## 🚀 Usage

### Simulation Mode (no hardware required)
```bash
python main.py --model-path models/vosk-model-small-en-us-0.15 --mode sim
```

### Raspberry Pi Mode (with GPIO)
```bash
python main.py --model-path models/vosk-model-small-en-us-0.15 --mode rpi
```

---

## 🎮 Voice Commands

| Command Example        | Action                           |
|-------------------------|----------------------------------|
| "Turn on the light"    | Light → ON                      |
| "Switch off fan"       | Fan → OFF                       |
| "Make the servo wave"  | Servo → WAVE                    |
| "Blink the light"      | Light → BLINK (3 times)         |
| "Hello / Hi"           | Small talk response             |

---

## 🛠️ Hardware Setup (Raspberry Pi + L293D)

- **GPIO Pin Map**:
  - `LIGHT` → GPIO 17
  - `FAN` → GPIO 27 (via L293D motor driver for DC motor)
  - `SERVO` → GPIO 18 (PWM)

⚠️ Connect **fan (DC motor)** via L293D motor driver:
- Pi GPIO 27 → L293D Input1  
- Pi GND → L293D GND (common ground with motor PSU)  
- Motor → L293D Output1/Output2  
- External PSU (6–12V) → L293D Vcc2  

---

## 📦 Dependencies
- [Vosk](https://alphacephei.com/vosk/) (speech recognition)
- [Silero TTS](https://github.com/snakers4/silero-models) (text-to-speech)
- [SoundDevice](https://python-sounddevice.readthedocs.io/)
- [RPi.GPIO](https://pypi.org/project/RPi.GPIO/) (only on Raspberry Pi)
- PyTorch

Install via:
```bash
pip install vosk sounddevice torch RPi.GPIO
```

---

## 📸 Demo

- User: *"Turn on the fan"*  
- Assistant: *"Okay, fan set to ON."*  
- Fan (DC motor) spins up via **L293D motor driver**.  

---

## 📜 License
MIT License © 2025
