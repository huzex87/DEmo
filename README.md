# Tarbiyyah AI MVP

This repository contains the initial code for **Tarbiyyah AI**, an online Islamiyya learning platform with AI powered tutors.

## Getting Started

1. Open the `tarbiyyah_ai_project` folder in VS Code for easy folder navigation.

2. Copy `.env.example` to `.env` and add your OpenAI API key.

3. Install dependencies (use `pip3` if `pip` isn't recognized):

```bash
pip install django==3.2.20 openai python-dotenv
```

4. Change into the project directory and run the development server:

```bash
cd tarbiyyah_ai_project
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

5. Open `http://localhost:8000/` in your browser.
   - Use the **Curriculum** link to view a list of upcoming learning modules.
   - After logging in you can access your personal **Dashboard** to see recent messages and update your goals.
   - The navigation bar still provides **Sign Up** and **Login** modals for easy authentication.
   - All chat messages are stored in the database and shown on your dashboard and the home page when logged in.

The application uses `python-dotenv` to load a `.env` file automatically. Set `OPENAI_API_KEY` there and never commit real API keys to the repository.
