from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    update_session_auth_hash,
    authenticate
)
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserChangeForm


def index(request):
    return render(request, "accounts/index.html")

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            authenticated_user = authenticate(username=user.username, password=form.cleaned_data["password1"])
            if authenticated_user is not None:
                auth_login(request, authenticated_user)
            return redirect("index")
    form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, 'accounts/singup.html',context)


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_path = request.GET.get("next") or "index"
            return redirect(next_path)
        
    form = CustomAuthenticationForm()
    context = {"form": form}
    return render(request, 'accounts/login.html',context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("index")


@require_POST
def delete(request, pk):
    if request.user.is_authenticated and request.user.pk==pk:
        request.user.delete()
        auth_logout(request)
    return redirect("index")


@require_http_methods(["GET", "POST"])
def update(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                user = form.save()
                return redirect("index")
            
        form = CustomUserChangeForm(instance=request.user)
        context = {"form": form}
        return render(request, "accounts/update.html", context)
    return redirect("accounts:login")

def kakao(request):
    return render(request, 'accounts/kakao.html')

def home(request):
    return render(request, 'accounts/home.html')

