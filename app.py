from flask import Flask, render_template, request, jsonify
import os, sys
import speech_recognition as sr
from deep_translator import GoogleTranslator
from pydub import AudioSegment

app = Flask(__name__)

@app.route('/')
def index():
    print("🌐 [GET] / → index.html 요청 수신됨")
    sys.stdout.flush()
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_audio():
    print("\n📩 [POST] /translate 요청 수신됨")
    sys.stdout.flush()

    if 'audio' not in request.files:
        print("⚠️ audio 파일 없음")
        sys.stdout.flush()
        return jsonify({'error': '오디오 파일이 전달되지 않았습니다.'})

    file = request.files['audio']
    recognizer = sr.Recognizer()

    try:
        # 1️⃣ 파일 저장
        webm_path = os.path.join(os.getcwd(), "uploaded_audio.webm")
        wav_path = os.path.join(os.getcwd(), "converted_audio.wav")
        file.save(webm_path)
        print(f"💾 파일 저장 완료: {webm_path}")
        sys.stdout.flush()

        # 2️⃣ WebM → WAV 변환
        print("🎧 ffmpeg 변환 시작...")
        sound = AudioSegment.from_file(webm_path, format="webm")
        sound.export(wav_path, format="wav")
        print(f"🔊 변환 완료: {wav_path}")
        sys.stdout.flush()

        # 3️⃣ 음성 인식
        print("🧠 음성 인식 중...")
        with sr.AudioFile(wav_path) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language='en-US')
        print(f"🗣 인식된 문장: {text}")
        sys.stdout.flush()

        # 4️⃣ 번역
        print("💬 번역 중...")
        translated = GoogleTranslator(source='en', target='ko').translate(text)
        print(f"💬 번역 결과: {translated}")
        sys.stdout.flush()

        # 5️⃣ 파일 정리
        try:
            os.remove(webm_path)
            os.remove(wav_path)
            print("🧹 임시 파일 삭제 완료")
        except Exception as cleanup_err:
            print(f"⚠️ 파일 삭제 중 오류: {cleanup_err}")
        sys.stdout.flush()

        # 6️⃣ 최종 응답
        print("✅ [SUCCESS] /translate 응답 송신 완료")
        sys.stdout.flush()
        return jsonify({'original': text, 'translated': translated})

    except Exception as e:
        print(f"❌ [ERROR] 처리 중 오류 발생: {e}")
        sys.stdout.flush()
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # ✅ Render 환경에서는 PORT를 반드시 환경변수로 받아야 함
    port = int(os.environ.get("PORT", 10000))
    print(f"🚀 Flask 서버 시작 (포트 {port})")
    sys.stdout.flush()
    app.run(host='0.0.0.0', port=port)
