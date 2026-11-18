# AI Interview Preparation Platform 🤖

An AI-powered Interview Preparation Platform that helps students and job seekers practice mock interviews, generate interview questions, evaluate answers, and improve their interview performance using Google Gemini AI.

## 🚀 Project Overview

InterviewAI is a web-based application designed to help candidates prepare for technical and HR interviews. Users can select their preferred interview category and difficulty level, receive AI-generated questions, submit answers, and get instant AI-powered feedback with scores and improvement suggestions.

## ✨ Features

- **AI Question Generation:** Generate interview questions using Google Gemini AI.
- **Multiple Categories:** Practice Python, Java, JavaScript, SQL, HTML & CSS, HR Interview, and Machine Learning.
- **Difficulty Levels:** Beginner, Intermediate, and Advanced.
- **Smart Answer Evaluation:** Evaluate answers using AI.
- **Instant Feedback:** Receive scores, feedback, and suggestions.
- **Dashboard:** View interview history and performance statistics.
- **Database Integration:** Store interview questions, answers, scores, and feedback using SQLite.
- **Responsive Design:** User-friendly interface for different screen sizes.

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Database
- SQLite

### AI Integration
- Google Gemini API
- Google Gen AI SDK

## 📁 Project Structure

```text
AI-Interview-Preparation/
│
├── app.py
├── ai_service.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── interview.html
│   └── result.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    └── js/
        └── script.js
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Interview-Preparation.git
```

### 2. Open the Project Folder

```bash
cd AI-Interview-Preparation
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Gemini API Key

Create a `.env` file in the project root directory.

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=your_supported_gemini_model
SECRET_KEY=your_secret_key
```

Get your API key from:

https://aistudio.google.com/apikey

Keep your API key private. Never upload your `.env` file to GitHub.

### 7. Run the Application

```bash
python app.py
```

### 8. Open in Browser

```text
http://127.0.0.1:5000/
```

## 💡 How It Works

1. Open the InterviewAI application.
2. Select an interview category.
3. Choose your difficulty level.
4. Click **Generate AI Question**.
5. Read the AI-generated interview question.
6. Enter your answer.
7. Submit your answer for AI evaluation.
8. View your score, feedback, and improvement suggestions.
9. Track your previous interview performance on the dashboard.

## 🎯 Project Objectives

- Help students prepare for technical and HR interviews.
- Improve interview answering skills.
- Provide instant AI-powered evaluation.
- Identify areas for improvement.
- Make interview preparation more accessible.

## 🔮 Future Enhancements

- User login and registration.
- Voice-based mock interviews.
- Speech-to-text answer submission.
- Resume-based interview questions.
- Interview performance analytics.
- Personalized learning recommendations.

## 👩‍💻 Author

**Sri Nithya**

Student | Aspiring Software Developer

## 📜 License

This project is created for educational and learning purposes.

---

⭐ If you find this project useful, consider giving it a star!
