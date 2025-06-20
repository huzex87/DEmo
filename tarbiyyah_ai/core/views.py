from django.shortcuts import render
from django.http import JsonResponse
import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY', '')


def index(request):
    return render(request, 'index.html')


def chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        if openai.api_key:
            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_message}],
                )
                reply = response.choices[0].message.content
            except Exception as e:
                reply = f"Error: {e}"
        else:
            reply = "OPENAI_API_KEY not configured."
        return JsonResponse({"reply": reply})
    return JsonResponse({"error": "Invalid request"}, status=400)
