# Tarbiyyah AI MVP

This repository contains the initial code for **Tarbiyyah AI**, an online Islamiyya learning platform with AI powered tutors.

## Getting Started

1. Open the `tarbiyyah_ai_project` folder in VS Code for easy folder navigation.

2. Install dependencies (use `pip3` if `pip` isn't recognized):

```bash
pip install django==3.2.20 openai
```

3. Change into the project directory and run the development server:

```bash
cd tarbiyyah_ai_project
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

4. Open `http://localhost:8000/` in your browser.

Set the environment variable `OPENAI_API_KEY` to enable AI responses.
