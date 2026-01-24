<div align="center">

# 🎙️ 영어강의 번역기 (English → 한국어)

**브라우저에서 음성을 녹음하고, 서버에서 음성 인식(STT) 후 한국어로 번역해주는 웹 앱**

<br/>

<!-- Badges -->
<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Flask-Web%20App-000000?style=for-the-badge&logo=flask&logoColor=white" />
<img src="https://img.shields.io/badge/SpeechRecognition-STT-6E56CF?style=for-the-badge" />
<img src="https://img.shields.io/badge/Google%20Translate-Deep%20Translator-4285F4?style=for-the-badge&logo=googletranslate&logoColor=white" />
<img src="https://img.shields.io/badge/FFmpeg-Audio%20Convert-007808?style=for-the-badge&logo=ffmpeg&logoColor=white" />

<br/><br/>

</div>

---

## 📌 프로젝트 개요

본 프로젝트는 다음 흐름으로 동작합니다.

1. 사용자가 브라우저에서 마이크로 음성 녹음(WebM/Opus)
2. Flask 서버로 업로드
3. 서버에서 **WebM → WAV 변환(FFmpeg 기반, pydub 사용)**
4. **SpeechRecognition(google)으로 영어 음성 인식(STT)**
5. **deep-translator로 한국어 번역**
6. 원문/번역 결과를 화면에 출력

> 서버 처리 흐름은 Flask 라우트 `/translate`에서 확인할 수 있습니다. :contentReference[oaicite:0]{index=0}  
> 프론트(Web) 녹음/전송 로직은 `index.html`에 포함되어 있습니다. :contentReference[oaicite:1]{index=1}

---

## ✨ 기능

- 🎤 브라우저 음성 녹음 시작/중지(버튼 토글)
- 🔁 음성 파일 업로드(FormData)
- 🧠 영어 음성 인식(STT)
- 💬 한국어 번역
- 🧾 원문/번역 결과 2컬럼 UI로 표시(반응형 포함)

---

## 🧰 기술 스택

### Backend
- **Flask** (API 서버)
- **SpeechRecognition** (Google STT)
- **pydub + FFmpeg** (오디오 포맷 변환: WebM → WAV)
- **deep-translator** (GoogleTranslator 기반 번역)

> 사용 라이브러리 목록은 `requirements.txt`에 명시되어 있습니다. :contentReference[oaicite:2]{index=2}

### Frontend
- **Vanilla HTML/CSS/JS**
- **MediaRecorder API** 기반 음성 녹음 및 업로드

> 실제 UI/녹음 구현은 `index.html`을 기준으로 합니다. :contentReference[oaicite:3]{index=3}

---

## 📁 구성 파일

| 파일 | 설명 |
|---|---|
| `app.py` | Flask 서버(렌더/배포 환경 PORT 대응 포함) :contentReference[oaicite:4]{index=4} |
| `index.html` | 브라우저 녹음, 업로드, 결과 표시 UI :contentReference[oaicite:5]{index=5} |
| `requirements.txt` | 의존성 목록 :contentReference[oaicite:6]{index=6} |
| `realtime_translator.py` | (옵션) 로컬 마이크 기반 실시간 번역 CLI 예시 :contentReference[oaicite:7]{index=7} |

---

## ✅ 실행 방법 (Local)

### 1) FFmpeg 설치 (필수)
`pydub`가 WebM → WAV 변환을 수행하려면 **FFmpeg 설치**가 필요합니다.

- Windows: FFmpeg 설치 후 `bin` 경로가 PATH에 포함되도록 설정
- macOS: `brew install ffmpeg`
- Linux: `sudo apt-get install ffmpeg`

> 로컬(Windows)에서 ffmpeg 경로를 코드에 하드코딩한 버전도 포함되어 있습니다. :contentReference[oaicite:8]{index=8}

### 2) 가상환경 생성 및 설치
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

