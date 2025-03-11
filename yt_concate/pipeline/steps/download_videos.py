# download_videos.py
import os
import yt_dlp

from. step import Step
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import logger

log = logger

class DownloadVideos(Step):
    def process(self,data, inputs, utils):

        yt_set = set([found.yt for found in data])

        log.info(f'video to download: {len(yt_set)}')

        for yt in yt_set:
            url = yt.url


            if utils.video_files_exists(yt):
                logger.info(f'found existing video file for {url}, skipping')
                continue

            ydl_opts = {
                "format": "best",  # 下載最佳畫質
                "outtmpl":os.path.join( VIDEOS_DIR,f"{yt.id}.mp4"),  # 設定影片輸出名稱
                'quiet': True,  # ✅ 關閉 yt-dlp 輸出 (option）
                'noprogress': True,  # ✅ 不顯示進度條 (option）
            }
            log.info(f'download: {url}')

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        return data