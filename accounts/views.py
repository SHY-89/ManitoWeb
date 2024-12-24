from django.shortcuts import render,redirect
from django.views.decorators.http import (
    require_POST, 
    require_http_methods,
    require_GET
)
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    update_session_auth_hash,
    authenticate
)
import requests
import bcrypt
from django.conf import settings
from django.http import JsonResponse
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserChangeForm
from .models import User


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


@require_GET
def socialkakao(request):
    return render(request, 'accounts/socialkakao.html')


@require_GET
def kakaos(request):
    url = "https://kauth.kakao.com/oauth/token"

    # 요청 파라미터
    data = {
        "grant_type": "authorization_code",
        "client_id": settings.KAKAO_REST_API_KEY,  # 카카오 REST API 키
        "redirect_uri": settings.KAKAO_CALLBACK_URI,  # 등록된 리다이렉트 URI
        "code": request.GET.get("code"),  # 인가 코드
    }

    # 요청 헤더
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
    }

    response = requests.get(url, params=data, headers=headers)
    token = response.json()
    check_error = token.get("error")
    if check_error:
        return redirect("socialkakao")
    
    access_token = token.get("access_token")
    kakao_request = requests.get("https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"})
    kakao_data = kakao_request.json()
    
    kakao_account = kakao_data.get("kakao_account")
    if not kakao_account or not kakao_account.get("email"):
        return JsonResponse({"error": "등록하려면 이메일이 필요합니다."})
    
    email = kakao_account.get("email")
    username = "kakao_"+email.split('@')[0]
    kakao_profile = kakao_data.get("properties")
    nickname = kakao_profile.get("nickname")
    id = str(kakao_data.get("id"))
    id = id.encode('utf-8')
    password = bcrypt.hashpw(id, bcrypt.gensalt() ) 

    user, created = User.objects.get_or_create(username=username, defaults={
        'email':email, 'first_name': nickname
    })

    if created:
        user.set_password(password)

    user.save()
    user =  authenticate(username=username, password=password)
    if user:
        # 인증된 사용자의 backend 명시
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth_login(request, user)
    
    return redirect("index")

    


def home(request):
    return render(request, 'accounts/home.html')

