# download_captions.py
import os
import time
import re
import glob
import yt_dlp

from yt_concate.settings import CAPTIONS_DIR
from yt_concate.pipeline.steps.step import Step, StepException
from yt_concate.settings import logger

log = logger

class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        lang = "en"
        for yt in data:
            log.info(f'downloading caption for: {yt.id}')
            if utils.caption_file_exists(yt):
                log.info('found existing caption file')
                continue
            try:
                video_id = yt.id
                output_txt = yt  # 設定 TXT 檔名

                ydl_opts = {
                    'writesubtitles': True,
                    'writeautomaticsub': True,  # 下載自動字幕
                    'subtitleslangs': [lang],
                    'subtitlesformat': 'vtt',
                    'skip_download': True,  # 不下載影片
                    'outtmpl': os.path.join(CAPTIONS_DIR, f"{video_id}.%(ext)s"),  # ✅ 讓 yt-dlp 直接存 .vtt
                    'quiet': True,  # ✅ 關閉 yt-dlp 輸出 (option）
                    'noprogress': True,  # ✅ 不顯示進度條 (option）
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([yt.url])
            except yt_dlp.utils.DownloadError as e:

                log.error(f'{e}, {yt}')
                continue
            # ** 自動尋找下載的字幕檔案**
            vtt_files = glob.glob(os.path.join(CAPTIONS_DIR, f"{video_id}*.vtt")) # 搜尋符合條件的 VTT 檔案

            if vtt_files:
                vtt_file = vtt_files[0]  # 取得第一個找到的字幕檔案
                log.info(f"✅ 找到字幕檔案: {vtt_file}")
                self.vtt_to_txt(vtt_file, output_txt)  # 轉換字幕
            else:
                log.info("❌ 無法找到字幕檔案，可能該影片無字幕。")

        end = time.time()
        log.info(f'took, {end - start}, seconds')

        return data


    def vtt_to_txt(self, vtt_file, txt_file):
        """將 VTT 字幕轉換為純文字 TXT"""

        with open(vtt_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        text_lines = []
        for line in lines:
            # # 移除時間戳記（例如 00:01.500 --> 00:04.000）
            # if re.match(r"\d+:\d+:\d+\.\d+", line):
            #     continue
            # 移除 VTT 標籤（可能有 <c> 或 </c> 這類標籤）
            line = re.sub(r"<[^>]+>", "", line)
            text_lines.append(line.strip())

        # 寫入 TXT 檔案
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write("\n".join(text_lines))

        log.info(f"✅ 已將字幕轉換為 TXT: {txt_file}")

