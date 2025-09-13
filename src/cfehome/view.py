from django.http import HttpResponse
from django.urls import path
from vistis.models import PageVist
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

import pathlib 



# pathlib là module chuẩn có thể thay thế cho os.Path
#  đường dẫn tuyệt đối đang chạy
this_dir = pathlib.Path(__file__).resolve().parent
def home_page_view(request,*args, **kwargs):
    my_title = "My page"
    
    # objects ở đây cho tương tác với database
    queryset= PageVist.objects.all() # tổng thể      vào trang bao nhiêu lần
    html_templates= "base.html"
    #số lần vào trang request 
    qs= PageVist.objects.filter(path=request.path)
    my_context = {
        "page_title":my_title,
        "page_visit": qs.count(),
        "page_total": queryset.count()
    }

   
    
    PageVist.objects.create()
    # yêu cầu, trang được trả về, dữ liệu sẽ trả về cho trang
    return render(request,html_templates,my_context) 


VALID_CODE = "abc123"
# hàm pw_protected_view cho phép nhập code để vào trang protected 
def pw_protected_view(request,*args, **kwargs):
    if request.method == "POST":
        user_pw_sent = request.POST.get("code") or None
   
    if user_pw_sent == VALID_CODE:
        return render(request,"protected/view.html",{})
    return render(request,"protected/entry.html",{})



# login_required: Người dùng buột phải đăng nhập mới được vào trang này 
@login_required
def user_only_view(request,*args, **kwargs):
    # print(request.user.is_staff)
    return render(request, "protected/onlyview.html",{})


# staff_member_required: Người dùng buột phải là nhân viên mới được vào trang này
@staff_member_required
def staff_only_view(request,*args, **kwargs):
    return render(request, "protected/staffview.html",{})