from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .models import ChatMessage, UserProfile
from django.contrib.auth.decorators import login_required
import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY', '')


def index(request):
    messages = None
    if request.user.is_authenticated:
        messages = ChatMessage.objects.filter(user=request.user).order_by('-created')[:20]
    return render(request, 'index.html', {'messages': messages})


def about(request):
    return render(request, 'about.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def dashboard(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    messages = ChatMessage.objects.filter(user=request.user).order_by('-created')[:5]
    return render(request, 'dashboard.html', {"profile": profile, "messages": messages})


def curriculum(request):
    return render(request, 'curriculum.html')


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
        ChatMessage.objects.create(user=request.user if request.user.is_authenticated else None,
                                  message=user_message, reply=reply)
        return JsonResponse({"reply": reply})
    return JsonResponse({"error": "Invalid request"}, status=400)
