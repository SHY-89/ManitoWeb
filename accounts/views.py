from django.shortcuts import render

# Create your views here.
def kakao(request):
    return render(request, 'accounts/kakao.html')

def home(request):
    return render(request, 'accounts/home.html')