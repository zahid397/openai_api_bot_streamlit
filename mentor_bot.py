"""
Mentor Bot — Career, learning, and programming guidance.
Uses OpenAI API if key is available, else rule-based fallback.
"""

import os
import random

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# ── System prompt for OpenAI ─────────────────────────────────
MENTOR_SYSTEM_PROMPT = """You are an expert tech mentor with 15+ years in software engineering.
You give clear, actionable advice on programming, career development, and learning strategies.
Always be encouraging, specific, and practical.
Use bullet points and structure your answers clearly.
Keep responses under 200 words unless a detailed explanation is needed."""

# ── Rule-based knowledge base ────────────────────────────────
RULES = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "howdy", "greetings", "sup", "what's up"],
        "responses": [
            "👋 **Hello, developer!** I'm your Mentor Bot.\n\nAsk me anything about:\n- 🐍 Python & programming\n- 💼 Career & job hunting\n- 📚 Learning roadmaps\n- 🛠️ Project ideas\n- 🤖 AI & machine learning\n\nWhat would you like to explore today?",
        ]
    },
    "python": {
        "keywords": ["python", "django", "flask", "fastapi", "pandas", "numpy", "pip", "decorator", "generator", "async"],
        "responses": [
            """🐍 **Python Learning Roadmap:**

**Beginner (Weeks 1–4):**
- Variables, data types, loops, functions
- List comprehensions, file I/O
- Virtual environments (`python -m venv env`)

**Intermediate (Months 2–3):**
- OOP: classes, inheritance, dunder methods
- Decorators, generators, context managers
- Libraries: NumPy, Pandas, Requests

**Advanced:**
- Async/await, multithreading
- FastAPI or Django REST Framework
- Testing with pytest

💡 **Daily tip:** Build one small project per week. Theory without practice is forgotten fast.""",
        ]
    },
    "career": {
        "keywords": ["career", "job", "interview", "resume", "salary", "hire", "linkedin", "portfolio", "work"],
        "responses": [
            """💼 **Developer Career Blueprint:**

**1. Build Your Portfolio**
- 3–5 real projects on GitHub (with README!)
- Deploy at least one project live

**2. Interview Prep**
- LeetCode: solve 50 medium problems
- System design: study patterns (load balancing, caching, DBs)
- Behavioral: STAR method (Situation, Task, Action, Result)

**3. Networking**
- LinkedIn: post weekly, engage genuinely
- Contribute to open source (even docs!)
- Join local meetups or Discord communities

💡 *Junior roles: care about projects. Senior roles: care about impact and system thinking.*""",
        ]
    },
    "learn": {
        "keywords": ["learn", "study", "start", "beginner", "roadmap", "how to", "resources", "course", "tutorial", "where"],
        "responses": [
            """📚 **How to Learn Programming Effectively:**

**The 70-20-10 Rule:**
- 70% → Build projects (learn by doing)
- 20% → Read docs, books, articles
- 10% → Watch tutorials

**Daily Routine:**
1. Morning: 30 min theory/concept
2. Evening: 60 min hands-on coding

**Free Resources:**
- 📖 docs.python.org (official, underrated)
- 🎯 roadmap.sh (visual career paths)
- 🏆 freecodecamp.org
- 📊 kaggle.com (for data science)

⚡ *The fastest learners build things they personally find useful.*""",
        ]
    },
    "ai": {
        "keywords": ["ai", "machine learning", "ml", "deep learning", "neural", "llm", "gpt", "artificial intelligence", "data science", "model"],
        "responses": [
            """🤖 **AI/ML Learning Path:**

**Step 1: Foundations**
- Python ✓ + NumPy + Pandas
- Statistics: mean, variance, distributions
- Linear algebra basics (matrix multiplication)

**Step 2: Classical ML**
- scikit-learn: regression, classification, clustering
- Practice on Kaggle datasets

**Step 3: Deep Learning**
- PyTorch (recommended) or TensorFlow
- CNNs for images, Transformers for text

**Step 4: Modern AI**
- OpenAI API + LangChain
- Build a RAG chatbot
- Prompt engineering patterns

💡 *Start a Kaggle competition this week — nothing beats real data for learning.*""",
        ]
    },
    "project": {
        "keywords": ["project", "build", "make", "create", "idea", "portfolio", "develop", "side project"],
        "responses": [
            """🛠️ **Project Ideas by Level:**

**Beginner:**
- 🌤️ Weather app (OpenWeatherMap API + UI)
- ✅ Task manager with file storage
- 🎮 Simple CLI quiz game

**Intermediate:**
- 🔌 REST API (FastAPI + PostgreSQL + Docker)
- 🤖 Telegram or Discord bot
- 📊 Data dashboard (Streamlit + Plotly)

**Advanced:**
- 🧠 RAG-based Q&A chatbot
- 📈 Real-time stock analyzer
- 🚀 Containerized ML model API

💡 *Always add: README, tests, deployment — that's what employers check first.*""",
        ]
    },
    "git": {
        "keywords": ["git", "github", "version control", "commit", "branch", "merge", "pull request", "fork"],
        "responses": [
            """🔧 **Git Essentials:**

**Daily Commands:**
```bash
git status          # see changes
git add .           # stage all files
git commit -m "msg" # save snapshot
git push            # upload to GitHub
git pull            # download latest
