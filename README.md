# PersonaAI

A modular AI system that extracts user memory from chat history and generates short, personality-based responses such as a witty friend, calm mentor, or therapist-style assistant.

---

## 🚀 Overview

This project contains **two main modules**:

### **1. Memory Extraction Module**
Takes 20–30+ raw chat messages and extracts:
- User preferences  
- Emotional patterns  
- Facts worth remembering  
- Preferred personality (witty, mentor, therapist, etc.)

Produces a structured JSON object.

---

### **2. Personality Engine**
Takes:
- `user_query`
- `user_memory` (from module 1)

Generates **short, natural responses** that match the detected personality style.

---

## Requirements
- Python 3.10+
- Tesseract-OCR

---

## 📁 Project Structure
```
├── chat_histories/
│   ├── before_calm_mentor_chat.py         # Sample chat dataset for "Calm Mentor" personality.
│   ├── before_therapist_style_chat.py     # Sample chat dataset for "Therapist-style" personality.
│   └── before_witty_friend_chat.py        # Sample chat dataset for "Witty Friend" personality.
├── src/
│   ├── prompts/
│   │   ├── assistant.py                   # Contains prompt templates for the AI assistant (Personality Engine).
│   │   └── extraction.py                  # Contains prompt template for memory extraction module.
│   ├── utils/
│   │   ├── json_parser.py                 # Utility functions to validate, parse, and clean JSON output from LLM.
│   │   └── llm.py                         # Wrapper functions for OpenAI API calls.
│   ├── requests.py                        # Handles incoming request payloads.
│   ├── routes.py                          # Defines FastAPI (or other framework) API endpoints.
│   └── services.py                        # Core business logic connecting LLM, prompts, and utils.
├── .env.example                           # Example environment variables file.
├── .gitignore                             # Specifies files/folders to ignore in git (e.g., __pycache__, .env, logs).
├── main.py                                # Entry point for the application.
├── README.md                              # Project documentation.
└── requirements.txt                       # Python dependencies (e.g., openai, fastapi, uvicorn, python-dotenv).
```

## ⚙️ Installation

### **1. Clone repo**
```bash
git clone https://github.com/GajrajSinghChundawat/PersonaAI.git
cd PersonaAI
```

### **2. Create and activate a virtual environment**
```
python3 -m venv venv
source venv/bin/activate
```

### **3. Install dependencies**
```
pip install -r requirements.txt
```

### 4. **Create your .env file**
```
cp .env.example .env
```
(Your service will not run without correctly updating these.)

### 5. Running the App
```
uvicorn main:app --reload
```