from django.shortcuts import render

def home(request):
    """صفحه اصلی - بسته به موبایل/دسکتاپ رفتار می‌کنه"""
    return render(request, 'main/home.html')

def col1_view(request):
    """ستون اول (منو) - فقط برای HTMX"""
    return render(request, 'main/partials/col1.html')

def col2_view(request):
    """ستون دوم (فید) - فقط برای HTMX"""
    return render(request, 'main/partials/col2.html')

def col3_view(request):
    """ستون سوم (محتوا) - فقط برای HTMX"""
    return render(request, 'main/partials/col3.html')