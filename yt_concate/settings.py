# settings.py
import os
import logging

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


# 確保下載資料夾在專案內
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 取得 `settings.py` 所在的專案路徑
DOWNLOADS_DIR = os.path.join(BASE_DIR, 'downloads')  # downloads 確保在專案內
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')
OUTPUT_DIR = os.path.join(BASE_DIR,  'outputs')


def logger(log_filename='app.log'):

    # 創建 logger 物件
    logger = logging.getLogger(__name__)  # 設定 Logger 名稱 若MyLogger 未給值，預設就是root
    logger.setLevel(logging.DEBUG)  # 設定最低記錄等級（DEBUG 以上都會記錄）
    # 避免重複添加 handler
    if not logger.handlers:
        # 創建（formatter）
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')

        # 建立處理器（Handlers）
        # 檔案處理器 - 寫入 app.log
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(logging.DEBUG)  # 設定最低等級
        file_handler.setFormatter(formatter)  # 將formatter 加裝載handler上
        logger.addHandler(file_handler)       # 將handler 加裝載logger上

        # 終端機處理器 - 輸出到 Console
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # 防止重複輸出
        logger.propagate = False
    return logger

logger = logger()