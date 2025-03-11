# main.py

from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYT
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.edit_video import EditVideo
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils
from yt_concate.settings import logger

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'

def main():
    inputs ={
        'channel_id':CHANNEL_ID,
        'search_word':'incredible',
        'limit':30,
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight(),
    ]

    log = logger
    utils = Utils()
    p = Pipeline(steps)

    log.info('程式開始執行')  # 直接使用 logger
    try:
        p.run(inputs, utils)
        log.info('完成')
    except StepException as e:
        log.error(f'發生錯誤: {e}', exc_info=True)

if __name__ == '__main__':
    main()
