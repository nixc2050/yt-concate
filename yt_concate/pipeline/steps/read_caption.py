# read_caption.py
import os
from pprint import pprint
from .step import Step
from yt_concate.settings import CAPTIONS_DIR

class ReadCaption(Step):
    def process(self, data, input, utils):
        data = {}

        for caption_file in os.listdir(CAPTIONS_DIR):

            if not caption_file.endswith(".txt"): #  檢查是否為 .txt 檔案
                continue  # 跳過非字幕檔案

            captions = {}

            with open(os.path.join(CAPTIONS_DIR,caption_file), 'r',encoding='utf-8', errors ='replace') as f:

                time_line = False
                time = None
                caption = None

                for line in f:
                    line = line.strip()
                    if "-->" in line:
                        time_line = True
                        time = line
                        continue
                    if time_line:
                        caption = line
                        captions[caption] = time
                        time_line = False
            data[caption_file] = captions

        pprint(data)
        return data
