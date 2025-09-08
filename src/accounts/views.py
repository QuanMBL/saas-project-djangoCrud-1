from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
# Create your views here.

""" 
render: trả về template HTML dễ dàng.

authenticate: kiểm tra tài khoản/mật khẩu.

login: lưu trạng thái đăng nhập của user vào session.
"""
 
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Login here!")
            return redirect("/")  # về trang chủ sau khi login
        else:
            return render(request, "auth/login.html", {"error": "Sai tài khoản hoặc mật khẩu"})
    return render(request, "auth/login.html")