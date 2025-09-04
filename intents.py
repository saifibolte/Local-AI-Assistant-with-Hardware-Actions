# Devices
DEVICES = ["light", "fan", "servo"]

# Action keywords
ACTION_KEYWORDS = {
    "turn on": "ON",
    "switch on": "ON",
    "on": "ON",
    "turn off": "OFF",
    "switch off": "OFF",
    "off": "OFF",
    "start": "ON",
    "stop": "OFF",
    "wave": "WAVE",
    "blink": "BLINK",
}

# Preloaded responses
PRELOADED_RESPONSES = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there!",
    "who are you": "I am your Raspberry Pi voice assistant.",
    "what is your name": "I am Pi Assistant.",
    "how are you": "I am doing great, thanks for asking!"
}

def detect_hardware_actions(text):
    txt = text.lower()
    actions = []

    detected_action = None
    for k, v in ACTION_KEYWORDS.items():
        if k in txt:
            detected_action = v
            break
    if not detected_action:
        return actions

    for device in DEVICES:
        if device in txt:
            if detected_action == "BLINK" and device != "light":
                continue
            if detected_action == "WAVE" and device != "servo":
                continue
            actions.append((device.upper(), detected_action))

    return actions

def is_small_talk(text):
    txt = text.lower()
    for q in PRELOADED_RESPONSES:
        if q in txt:
            return PRELOADED_RESPONSES[q]
    return None
