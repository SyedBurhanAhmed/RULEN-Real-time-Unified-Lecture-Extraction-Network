import whisper
import os

# Optional: Set a persistent cache directory (useful for Colab or remote VMs)
# os.environ["XDG_CACHE_HOME"] = "/content/drive/MyDrive/whisper_cache"  # for Colab
# os.environ["XDG_CACHE_HOME"] = "/your/local/cache/path"               # for PyCharm/local

# Global model cache
_model_instance = None

def get_whisper_model(size="tiny"):
    global _model_instance
    if _model_instance is None:
        print(f"Loading Whisper model: {size}...")
        _model_instance = whisper.load_model(size)
    return _model_instance

def transcribe_audio_agent(audio_path, model_size="tiny"):
    model = get_whisper_model(model_size)
    result = model.transcribe(audio_path, task="transcribe")
    language_code = result.get("language", None)
    print(language_code)
    print(result["text"])
    return result["text"], language_code

# print(os.path.exists("../What is Deep Learning_ (in 5 Minutes).mp3"))  # Should return True
#
# print(transcribe_audio_agent("../What is Deep Learning_ (in 5 Minutes).mp3"))
#
# def transcribe_audio_agent():
#     return