import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import playsound
import os
from tempfile import NamedTemporaryFile

def listen_english() -> str:
    """🎙 마이크에서 영어 음성을 텍스트로 ;;;;;;;;;;;변환"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 영어로 말하세요... (끝내려면 Ctrl + C)")
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=15)
        except sr.WaitTimeoutError:
            print("⏰ 10초 동안 아무 말도 하지 않아 대기 중...")
            return ""
    try:
        text = r.recognize_google(audio, language="en-US")
        print(f"🗣 인식된 문장: {text}")
        return text
    except sr.UnknownValueError:
        print("🤔 음성을 인식하지 못했습니다.")
        return ""
    except sr.RequestError as e:
        print(f"🌐 Google API 요청 에러: {e}")
        return ""

def translate_to_korean(text: str) -> str:
    """💬 영어 텍스트를 한국어로 번역"""
    if not text:
        return ""
    translated = GoogleTranslator(source="en", target="ko").translate(text)
    print(f"🔤 번역된 문장: {translated}")
    return translated

def speak(text: str, lang="ko"):
    """🔊 텍스트를 음성으로 출력"""
    if not text:
        return
    tts = gTTS(text=text, lang=lang)
    with NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        playsound.playsound(fp.name)
        os.remove(fp.name)

def main():
    print("🟢 실시간 영어→한국어 번역기 시작 (종료: Ctrl + C)\n")
    try:
        while True:
            english_text = listen_english()
            korean_text = translate_to_korean(english_text)
            speak(korean_text, lang="ko")
    except KeyboardInterrupt:
        print("\n🛑 프로그램을 종료합니다. 감사합니다!")

if __name__ == "__main__":
    main()
