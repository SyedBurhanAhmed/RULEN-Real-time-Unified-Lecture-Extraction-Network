import torch
import whisper

def load_whisper_model():
    if torch.cuda.is_available():
        print("✅ GPU detected: Using 'turbo' model")
        return whisper.load_model("turbo")
    else:
        print("⚠️ No GPU detected: Using 'tiny' model")
        return whisper.load_model("tiny")

