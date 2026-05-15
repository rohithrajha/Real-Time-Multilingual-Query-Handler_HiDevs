from deep_translator import GoogleTranslator
from langdetect import detect

LANGUAGE_MAP = {
    "ta": "Tamil",
    "en": "English",
    "hi": "Hindi",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "zh-cn": "Chinese",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic",
    "ru": "Russian",
    "te": "Telugu",
    "ml": "Malayalam",
    "kn": "Kannada"
}

def detect_language(text):
    try:
        lang_code = detect(text)

        return LANGUAGE_MAP.get(lang_code, lang_code)

    except:
        return "Unknown"

def translate_to_english(text):
    try:
        translated = GoogleTranslator(
            source='auto',
            target='en'
        ).translate(text)

        return translated

    except Exception as e:
        return f"Translation Error: {str(e)}"