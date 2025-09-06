# Nó không ảnh hưởng khi chạy code, mà chủ yếu dùng cho type hinting (chú thích kiểu dữ liệu).
from typing import Any
import helpers
# này lấy dữ liệu từ setting
from django.conf import settings

# 
from django.core.management.base import BaseCommand

# connect với dữ liệu ở file setting
STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')


VENDOR_STATICFILES = {
"flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
"flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
}

class Command(BaseCommand):
    def handle(self, *args, **options):
        #  lệnh  self.stdout.write đây là dạng print nhưng nó sẽ chạy khi bạn gõ chạy lệnh của manage   
        self.stdout.write("downloanding vendor static files") 
        completed_urls = []
        for name,url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR/name
            dl_success= helpers.download_to_local(url,out_path)
            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f'Failed to downloading {url}')
                )
        if set(completed_urls) ==set(VENDOR_STATICFILES.values()):
            self.style.SUCCESS("Đã thành công updated all vender files")
        else: 
            self.style.WARNING('Some files were not update')