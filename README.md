
# 🤖 Aditi's AI Chatbot

A simple, interactive chatbot built using **React.js** (frontend), **Flask** (backend), and **spaCy** (NLP).  
It answers basic user queries with smart responses, and has a clean modern UI!

## 🔗 Deployed Projects

- 🚀 **Frontend (React)** — Deployed on Netlify  
  👉 [Click here to view frontend](https://chatbot-aditi.netlify.app/)

- ⚙️ **Backend (Flask)** — Deployed on Render  
  👉 [Click here to view backend API](https://your-backend.onrender.com)

---

## 🔥 Features

- 💬 Real-time chat interface
- 🤖 NLP processing using spaCy
- 🧠 Flask backend handles responses
- 🎨 Stylish and responsive frontend using React
- 🌈 Gradient background with glass-style chatbot box

---

## 🛠️ Tech Stack

| Frontend | Backend | NLP Engine |
|----------|---------|------------|
| React.js | Flask   | spaCy      |

---

## 📂 Project Structure

chatbot/
├── backend/
│ └── app.py # Flask server + spaCy logic
│ └── requirements.txt # Python dependencies
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── App.js
│ │ └── App.css
│ └── package.json
└── README.md


---

## 🚀 Getting Started

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Setup Backend (Flask + spaCy)
cd backend
python -m venv venv
source venv/bin/activate  # use venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py

💻 3. Setup Frontend (React)
cd frontend
npm install
npm start
React will start on: http://localhost:3000

📌 TODOs / Future Improvements

 Add voice-to-text input
 Integrate OpenAI or GPT API
 Store chat history
 Add typing animation or loading dots

