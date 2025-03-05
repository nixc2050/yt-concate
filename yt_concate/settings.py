# settings.py
import os

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


# 確保下載資料夾在專案內
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 取得 `settings.py` 所在的專案路徑
DOWNLOADS_DIR = os.path.join(BASE_DIR, 'downloads')  # downloads 確保在專案內
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')