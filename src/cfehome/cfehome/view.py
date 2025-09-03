from django.http import HttpResponse
from django.urls import path
from vistis.models import PageVist
from django.shortcuts import render
import pathlib 

# pathlib là module chuẩn có thể thay thế cho os.Path
#  đường dẫn tuyệt đối đang chạy
this_dir = pathlib.Path(__file__).resolve().parent
def home_page_view(request,*args, **kwargs):
    my_title = "My page"
    
    # objects ở đây cho tương tác với database
    queryset= PageVist.objects.all() # tổng thể      vào trang bao nhiêu lần
    html_templates= "home.html"
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