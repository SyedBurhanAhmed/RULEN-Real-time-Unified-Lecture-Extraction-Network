# RULEN: Real-Time Unified Lecture Extraction Network

**RULEN** is an AI-powered, end-to-end multilingual educational assistant that automates lecture transcription, bilingual note generation, and curriculum-aligned quiz/assessment creation. Designed for both students and educators, RULEN simplifies academic workflows with modern AI models, intuitive dashboards, and intelligent retrieval-augmented learning tools.

---

## 🚀 Key Features

- 🎤 **Automatic Speech Recognition**  
  Transcribe lectures in 99+ languages using OpenAI Whisper (supports large-v3, small, tiny models).

- 📝 **Multilingual Note Generation**  
  Generate structured notes in Roman Urdu/Hindi and English. Export as `.docx` for offline study.

- 🧠 **Quiz & Assessment Creation**  
  Build MCQs, short/long questions, assignments, and exams with FAISS-powered semantic search and RAG.

- 👨‍🎓👩‍🏫 **Dual Dashboards**  
  - **Students**: Upload audio → receive notes → prepare for quizzes
  - **Teachers**: Upload lectures/materials/CLOs → generate curriculum-aligned assessments

- 📄 **Supplementary Material Integration**  
  Upload PDFs, PPTX, DOCX, and TXT documents to expand knowledge base.

- 🎯 **CLO/PLO Mapping**  
  Automatically align questions with institutional outcomes for accreditation readiness.

- 🌐 **Modern Web Interface**  
  Built on Flask and Jinja2 with responsive UI, file management, and role-based workflows.

---

## 📦 Getting Started

1. **Clone the Repository:**
```bash
git clone https://github.com/SyedBurhanAhmed/RULEN-Real-time-Unified-Lecture-Extraction-Network.git
cd RULEN-Real-time-Unified-Lecture-Extraction-Network
```

2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

3. **Install Whisper and FFmpeg:**
```bash
pip install git+https://github.com/openai/whisper.git
```

- **Install FFmpeg**:
  - Ubuntu/Debian:
    ```bash
    sudo apt update && sudo apt install ffmpeg
    ```
  - MacOS:
    ```bash
    brew install ffmpeg
    ```
  - Windows: [Download from ffmpeg.org](https://ffmpeg.org/download.html) and add to system PATH.

4. **Configure Environment:**
Edit the `.env` file for:
```
WHISPER_MODEL=small
EMBEDDING_MODEL=all-MiniLM-L6-v2
UPLOAD_FOLDER=./uploads
FAISS_INDEX_PATH=./faiss_index
```
⚠️ Never commit `.env` or credentials. Add it to `.gitignore`.

5. **Run the Application:**
```bash
python app.py
```

6. **Access the Dashboard:**
Visit [http://localhost:5000](http://localhost:5000)

---

## 🌐 Google API Integration (Optional)

1. **Create a Google Cloud Project:**  
   Enable required APIs (Drive, Sheets, etc.)

2. **Download OAuth credentials (JSON)**  
   Reference it in `.env`.

3. **Install Required Libraries:**
```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

4. **Authenticate in Code**
Follow Google documentation for using OAuth or Service Accounts securely.

---

## 📊 Example Results

- **Hindi Lecture** ([CodeWithHarry](https://youtu.be/ajeTYqhRHno))  
  > Transcribed → Roman Hindi/English Notes → Quiz Created → .docx Exported

- **English Lecture** ([deeplearning.ai](https://youtu.be/dLc-lfEEYss))  
  > Transcribed → English Notes → Quiz Generated → .docx Delivered

---

## 📁 Project Structure

```bash
rulen-lecture-extraction/
├── app.py
├── requirements.txt
├── static/
├── templates/
│   ├── base.html
│   └── results.html
├── modules/
│   ├── transcription.py
│   ├── notes_generation.py
│   └── quiz_generation.py
├── uploads/
└── README.md
```

---

## 🔒 Security & Privacy

- End-to-end encryption (HTTPS in production)
- Role-based access for students and teachers
- All processing is local — no third-party audio sharing
- Environment variables secure API keys & configs

---

## 📚 References

- [OpenAI Whisper](https://github.com/openai/whisper)
- [FAISS Similarity Search](https://github.com/facebookresearch/faiss)
- [LangChain Documentation](https://python.langchain.com/)
- [CodeWithHarry YouTube](https://www.youtube.com/@CodeWithHarry)
- [deeplearning.ai](https://www.youtube.com/@deeplearningai)

---

## 🧭 Future Advancements

- 🔗 LMS Integration: Moodle, Canvas, Blackboard
- 🌍 Cloud deployment (GCP, Azure, AWS)
- 🎛️ Dedicated edge device (ESP32 + mic + Wi-Fi)
- 🖥️ Frontend revamp (React + Tailwind)
- 🛡️ SSO, JWT-based Auth, and OAuth integrations

---

## 🤝 Contributing

Contributions are welcome! 
Please fork the repo and open a pull request or issue. 
See [CONTRIBUTING.md](CONTRIBUTING.md) for code style and feature roadmap.

---

## 📝 License

Licensed under the MIT License. See [LICENSE](LICENSE) for details.
