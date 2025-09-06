import requests
from pathlib import Path

# download địa chỉ gồm url, nơi lưu file out_path, 
def download_to_local(url:str, out_path, parent_mkdir:bool=True):
    if not isinstance(out_path, Path):
        raise ValueError(f"{out_path} must be a vaild pathlib.Path object") # phần này sẽ được ném lỗi 
    if parent_mkdir: 
        out_path.parent.mkdir(parents=True, exist_ok=True)
        
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        out_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f'Failed to download {url}: {e}')
        return False