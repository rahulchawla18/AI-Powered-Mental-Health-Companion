# 🧠 MindMosaic - AI-Powered Mental Health Companion

MindMosaic is a Streamlit + FastAPI powered web application designed to help users maintain mental well-being through journaling, AI feedback, emotion tracking, and personalized activity suggestions. It uses LLMs and embeddings to deliver intelligent insights and semantic search over past entries.

---

## 🚀 Features

### ✅ User Authentication
- Lightweight login system to register and log in users (no password for demo simplicity).
- Secure journaling tied to individual users.

### 📝 AI-Powered Journal Analysis
- Users write or speak journal entries.
- Entries are analyzed to extract:
  - **Primary Emotion** (e.g., sad, happy, anxious)
  - **Feedback from AI therapist**
  - **Uplifting activity suggestions**

### 🔊 Voice Input Integration
- Speak your thoughts directly into the app via microphone.
- Uses `SpeechRecognition` and `PyAudio` to convert speech to text.

### 📈 Mood Analytics & Visualization
- Line chart of mood trends over time
- Pie chart of emotion distribution
- Weekly emotion frequency bar chart
- Daily journaling activity insights

### 💡 Mood-Based Uplift Suggestions
- Based on your detected emotion, the app offers tailored activity suggestions (e.g., creative, calming, social).
- Calls a dedicated FastAPI endpoint: `/uplift/{emotion}`

### 🔎 Semantic Search
- Search your journal using **natural language**.
- Powered by **ChromaDB + Embeddings** to retrieve semantically relevant past entries.

---

## 🧰 Tech Stack

| Layer        | Tech Used                                |
|--------------|------------------------------------------|
| Frontend     | Streamlit                                |
| Backend      | FastAPI                                  |
| Database     | SQLite (`mosaic.db`)                     |
| LLM Model    | Ollama LLM (local model, e.g., `llama2`) |
| Embeddings   | ChromaDB                                 |
| Voice Input  | SpeechRecognition + PyAudio              |
| Visualization| Plotly + Pandas                          |

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/rahulchawla18/AI-Powered-Mental-Health-Companion.git
cd AI-Powered-Mental-Health-Companion.git
```

### 2. Setup virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4.  Install PyAudio (Windows users)

```bash
# First try:
pip install pyaudio

# If it fails, use the .whl method from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
```

### 5. Start the backend

```bash
uvicorn backend.main:app --reload
```

### 6. Start the frontend (in another terminal)

```bash
streamlit run frontend/app.py
```

---

## 🤖 Example Prompts (Semantic Search)

"When did I feel very low?"

"Days I was happy after yoga"

"How was my mood last weekend?"

"Times I felt anxious and stressed"

## 🔐 Optional Enhancements

Add password-based authentication

Daily check-in reminders via email

Export insights as PDF

Multilingual support

## ❤️ Contributing

Pull requests are welcome! For major changes, please open an issue first.

## 📜 License

This project is licensed under the MIT License.

## 🙌 Acknowledgements

#### Streamlit [https://streamlit.io/]

#### FastAPI [https://fastapi.tiangolo.com/]

#### Ollama [https://ollama.com/]

#### ChromaDB [https://www.trychroma.com/]

#### SpeechRecognition [https://pypi.org/project/SpeechRecognition/]