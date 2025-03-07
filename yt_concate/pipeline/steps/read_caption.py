# read_caption.py


from .step import Step


class ReadCaption(Step):
    def process(self, data, input, utils):
        for yt in data:
            if not utils.caption_file_exists(yt):
                continue

            if not yt.caption_filepath.endswith(".txt"): #  檢查是否為 .txt 檔案
                continue  # 跳過非字幕檔案

            captions = {}

            with open(yt.caption_filepath, 'r',encoding='utf-8', errors ='replace') as f:

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
            yt.captions = captions

        return data
