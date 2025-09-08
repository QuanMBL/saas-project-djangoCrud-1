from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, get_user_model
# Create your views here.

""" 
render: trả về template HTML dễ dàng.

authenticate: kiểm tra tài khoản/mật khẩu.

login: lưu trạng thái đăng nhập của user vào session.
"""
User = get_user_model()
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username") or None
        password = request.POST.get("password") or None

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Login here!")
            return redirect("/")  # về trang chủ sau khi login
        else:
            return render(request, "auth/login.html", {"error": "Sai tài khoản hoặc mật khẩu"})
    return render(request, "auth/login.html")

def register_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username") or None
        email = request.POST.get("email") or None
        password = request.POST.get("username") or None
        try:
            User.objects.create_user(username,email=email,password=password)
        except:
            pass
        
    return render(request, 'auth/register.html',{})