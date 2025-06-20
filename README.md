# Tarbiyyah AI MVP

This repository contains the initial code for **Tarbiyyah AI**, an online Islamiyya learning platform with AI powered tutors.

## Getting Started

1. Install dependencies:

```bash
pip install django==3.2.20 openai
```

2. Run the development server:

```bash
cd tarbiyyah_ai
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

3. Open `http://localhost:8000/` in your browser.

Set the environment variable `OPENAI_API_KEY` to enable AI responses.
