from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
# Create your views here.

# get_user_model() trả về model User hiện tại được sử dụng trong dự án, có thể là User mặc định của Django hoặc một model tùy chỉnh nếu bạn đã định nghĩa một.
User = get_user_model()

def profile_view(request,username =None,*args, **kwargs):
    user = request.user
    
    # User.objects.get làm truy vấn để lấy đối tượng User từ cơ sở dữ liệu dựa trên username được truyền vào.
    # profile_view_obj = User.objects.get(username=username)
    
    # get_object_or_404 là một hàm tiện ích của Django. Nó cố gắng lấy đối tượng từ cơ sở dữ liệu dựa trên các tham số được cung cấp (trong trường hợp này là username).
    # 404 nếu không tìm thấy đối tượng, thay vì ném ra một ngoại lệ. 
    profile_view_obj = get_object_or_404(User,username=username)
    
    
    is_me = profile_view == user
    return HttpResponse(f"Hello : {username}- {profile_view_obj.id}-{user.id}- is_me: {is_me}")
