```markdown
# RULEN: Real-Time Unified Lecture Extraction Network

Automate multilingual lecture transcription, structured note generation, and adaptive quiz/assessment creation with a single AI-driven toolkit. RULEN is designed for both students and educators, supporting bilingual and multilingual classrooms with seamless integration of audio, supplementary materials, and learning outcomes.

---

## 🚀 Features

- **Automatic Speech Recognition:**  
  Transcribe lecture audio in 99+ languages using OpenAI Whisper (supports large-v3, small, and tiny models).

- **Multilingual Note Generation:**  
  Generate structured notes in English, Roman Urdu/Hindi, or any language supported by Whisper. Download notes as .docx files.

- **Quiz & Assessment Creation:**  
  Prepare customizable quizzes (MCQ, short, long) and teacher assessments (quiz, assignment, midterm, final) using retrieval-augmented generation (RAG) and FAISS vector search.

- **Student & Teacher Dashboards:**  
  Students: Upload audio, receive notes, and generate quizzes.  
  Teachers: Upload audio/materials/CLOs, generate outcome-aligned assessments.

- **Supplementary Material Support:**  
  Upload PDFs, PPTX, DOCX, or TXT files to enhance the knowledge base and quiz generation.

- **CLO/PLO Alignment:**  
  Teachers can upload Course Learning Outcomes (CLOs) and Program Learning Outcomes (PLOs) for curriculum-aligned assessment creation.

- **Modern Web Interface:**  
  Built with Flask and Jinja2; supports session management, file uploads, and multi-step workflows.

---

## 📦 Getting Started

1. **Clone the repository:**
   ```
   git clone https://github.com/SyedBurhanAhmed/RULEN-Real-time-Unified-Lecture-Extraction-Network.git
   cd RULEN-Real-time-Unified-Lecture-Extraction-Network
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Install Whisper and FFmpeg:**

   - **Install Whisper (from GitHub):**
     ```
     pip install git+https://github.com/openai/whisper.git
     ```

   - **Install FFmpeg:**
     - On Ubuntu/Debian:
       ```
       sudo apt-get update
       sudo apt-get install ffmpeg
       ```
     - On Mac (with Homebrew):
       ```
       brew install ffmpeg
       ```
     - On Windows:  
       Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) and add FFmpeg to your system PATH.

   **Note:**  
   Whisper requires FFmpeg to be installed and accessible from your command line. If FFmpeg is not installed, Whisper will not work.

4. **Configure environment:**
   - Edit `.env` for model selection, API keys, and paths.
   - **Important:** Never commit your `.env` or credentials files to the repository. Add `.env` to your `.gitignore`.

5. **Run the application:**
   ```
   python app.py
   ```

6. **Access the dashboard:**  
   Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🌐 Google API Initialization

To use Google APIs (for authentication, storage, or other integrations):

1. **Create a Google Cloud Project:**  
   [Google Cloud Console](https://console.cloud.google.com/)

2. **Enable the required APIs** (e.g., Google Drive API).

3. **Create and download credentials** (OAuth client or service account) as a JSON file.

4. **Add the credentials JSON path to your `.env` file** (never commit this file).

5. **Install Google API Python client libraries:**
   ```
   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
   ```

6. **Authenticate in your code** using the credentials file.

---

## 📊 Example Results

- **Hindi Lecture:**  
  [CodeWithHarry Video](https://youtu.be/ajeTYqhRHno?si=t7xXbVLXNVZGTuqS)  
  Transcribed and generated notes in Roman Hindi and English, with .docx export and quiz generation.

- **English Lecture:**  
  [deeplearning.ai Video](https://youtu.be/dLc-lfEEYss?si=9Xvc8RkON--tabCa)  
  Transcribed and generated notes in English, with .docx export and quiz generation.

---

## 📁 Project Structure

```
rulen-lecture-extraction/
├── app.py
├── requirements.txt
├── templates/
│   └── results.html
├── static/
├── modules/
│   ├── transcription.py
│   ├── notes_generation.py
│   └── quiz_generation.py
├── uploads/
└── README.md
```

---

## 🔒 Security & Privacy

- End-to-end encryption for data in transit and at rest.
- Role-based access control for student/teacher content.
- No lecture data is shared with third parties.
- **Never commit API keys or credentials. Always use a `.env` file and add it to `.gitignore`.**

---

## 📚 References

- [OpenAI Whisper](https://github.com/openai/whisper)
- [CodeWithHarry YouTube Channel](https://www.youtube.com/@CodeWithHarry)
- [deeplearning.ai YouTube Channel](https://www.youtube.com/@deeplearningai)
- See `/docs` for full bibliography and methodology.

---

## 📣 Future Advancements

- Cloud deployment and LMS integration (Moodle, Canvas, Blackboard)
- Dedicated lecture recorder device with microcontroller and Wi-Fi
- Enhanced frontend (React/Vue) and real-time features
- Advanced security layers and institutional SSO

---

## 🤝 Contributing

Pull requests and suggestions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📝 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
```
